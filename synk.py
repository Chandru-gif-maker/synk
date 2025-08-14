from flask import Flask, request

app = Flask(_name_)

@app.route("/")
def index():
    name = request.args.get("name", "")
    return f"<h1>Welcome, {name}</h1>"  
