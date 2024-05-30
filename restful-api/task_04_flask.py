from flask import Flask, jsonify, request


app = Flask(__name__)
users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}


@app.route('/')
def home():
    return "Welcome to the Flask API!"


@app.route('/data')
def data():
    users_list = list(users.keys())
    return jsonify(users_list)


@app.route('/status')
def status():
    return "OK"


@app.route('/users/<username>')
def user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    user_data = request.json
    if "username" in user_data:
        username = user_data["username"]
        if username not in users:
            users[username] = user_data
            return jsonify({"message": "User added successfully"}), 200
        else:
            return jsonify({"error": "User already exists"}), 400
    else:
        return jsonify({"error": "Username not provided"}), 400


if __name__ == "__main__":
    app.run()
