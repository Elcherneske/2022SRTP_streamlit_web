class parameters:
    parameter = ""
    db = None
    para_table_name = "parametertable"
    def __init__(self, db):
        self.db = db
        self.db.create_table("parametertable",("parameter", "TEXT", "value", "TEXT"))

    def change_parameter(self, para_name, value):
        if(self.db.find_value_exist(self.para_table_name, ("parameter", ), (para_name, )) == False):
            raise Exception("no existing parameter")
        self.db.delete_value(self.para_table_name, ("parameter", ), (para_name, ))
        self.db.insert_value(self.para_table_name, ("parameter", "value"), (para_name, value))

    def add_new_parameter(self, para_name, value):
        if (self.db.find_value_exist(self.para_table_name, ("parameter",), (para_name,)) == True):
            raise Exception("parameter is existing")
        self.db.insert_value(self.para_table_name, ("parameter", "value"), (para_name, value))

    def add_parameter(self, para_name, value):
        if (self.db.find_value_exist(self.para_table_name, ("parameter",), (para_name,)) == True):
            self.change_parameter(para_name, value)
            return
        self.db.insert_value(self.para_table_name, ("parameter", "value"), (para_name, value))


    def get_parameter(self, para_name):
        if (self.db.find_value_exist(self.para_table_name, ("parameter",), (para_name,)) == False):
            raise Exception("no existing parameter")
        result = self.db.select_value(self.para_table_name, ("parameter", ), (para_name,))
        return result[0][1]
