from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    username = data.get("username")
    password = data.get("password")

    if username == "admin" and password == "1234":
        return jsonify({"status": "success"})
    else:
        return jsonify({"status": "failed"})

if __name__ == "__main__":
    app.run(debug=True)

