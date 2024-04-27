class Intern:
    """
    Represents an intern
    Attributes:
        - Name (str): name of the intern
    """

    def __init__(self, name="My name? I’m nobody, an intern, I have no name.") -> None:
        """
        Init a new intern with a name of a message by default

        Args:
            name (str, optional): name of the intern. Defaults to "My name? I’m nobody, an intern, I have no name.".
        """
        self.Name = name

    def __str__(self):
        """
        Returns a string representation of the intern

        Returns:
            str: name of the intern
        """
        return self.Name

    class Coffee:
        def __str__(self):
            """
            Returns a string representation of the cup of coffee

            Returns:
                str: cup of coffee
            """
            return "This is the worst coffee you ever tasted."

    def work(self):
        """
        Simulates an attempt for the intern to work

        Raises:
            Exception: Always raised because the intern cannot work
        """
        raise Exception("I'm just an intern, I can't do that...")

    def make_coffee(self):
        """
        Creates a new coffee

        Returns:
            Coffee: instance of the Coffee class
        """
        return self.Coffee()


if __name__ == "__main__":
    nobody = Intern()
    mark = Intern("Mark")

    print(nobody.__str__())
    print(mark.__str__())

    print(mark.make_coffee())

    try:
        nobody.work()
    except Exception as e:
        print(e)
