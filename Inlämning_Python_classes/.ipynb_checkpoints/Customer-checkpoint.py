from Account import Account as ac
customers = {}

class Customer():
    def __init__(self, customer_id, name, pnr):
        self.customer_id = customer_id
        if self.check_if_customer_id_not_exist(self.customer_id):
            self.name = name
            self.pnr = pnr
            self.update_values(self.customer_id)
        else:
            print("Choose another Customer_id!")
            
    def add_account(self, customer_id, account_nbr, balance):
        global customers
        self.balance = balance
        self.account_nbr = account_nbr
        self.customer_id = customer_id
        self.account_type = "debit account"

        if str(self.account_nbr) not in str(customers):
            customers[self.customer_id] += str(account_nbr) + ":" + self.account_type + ":" + str(self.balance) + "#"
            return True
        else:
            return False
            
    def change_name(self, new_name, pnr):
        global customers
        cu_id = [customer_id for customer_id in customers if str(pnr) in customers[customer_id]]
        self.name = new_name 
        self.pnr = pnr
        self.customer_id = cu_id[0]
        self.update_values(self.customer_id)
        print("Customer name is changed to", new_name)
            
    def check_if_customer_id_not_exist(self, customer_id):
        global customers
        self.customer_id = customer_id
        if str(self.customer_id) not in customers:
            print("Customer_id: " + str(self.customer_id) + " is new customer_id!")
            return True
        else:
            print("Customer_id: " + str(self.customer_id) + " already exists!")
            return False
        
    def update_values(self, customer_id):
        global customers
        customers[self.customer_id] = ":" + self.name + ":" + str(self.pnr) + ":"
        
    def show_customer_info(self, pnr):
        global customers
        for customer in customers:
            if str(pnr) in customers[customer]:
                print(str(customer) + customers[customer])
                
    def update_DB():
        global customers
        
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
