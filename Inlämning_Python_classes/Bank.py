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
        if str(pnr) not in customer_info.values():
            cu().add_new_customer(name, pnr)
        
    def get_customer(self, pnr):
        customer_info = self._load()
        for i in customer_info:
            if str(pnr) in customer_info[i]:
                name, pnr,  *accounts = customer_info[i].split(":")
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
                search_text = line
                print("search_text", search_text)
                replace_text = customer_id + ":" + newname + ":" + pnr 
                
                for item in accounts:
                    replace_text += ":" + str(item)
                    
                print("replace_text", replace_text)
                file.close()
                
                with open(r'customers.txt', 'r') as file:
                    data = file.read()
                    data = data.replace(search_text, replace_text)
                    
                with open(r'customers.txt', 'w') as file:
                    file.write(data)
                    
                print("Name is Changed")
                return True
            
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
                
            for line in data: 
                if str(self.newpnr) in line:
                    customer_id, name, pnr,  *accounts = line.split(":")
                    search_text = line
                    #print("search_text", search_text)
                    replace_text = customer_id + ":" + name + ":" + pnr 
                    for item in accounts:
                        replace_text += ":" + str(item)
                    #print("frsta for replace_text", replace_text)
            dic = ac().add_new_account()
            print(dic)
            for item in dic:
                replace_text += str(item) + ":" + str(dic[item])
            
                #print(" andra replace_text", replace_text)

            file.close()

            with open(r'customers.txt', 'r') as file:
                data = file.read()
                data = data.replace(search_text, replace_text)

            with open(r'customers.txt', 'w') as file:
                file.write(data)
                print("New account is added")
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
                print(name, pnr, i, strofaccount)
                return customer_info[i]
                
    def deposit(self, newpnr, newaccount_id, newamount):
        self.newaccount_id = newaccount_id 
        self.newpnr = newpnr
        self.newamount = newamount 
        from Bank import Bank as ba
        line = ba().get_account(self.newpnr, self.newaccount_id)
        print(line)
        customer_id, name, pnr,  *accounts = line.split(":")
        replace_text = customer_id + ":" + name + ":" + pnr 

        for item in accounts:
            if str(item) == str(self.newaccount_id):
                x = accounts.index(item)
                print(x)
                accounts[x+2] += newamount
                replecement = str(accounts[x+2])
                print(replecement)
        
        """with open('customers.txt') as file:
            contents = file.read()
        
        if str(newpnr) in contents:
            with open("customers.txt", 'r') as file:
                data = [line.strip() for line in file]
                
            for line in data: 
                if str(self.newpnr) in line:
                    customer_id, name, pnr,  *accounts = line.split(":")
                    search_text = line
                    
                    replace_text = customer_id + ":" + name + ":" + pnr 
                    for item in accounts:
                        replecement = ""
                        if str(item) == str(self.newaccount_id):
                            x = accounts.index(item)
                            print(x)
                            accounts[x] = newamount
                            replecement = str(newamount)
                            print(replecement)
                        elif str(item) == "#"+str(self.newaccount_id):
                            x = accounts.index(item)
                            print(x)
                            accounts[x+3] = "#"+ str(newamount)
                            replecement = "#"+ str(newamount)
                            print(replecement)

                        replace_text += ":" + str(item)
            print("search_text", replace_text)
            with open(r'customers.txt', 'r') as file:
                data = file.read()
                data = data.replace(search_text, replace_text)

            with open(r'customers.txt', 'w') as file:
                file.write(data)
                print("depossit is added")
        else:
            return -1"""

    def withdraw(pnr, account_id, amount):
        ""
    def close_account(pnr, account_id):
        ""
 