import json

data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}


with open("db.json", "r") as write_file:
    print(write_file)