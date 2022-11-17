from Account import Account as ac
from Customer import Customer as cu

class Bank:
    customer_info = {}
    def __init__(self):
        self._load()
    
    def _load(self):        
        with open("customers.txt", 'r') as file:
            data = [line.strip() for line in file]
            
        for line in data: 
            global customer_info
            customer_id, name, pnr,  *accounts = line.split(":")
            info = name + ":" + pnr
            
            for item in accounts:
                if("#" in item):
                    balance, new_account_nbr = item.split("#")
                    info += ":" + balance + "#" + new_account_nbr
                else:
                    info += ":" + str(item)
                    
            self.customer_info[customer_id] = info 
        
    def get_customers(self):
        for key in self.customer_info: 
            name, pnr,  *accounts = self.customer_info[key].split(":")
            print(name, pnr)
            
    def add_customer(self, name, pnr):
        cu().add_new_customer(name, pnr)
        
    def get_customer(self, pnr):
        for i in self.customer_info:
            if str(pnr) in self.customer_info[i]:
                name, pnr,  *accounts = self.customer_info[i].split(":")
                strofaccount = ""
                for item in accounts:
                    strofaccount += ":" + str(item)
                print(name, pnr, i, strofaccount)
            
    def change_customer_name(self, newname, pnr):
        with open("customers.txt", 'r') as file:
            data = [line.strip() for line in file]
        for line in data: 
            if str(pnr) in line:
                customer_id, name, pnr,  *accounts = line.split(":")
                # creating a variable and storing the text
                # that we want to search
                search_text = line
                print("search_text", search_text)
                # creating a variable and storing the text
                # that we want to add
                replace_text = customer_id + ":" + newname + ":" + pnr 
                for item in accounts:
                    replace_text += ":" + str(item)
                print("replace_text", replace_text)
                file.close()
                
                # Opening our text file in read only
                # mode using the open() function
                with open(r'customers.txt', 'r') as file:

                    # Reading the content of the file
                    # using the read() function and storing
                    # them in a new variable
                    data = file.read()

                    # Searching and replacing the text
                    # using the replace() function
                    data = data.replace(search_text, replace_text)

                # Opening our text file in write only
                # mode to write the replaced content
                with open(r'customers.txt', 'w') as file:

                    # Writing the replaced data in our
                    # text file
                    file.write(data)

                # Printing Data replaced
                print("Name is Changed")

        
    def remove_customer(self, pnr):
        
        with open("customers.txt", 'r') as file:
            data = [line.strip() for line in file]
            for line in data: 
                if str(pnr) in line:
                    customer_id, name, pnr,  *accounts = line.split(":")

                    search_text = line
                    print("search_text", search_text)
                    # creating a variable and storing the text
                    # that we want to add
                    replace_text = ""
                    print("replace_text", replace_text)
                    file.close()

                    # Opening our text file in read only
                    # mode using the open() function
                    with open(r'customers.txt', 'r') as file:

                        # Reading the content of the file
                        # using the read() function and storing
                        # them in a new variable
                        data = file.read()

                        # Searching and replacing the text
                        # using the replace() function
                        data = data.replace(search_text, replace_text)

                    # Opening our text file in write only
                    # mode to write the replaced content
                    with open(r'customers.txt', 'w') as file:

                        # Writing the replaced data in our
                        # text file
                        file.write(data)

                    # Printing Data replaced
                    print("Customer is removed")

    def add_account(pnr):
        #ac().add_new_account()
        
    def get_account(self, pnr, account_id):
        for i in self.customer_info:
            if str(pnr) and str(account_id) in self.customer_info[i]:
                name, pnr,  *accounts = self.customer_info[i].split(":")
                strofaccount = ""
                for item in accounts:
                    strofaccount += ":" + str(item)
                print(name, pnr, i, strofaccount)
                
    def deposit(pnr, account_id, amount):
        balance = balance +  amount
        print("The balance is: ", balance)

    def withdraw(pnr, account_id, amount):
        ""
    def close_account(pnr, account_id):
        ""
 