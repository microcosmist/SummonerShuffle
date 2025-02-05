import os   
import json  

roles = ["Jungle", "Top", "Mid", "Bot", "Support"]
imagePaths = []

for role in roles:
    
    full_path = fr"Web Dev\Summoner Shuffle\champs-role-sorted\{role}"
    images = os.listdir(full_path)

    for champ_name in images:
        imagePaths.append(f"https://d2ly2ivukf9hi9.cloudfront.net/champs/{champ_name}") 

    # Writes to JSON file
    json_path = f"aws_champIcons{role}.json"
    with open(json_path, 'w') as jsonFile:
        json.dump(imagePaths, jsonFile, indent=2)

    imagePaths.clear()
