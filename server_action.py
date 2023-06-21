import os.path
import csv

base_dir = 'C:\\Users\\DELL\\Documents\\Lab_work\\python\\'

def make_find_file():
    # base_dir = 'C:\\Users\\DELL\\Documents\\Lab_work\\python\\'  # Specify the base directory

    if not os.path.isfile(base_dir + 'accounts.csv'):
        headings = ['username', 'password']

        accounts = open(base_dir + 'accounts.csv', 'w')
        csvwrite = csv.writer(accounts)

        csvwrite.writerow(headings)
        accounts.close()
        print("accounts data file successfully created\n")
        
    else:
        print("account data file successfully detected\n")

    if not os.path.isfile(base_dir + 'messages.csv'):
        messages = open(base_dir + 'messages.csv', 'w')
        print("messages data file successfully created\n")
        messages.close()
    else:
        print("messages data file successfully detected\n")
    
def create_account(data):
    accounts = open(base_dir + 'accounts.csv', 'a')

    csvwrite = csv.writer(accounts)

    row = [data[1], data[2]]
    csvwrite.writerow(row)

    accounts.close()
    return"accountCreated"

def check_account(data):
    accounts = open(base_dir + 'accounts.csv', 'r')
    csvread = csv.reader(accounts)

    for row in csvread:

        if len(row) == 0:
            continue
        if ((row[0] == data[1]) and (row[1] == data[2])):
            print("Login successful")
            return "loginTrue"

    accounts.close()
    print("Login failed")
    return "loginFalse"
        
def main_action(data):
    make_find_file()

    data = data.split('-')

    if data[0] == 'signup':

        #checks if account already exists. 
        if check_account(data) == 'loginTrue':
            return str('accountExists')
        else:
            return str(create_account(data))
    elif data[0] == 'login':
        return str(check_account(data))
#functions to make
#new account//login//store message//get messages

main_action('login-hassan-zxc')
#main_action('signup-hassan-zxc')