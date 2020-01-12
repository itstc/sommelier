def connect(path):
    global connection, cursor, p
    connection = sqlite3.connect(path)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute(' PRAGMA foreign_keys=ON; ')
    insert_statement = '''INSERT INTO TABLE wine (id, name, description, price, points) VALUES (:title,:country,:description,:price,:points);'''
    cursor.execute(insert_statement, {"title":p.name,"country":p.country,"description":p.description,"price":p.price,"points":p.points})
    connection.commit()
  
def main():
    import csv
    import sqlite3
    import os    
    global connection, cursor, p
    path="./wines.db" 
    #path =  "C:\\...." # Set path of new directory here
    #os.chdir(path) # changes the directory
    from dashboard.models import Wine # imports the model
    with open('winemag-data-130k-v2.csv') as csvfile:
        reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['country'])
        p = Wine(name=row['title'], country=row['country'], description=row['description'], price=row['price'], points=row['points'])
        connect(path) 
        p.save()
        connection.commit()
        exit()    
    return

main()