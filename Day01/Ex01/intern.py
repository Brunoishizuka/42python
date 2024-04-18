class Intern:
    def __init__(self, name="My name? I’m nobody, an intern, I have no name."):
        self.Name = name

    def __str__(self):
        return self.Name

    def make_coffee(self):
        return Coffee()

    def work(self):
        raise Exception("I’m just an intern, I can’t do that...")


class Coffee:
    def __str__(self):
        return "This is the worst coffee you ever tasted."


# Test the functionalities
if __name__ == "__main__":
    # Instantiate an Intern without a name
    intern1 = Intern()
    print("Intern 1:", intern1)

    # Instantiate an Intern with the name "Mark"
    intern2 = Intern("Mark")
    print("Intern 2:", intern2)

    # Ask Mark to make coffee
    print(f"{intern2} makes coffee:", intern2.make_coffee())

    # Ask the other intern to work (handling the exception)
    try:
        print("Intern without a name: ", end="")
        intern1.work()
    except Exception as e:
        print(e)
