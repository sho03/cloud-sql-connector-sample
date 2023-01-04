from google.cloud.sql.connector import Connector
import sqlalchemy
import pymysql

# initialize Connector object
connector = Connector()

# function to return the database connection
def getconn() -> pymysql.connections.Connection:
    try:
        conn: pymysql.connections.Connection = connector.connect(
            "project:region:instance",
            "pymysql",
            user="<user>",
            password="<password>",
            db="<db-name>"
        )
        return conn
    except:
        print('error')

# create connection pool
pool = sqlalchemy.create_engine(
    "mysql+pymysql://",
    creator=getconn,
)

with pool.connect() as db_conn:
    query = "select * from user"
    result = db_conn.execute(query).fetchall()

    for row in result:
        print(row)