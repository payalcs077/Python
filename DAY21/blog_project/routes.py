from flask import Blueprint, render_template, redirect, url_for, flash, abort, request
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import or_

from models import db, User, Post
from forms import RegisterForm, LoginForm, PostForm

import os
from werkzeug.utils import secure_filename
from flask import current_app

main = Blueprint("main", __name__)


@main.route("/")
def index():
    page = request.args.get("page", 1, type=int)
    search = request.args.get("search", "")

    if search:
        posts = Post.query.filter(
            or_(
                Post.title.ilike(f"%{search}%"),
                Post.content.ilike(f"%{search}%")
            )
        ).order_by(Post.date_created.desc()).paginate(
            page=page,
            per_page=5
        )
    else:
        posts = Post.query.order_by(
            Post.date_created.desc()
        ).paginate(
            page=page,
            per_page=5
        )

    return render_template("index.html", posts=posts, search=search)


@main.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():

        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash("Email already registered!", "danger")
            return redirect(url_for("main.register"))

        # 👇 THIS IS THE IMPORTANT FIX
        selected_role = form.role.data

        # 🔐 Security validation
        if selected_role not in ["user", "author","admin"]:
            selected_role = "user"

        hashed_password = generate_password_hash(form.password.data)

        new_user = User(
            username=form.username.data,
            email=form.email.data,
            password=hashed_password,
            role=selected_role   # 👈 NOT "user"
        )

        db.session.add(new_user)
        db.session.commit()

        flash("Account created successfully!", "success")
        return redirect(url_for("main.login"))

    return render_template("register.html", form=form)

@main.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash("Login successful!", "success")

            if user.role == "admin":
                return redirect(url_for("main.dashboard"))
            elif user.role == "author":
                return redirect(url_for("main.author_dashboard"))
            else:
                return redirect(url_for("main.user_dashboard"))
        else:
            flash("Invalid credentials", "danger")

    return render_template("login.html", form=form)


@main.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out successfully", "info")
    return redirect(url_for("main.index"))


@main.route("/create-post", methods=["GET", "POST"])
@login_required
def create_post():

    print("LOGGED IN USER:", current_user.username)
    print("ROLE:", current_user.role)

    if current_user.role not in ["admin", "author"]:
        abort(403)

    form = PostForm()

    if form.validate_on_submit():

        filename = None

        if form.image.data:
            image_file = form.image.data
            filename = secure_filename(image_file.filename)
            upload_path = os.path.join(current_app.root_path, "static/uploads", filename)
            image_file.save(upload_path)

        new_post = Post(
            title=form.title.data,
            content=form.content.data,
            image=filename,
            user_id=current_user.id
        )

        db.session.add(new_post)
        db.session.commit()

        flash("Post created successfully!", "success")
        return redirect(url_for("main.index"))

    return render_template("create_post.html", form=form)


@main.route("/post/<int:post_id>")
def post_detail(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template("post_detail.html", post=post)


@main.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@login_required
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)

    if current_user.role != "admin" and post.author != current_user:
     abort(403)

    form = PostForm()

    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()

        flash("Post updated successfully!", "success")
        return redirect(url_for("main.post_detail", post_id=post.id))

    form.title.data = post.title
    form.content.data = post.content

    return render_template("create_post.html", form=form)


@main.route("/delete-post/<int:post_id>")
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)

    if current_user.role != "admin" and post.author != current_user:
        abort(403)

    db.session.delete(post)
    db.session.commit()

    flash("Post deleted successfully!", "info")
    return redirect(url_for("main.index"))


@main.route("/user-dashboard")
@login_required
def user_dashboard():
    if current_user.role != "user":
        abort(403)

    posts = Post.query.filter_by(user_id=current_user.id).all()
    total_posts = len(posts)

    return render_template(
        "user_dashboard.html",
        posts=posts,
        total_posts=total_posts
    )

@main.route("/author-dashboard")
@login_required
def author_dashboard():
    if current_user.role not in ["author", "admin"]:
        abort(403)

    posts = Post.query.filter_by(user_id=current_user.id).all()
    total_posts = len(posts)

    return render_template(
        "author_dashboard.html",
        posts=posts,
        total_posts=total_posts
    )

@main.route("/admin-dashboard")
@login_required
def admin_dashboard():
    if current_user.role != "admin":
        abort(403)

    total_users = User.query.count()
    total_posts = Post.query.count()

    users = User.query.all()
    posts = Post.query.order_by(Post.date_created.desc()).all()

    return render_template(
        "admin_dashboard.html",
        total_users=total_users,
        total_posts=total_posts,
        users=users,
        posts=posts
    )

@main.route("/change-role/<int:user_id>/<string:new_role>")
@login_required
def change_role(user_id, new_role):

    if current_user.role != "admin":
        abort(403)

    user = User.query.get_or_404(user_id)

    # Prevent admin from demoting themselves accidentally
    if user.id == current_user.id:
        flash("You cannot change your own role.", "danger")
        return redirect(url_for("main.admin_dashboard"))

    if new_role not in ["user", "author", "admin"]:
        abort(400)

    user.role = new_role
    db.session.commit()

    flash("User role updated successfully.", "success")
    return redirect(url_for("main.admin_dashboard"))


@main.route("/dashboard")
@login_required
def dashboard():
    if current_user.role == "admin":
        return redirect(url_for("main.admin_dashboard"))

    elif current_user.role == "author":
        return redirect(url_for("main.author_dashboard"))

    else:
        return redirect(url_for("main.user_dashboard"))
    

@main.route("/delete-user/<int:user_id>", methods=["POST"])
@login_required
def delete_user(user_id):

    # Only admin can delete users
    if current_user.role != "admin":
        abort(403)

    user = User.query.get_or_404(user_id)

    # Prevent admin deleting themselves
    if user.id == current_user.id:
        flash("You cannot delete your own account.", "danger")
        return redirect(url_for("main.admin_dashboard"))

    db.session.delete(user)
    db.session.commit()

    flash("User deleted successfully.", "success")
    return redirect(url_for("main.admin_dashboard"))