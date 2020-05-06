DATABASES = {
    'default' : {
        'ENGINE' : 'django.db.backends.mysql',
        'NAME' : 'Proj4DB',
        'USER' : 'AuthorizedUser',
        'PASSWORD' : 'AuthorizedUser',
        'HOST' : 'localhost',
        'PORT' : '3306',
    }
}

from django import connection

def insertandtxt():
    sql = """INSERT INTO Proj4DB.faculty (firstname, lastname, coursename, courselocation) VALUES (Luke, Scanlon, BUS443, B410)")"""
    sql2 = """SELECT * FROM Proj4DB.faculty)"""
    cursor = connection.cursor()
    cursor.execute(sql)
    cursor.execute(sql2)
    with open ("facultyinfo.txt", "w") as f:
        for row in cursor:
            print(row[0], file=f)
    f.close()