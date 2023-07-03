function togglePasswordVisibility() {
    var passwordInput = document.getElementById("exampleInputPassword1");
    var showPasswordBtn = document.getElementById("showPasswordBtn");

    if (passwordInput.type === "password") {
        passwordInput.type = "text";
    } else {
        passwordInput.type = "password";
    }
}
