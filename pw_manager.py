from cryptography.fernet import Fernet


'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key) '''


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key



master_pwd = input("What is the master password? ")

key = load_key() + master_pwd.encode()
fer = Fernet(key)



 #r.strip() strips off \n from line, data.split() breaks off the line into new item when the character is found
def view():
    with open('passwords.txt', 'r') as f: 
        for line in f.readlines():
            data = (line.rstrip())
            user, passw = data.split("|")
            print("USER:", user, "PASSWORD:",fer.decrypt(passw.encode()).decode())



def add():
    name = input('Account Name: ')
    pwd = input("Password: ")
    

# w= write new, r= just read, a= allows you to add something to the end of the file and creates a new one if it doesnt exist. With closes the file right after
    with open('passwords.txt', 'a') as f: 
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")




while True:
    mode = input("Would you like add a new password or view the existing ones? (view / add) Press q to quit ").lower()

    if mode == "q":
        break
    
    if mode == "view":
        view()

    elif mode == "add":
        add()

    else:
        print("Invalid mode.")
        continue    #Brings the user to the top of the while-loop