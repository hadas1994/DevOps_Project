import pymysql


def get_data(user_id):
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='nUaXW57hSo', passwd='3QG85WHfcS',
                           db='nUaXW57hSo')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM nUaXW57hSo.users;")
    for row in cursor:
        id = row[0]
        if str(id) == user_id:
            cursor.close()
            conn.close()
            return row


def insert_user(user_id, user_name):
    import datetime
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='nUaXW57hSo', passwd='3QG85WHfcS',
                           db='nUaXW57hSo')
    conn.autocommit(True)
    cursor = conn.cursor()
    now = datetime.datetime.now()
    formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute("INSERT into nUaXW57hSo.users (user_id, user_name, creation_date) VALUES (%s, %s, %s)" %
                   (user_id, "'" + user_name + "'", "'" + formatted_date + "'"))
    cursor.close()
    conn.close()


def delete_data(user_id):
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='nUaXW57hSo', passwd='3QG85WHfcS',
                           db='nUaXW57hSo')
    conn.autocommit(True)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM nUaXW57hSo.users WHERE user_id = %s" % "'"+user_id+"'")
    cursor.close()
    conn.close()


def put_data(user_id, user_name):
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='nUaXW57hSo', passwd='3QG85WHfcS',
                           db='nUaXW57hSo')
    conn.autocommit(True)
    cursor = conn.cursor()
    cursor.execute("UPDATE nUaXW57hSo.users SET user_name = %s WHERE user_id = %s" % ("'"+user_name+"'", user_id))
    cursor.close()
    conn.close()
