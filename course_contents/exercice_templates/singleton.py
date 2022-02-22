

# Singleton Design Pattern
    # pour une classe donnée, nous pouvons avoir qu'un seul objet.
    # ex: app window when we launch an application

class MyApplication:

    instance = None
    
    def __init__(self, *args) -> None:
        assert(self.__class__.instance == None, "this is a singleton")
        self.contents = args

    @classmethod
    def initialize(cls, *args):
        if not cls.instance:
            cls.instance = cls(*args)

    @classmethod
    def get_instance(cls):
        return cls.instance

    @classmethod
    def flush(cls):
        cls.instance = None

    def __str__(self):
        return str(self.contents)

def main() -> None:
    MyApplication.initialize(1, 2, 3, 4)
    MyApplication.initialize(2, 3, 4, 5)

    # app = MyApplication.get_instance()
    app = MyApplication(1, 2, 3, 4)
    print(app.contents)

if __name__ == "__main__":
    main()