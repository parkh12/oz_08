import pymysql

connection = pymysql.connect(
    host='localhost',  
    user='root',      
    password='',  
    db='db_test',      
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

with connection.cursor() as cursor:

    # 문제1

    sql = 'first_name,last_name,email,password,address,gender,is_active,is_staff) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
    cursor.execute(sql, ('8ki', 'joa', 'joa@.com', 3412, 'Seoul', 'MALE', 1, 1))
    connection.commit()

    #문제2

    sql = "UPDATE users SET address=%s WHERE id=%s"
    cursor.execute(sql, ('Seoul', 11))
    connection.commit()

    #문제3

    sql = "INSERT INTO sales_records (user_id, store_id, is_refund, created_at) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (11, 1, 0, 'datetime.now()'))
    connection.commit()
    sql = "INSERT INTO sales_items (sales_record_id, product_id, quantity, created_at) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (11, 1, 3, 'datetime.now()'))
    connection.commit()
    sql = "INSERT INTO sales_items (sales_record_id, product_id, quantity, created_at) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (11, 2, 2, 'datetime.now()'))
    connection.commit()
    sql = "INSERT INTO sales_items (sales_record_id, product_id, quantity, created_at) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (11, 5, 5, 'datetime.now()'))
    connection.commit()

    #문제4

    sql = "INSERT INTO order_records (employee_id, supplier_id, raw_material_id, quantity) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (1, 1, 1, 10))
    connection.commit()
    sql = "INSERT INTO order_records (employee_id, supplier_id, raw_material_id, quantity) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (2, 1, 2, 10))
    connection.commit()
    sql = "INSERT INTO order_records (employee_id, supplier_id, raw_material_id, quantity) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (3, 1, 5, 10))
    connection.commit()

    #문제5

    sql = "INSERT INTO stocks (raw_material_id, pre_quantity, quantity, change_type, store_id) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, (1, 30, 10, 'OUT', 1))
    connection.commit()
    sql = "INSERT INTO stocks (raw_material_id, pre_quantity, quantity, change_type, store_id) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, (2, 30, 10, 'OUT', 1))
    connection.commit()
    sql = "INSERT INTO stocks (raw_material_id, pre_quantity, quantity, change_type, store_id) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, (5, 10, 5, 'OUT', 1))
    connection.commit()
    sql = "select * from stocks order by create_at desc limit 3"
    cursor.execute(sql)
    for i in cursor.fetchall():
        print(i)

    #문제6

    sql = '''
    SELECT u.first_name, u.last_name, p.name AS product_name, p.price, si.quantity, (p.price * si.quantity) AS total_price, sr.created_at
    FROM users u
    JOIN sales_records sr ON u.id = sr.user_id
    JOIN sales_items si ON sr.id = si.sales_record_id
    JOIN products p ON si.product_id = p.id
    WHERE u.id = %s
    ORDER BY p.price DESC
    '''
    cursor.execute(sql, (11))
    for i in cursor.fetchall():
        print(i)

    cursor.close()