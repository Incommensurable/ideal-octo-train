# json is a common format for data, and python has a built in library for working with it
import json

person_info = json.loads(
    '{"name": "John", "age": 30}'
)  # converts a json string into a python dictionary
print(person_info["name"])  # prints "John"
