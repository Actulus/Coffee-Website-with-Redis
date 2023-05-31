#!/bin/env python3

import redis

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# Define the new coffee data
new_coffee = {
    'name': 'Cappuccino',
    'price': 3.50,
    'description': 'Espresso with milk and milk foam'
}

# Add the new coffee data to the relevant Redis data structures
r.sadd('coffee:names', new_coffee['name'])  # sethez adja hozza a kave nevet
# sorted sethez adja hozza a kave nevet es arat
r.zadd('coffee:prices', {new_coffee['name']: new_coffee['price']})

# Confirm that the data was added successfully
print('Added new coffee:', new_coffee['name'])  # kiirja a kave nevet
