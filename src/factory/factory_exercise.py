class Person:
    def __init__(self, id, name):
        self.name = name
        self.id = id

    def __str__(self):
        return f"{self.name} with id {self.id}."


class PersonFactory:
    id_ = 0
    def create_person(self, name):
        p = Person(self.id_, name)
        self.id_ += 1
        return p

pf = PersonFactory()
p1 = pf.create_person("Skarlos")
p2 = pf.create_person("Mmitrou")
p3 = pf.create_person("Nioannou")

print(p1)
print(p2)
print(p3)