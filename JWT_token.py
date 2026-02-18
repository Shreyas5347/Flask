from flask import Flask,request,jsonify
import jwt
import datetime
from werkzeug.security import generate_password_hash, check_password_hash

app=Flask(__name__)
#secret key for jwt
#The SECRET_KEY is used to create a digital signature
#It is used to sign the JWT (JSON Web Token) to ensure its integrity and authenticity.
#If someone changes even 1 letter in token → signature check fails.
secret_key="kshd8734hsdKJHSD89@#ksjdhKJH87sd!@#" #hardcoded for practice purpose

users = {} #database for practice

@app.route("/register",methods=["POST"])
def register():
    data=request.get_json()
    if not data:
        return jsonify({"error":"No data provided"}),400
    username=data.get("username")
    password=data.get("password")
    if not username or not password:
        return jsonify({"error":"Username and password are required"}),400
    hashed_password=generate_password_hash(password)
    users[username]=hashed_password
    return jsonify({"message":"User registered successfully"})

@app.route("/login",methods=["POST"])
def login():
    data=request.get_json()
    if not data:
        return jsonify({"error":"No data provided"}),400
    username=data.get("username")
    password=data.get("password")
    if not username or not password:
        return jsonify({"error":"Username and password are required"}),400
    hashed_password=users.get(username)
    if not hashed_password:
        return jsonify({"error":"User not found"}),404
    if not check_password_hash(hashed_password,password):
        return jsonify({"error": "Invalid password"}), 401
    #generate the token
    payload={
              "username":username,
              "exp":datetime.datetime.utcnow()+datetime.timedelta(hours=1)
        }
    #encode the token using jwt
    #HS256 is the algorithm used to sign the token
    token=jwt.encode(payload,secret_key,algorithm="HS256")
    return jsonify({"token":token})

@app.route("/dashboard",methods=["GET"])
def dashboard():
    auth_header=request.headers.get("Authorization")
    if not auth_header:
        return jsonify({"error":"Token is missing"}),401
    #get the token from the header
    #Authorization: Bearer <token> 
    #split the header to get the token 
    #bearer is seperated from token by list and accessed by index 1
    token=auth_header.split(" ")[1]
    try:
        #decode the token
        payload=jwt.decode(token,secret_key,algorithms=["HS256"])
        username=payload["username"]
        return jsonify({
            "message": "Access granted",
            "user": username
        })
    
    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Token expired"}), 401
    
    except jwt.InvalidTokenError:
        return jsonify({"error": "Invalid token"}), 401

if __name__=="__main__":
    app.run(debug=True)