import os
from dotenv import load_dotenv
import mysql.connector
load_dotenv()

class Connection():

    def query(self, filter):
        mydb = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            passwd=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME'),
            port=os.getenv('DB_PORT')
        )
        conection = mydb.cursor()
        conection.execute(filter)
        myresult = conection.fetchall()
        return myresult







