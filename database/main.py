import sqlite3


#create connection and cursor
connection = sqlite3.connect('pokemon.db')
cursor = connection.cursor()

#create player table 
cursor.execute("""
            CREATE TABLE IF NOT EXISTS players (
                player_id INTEGER PRIMARY KEY,
                player_name VARCHAR (20) NOT NULL, 
                password_hash VARCHAR (255) NOT NULL,
                level INT NOT NULL,
                experience INT NOT NULL)
            """)


#player creation
start = input("Do you have a character(y/n):")
if start == "n":
    name = input("Enter Your Name: ")
    password_hash = input("Enter Your Password: ")


    cursor.execute("""
                    INSERT INTO players(
                    player_name,
                    password_hash, 
                    level, 
                    experience)
                    VALUES (?,?,?,?)
                    """, (name, password_hash, 1, 0))

    print("character created!")
    print(f"Welcome {name}")


elif start == "y":

    name = input("Player name: ")


cursor.execute("""
                UPDATE players
                SET experience = experience + 100
                WHERE player_name = ?
                """, (name,))

if cursor.rowcount == 1:
    # success
    cursor.execute("SELECT * FROM players WHERE player_name = ?", (name,))
    player = cursor.fetchone()
    lvl = player[3]
    xp = player[4]

    xp_required = lvl * 100
    

    if xp >= xp_required:
        xp -= xp_required
        lvl += 1

        cursor.execute("""
                        UPDATE players
                        SET level = ?
                        WHERE player_name = ?
                        """, (lvl, name))
        if cursor.rowcount == 1:
            print(f"congratulations {name} is now level {lvl}")
        else:
            print(f"{name}'s is still level {lvl}")

    
else:
    print("null no player")


    

connection.commit()
connection.close()



