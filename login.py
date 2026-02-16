from flask import Flask,request,jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
app=Flask(__name__)

@app.route("/login", methods=["POST"])
def login():
    user=request.get_json()
    if not user:
        return jsonify({"error":"No data provided"}),400
    username=user.get("username")
    password=user.get("password")
    if not username or not password:
        return jsonify({"error":"Username and password are required"}),400
    
    conn=sqlite3.connect("test.db")
    cursor=conn.cursor()
    #fetch the password from the database
    cursor.execute("SELECT password FROM users WHERE username = ?",
        (username,))
    result=cursor.fetchone()
    if not result:
        return jsonify({"error":"User not found"}),404
    hashed_password=result[0]
    #check the password
    if check_password_hash(hashed_password, password):
        return jsonify({"message":"Login successful"})
    else:
        return jsonify({"error":"Invalid credentials"})
    
    conn.close()

