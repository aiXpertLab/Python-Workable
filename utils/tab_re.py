import streamlit as st
import psycopg2,os

def db_general():
    st.info("""
        In 1951, mathematician **Stephen Cole Kleene** described the concept of a regular language, a language that is recognizable by a finite automaton and formally expressible using regular expressions. 
    """)

def db_email():
    st.code("""
        pass
    """)

def db_postgreql():
    st.code("""
    import psycopg2,os
    uri = os.environ.get('POSTGRESQL_URI')
    def main():
        conn = psycopg2.connect(uri)
        query_sql = 'SELECT VERSION()'
        cur = conn.cursor()
        cur.execute(query_sql)
        version = cur.fetchone()[0]
        st.success(version)
    """)

    uri = os.environ.get('POSTGRESQL_URI')
    conn = psycopg2.connect(uri)
    query_sql = 'SELECT VERSION()'
    cur = conn.cursor()
    cur.execute(query_sql)
    version = cur.fetchone()[0]
    st.success(version)
   

def db_mysql1():
    import pymysql, os
    st.code("""
            import pymysql, os
            timeout = 10
            connection = pymysql.connect(
                charset="utf8mb4",
                connect_timeout=timeout,
                cursorclass=pymysql.cursors.DictCursor,
                db="defaultdb",
                host="mysql-omni-omni.b.aivencloud.com",
                password= os.environ.get('MYSQL_PWD'),
                read_timeout=timeout,
                port=21906,
                user="avnadmin",
                write_timeout=timeout,
            )
            
            try:
                cursor = connection.cursor()
                cursor.execute("CREATE TABLE mytest2 (id INTEGER PRIMARY KEY)")
                cursor.execute("INSERT INTO mytest (id) VALUES (1), (2)")
                cursor.execute("SELECT * FROM mytest")
                st.success(cursor.fetchall())
            except:
                st.success('table created')
            finally:
                connection.close()    
            
            st.image("./images/zhang.gif")

    """)
    timeout = 10
    connection = pymysql.connect(
        charset="utf8mb4",
        connect_timeout=timeout,
        cursorclass=pymysql.cursors.DictCursor,
        db="defaultdb",
        host="mysql-omni-omni.b.aivencloud.com",
        password= os.environ.get('MYSQL_PWD'),
        read_timeout=timeout,
        port=21906,
        user="avnadmin",
        write_timeout=timeout,
    )
    
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE mytest2 (id INTEGER PRIMARY KEY)")
        cursor.execute("INSERT INTO mytest (id) VALUES (1), (2)")
        cursor.execute("SELECT * FROM mytest")
        st.success(cursor.fetchall())
    except:
        st.success('table created')
    finally:
        connection.close()    
    
    st.image("./images/zhang.gif")

def db_mysql2():
    import mysql.connector
    st.code("""
            import mysql.connector
            mydb = mysql.connector.connect(
                host="mysql-omni-omni.b.aivencloud.com",
                port='21906',
                user="avnadmin",
                password= os.environ.get('MYSQL_PWD'),
                database = 'defaultdb',
            )

            show_existing_db = "SHOW DATABASES"

            with mydb.cursor() as cursor: 
                cursor.execute(show_existing_db)
                for db in cursor:
                    st.success(db)

            mycursor = mydb.cursor()
            mycursor.execute("SHOW TABLES")
            for x in mycursor: 
                st.success(x)
            
            
            """)
    
    mydb = mysql.connector.connect(
        host="mysql-omni-omni.b.aivencloud.com",
        port='21906',
        user="avnadmin",
        password= os.environ.get('MYSQL_PWD'),
        database = 'defaultdb',
    )

    show_existing_db = "SHOW DATABASES"

    with mydb.cursor() as cursor: 
        cursor.execute(show_existing_db)
        for db in cursor:
            st.success(db)

    mycursor = mydb.cursor()
    mycursor.execute("SHOW TABLES")
    for x in mycursor: 
        st.success(x)
    
    # mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
    return mydb