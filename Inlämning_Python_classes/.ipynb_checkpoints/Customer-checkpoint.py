id_name_pnr_acount_data = {}
customer_id = 0
gname = ""
gpnr = 0


class Customer():
    def __init__(self):
        global gname, gpnr, customer_id, id_name_pnr_acount_data
     
    def add_new_customer(self, name, pnr):
        self.name = name
        self.pnr = pnr
        self.set_customer_id()
        data = str(customer_id) + ":" + self.name +":"+ str(self.pnr) +":"
        with open(r'customers.txt', 'a') as file:
            file.write(data)

    def change_name(newname, **line):
        customer_id, name, pnr,  *accounts = line.split(":")
        search_text = line
        print("search_text", name)
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
        """
        global id_name_pnr_acount_data, customer_id, gname, gpnr
        gname = new_name
        id_name_pnr_acount_data[customer_id] = gname +":"+ str(gpnr) +":"
        return id_name_pnr_acount_data[customer_id]
        """
    
    def get_customer_info(self):
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
    
    
        """global id_name_pnr_acount_data, customer_id, gname, gpnr
        print("Customer data: ")
        print(" ")
        print("Pnr: ", gpnr)
        print("Full name: ", gname)
        print("All_Customers", id_name_pnr_acount_data)
    """
    def set_customer_id(self):
        global customer_id
        count = 111111
        with open(r"customers.txt", 'r') as fp:
            x = len(fp.readlines())
            print('Total lines:', x) # 8
            customer_id = count+x
   