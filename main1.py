#Create class
class IOSstring():

    #Constructor to set the default value
    def __init__(self):
        self.strl = ""


    #Function to get the input from the user
    def get_String(self):
        self.strl = input("Enter a string.")

    #Function to print the string in uppercase characters
    def print_String(self):
        print("The result is:", self.strl.upper())

#Object creation
strl = IOSstring()

#Call the functions
strl.get_String()
strl.print_String()