from flask  import Flask
app=Flask(__name__)
#static routes - here url is fixed and function alwasy return the same thing
@app.route("/about")
def about():
    return "About page"
#dynamic routes- The parameter name receives the string "Rahul" inside the function and the function returns the value which is sent to the browser

@app.route("/user/<name>")
def user(name):
    return f"Hello {name}"
#In the function, return can only send string to the browser not an integer
#To send an integer to the browser, we need to use the int:age
@app.route("/user/<name>/<int:age>")
def user_age(name,age):
    return f"Hello {name} and your age is {age}"


