from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/sanitize", methods=["GET"])
def sanitize():
    text = request.args.get("text")

    if not text:
        return jsonify({"error": "text is required"}), 400

    return jsonify({
        "original": text,
        "upper": text.upper(),
        "lower": text.lower()
    })

app.run(debug = True)
