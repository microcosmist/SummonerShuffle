from dotenv import load_dotenv
import os   
import mysql.connector


load_dotenv()

conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
)

#test db connection
if conn.is_connected():
    print("connected")
else:
    print("not connected")


cursor = conn.cursor()


#List to hold roles, used to search through our sorted images folder
roles = ["Jungle", "Top", "Mid", "Bot", "Support"]


# Fill Role table in database - Role holds name and role
# Currently O(n*m) time, can be improved using dictionary
# Can improve database insertion with batch insertion

for role in roles:
    names_png = os.listdir(f"Web Dev\Summoner Shuffle\champs-role-sorted\{role}")
    for champ in names_png:
        try:
            query = "INSERT INTO Role(name, role) VALUES (%s, %s)"
            cursor.execute(query, (champ.split('.png')[0], role))
            conn.commit()
            print(f"{champ.split('.png')[0]} with {role} role inserted successfully")
        except Exception as e:
            print("error inserting data: ", e)
            conn.rollback()


# Fill Champion table in database - Champion holds name and path to icon
#Can improve database insertion with batch insertion

names = os.listdir(f"Web Dev\Summoner Shuffle\champs")
for champ in names:
    try:
        query = "INSERT INTO Champion(name, path) VALUES (%s, %s)"
        path = f"s3://summoner-shuffle/champs/{champ}"
        cursor.execute(query, (champ.split('.png')[0], path))
        conn.commit()
        print(f"{champ.split('.png')[0]} inserted successfully")
    except Exception as e:
        print("error inserting data: ", e)
        conn.rollback()


