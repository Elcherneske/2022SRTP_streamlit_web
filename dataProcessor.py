class dataProcessor:
    username = ""
    db = None

    def __init__(self, username, db):
        self.db = db
        self.username = username
