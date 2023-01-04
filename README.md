# Cloud SQL Connector Sample
[reference](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector#how-to-use-this-connector)

# How to use
## Install dependencies
```shell
$ pip install "cloud-sql-python-connector[pymysql]"
$ pip install sqlalchemy
$ pip install PyMySQL
```

## Write your environment
Write your Cloud SQL environment variables on `main.py` like below.
```python
def getconn() -> pymysql.connections.Connection:
    try:
        conn: pymysql.connections.Connection = connector.connect(
            "your instance like <project:region:instance>",
            "pymysql",
            user="<db-user>",
            password="<db-password>",
            db="<db-name>"
        )
        return conn
    except:
        print('error')
```

