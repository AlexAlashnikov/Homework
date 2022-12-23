import sqlite3 as sq 

with sq.connect('chinook.db') as con:
    cur = con.cursor()

    cur.execute("SELECT sum(Bytes) FROM tracks")
    sum_bytes = cur.fetchone()
    for sum in sum_bytes:
        print(f"Sum of bytes = {sum} \n")

    cur.execute("""SELECT sum(Total.c) FROM(SELECT count(*) as c FROM employees
                UNION ALL SELECT count(*) as c FROM customers) Total""")
    result = cur.fetchone()
    for res in result:
        print(f"Total records = {res}\n")

    cur.execute("""SELECT name FROM tracks
                WHERE AlbumId = (SELECT AlbumId FROM albums WHERE Title = 'A-Sides')
                ORDER BY name ASC""")
    tracks = cur.fetchall()
    for all in tracks:
        print(f"Track from the album A-Sides = {all}")
    print('\t')

    cur.execute("""SELECT albums.Title, sum(tracks.UnitPrice) as all_price FROM tracks
                LEFT JOIN albums ON tracks.AlbumId = albums.AlbumId
                GROUP BY Title;""")
    all_price = cur.fetchall()
    for price in all_price:
        print(f"Album : {price[0]} = {price[1]:.2f} $")