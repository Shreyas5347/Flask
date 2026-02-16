from flask import Flask,request,jsonify

from werkzeug.security import generate_password_hash, check_password_hash

import sqlite3
app=Flask(__name__)

@app.route("/register", methods=["POST"])
def register():
    #get the user data from the request
    user=request.get_json()
    if not user:
        return jsonify({"error":"No data provided"}),400
    #get the username and password from the request
    username=user.get("username")
    password=user.get("password")
    if not username or not password:
        return jsonify({"error":"Username and password are required"}),400
    #hash the password
    hashed_password=generate_password_hash(password)
    #connect to the database
    conn=sqlite3.connect("test.db")
    cursor=conn.cursor()
    #check if the user already exists
    cursor.execute(
        "SELECT id FROM users WHERE username = ?",
        (username,)
    )
    if cursor.fetchone():
        conn.close()
        return jsonify({"error": "User already exists"}), 409
    #insert the new user
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)",
        (username, hashed_password))
    conn.commit()
    conn.close()
    return jsonify({"message":"User registered successfully"})

