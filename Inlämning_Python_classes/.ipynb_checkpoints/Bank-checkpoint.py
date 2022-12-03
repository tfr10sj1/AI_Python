from Customer import Customer as cu
from Account import Account as ac
customers = []
obj_customer = None 
class Bank:
    def __init__(self):
        pass
    
    def _load(self): 
        global customers
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
            customers.append(info) 
        return customers
    
    def get_customers(self):
        for customer in customers: 
            name, pnr,  *accounts = customer.split(":")
            print(name, pnr)
            
    def add_customer(self, customer_id, name, pnr):
        global obj_customer
        if str(pnr) not in str(customers):
            obj_customer = cu(customer_id, name, pnr)
            customers.append(obj_customer.get_customer())
            print(customers)
            return True
        else:
            print("You are already a customer!")
            return False

    def get_customer(self, searched_pnr):
        global obj_customer
        for customer in customers:
            customer_id ,name, pnr,  *accounts = customer.split(":")
            if str(searched_pnr) == str(pnr):
                customerl = name + ":" +  str(pnr) + ":" + str(customer_id) + ":" +  str(accounts)
                return obj_customer.get_customer()
            
    def change_customer_name(self, newname, newpnr):
        global obj_customer
        obj_customer.change_name(newname)
        index1 = [customers.index(customer) for customer in customers if str(newpnr) in str(customer)][0]
        customers[index1] = obj_customer.get_customer()
        
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
        if str(newpnr) in str(customers) and str(newaccount_nbr) not in str(customers):
            index1 = [ customers.index(customer) for customer in customers if str(newpnr) in str(customer)][0]
            customers[index1] = customers[index1] + ac(newaccount_nbr, newamount).get_account()
            print(customers)
        
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