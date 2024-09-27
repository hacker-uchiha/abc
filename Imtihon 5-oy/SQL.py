import mysql.connector

class SQL:
    def __init__(self) -> None:
        self.connect()
        self.createdatabase()
    
    def connect(self):
        self.database = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'suxrob2006'
        )
    
    def createdatabase(self):
        self.data = self.database.cursor()
        self.data.execute("CREATE DATABASE Suxrob_project IF NOT EXISTS")
        self.database.commit()
        self.data.execute("USE Suxrob_project")
        
    