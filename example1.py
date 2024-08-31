import json
import hashlib


class JsonFile:
    @staticmethod
    def write(file_name, data):
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(json.dumps(data, indent=4, ensure_ascii=False, sort_keys=True))

    @staticmethod
    def read(file_name):
        try:
            with open(file_name, "a+", encoding="utf-8") as file:
                file.seek(0)
                data = json.load(file)
        except Exception:
            data = {}
        return data


class User:
    saved = False

    def __init__(self, username, password=None, full_name=None, phone=None):
        self.username = username
        self.password = ""
        self.full_name = ""
        self.phone = ""

        data = JsonFile.read("./data.json")

        if self.username in data:
            self.password = data[self.username]["password"]
            self.full_name = data[self.username]["full_name"]
            self.phone = data[self.username]["phone"]

        if password:
            self.password = hashlib.md5(password.encode()).hexdigest()
        if full_name:
            self.full_name = full_name
        if phone:
            self.phone = phone

    def save(self):
        data = JsonFile.read("./data.json")
        data.update({self.username: {"password": self.password, "full_name": self.full_name, "phone": self.phone}})
        JsonFile.write("./data.json", data)
        self.saved = True

    def verify_password(self, password):
        if hashlib.md5(password.encode()).hexdigest() == self.password:
            return True
        return False

    def __del__(self):
        if not self.saved:
            answer = input("Do you want to save the data? (Y/N)").upper()
            if answer == "Y":
                try:
                    self.save()
                except Exception as e:
                    print(e, "kayıt yapılamadı")


if __name__ == "__main__":
    user = User("Zübeyir", "1234", "Çiğdem", "707")
    user.save()
    # # user = User("John")
    # result = user.verify_password("4321")
    # print(result)
