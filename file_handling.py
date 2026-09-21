class Customer:
    agency_name ="Skyline Digital Solutions"
    def __init__(self, name, city, project_type):
        self.name = name
        self.city = city
        self.project_type = project_type

    def get_name(self):
        return self.name
    def get_city(self):
        return self.city
    def get_project_type(self):
        return self.project_type    
    def show_us(self):
       print(f"{self.agency_name} Client name is {self.name}, located in {self.city}, and is working on a {self.project_type} project.")
    def update_city(self, city):
        self.city = city
       # print(f"Client {self.name} is now located in {self.city}.")
class WordPress_Customers(Customer):
    def __init__(self, name, city, project_type, hosting_provider):
        super().__init__(name, city, project_type)
        self.hosting_provider= hosting_provider

    def get_hosting_provider(self):
        return self.hosting_provider
    def show_us(self):
        print(f"{self.agency_name} Client name is {self.name}, located in {self.city}, and is working on a {self.project_type} project, hosted by {self.hosting_provider}.")


#------------------------------------------MAIN FUNCTION------------------------------------------
client1 = WordPress_Customers("Rao Muhammad Imran", "Lahore", "Website Development", "Hostinger")
client2 = WordPress_Customers("Ali Raza", "Karachi", "Mobile App Development", "Go Daddy")
client3 = WordPress_Customers("Ayesha Khan", "Faisalabad", "Software Development", "Name Cheap")
client4 = Customer("Zainab Malik", "Islamabad", "Digital Marketing")
client5 = Customer("Zayn Mehar", "Peshawar", "Git Setup")


all_clients = [client1, client2, client3, client4, client5]

for clients in all_clients:
    if isinstance(clients, Customer):
        clients.show_us()
#print(isinstance(client1, WordPress_Customers))   # True
#print(isinstance(client4, WordPress_Customers))   # False
#print(isinstance(client4, Customer))              # True — kyunke WordPress_Customers khud Customer se inherit karta hai
#client4.show_us