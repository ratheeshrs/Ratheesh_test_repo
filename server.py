## Filename: server.py 

import os, sys
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def verify():
    #webhook verification
    if request.args.get("hub.mode") == "suscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "hello":
            return "verification token missmatch", 403
        return request.args["hub.challenge"], 200
    return "Hello world", 200

if __name__ == '__main__':
    app.run(debug=True,port=80)
    
    

    


    
