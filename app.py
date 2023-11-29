from flask import Flask

from src.application.ideas.queries import getidealist

app = Flask(__name__)

@app.route("/dashboard", methods=['GET'])
def get_dashboard():
    return "Welcome to Idea day event!"

@app.route("/idealist", methods=['GET'])
def get_idealist():
    return getidealist.fetch_idea_list()