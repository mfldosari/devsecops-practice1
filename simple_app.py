from flask import Flask, request

#Build simple Flask app
# This is a simple Flask application that listens on port 5000
# and responds to HTTP GET requests at the root URL ("/") with a greeting message.
# It also responds to HTTP POST requests at the "/echo" URL with the data sent in the request body.
# The application is designed to be run in a Docker container, and it uses the Flask framework to handle HTTP requests.
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Secure Python App!"

@app.route("/echo", methods=["POST"])
def echo():
    data = request.json
    return {"you_sent": data}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
