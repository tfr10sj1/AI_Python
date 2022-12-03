from Customer import Customer as cu
from Account import Account as ac
#from collections import namedtuple as nt

customers = []
obj_customer = [] 
obj_account = []

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

    def get_customer(self, newpnr):
        global obj_customer, obj_account
        #index1 = [customer if str(searched_pnr) in str(customer) else False for customer in customers][0]
        if str(newpnr) in str(obj_customer.get_customer()):
            customer_id, name, pnr, *extra = str(obj_customer.get_customer()).split(":")
            result = name +":"+ str(pnr) + str(obj_account.get_account())
            return result
  
    def change_customer_name(self, newname, newpnr):
        global obj_customer
        obj_customer.change_name(newname)
        index1 = [customers.index(customer) for customer in customers if str(newpnr) in str(customer)][0]
        customers[index1] = obj_customer.get_customer()
        
    def remove_customer(self, pnr):
        saldo = ""
        with open("customers.txt", 'r') as file:
            data = [line.strip() for line in file]
            for line in data: 
                if str(pnr) in line:
                    customer_id, name, pnr,  *accounts = line.split(":")
                    sal = [s[0:6] for s in accounts if "#" in str(s)]
                    sald, *extra = str(sal).split("#")
                    cunvert = sald[1:]  
                    saldo1, *saldo2 = str(accounts).split("#")
                    ss = sald[1:].replace(".",'')
                    ss = sald[1:].replace("'",'')
                    
                    print(ss)

                    sek = (ss.split(","))
                    
                    saldo +=[int(x)  for x in sek]
                    print(saldo)

                    search_text = line
                    replace_text = ""
                    file.close()
                    with open(r'customers.txt', 'r') as file:
                        data = file.read()
                        data = data.replace(search_text, replace_text)
                    with open(r'customers.txt', 'w') as file:
                        file.write(data)
                    print("Customer is removed")

    def add_account(self, newpnr, newaccount_nbr, newamount):
        global obj_account, obj_customer
        if str(newpnr) in str(customers) and str(newaccount_nbr) not in str(customers):
            index1 = [ customers.index(customer) for customer in customers if str(newpnr) in str(customer)][0]
            obj_account = ac(newaccount_nbr, newamount)
            customers[index1] = customers[index1] + obj_account.get_account()
            print(customers)
        else:
            return -1
        
    def get_account(self, newpnr, newaccount_id):
        index1 = [customer if str(newpnr) in str(customer) and str(newaccount_id) in str(customer) else False for customer in customers][0]
        index2, index3, index4, *account = index1.split(":")
        account1, *account11 = str(account).split("#")
        a = [x for x in str(account).split("#") if str(newaccount_id) in x]
        a[0] = a[0].replace("[", "")
        return a[0].replace('"', "")
             
    def deposit(self, newpnr, newaccount_id, newamount): 
        global obj_customer, obj_account
        
        if str(newpnr) in str(obj_customer.get_customer()) and str(newaccount_id) in str(obj_account.get_account()):
            obj_account.deposit(newamount)
            print(str(obj_customer.get_customer())+str(obj_account.get_account()))