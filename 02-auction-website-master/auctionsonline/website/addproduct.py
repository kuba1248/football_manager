import sqlite3

conn = sqlite3.connect('db.sqlite3')


c = conn.cursor()

print('connection successfull')


# c.execute("UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='website_product'")


# c.execute("INSERT INTO website_product VALUES ('messi', 'images/game-05.png', 'FWD', '1', 'CON' )")

addprods = """INSERT INTO website_product (title, image, description, quantity, category) 
VALUES ('messi', 'images/game-05.png', 'FWD', '1', 'CON' )"""


INSERT INTO website_product (title, image, description, quantity, date_posted, category)

VALUES ('messi', 'images/game-05.png', 'FWD', '1', '2022-08-03 17:45:25.053226','CON' ),
('salah', 'images/game-05.png', 'FWD', '1', '2022-08-03 17:45:25.053226','CON' ),
('pele', 'images/game-05.png', 'FWD', '1', '2022-08-03 17:45:25.053226','CON' ),
('ribery', 'images/game-05.png', 'FWD', '1', '2022-08-03 17:45:25.053226','CON' ),
('silva', 'images/game-05.png', 'FWD', '1', '2022-08-03 17:45:25.053226','CON' ),
('haaland', 'images/game-05.png', 'FWD', '1', '2022-08-03 17:45:25.053226','CON' ),
('de Jong', 'images/game-05.png', 'FWD', '1', '2022-08-03 17:45:25.053226','CON' ),
('maradonna', 'images/game-05.png', 'FWD', '1', '2022-08-03 17:45:25.053226','CON' ),
('zidane', 'images/game-05.png', 'FWD', '1', '2022-08-03 17:45:25.053226','CON' ),
('alves', 'images/game-05.png', 'FWD', '1', '2022-08-03 17:45:25.053226','CON' ),
('ronaldinho', 'images/game-05.png', 'FWD', '1', '2022-08-03 17:45:25.053226','CON' ),
('ederson', 'images/game-05.png', 'FWD', '1', '2022-08-03 17:45:25.053226','CON' ),
('buffon', 'images/game-05.png', 'FWD', '1', '2022-08-03 17:45:25.053226','CON' ),
('roberto carlos', 'images/game-05.png', 'FWD', '1', '2022-08-03 17:45:25.053226','CON' ),
('puyol', 'images/game-05.png', 'FWD', '1', '2022-08-03 17:45:25.053226','CON' ),
('ballack', 'images/game-05.png', 'FWD', '1', '2022-08-03 17:45:25.053226','CON' ),
('beckham', 'images/game-05.png', 'FWD', '1', '2022-08-03 17:45:25.053226','CON' ),
('hakan sukur', 'images/game-05.png', 'FWD', '1', '2022-08-03 17:45:25.053226','CON' ),
('arda', 'images/game-05.png', 'FWD', '1', '2022-08-03 17:45:25.053226','CON' ),
('rivaldo', 'images/game-05.png', 'FWD', '1', '2022-08-03 17:45:25.053226','CON' ),
('shevchenko', 'images/game-05.png', 'FWD', '1', '2022-08-03 17:45:25.053226','CON' ),
('iniesta', 'images/game-05.png', 'FWD', '1', '2022-08-03 17:45:25.053226','CON' ),
('ryan giggs', 'images/game-05.png', 'FWD', '1', '2022-08-03 17:45:25.053226','CON' ),
('zambrotta', 'images/game-05.png', 'FWD', '1', '2022-08-03 17:45:25.053226','CON' ),
('batistuta', 'images/game-05.png', 'FWD', '1', '2022-08-03 17:45:25.053226','CON' );












c.execute(addprods)

conn.commit()

print('Command executed successfully!!!')

# close our connection
conn.close()


#     a = Product()
#     a.title = "messi"
#     a.description = "Sony's PlayStation 4 Pro 1TB"
#     a.quantity = 8
#     a.category = "CON"
#     a.image.save('console-01.png', File(open('website/static/images/products/console-01.png', 'rb')))
#