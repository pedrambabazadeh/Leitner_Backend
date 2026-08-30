import os
import pymysql
from dotenv import load_dotenv
from urllib.parse import urlparse

load_dotenv()

database_url = os.getenv("DATABASE_URL")

if not database_url:
    raise RuntimeError("DATABASE_URL not found in .env")

parsed = urlparse(database_url)

host = parsed.hostname
port = parsed.port or 3306
user = parsed.username
password = parsed.password
database = parsed.path.lstrip("/")

print(f"Connecting to MySQL at {host}:{port} as {user}...")

try:
    connection = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password
    )

    print("Connected to MySQL.")

    with connection.cursor() as cursor:
        cursor.execute(
            f"CREATE DATABASE IF NOT EXISTS `{database}` "
            "CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"
        )

    connection.commit()
    connection.close()

    print(f"Database '{database}' created successfully.")

except Exception as e:
    print("Could not create database:")
    print(type(e).__name__, e)