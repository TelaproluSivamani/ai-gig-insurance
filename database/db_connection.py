import mysql.connector

def get_connection():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sivamani@48",
        database="gig_insurance"
    )

    return conn