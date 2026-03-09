// Simple welcome message
function showMessage() {
    alert("Welcome to My Flask Website!");
}

// Simple login validation
function validateLogin() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    if (username === "" || password === "") {
        alert("Both fields are required!");
        return false;  // prevent form submission
    }

    return true;
}
