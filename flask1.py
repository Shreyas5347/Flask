'''
Flask is request-driven: each route executes only when its URL is requested.
Concept	                   |   Analogy
Flask                	   |   Blueprint
app = Flask(...)	       |   Actual house
app.run()	               |    Open the house to visitors


'''
from flask  import Flask
app=Flask(__name__)
@app.route("/")
def home():
    return "hello world via flask"
if __name__=="__main__":
    app.run(debug=True)
'''
home = app.route("/")(home)
So @app.route("/") means:

“Pass the function home into app.route("/") and replace it with the result.”
@ is a decorator - A decorator in Python is:
Decorator = wrapper Just like wrapping a gift , Decorator wraps a function
'''

'''
app = Flask(__name__)
Flask is a class.
app is an instance of that class.
it says:
“Create a web application object.”

'''
'''
If you run a file directly:
python flask1.py
Then inside flask1.py:
__name__ == "__main__"

If the file is imported then – 
import flask1
Then inside flask1.py:
__name__ == "flask1"
'''
