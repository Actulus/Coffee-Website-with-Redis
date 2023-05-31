#!/bin/env python3
import redis


def add_coffee(coffee_name, coffee_description, coffee_image, coffee_price):
    # Connect to Redis
    r = redis.Redis(host='localhost', port=6379, db=0)

    # Generate a new ID for the coffee
    # coffee_id = r.incr('coffee:ids')

    # Add the coffee details to the hashes
    r.hset('coffee:description', coffee_name, coffee_description)
    r.hset('coffee:img', coffee_name, coffee_image)

    # Add the coffee name to the set
    r.sadd('coffee:names', coffee_name)

    # Add the coffee price to the sorted set
    r.zadd('coffee:prices', {coffee_name: coffee_price})

    print(f"Successfully added coffee '{coffee_name}' to the database.")


# Example usage
add_coffee("Pumpkin Spice Latte", "Coffee drink made with a mix of traditional fall spice flavors (cinnamon, nutmeg, and clove), steamed milk, espresso, and often sugar, topped with whipped cream and pumpkin pie spice.",
           "https://www.inspiredtaste.net/wp-content/uploads/2011/11/Pumpkin-Spice-Latte-Recipe-1200.jpg", 5.99)
