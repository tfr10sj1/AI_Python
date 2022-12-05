from Customer import Customer as cu
from Account import Account as ac
#from collections import namedtuple as nt

customers = []
obj_customer = None 
obj_account = None

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
        global obj_customer, customers
        if str(pnr) not in str(customers):
            obj_customer = cu(customer_id, name, pnr)
            nykund = obj_customer.get_customer()
            customers.append(nykund)
            
            return customers[customers.index(nykund)]
        else:
            print("You are already a customer!")
            return False

    def get_customer(self, newpnr):
        global obj_customer, obj_account
        if str(newpnr) in str(obj_customer.get_customer()):
            customer_id, name, pnr, *extra = str(obj_customer.get_customer()).split(":")
            if obj_account.get_account() != None:
                result = name +":"+ str(pnr) +":"+ str(obj_account.get_account())
            else:
                result = name +":"+ str(pnr) +":" 
            return result
        else:
            return False
  
    def change_customer_name(self, newname, newpnr):
        global obj_customer, obj_account, customers
        index1 = [customers.index(customer) for customer in customers if str(newpnr) in str(customer)][0]
        if index1:
            obj_customer.change_name(newname)
            customers[index1] = obj_customer.get_customer() + obj_account.get_account()
            return customers[index1]
        else:
            return False
        
    def remove_customer(self, newpnr):
        global customers
        index1 = [customers.index(customer) for customer in customers if str(newpnr) in str(customer)][0]
        customer = [customer for customer in customers if str(newpnr) in str(customer)]

        amount = str(str(str(customer).replace("#"," ")).split(":")).split(" ")
        pengar = [amo for amo in amount if "." in str(amo)]
        peng = str(str(str(pengar).replace('"', '')).replace("'",'')).replace(".0", "")[1:-1]
        print(peng)
        return customers.pop(index1)
    
    def add_account(self, newpnr, newaccount_nbr, newamount):
        global obj_account, obj_customer, customers
        if str(newpnr) in str(customers) and str(newaccount_nbr) not in str(customers):
            index1 = [ customers.index(customer) for customer in customers if str(newpnr) in str(customer)][0]
            obj_account = ac(newaccount_nbr, newamount)
            customers[index1] = customers[index1] + obj_account.get_account()
            return customers[index1]
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
        global obj_customer, obj_account, customers
        if str(newpnr) in str(obj_customer.get_customer()) and str(newaccount_id) in str(obj_account.get_account()):
            obj_account.deposit(newamount)
            index1 = [ customers.index(customer) for customer in customers if str(newpnr) in str(customer)][0]
            customers[index1] = obj_customer.get_customer() + obj_account.get_account()
            return customers[index1]
        else:
            return False
            
    def withdraw(self, newpnr, newaccount_id, newamount):
        global obj_customer, obj_account, customers
        if str(newpnr) in str(obj_customer.get_customer()) and str(newaccount_id) in str(obj_account.get_account()):
            obj_account.withdraw(newamount)
            index1 = [ customers.index(customer) for customer in customers if str(newpnr) in str(customer)][0]
            customers[index1] = obj_customer.get_customer() + obj_account.get_account()
            return customers[index1]
        else:
            return False
            
    def close_account(self, newpnr, newaccount_id):
        global obj_customer, obj_account, customers
        index1 = [customers.index(customer) for customer in customers if str(newpnr) in str(customer)][0]
      
        if str(newpnr) in str(obj_customer.get_customer()) and str(newaccount_id) in str(obj_account.get_account()):
            account_nbr, account_type, amount = str(obj_account.get_account()).split(":")
            money, extra = str(amount).split("#")
            print("Account_nbr:",newaccount_id, "is closed.", "You will get back:", money)
            customers[index1] = obj_customer.get_customer()
            return customers[index1]
        else:
            return False