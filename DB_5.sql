-- 1
INSERT INTO users(id,first_name,last_name,email,password,address,contact,gender,is_active,is_staff)
VALUES (2,'hs','park','fdas@.com','1111','ewrq','1423','MALE',1,1),
	(3,'john','park','acxvz@.com','1111','dfgs','2341','FEMALE',1,1),
	(4,'jjong','paik','asdfdas3@.com','1111','ghnf','2564','FEMALE',1,1),
	(5,'sin','hwnag','aqsfdf@.com','1111','d1hrteyg','5423','MALE',1,1),
	(6,'orc','man','afdsasd@com','1111','das124f','6574','FEMALE',1,1),
	(7,'look','ki','asfdsaf4df@com','1111','dafdsasf','1432','FEMALE',1,1),
	(8,'u','xiao','as1fewq4df@com','1111','da1bvc','5674','MALE',1,1),
	(9,'miyuki','haruki','asd1hgtdfrsf@com','1111','da1qwer','2345','MALE',1,1),
	(10,'hyun','park','fdsae@com','1111','dfdssf','1534','MALE',1,1);

-- 2
INSERT INTO raw_materials(id,name,price)
VALUES (1,'kim',10.00),
	(2,'kim',13.00),
    (3,'kim',10.40),
    (4,'kim',10.60),
    (5,'kim',11.08),
    (6,'kim',15.00),
    (7,'kim',19.00),
    (8,'kim',20.00),
    (9,'kim',30.00),
    (10,'kim',60.00);
INSERT INTO stores(id,name,address,contact,is_active)
VALUES(1,'jjang','dongtan','sadf',1),
	(2,'hwang','soeul','saddf',1),
    (3,'dduck','daegu','sadfdf',0),
    (4,'chick','soeul','saddf',0),
    (5,'cho','dongtan','safsdf',1),
    (6,'bbaek','soeul','sasdadf',1),
    (7,'bbkak','dongtan','sadadf',0),
    (8,'yuo','soeul','safaddf',0),
    (9,'jupy','dongtan','saafdf',1),
    (10,'jjg','soeul','sagwqdf',1);
    
INSERT INTO stocks(id,raw_material_id,pre_quantity,quantity,store_id,create_at)
VALUES (1,1,10,100,1,'2010-01-01 09:00:00'),
	(2,2,20,200,2,'2011-01-01 09:00:00'),
    (3,3,30,300,3,'2012-01-01 09:00:00'),
    (4,4,40,400,4,'2013-01-01 09:00:00'),
    (5,5,50,500,5,'2014-01-01 09:00:00'),
    (6,6,60,600,6,'2015-01-01 09:00:00'),
    (7,7,70,600,7,'2016-01-01 09:00:00'),
    (8,8,80,300,8,'2017-01-01 09:00:00'),
    (9,9,90,400,9,'2018-01-01 09:00:00'),
    (10,10,100,500,10,'2019-01-01 09:00:00');

-- 3 , 4
INSERT INTO sales_records(id,user_id,store_id,is_refund,created_at)
VALUES (1,3,4,1,'2010-01-01 09:00:00'),
	(2,1,1,1,'2010-01-01 09:00:00'),
    (3,3,2,0,'2010-01-01 09:00:00'),
    (4,5,3,1,'2010-01-01 09:00:00'),
    (5,8,4,1,'2010-01-01 09:00:00'),
    (6,2,5,1,'2010-01-01 09:00:00'),
    (7,3,6,0,'2010-01-01 09:00:00'),
    (8,1,8,1,'2010-01-01 09:00:00'),
    (9,10,1,1,'2010-01-01 09:00:00'),
    (10,3,10,1,'2010-01-01 09:00:00');

INSERT INTO products(name,description,price)
VALUES ('car','drive',10.23),
	('ship','drive',14.23),
    ('car','drive',11.23),
    ('airplane','drive',20.23),
    ('car','drive',540.23),
    ('aircar','drive',510.23),
    ('airship','drive',210.23),
    ('car','drive',130.23),
    ('carair','drive',140.23),
    ('air','drive',110.23);

INSERT INTO sales_items(id,sales_record_id,product_id,quantity,created_at)
VALUES (1,3,2,10,'2010-01-01 09:00:00'),
	(2,1,1,20,'2010-01-01 09:00:00'),
    (3,4,5,30,'2010-01-01 09:00:00'),
    (4,6,2,10,'2010-01-01 09:00:00'),
    (5,8,3,50,'2010-01-01 09:00:00'),
    (6,1,1,80,'2010-01-01 09:00:00'),
    (7,3,7,90,'2010-01-01 09:00:00'),
    (8,4,9,20,'2010-01-01 09:00:00'),
    (9,2,1,10,'2010-01-01 09:00:00'),
    (10,3,2,10,'2010-01-01 09:00:00');

-- 5
INSERT INTO employees(id,code,type,user_id,store_id,is_active)
VALUES (1,1,'STAFF',1,1,1),
	(2,2,'STAFF',1,3,1),
    (3,3,'MANAGER',1,5,1),
    (4,4,'STAFF',1,2,1),
    (5,5,'STAFF',1,8,1),
    (6,6,'STAFF',1,2,1),
    (7,7,'MANAGER',1,4,1);

UPDATE employees SET store_id = 5 WHERE user_id =1;
UPDATE employees SET store_id = 7 WHERE user_id =2;
