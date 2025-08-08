from flask import Flask, render_template

app = Flask(__name__)

users = [
    {"id": 1, "name": "이배형", "email": "lee@example.com"},
    {"id": 2, "name": "김강패", "email": "kim@example.com"},
    {"id": 3, "name": "최지환", "email": "chi@example.com"},
]

@app.route("/")
def user_list():
    return render_template("users.html", users=users)

if __name__ == "__main__":
    app.run(debug=True)
