id_name_pnr_acount_data = {}
customer_id = 0
gname = ""
gpnr = 0


class Customer():
    def __init__(self):
        pass
     
    def add_new_customer(self, name, pnr):
        self.name = name
        self.pnr = pnr
        self.set_customer_id()
        data = str(customer_id) + ":" + self.name +":"+ str(self.pnr) +":"
        with open(r'customers.txt', 'a') as file:
            file.write('\n' + data)

    def change_name(self, search_text, replace_text):
        with open(r'customers.txt', 'r') as file:
            data = file.read()
            data = data.replace(search_text, replace_text)

        with open(r'customers.txt', 'w') as file:
            file.write(data)
         
        print("Name is Changed")
        return True
    
    def get_customer_info(self):
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
    
    def set_customer_id(self):
        global customer_id
        count = 111111
        with open(r"customers.txt", 'r') as fp:
            x = len(fp.readlines())
            print('Total lines:', x) # 8
            customer_id = count+x
   