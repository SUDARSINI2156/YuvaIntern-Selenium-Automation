
from flask import Flask, render_template, request

app = Flask(__name__, template_folder="app/templates")

registered_emails = set()


@app.route("/", methods=["GET", "POST"])
def register():
    message = ""

    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm-password")

        if password != confirm_password:
            message = "Passwords do not match"

        elif email in registered_emails:
            message = "Email is already registered"

        else:
            registered_emails.add(email)
            message = "Registration successful"

    return render_template("register.html", message=message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
