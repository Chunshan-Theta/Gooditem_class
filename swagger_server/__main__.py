#!/usr/bin/env python3

import connexion

from swagger_server import encoder
import os

def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    for jsonfile in os.listdir("{}/swagger/".format(os.path.dirname(os.path.abspath(__file__)))):
        if jsonfile.endswith(".yaml"):
            print("loading: {}".format(jsonfile))
            app.add_api(jsonfile, arguments={'title': 'Simple Inventory API'})
    app.run(port=8080)


if __name__ == '__main__':
    main()
