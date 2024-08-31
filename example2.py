import hashlib
import json

import goody


class JsonFile:
    @staticmethod
    def write(file_name, data):
        with open(file_name, "w", encoding="utf-8") as file:
            # file.write(json.dumps(data, indent=4, ensure_ascii=False, sort_keys=True))
            file.write(json.dumps(data, indent=4, ensure_ascii=False))

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
        data = Data("./data.json")
        data.add_or_update(self.username, password=self.password, full_name=self.full_name, phone=self.phone)


    def verify_password(self, password):
        if hashlib.md5(password.encode()).hexdigest() == self.password:
            return True
        return False

    def __del__(self):
        pass


class Data:
    def __init__(self, file_name):
        self.file_name = file_name

    def add_or_update(self, item_name, **kwargs):
        item_dict = {}
        for key, value in kwargs.items():
            item_dict[key] = value

        data = JsonFile.read(self.file_name)
        data[item_name] = item_dict

        # JsonFile.write("./data.json", data)
        JsonFile.write("./data.json", goody.sort_dict_turkish_by_key(data))

    def get_item_dict(self, item_name):
        return JsonFile.read(self.file_name).get(item_name)

    def get_item_values(self, item_name):
        return JsonFile.read(self.file_name).get(item_name).values() if item_name in JsonFile.read(self.file_name) else None

    def get_items(self):
        return JsonFile.read("./data.json")


if __name__ == "__main__":
    user = User("Tayfur", "hfgh", "İbrahim Obut", "896")
    user.save()
