import sqlite3

path = 'C:/Users/salam/Desktop/testing/testing_project.db'
con = sqlite3.connect(path)
cur = con.cursor()

cur.execute('DROP TABLE Ceremony')
# cur.execute('DELETE FROM Ceremony')
con.commit()
cur.execute('DROP TABLE Manager')
# cur.execute('DELETE FROM Manager')
con.commit()
cur.execute('DROP TABLE Customer')
# cur.execute('DELETE FROM Customer')
con.commit()
# cur.execute('DROP TABLE Customer')
# con.commit()
# cur.execute('DROP TABLE Customer')
# cur.execute('SELECT * FROM Customer')
# c = cur.fetchall()
# con.commit()
con.close()
# print(bool(c))
# print(c)
# cur.execute("SELECT * FROM Ceremony WHERE Ceremony_name = ?", ('sjdkf;alksfj', ))
# c = cur.fetchone()


