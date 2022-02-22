

class Memento:
    def __init__(self, contents) -> None:
        self.contents = contents

class Database:

    instance = None
    
    def __init__(self, participants) -> None:
        self.contents = participants
        self.mementos = [Memento(contents=None)]

    @classmethod
    def initialize(cls, participants):
        if not cls.instance:
            cls.instance = cls(participants)

    @classmethod
    def rollback(cls):
        instance = cls.instance
        instance.contents = instance.mementos[-1].contents[:]
        instance.mementos = instance.mementos[:-1]

    @classmethod
    def add_participant(cls, participant):
        instance = cls.instance
        current = instance.contents[:]
        new = current[:] + [participant]
        cls.update_instance(new)

    @classmethod
    def remove_last_participant(cls):
        instance = cls.instance
        current = instance.contents[:]
        new = current[:-1]
        cls.update_instance(new)

    @classmethod
    def update_instance(cls, new_content) -> None:
        instance = cls.instance
        current = instance.contents[:]
        instance.mementos.append(Memento(contents=current))
        instance.contents = new_content

    @classmethod
    def get_instance(cls):
        return cls.instance

    @classmethod
    def flush(cls):
        cls.instance = None

    def __str__(self):
        return str(self.contents)




def main() -> None:
    participants = ["Taonga", "Anthony", "Juan", "Sergey"]

    Database.initialize(participants)
    print(Database.get_instance())

    new_participant = "Tanja"

    Database.add_participant(new_participant)
    print(Database.get_instance())

    Database.remove_last_participant()
    print(Database.get_instance())

    Database.rollback()
    print(Database.get_instance())

    Database.rollback()
    print(Database.get_instance())

    Database.flush()

    participants = ["Taonga", "Anthony", "Juan"]

    Database.initialize(participants)
    print(Database.get_instance())

    Database.add_participant("Sergey")
    print(Database.get_instance())




if __name__ == '__main__':
    main()