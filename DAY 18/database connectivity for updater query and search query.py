import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="your_database"
    )

#search query

def search_user(user_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM users WHERE id = %s"
    cursor.execute(query, (user_id,))

    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return result
user = search_user(1)
print(user)

#update query

def update_user_email(user_id, new_email):
    conn = get_connection()
    cursor = conn.cursor()

    query = "UPDATE users SET email = %s WHERE id = %s"
    cursor.execute(query, (new_email, user_id))

    conn.commit()

    rows_affected = cursor.rowcount

    cursor.close()
    conn.close()

    return rows_affected

rows = update_user_email(1, "new@email.com")
print(f"Updated {rows} row(s)")
