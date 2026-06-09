import json

# if you need to handle errors, you can use a try/except block. This is useful for example when working with json, because if you try to load something that isn't valid json, it will raise an error. You can catch that error and handle it gracefully instead of crashing your program.
try:
    json.loads(
        "this is not json"
    )  # this will raise an error because it's not valid json
except json.JSONDecodeError as e:
    print("There was an error decoding the json:", e)

print("This will still run even though there was an error above")
