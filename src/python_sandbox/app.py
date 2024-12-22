from flask import Flask

app = Flask(__name__)
app.json.ensure_ascii = False
users = {
    1: {"name": "(API)John Doe", "email": "john@example.com"},
    2: {"name": "(API)Jane Michael", "email": ""},
    3: {"name": "(API)Joe Bloggs", "email": ""},
}


@app.route("/user/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = users.get(user_id)
    return user, 200


app.run(debug=True)
