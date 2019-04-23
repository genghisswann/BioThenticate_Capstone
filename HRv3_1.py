import xlsxwriter
import openpyxl
from progDataExtraction import accessAPI, plotting, bioThenticate




################################### CODE START ###################################

#RETURNS A BOOL VALUE TO SIGNIFY IF USER IS CURRENTLY LOGGED IN OR NOT
def login():
    welcome = input("Do you have an account? y/n: ")

    #YES CHOICE
    if welcome == "y":
        print("\nPlease login")
        is_authenticated = False
        for r in range(3):
            print("Attempt count", r, "out of 3.")
            use = input("Username: ")
            pwd = input("Password: ")

            try:
                authenticate(use, pwd)
                is_authenticated = True
                return True
            except Exception as error:
                print(error)

        if is_authenticated:
            print("Welcome you are logged in")
            return True
        else:
            print("Attempts exceeded!")
            return False


    #NO CHOICE
    elif welcome == "n":
        while True:
            username = input("Please enter a username:")
            found_username = False

            with open("Credentials.txt", "r") as file:
                for line in file:
                    username_create, password_create = line.strip().split(':')
                    if username == username_create:
                        found_username = True
                        print("User already exists...")
                        return False
                else:
                    for line in file:
                        if not line:
                            return False

            password = input("Please enter a password which must be a min 8 characters and a max of 15 characters:")
            if len(password) > 15:
                print("password is too long")
                return False
            elif len(password) < 8:
                print("password is too short")
                return False

            ConfirmPassword = input("Please confirm your password: ")


            if password != ConfirmPassword:
                print("Passwords do NOT match!")
                return False

            else:
                if len(password) >= 8 and len(password) <= 15:
                    with open("Credentials.txt", "a") as file:
                        file.write(username + ":" + password)
                        file.write("\n")
                        file.close()
                        # welcome = "y"
                        # break
                        return False


    # EXIT OPTION (DEBUGGING)
    elif welcome == "exit":
        print("Exiting...")
        exit()
    # INVALID CHOICE
    else:
        print("Invalid option.")


def authenticate(use, pwd):
    with open("Credentials.txt", "r") as credentials_file:
        for line in credentials_file:
            username_login, password_login = line.strip().split(':')
            if username_login == use and password_login == pwd:
                return True
            elif username_login == use and password_login != pwd:
                raise Exception("Password is incorrect!")
            else:
                continue
    raise Exception("Username and/or password do not exist!")



# Driver program
if __name__ == "__main__":
    loginStatus = False
    authStatus = False

    while loginStatus != True or authStatus != True:
        print("Login status: Logged Out...", "\n")
        loginStatus = login()
        if loginStatus == True:
            accessAPI()
            authStatus = bioThenticate()
            print(authStatus)




    print("Login status: Logged In...", "\n")

