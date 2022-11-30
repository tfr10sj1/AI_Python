from Customer import Customer as cu

class Bank:
    def __init__(self):
        self.customers = []
        self._load()
        
    def _load(self):     
        with open("customers.txt", 'r') as file:
            data = [line.strip() for line in file] 
        for line in data: 
            customer_id, name, pnr,  *accounts = line.split(":")
            info = str(customer_id) +":"+ name + ":" + str(pnr)
            for item in accounts:
                if("#" in item):
                    balance, new_account_nbr = item.split("#")
                    info += ":" + balance + "#" + str(new_account_nbr)
                else:
                    info += ":" + str(item)     
            self.customers.append(info) 
        return self.customers
    def get_customers(self):
        for customer in self.customers: 
            name, pnr,  *accounts = customer.split(":")
            print(name, pnr)
            
    def add_customer(self, customer_id, name, pnr):
        for customer in self.customers:
            if str(pnr) not in customer and str(customer_id) not in customer:
                self.customers.append(cu(customer_id, name, pnr).get_customer())
                print(self.customers)
                return True
        else:
            print("You are already a customer!")
            return False
        
    
            
    def get_customer(self, pnr):
        customer_info = [customer for customer in self.customers if str(pnr) in customer]
        if len(customer_info) != None or customer_info == 0:
            print(customer_info[0])
        
    def change_customer_name(self, newname, newpnr):
        customer_info = self._load()
        if [cu().change_name(newname, newpnr) for i in customer_info if str(newpnr) in customer_info[i]]:     
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

    def add_account(self, newpnr, newaccount_nbr, newamount):
        customer_info = self._load()
        for i in customer_info:
            if str(newpnr) in customer_info[i] and str(newaccount_nbr) not in customer_info[i]:
                #cu.add_account(i, newaccount_nbr, newamount)
                print("new account to ", i, "is added")
                print(i, newaccount_nbr, newamount)
                return True
        else:
            print("You are already a customer!")
            return False
        
    def get_account(self, newpnr, newaccount_id):
        customer_info = self._load()
        for i in customer_info:
            if str(newpnr) in customer_info[i] and str(newaccount_id) in customer_info[i]:
                name, pnr,  *accounts = customer_info[i].split(":")
                strofaccount = ""
                for item in accounts:
                    strofaccount += ":" + str(item)
                return customer_info[i]
        else:
            return False
"""              
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
                with open(r'customers.txt', 'r') as file:
                    data = file.read()
                    data = data.replace(search_text, replace_text)

                with open(r'customers.txt', 'w') as file:
                    file.write(data)

                print("Name is Changed")
                ac().deposit(search_txt, replace_txt)
            else:
                return False
            
    def withdraw(pnr, account_id, amount):
        ""
    def close_account(pnr, account_id):
"""