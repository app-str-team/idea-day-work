from flask import Flask, request

from src.application.ideas.queries import getidealist
from src.application.judgement.command import processscore
from src.application.users.command import createuser, signin

app = Flask(__name__)

@app.route("/dashboard", methods=['GET'])
def get_dashboard():
    return "Welcome to Idea day event!"


@app.route("/idealist", methods=['GET'])
def get_idealist():
    return getidealist.fetch_idea_list()


@app.route("/postscore", methods=['POST'])
def process_postscore():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        return processscore.process_score(json)
    else:
        return {'error':'Content-Type not supported!'}
    

@app.route("/createuser", methods=['POST'])
def process_create_user():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        return createuser.create_user(json)
    else:
        return {'error':'Content-Type not supported!'}
    

@app.route("/signin", methods=['POST'])
def process_login():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        return signin.signin_user(json)
    else:
        return {'error':'Content-Type not supported!'}   


if __name__ == "__main__":
    app.run()
    