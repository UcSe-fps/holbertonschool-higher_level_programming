from flask import Flask, jsonify, request


app = Flask(__name__)

users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    return jsonify(list(users.keys()))


@app.route("status/")
def get_status():
    return "OK"


@app.route("/user/<username>")
def get_username(username):
    if username in users:
        return jsonify(users[username])
    return jsonify("error": "User not found")

@app_route("/add_user", methods=["POST"])
def add_user():
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error":"Username already exists"}), 409

    user = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    users[username] = user

    return jsonify({
        "message": "User added",
        "user": user
    }), 201


    # Run server
if __name__ == "__main__":
    app.run()
