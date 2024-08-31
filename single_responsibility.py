class PersonDB:
    def save(self, person):
        print(f'Save the {person} to the database')

class PersonJson:
    def save(self, person):
        print(f'Save the {person} to the json')


class Person:
    def __init__(self, name):
        self.name = name
        self.db = PersonJson()

    def __repr__(self):
        return f'Person(name={self.name})'

    def save(self):
        self.db.save(person=self)


if __name__ == '__main__':
    p = Person('John Doe')
    p.save()
