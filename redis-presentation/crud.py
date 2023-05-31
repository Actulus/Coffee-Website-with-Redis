#!/bin/env python3

import redis

# connect to redis
redis_client = redis.Redis(host='localhost', port=6379, db=0)

# create


def create_user(user_id, name, email):
    user = {
        'id': user_id,
        'name': name,
        'email': email
    }
    redis_client.hmset(f'user:{user_id}', user)


# read
def get_user(user_id):
    # formatted string where user_id is dinamicallz inserted into the string
    user = redis_client.hgetall(f'user:{user_id}')
    return user

# update


def update_user_email(user_id, new_email):
    redis_client.hset(f'user:{user_id}', 'email', new_email)

# delete


def delete_user(user_id):
    redis_client.delete(f'user:{user_id}')


# example usage
create_user(1, 'John', 'john_doe@example.com')
create_user(2, 'Jane', 'jane.smith@example.com')

user_1 = get_user(1)
print(user_1)

update_user_email(2, 'jane.smith@new_example.com')
user_2 = get_user(2)
print(user_2)

delete_user(1)
user_1 = get_user(1)
print(user_1)
