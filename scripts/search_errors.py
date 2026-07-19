import os
import json

error_folder = "../errors"

search = input("Enter error name: ")

for file in os.listdir(error_folder):

    if file.endswith(".json"):

        filepath = os.path.join(error_folder, file)

        with open(filepath, "r") as f:

            data = json.load(f)

            if search.lower() in data["error_name"].lower():

                print("\nFound Error")
                print("Code:", data["error_code"])
                print("Name:", data["error_name"])
                print("Cause:", data["cause"])
                print("Solution:", data["solution"])

# Made with Bob
