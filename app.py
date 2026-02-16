from flask  import Flask,request,jsonify
app=Flask(__name__)
@app.route("/")
def home():
    return "hello world via flask"

@app.route("/about")
def about():
    return "about page"

@app.route("/contact/<name>")
def contact(name):
    return f"contact {name} "

@app.route("/yourself/<name>/<age>")
def yourself(name,age):
    return f"your name is {name} and your age is {age}"

@app.route("/square/<int:num>")
def square(num):
    return str(num * num)

@app.route("/calculator/<int:a>/<int:b>")
def calculator(a,b):
    return f"the sum of {a} and {b} is {a+b}"

@app.route("/search")
def search():
    name=request.args.get("name")
    age=request.args.get("age")
    return f"myself {name} and my age is {age}"

@app.route("/user")
def user():
    return jsonify({"name":"shreyas","age":20})

@app.route("/search1")
def search1():
    
    name=request.args.get("name")
    if name:
        return jsonify({
        "searched_name":name
    })
    else:
        return jsonify({
        "error":"name parameter missing"
    })
 

if __name__=="__main__":
    app.run(debug=True)
