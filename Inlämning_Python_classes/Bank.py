class Bank:
    customer_info = {}
    account_info = []
    info = ""
    customer_id = ""
    name = ""
    pnr = ""
    balance = ""
    new_account_nbr = ""
    
    def __init__(self):
        self._load()
    
    def _load(self):
        with open("customers.txt", 'r') as file:
            data = [line.strip() for line in file]
            
        for line in data: 
            global customer_info, info, customer_id, name, pnr, balance, new_account_nbr
            customer_id, name, pnr,  *accounts = line.split(":")
            #print(customer_id, name, pnr, accounts) 
            #account_info.append(customer_id)
            #account_info.append(name)
            #account_info.append(pnr)
            info = str(self.name) + ":" + str(self.pnr)
            for item in accounts:
                if("#" in item):
                    balance, new_account_nbr = item.split("#")
                    #account_info.append(balance)
                    #account_info.append("#")
                    #account_info.append(new_account_nbr)
                    info += ":" + str(balance) + "#" + str(new_account_nbr)
                else:
                    #print(item)
                    #account_info.append(item)
                    info += ":" + str(item)
                    self.customer_info[str(customer_id)] = info 
                    info = ""      
        print(self.customer_info)

    def ger_customers():
        with open("customers.txt", 'r') as file:
            data = [line.strip() for line in file]
  
        #print(data)
        # iterating through data
        for line in data:
            Customer_id, firstname, pnr, *account_type = line.split(":")
            print("name/Prn:",firstname, pnr)
    
    def add_customer(name, pnr):
        "add customer"
    def get_customer(pnr):
        ""
    def change_customer_name(name, pnr):
        ""
    def remove_customer(pnr):
        ""
    def add_account(pnr):
        ""
    def get_account(pnr, account_id):
        ""
    def deposit(pnr, account_id, amount):
        balance = balance +  amount
        print("The balance is: ", balance)

    def withdraw(pnr, account_id, amount):
        ""
    def close_account(pnr, account_id):
        ""
    def get_all_transactions_by_pnr_acc_nr( pnr, acc_nr ):
        "VG"
    
