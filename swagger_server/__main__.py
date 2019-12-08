#!/usr/bin/env python3

import connexion
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from swagger_server import encoder
#from flask_cors import CORS

def set_cors_headers_on_response(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,POST,GET,DELETE,PUT'
    return response

def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    #CORS(app.app)
    app.app.json_encoder = encoder.JSONEncoder
    for jsonfile in os.listdir("{}/swagger/".format(os.path.dirname(os.path.abspath(__file__)))):
        if jsonfile.endswith(".yaml"):
            print("loading: {}".format(jsonfile))
            app.add_api(jsonfile, arguments={'title': 'Simple Inventory API'})

    app.app.after_request(set_cors_headers_on_response)
    app.run(threaded=True,port=8080,ssl_context=('/etc/letsencrypt/live/goodclass.cf/fullchain.pem', '/etc/letsencrypt/live/goodclass.cf/privkey.pem'))
    #app.run(threaded=True,port=8080)


if __name__ == '__main__':
    main()
