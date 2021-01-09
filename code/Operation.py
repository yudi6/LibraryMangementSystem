INSERT_NEW_BOOK = """INSERT INTO book(BookID, BookName, Author, Publisher, sellPrice)
VALUES (%s, %s, %s, %s, %s);"""

INSERT_NEW_SUPPLIER = """INSERT INTO supplier(supplierID, supplierName)
VALUES (%s, %s);"""

INSERT_SUPPLIER_PRICE = """INSERT INTO supplierPrice(supplierID,BookID,Price)
VALUES (%s, %s, %s);"""

PURCHASE_BOOK = """INSERT INTO supplyList(supplierID,BookID,Price,Amount)
VALUES (%s, %s, %s, %s);"""

INSERT_NEW_BOOK_INTO_STORE ="""INSERT INTO storehouse(BookID,Price,Amount)
VALUES (%s, %s, %s)"""

SHOW_INF_BY_BOOK_NAME="""select BookID, supplierID, price
from book natural join supplierPrice 
where book.BookName = %s;"""

SHOW_SALE_BY_SALEID ="""select sale.BookID, BookName, Amount 
from book, sale 
where book.BookID = sale.BookID and sale.ID = %s;"""

SHOW_ALL_SALE = """select sellTime, sale.BookID, book.BookName, storehouse.Price,  sale.Amount 
from book, sale , storehouse 
where book.BookID = sale.BookID and sale.BookID = storehouse.BookID;"""

SHOW_STORE = """select s.bookid,b.bookname,s.amount
from book b natural join storehouse s;"""