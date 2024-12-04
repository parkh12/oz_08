import pymysql

connection = pymysql.connect(
    host='localhost',  
    user='root',      
    password='',  
    db='test',      
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

with connection.cursor() as cursor:
    # 문제1
    sql = 'INSERT INTO Products(productName, price, stockQuantity) VALUES (%s,%s,%s)'
    cursor.execute(sql, ('Python Book', 10000, 10))
    connection.commit()

    # 문제2
    cursor.execute("SELECT * FROM Products")
    for book in cursor.fetchall():
        print(book)

    #문제3
    sql = 'UPDATE Products SET stockQuantity = stockQuantity -%s WHERE productID = %s'
    cursor.execute(sql,(1,1))
    connection.commit()

    #문제4
    sql = 'SELECT customerID, SUM(totalAmount) AS totalAmount FROM Orders GROUP BY customerID'
    cursor.execute(sql)
    datas = cursor.fetchall()

    #문제5
    sql = 'UPDATE Customers SET email=%s WHERE customerID = %S'
    cursor.execute(sql, ('update@update.com', 1))
    connection.commit()

    #문제6
    sql = 'DELETE FROM Orders WHERE orderID = %s'
    cursor.execute(sql, (15))
    connection.commit()

    #문제7
    sql = 'SELECT * FROM Products WHERE productName LIKE %s'
    cursor.execute(sql, ('%Book%'))
    datas = cursor.fetchall()

    #문제8
    sql = 'SELECT * FROM Oreders WHERE customerID = %s'
    cursor.execute(sql,(1))
    datas = cursor.fetchall()

    #문제9
    sql = '''
        SELECT customerID, COUNT(*) as ordercount * 
        FROM Oreders GROUP BY customerID 
        OREDER BY orderCount DESC LIMIT 1'
        '''
    cursor.execute(sql)
    datas = cursor.fetchone()


cursor.close()