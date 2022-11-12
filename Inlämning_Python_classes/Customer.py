from Account import Account as ac
class Customer(ac):
    cusomers_id_list = []
    id_name_pnr_acount_data = {}

    def __init__(self, name, pnr):
        super().__init__(self)
        self.id = 0000000
        self.et_customer_id()
        self.name = name
        self.pnr = pnr
        #self.transactions = transactions
        self.id_name_pnr_acount_data[self.id] = self.id +":"+ self.name +":"+ self.pnr +":"
        f = open("demofile2.txt", "a")
        f.write(self.id +":"+ self.name +":"+ self.pnr +":"+ ac.Account.account_nbr_acount_type_balance_list)
        f.close()

    def change_name(self, Id, new_name):
        if self.Id == self.id:
            self.name = new_name
            self.id_name_pnr_acount_data[self.id] = self.id +":"+ self.name +":"+ self.pnr +":"
   
    def get_customer_info(self, Id):
        if self.Id == self.id:
            print("Customer data: ")
            print("Pnr: ", self.pnr)
            print(" ")
            print("Full name: ", self.name)
            print(" ")
            
            
    def set_customer_id(self):
        nbr = 111111
        while nbr in self.cusomers_id_list :
              nbr += 1
        else:
            self.id = nbr
            self.cusomers_id_list(nbr)