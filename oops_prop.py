class Chartbook:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.loggedin = False
        self.menu()
    
    def menu(self):
        user_input = input("""welcome to chetbook  How would you like to proceed?
                            1. Press 1 to Signup
                            2. Press 2 to signin
                            3. Press 3 to write a post
                            4. Press 4 to message a friend
                            5. Press any other key to exit""")
        
        if user_input =="1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()
    
    def signup(self):
        email = input("enter your email:")
        pwd = input("enter your password:")
        self.username = email
        self.password = pwd
        print("you have signed up successfully\n")
        self.menu()
    def signin(self):
        if self.username =="" and self.password == "":
            print("you have not signed up yet press 1 for signin")
        else:
            uname = input("enter your username:")
            pwd = input("enter your password:")
            if uname == self.username and pwd == self.password:
                print("sign in successful")
                self.loggedin = True
            else:
                print("Please input correct credictial\n")
            print("\n")
            self.menu()


obj = Chartbook()

