#!/bin/env python3

import redis

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# Delete problematic keys
r.delete('coffee:names')
r.delete('coffee:prices')

# Get all keys in the 'coffee' namespace
keys = r.keys('coffee:*')

# Loop through keys and add coffee prices to the sorted set 'coffee:prices'
for key in keys:
    # coffee:1:price tipusu key-k value-jat adja vissza
    price = r.hget(key, 'price')
    # coffee:1:name tipusu key-k value-jat adja vissza
    name = r.hget(key, 'name')

    # hozzaadjuk a 'coffee:names' set-hez a kave nevet
    r.sadd('coffee:names', name.decode('utf-8'))
    # hozzaadjuk a 'coffee:prices' sorted set-hez a kave nevet es arat
    r.zadd('coffee:prices', {name.decode('utf-8'): float(price)})

print('All coffee data added to sets.')
