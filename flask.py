from flask import Flask, request

app = Flask(__name__)

@app.route("/first_script")
def hello_world():
    request_body = request.json
    return f"<p>Hello, World! {request_body}</p>"
  
@app.route("/second_script")
def second_script():
    return "<p>This is the second script</p>"
