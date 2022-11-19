id_name_pnr_acount_data = {}
customer_id = 0
gname = ""
gpnr = 0


class Customer():
    def __init__(self):
        global gname, gpnr, customer_id, id_name_pnr_acount_data
     
    def add_new_customer(self, name, pnr):
        global gname, gpnr, customer_id, id_name_pnr_acount_data
        gname = self.name = name
        gpnr = self.pnr = pnr
        
        if str(gpnr) not in str(id_name_pnr_acount_data.values()):
            self.set_customer_id()
            id_name_pnr_acount_data[customer_id] = gname +":"+ str(gpnr) +":"
            return True
        else:
            print("You are already a customer!")
            return False

    def change_name(self, new_name):
        global id_name_pnr_acount_data, customer_id, gname, gpnr
        gname = new_name
        id_name_pnr_acount_data[customer_id] = gname +":"+ str(gpnr) +":"
        return id_name_pnr_acount_data[customer_id]
    
    def get_customer_info(self):
        global id_name_pnr_acount_data, customer_id, gname, gpnr
        print("Customer data: ")
        print(" ")
        print("Pnr: ", gpnr)
        print("Full name: ", gname)
        print("All_Customers", id_name_pnr_acount_data)
            
    def set_customer_id(self):
        global customer_id
        if customer_id == 0:
            customer_id = 111111
        else:
            customer_id += 1
