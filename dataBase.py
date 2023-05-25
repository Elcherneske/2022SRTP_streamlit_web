import mysql.connector
class mDatabase:
    mydb = None
    db_cursor = None
    host = ''
    user = ''
    password = ''
    def __init__(self, host, user, password, database):
        self.password = password
        self.host = host
        self.user = user
        self.mydb = mysql.connector.connect(
            host=host,
            user=user,
            passwd=password,
            database=database,
            auth_plugin='mysql_native_password'
        )
        self.db_cursor = self.mydb.cursor()

    def get_Database_Cursor(self):
        return self.db_cursor

    def select_database(self,name):
        self.db_cursor.execute("use %s",name)

    def create_table(self, name, kind):
        size = (int)(len(kind)/2)
        string = 'CREATE TABLE IF NOT EXISTS ' + name + '('
        for i in range(size):
            if i == 0:
                string = string + kind[2 * i] + ' ' + kind[2 * i + 1]
            else:
                string = string + ', ' + kind[2*i] + ' ' + kind[2*i + 1]
        string = string + ')'
        self.db_cursor.execute(string)

    def drop_table(self, name):
        string = 'DROP TABLE IF EXISTS ' + name
        self.db_cursor.execute(string)

    def select_value(self, table_name, field, value):
        field_size = len(field)
        value_size = len(value)
        if (field_size != value_size):
            raise Exception("length not match")
            return
        else:
            size = field_size
        string = 'SELECT * FROM ' + table_name + ' WHERE '
        value_string = self.construct_field_value_string(size,field,value)
        string += value_string
        self.db_cursor.execute(string)
        result = self.db_cursor.fetchall()
        return result

    def select_all_value(self, table_name):
        string = "select * from " + table_name
        self.db_cursor.execute(string)
        result = self.db_cursor.fetchall()
        return result

    def find_value_exist(self, table_name, field, value):
        result = self.select_value(table_name,field,value)
        if(result):
            return True
        else:
            return False

    def insert_value(self, table_name, field, value):
        field_size = len(field)
        value_size = len(value)
        if(field_size!=value_size):
            raise Exception("length not match")
            return
        else:
            size = field_size
        string = "INSERT INTO " + table_name
        field_string = '(' + self.construct_value_string(field) + ')'
        value_string = '(' + self.construct_value_string(value) + ')'
        string += field_string + " VALUES" + value_string
        self.db_cursor.execute(string)
        self.mydb.commit()

    def delete_value(self, table_name, field, value):
        field_size = len(field)
        value_size = len(value)
        if (field_size != value_size):
            raise Exception("length not match")
            return
        else:
            size = field_size

        string = "DELETE FROM " + table_name + " WHERE " + self.construct_field_value_string(size, field, value)
        self.db_cursor.execute(string)
        self.mydb.commit()


    def construct_field_value_string(self, size, field, value):
        value_string = ''
        for i in range(size):
            if i == 0:
                value_string += (field[i] + " = " + value[i])
            else:
                value_string += (" AND " + field[i] + " = " + value[i])
        return value_string
    def construct_value_string(self, value):
        value_string = ''
        size = len(value)
        for i in range(size):
            if i == 0:
                value_string += (value[i])
            else:
                value_string += (", " + value[i])
        return value_string