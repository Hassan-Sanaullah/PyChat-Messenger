import os.path

def make_find_file():
    if(os.path.isfile(r'./accounts.txt') == False):
        accounts = open('accounts.txt', 'w')
        accounts.write("Account data\n")
        print("accounts data file successfully created\n")
        accounts.close()
    else:
        print("account data file successfully detected\n")

    if(os.path.isfile(r'./messages.txt') == False):
        messages = open('messages.txt', 'w')
        messages.write("Messages data\n")
        print("messages data file successfully created\n")
        messages.close()
    else:
        print("messages data file successfully detected\n")
    
def create_account(data):
    accounts = open("accounts.txt", 'a')

    accounts.write(data[1])
    accounts.write('\n')
    accounts.write(data[2])
    accounts.write('\n')

    accounts.close()

def login(data):
    accounts = open("accounts.txt", 'r')
    username = 'hassan'
    password = 'null'
    
    #all the strings read from file have \n at the end. 
    #the strip method removes that so it matches with data
    for line in accounts:
        username = line.strip('\n')
        password = next(accounts).strip('\n')

        if ((username == data[1]) and (password == data[2])):
            print("Login successful")

    accounts.close()
        

make_find_file()

data = 'login-hasan-123'

data = data.split('-')

if data[0] == 'signup':
    create_account(data)
elif data[0] == 'login':
    login(data)
#functions to make
#new account//login//store message//get messages