import os   
import json  

imagePaths = []

# Creates a list of all images. Example: "Ahri.png"
images = os.listdir(r'C:\Users\Samantha Ekanem\Desktop\Projects\Web Dev\Summoner Shuffle\champs')


# Combines the path with the file name to create the full path to the image file
for i in images:
    imagePaths.append(f"https://d2ly2ivukf9hi9.cloudfront.net/champs/{i}")

# Writes to JSON file
with open('aws_champIconsAll.json', 'w') as jsonFile:
    json.dump(imagePaths, jsonFile, indent=2)

