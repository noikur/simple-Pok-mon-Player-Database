import sqlite3


#create connection and cursor
conncection = sqlite3.connect('pokemon.db')
cursor = conncection.cursor()

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
player_name = input("Enter Your Name: ")
password_hash = input("Enter Your Password: ")


cursor.execute("""
                INSERT INTO players(
                player_name,
                password_hash, 
                level, 
                experience)
                VALUES (?,?,?,?)
                """, (player_name, password_hash, 1, 0))


conncection.commit()
conncection.close()
