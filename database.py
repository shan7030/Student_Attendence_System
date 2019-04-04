# database.py

import datetime


class DataBase:
    def __init__(self, filename):
        self.filename = filename
        self.users = None
        self.file = None
        self.load()

    def load(self):
        self.file = open(self.filename, "r")
        self.users = {}

        for line in self.file:
            email, password, name, created = line.strip().split(";")
            self.users[email] = (password, name, created)

        self.file.close()

    def get_user(self, email):
        if email in self.users:
            return self.users[email]
        else:
            return -1

    def add_user(self, email, password, name):
        if email.strip() not in self.users:
            self.users[email.strip()] = (password.strip(), name.strip(), DataBase.get_date())
            self.save()
            return 1
        else:
            print("Email exists already")
            return -1

    def validate(self, email, password):
        if self.get_user(email) != -1:
            return self.users[email][0] == password
        else:
            return False

    def save(self):
        with open(self.filename, "w") as f:
            for user in self.users:
                f.write(user + ";" + self.users[user][0] + ";" + self.users[user][1] + ";" + self.users[user][2] + "\n")

    def update(self,email):
        if self.get_user(email) != -1:
            print("okoko:"+self.users[email][1])
            with open(self.filename, "w") as f:
                for user in self.users:
                    f.write(user + ";" + self.users[user][0] + ";" + self.users[user][1] + ";" + "PRESENT" + "\n")
    
    def retstring(self):
        self.file = open(self.filename, "r")
        self.users2 = {}
        va="Student ID          Student Name        Present/Absent\n\n"
        for line in self.file:
            email, password, name, created = line.strip().split(";")
            self.users2[email] = (password, name, created)
            va=va+"\n"+email+"         "+name+"           "+created
        return va


    @staticmethod
    def get_date():
        return "Absent"
