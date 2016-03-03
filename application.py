# Canvas Demo App
# Written in Python 2.7 with the Flask Framework
# Author: Matt Auerbach (matthew.auerbach@optimizely.com)
# Dev Docs - http://developers.optimizely.com/canvas/

import os
from flask import Flask, request, render_template
import optimizely
import optimizely_canvas_sdk

# Note: I'm sharing this because the Canvas Demo App can only be used locally
CLIENT_SECRET = 'vhxUuxUXruG3ZJ-AYOrrgLGDZp-bGqVkuEQpEldYJcE'

application = Flask(__name__)
application.secret_key = os.urandom(24)


@application.route('/')
def index():
    # Access the signed_request
    signed_request = request.args.get('signed_request')

    # Decode the signed request
    user_info = optimizely_canvas_sdk.extract_user_context(signed_request, CLIENT_SECRET)

    # Get user's access token & project id
    token = user_info['context']['client']['access_token']
    current_project_id = user_info['context']['environment']['current_project']

    # Initialize Python Client Library
    client = optimizely.Client(token)

    # Get all experiments in a project
    experiments = client.Projects.get(current_project_id).experiments()

    data = []

    # Iterate through each experiment and get status
    for experiment in experiments:
        result = experiment.__dict__
        name = result['description']
        status = result['status']
        data.append((name, status))
        print "Experiment: " + name + " is in the status: " + status

    return render_template('index.html', data=data)

if __name__ == '__main__':
    # Toggle to debug
    application.debug = True
    application.run(port=4001)
