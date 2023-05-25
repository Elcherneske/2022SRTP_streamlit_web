from dataBase import mDatabase

class userManagement:
    mydb = None
    def __init__(self, mydb):
        self.mydb = mydb
        self.mydb.create_table("userstable",("username", "TEXT", "password", "TEXT"))

    def add_userdata(self, username, password):
        if(self.mydb.find_value_exist("userstable",("username", ), (username, ))):
            return False
        else:
            self.mydb.insert_value("userstable",("username", "password"), (username,password))
            return True

    def login_user(self, username, password):
        if(self.mydb.find_value_exist("userstable", ("username", "password"), (username,password))):
            data = self.mydb.select_value("userstable", ("username", "password"), (username,password))
            return True
        else:
            return False

    def view_all_users(self):
        return self.mydb.select_all_value()