from flask import Flask, request, render_template
from users_db import is_user_registered, add_user, count_users, init_db
import os

app = Flask(__name__)
init_db()

@app.route("/form", methods=["POST", "GET"])
def call_form():
    if request.method == "POST":
        result = request.form
        user = [result["name"], result["email"]]
        if is_user_registered(user):
            msg = "Error! This contact is already in the list."
            list_size = f"{count_users()}"
            return render_template("index.html", data={"list_size": list_size, "msg": msg})
        else:
            msg = "Success! You have added a new contact to the list."
            add_user(user)
            list_size = f"{count_users()}"
            return render_template("index.html", data={"list_size": list_size, "msg": msg})

    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)


