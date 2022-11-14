class Bank:
    def __init__(self):
        self._load()
    
    def _load(self):
        "Läser in text filen och befolkar listan som ska innehålla kunderna."
        f = open("customers.txt", "r")
        for x in f:
            print(x)
            
    def ger_customers():
        "do somthing" 
    
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
    
