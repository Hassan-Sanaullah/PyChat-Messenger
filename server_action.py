import os.path
import csv

base_dir = os.path.dirname(os.path.realpath(__file__)) # Specify the base directory

def make_find_file():
    # base_dir = 'C:\\Users\\DELL\\Documents\\Lab_work\\python\\'  # Specify the base directory

    if not os.path.isfile(base_dir + 'accounts.csv'):
        headings = ['username', 'password']

        accounts = open(base_dir + 'accounts.csv', 'w')
        csvwrite = csv.writer(accounts)

        csvwrite.writerow(headings)
        accounts.close()
        print("accounts data file successfully created")
        
    else:
        print("account data file successfully detected")

    if not os.path.isfile(base_dir + 'messages.csv'):
        headings = ['receiver', 'sender', 'message']

        messages = open(base_dir + 'messages.csv', 'w')
        csvwrite = csv.writer(messages)

        csvwrite.writerow(headings)
        print("messages data file successfully created")
        messages.close()
    else:
        print("messages data file successfully detected")
    
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
            print("Account exists")
            return "loginTrue"

    accounts.close()
    print("Account does not exist")
    return "loginFalse"
        
def new_message(data):
    messages = open(base_dir + 'messages.csv', 'a')
    csvwrite = csv.writer(messages)

    text = [data[2], data[1], data[3]]
    csvwrite.writerow(text)

    messages.close()
    print('New message received and saved')

    return 'null'

def inbox(data):
    inboxlist = []

    messages = open(base_dir + 'messages.csv', 'r')
    csvread = csv.reader(messages)


    for row in csvread:
        if len(row) == 0:
            continue
        elif row[0] == data[1]:
            inboxlist.append(row[1])
        elif data[1] == row[1]:
            inboxlist.append(row[0])
    
    messages.close()

    if len(inboxlist) == 0:
        return ('No messages')

    # set removes repeating elements in a list
    inboxlist = set(inboxlist)
    inboxlist = '-'.join(inboxlist)
    
    return inboxlist

def get_message(data):
    line = []

    messages = open(base_dir+'messages.csv', 'r')
    csvread = csv.reader(messages)

    for row in csvread:

        if len(row) == 0:
            continue
        if ((row[0] == data[1]) and (row[1] == data[2]) or (row[0] == data[2]) and (row[1] == data[1])):
            print("getting message")
            line.append(row[1])
            line.append(row[2])
            line.append('  ')

    messages.close()

    line = '-'.join(line)
    return line

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
    elif data[0] == 'newMessage':  ######
        new_message(data)
        return 'null'
    elif data[0] == 'inbox':
        return str(inbox(data))
    elif data[0] == 'getMessages':
        return get_message(data)
    elif data[0] == 'sendMessage':
        new_message(data)
        return 'null'
        






#main_action('login-hassan-zxc')
#main_action('signup-hassan-zxc')
#main_action('newMessage-hassan-ali-hey')
#main_action('inbox-z')
#main_action('getMessages-z-z')
#sendMessage-hassan-ahmed-hello hi