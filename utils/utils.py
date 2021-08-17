import os, json

def open_json(json_file):
    with open(json_file) as data:
        return json.load(data)

def write_dotenv(env, file=".env"):
    with open(".env", "w") as f:
        for i in env:
            f.write(f'{i}={env[i]}\n')