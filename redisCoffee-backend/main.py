#!/usr/bin/env python3

#  create backend server
from flask import Flask, jsonify
from flask_cors import CORS
import redis
import json
app = Flask(__name__)
CORS(app)

# Define a route for the GET request
r = redis.Redis(host='localhost', port=6379, db=0)


@app.route('/getMenu', methods=['GET'])
def get_menu():

    # Get all the coffee names
    coffee_names = r.smembers('coffee:names')

    # get all the coffees
    coffee_menu = []

    # Iterate over the coffee names and print the data for each coffee
    for coffee_name in coffee_names:  # coffee_name = b'Espresso'
        price = r.zscore('coffee:prices', coffee_name)  # price = 2.5
        # description = b'Espresso is a coffee-brewing method of Italian origin, in which a small amount of nearly boiling water is forced under pressure through finely-ground coffee beans.'
        description = r.hget('coffee:description', coffee_name)
        if description is None:
            description_str = ""
        else:
            description_str = description.decode('utf-8')
        # img = b'https://upload.wikimedia.org/wikipedia/commons/4/45/A_small_cup_of_coffee.JPG'
        img = r.hget('coffee:img', coffee_name)
        if img is None:
            img_str = ""
        else:
            img_str = img.decode('utf-8')

        coffee = {
            'name': coffee_name.decode('utf-8'),
            'price': price,
            'description': description_str,
            'img': img_str
        }

        coffee_menu.append(coffee)

    # convert the coffee menu to JSON array
    coffee_menu_json = json.dumps(coffee_menu)
    return coffee_menu_json


if __name__ == '__main__':
    app.run(debug=True)
