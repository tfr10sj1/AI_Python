from Account import Account as ac
from Customer import Customer as cu

class Bank:
    def __init__(self):
        self._load()
    
    def _load(self):     
        customer_info = {}
        with open("customers.txt", 'r') as file:
            data = [line.strip() for line in file]
            
        for line in data: 
            customer_id, name, pnr,  *accounts = line.split(":")
            info = name + ":" + pnr
            
            for item in accounts:
                if("#" in item):
                    balance, new_account_nbr = item.split("#")
                    info += ":" + balance + "#" + new_account_nbr
                else:
                    info += ":" + str(item)
                    
            customer_info[customer_id] = info 
        return customer_info
        
    def get_customers(self):
        customer_info = self._load()
        for key in customer_info: 
            name, pnr,  *accounts = customer_info[key].split(":")
            print(name, pnr)
            
    def add_customer(self, name, pnr):
        customer_info = self._load()
        print(customer_info.values())
        if str(pnr) not in str(customer_info.values()):
            cu().add_new_customer(name, pnr)
            print("new customer added")
            print(pnr, name)
            return True
        else:
            print("You are already a customer!")
            return False
    def get_customer(self, pnr):
        customer_info = self._load()
        for i in customer_info:
            if str(pnr) in customer_info[i]:
                name, pnr,  *accounts = customer_info[i].split(":")
                strofaccount = ""
                for item in accounts:
                    strofaccount += ":" + str(item)
                print(name, pnr, i, strofaccount)
            
    def change_customer_name(self, newname, newpnr):
        data = self._load()    
        for line in data: 
            customer_id = line
            if str(newpnr) in data[line]:
                name, pnr,  *accounts = data[line].split(":")
                search_text =  customer_id + ":" + name + ":" + pnr 
                
                replace_text = customer_id + ":" + newname + ":" + pnr 

                for item in accounts:
                    replace_text += ":" + str(item)
                    search_text += ":" + str(item)
                    
                print("replace_text", replace_text)
                print("search_text", search_text)
                
                cu().change_name(search_text, replace_text)
        else:
            return False

    def remove_customer(self, pnr):
        with open("customers.txt", 'r') as file:
            data = [line.strip() for line in file]
            for line in data: 
                if str(pnr) in line:
                    customer_id, name, pnr,  *accounts = line.split(":")
                    search_text = line
                    print("search_text", search_text)
                    replace_text = ""
                    print("replace_text", replace_text)
                    file.close()
                    with open(r'customers.txt', 'r') as file:
                        data = file.read()
                        data = data.replace(search_text, replace_text)
                    with open(r'customers.txt', 'w') as file:
                        file.write(data)
                    print("Customer is removed")

    def add_account(self, newpnr):
        self.newpnr = newpnr 
        with open('customers.txt') as file:
            contents = file.read()
        
        if str(newpnr) in contents:
            with open("customers.txt", 'r') as file:
                data = [line.strip() for line in file]
            new_account_nbr = ac().set_account_nbr()
            for line in data: 
                if str(self.newpnr) in line:
                    customer_id, name, pnr,  *accounts = line.split(":")
                    search_text = customer_id + ":" + name + ":" + pnr 
                    replace_text = customer_id + ":" + name + ":" + pnr + ":" + new_account_nbr
              
                    for item in accounts:
                        replace_text += ":" + str(item)
                        search_text += ":" + str(item)
                    
            print(ac().add_new_account(search_text, replace_text))          
        else:
            return -1

    def get_account(self, pnr, account_id):
        customer_info = self._load()
        for i in customer_info:
            if str(pnr) and str(account_id) in customer_info[i]:
                name, pnr,  *accounts = customer_info[i].split(":")
                strofaccount = ""
                for item in accounts:
                    strofaccount += ":" + str(item)
                return customer_info[i]
                
    def deposit(self, newpnr, newaccount_id, newamount):  
        customer_info = self._load()
        for i in customer_info:
            if str(newpnr) in customer_info[i]:
                name, pnr,  *accounts = customer_info[i].split(":")
                replace_txt = str(i) + ":" + name + ":" + str(pnr)
                search_txt = str(i) + ":" + name + ":" + str(pnr)
                for item in accounts:
                    search_txt += ":" + str(item)
                    
                for item in accounts:
                    one = item.split("#")
                    if str(newaccount_id) in str(one):
                        balance, after_hashtag = accounts[accounts.index(item)+2].split("#")
                        print("accounts[accounts.index(item)+2]", accounts[accounts.index(item)+2])
                        newbalance = str(int(balance) + int(newamount))
                        accounts[accounts.index(item)+2] = str(newbalance) + "#" 
                        replace_txt += ":" + str(balance) + "#" + str(after_hashtag) + str(newaccount_id) 
                    else:
                        replace_txt += ":" + str(item)
                print("search_txt " , search_txt)
                print("replace_txt ", replace_txt)
                
                ac().deposit(search_txt, replace_txt)
            else:
                return False
            
    def withdraw(pnr, account_id, amount):
        ""
    def close_account(pnr, account_id):
        ""
 