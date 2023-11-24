from flask import Flask
app = Flask(__name__)



# Controller-1
@app.route("/dashboard", methods=['GET'])
def get_dashboard():
    return "Welcome to Idea day event!"