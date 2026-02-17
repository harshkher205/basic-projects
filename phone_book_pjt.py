class PhoneBook:
    phone_directory = []

    def __init__(self, name,phone_number):
        self.name = name
        self.phone= phone_number
        PhoneBook.phone_directory.append(self)

    def show_contact(self):
        return f" Name : {self.name},contact number : {self.phone}"

    @classmethod
    def show_all_contact(cls):
        if len(cls.phone_directory)==0:
            print("No contact found")
        else:
            print("All contacts from directory ==> ")
            for number in cls.phone_directory:
                print(PhoneBook.show_contact(number))

    @classmethod
    def search_contact(cls,search_name):
        for number in cls.phone_directory:
            if number.name.lower() == search_name:
                return number.phone
        return f"No contact found for {search_name}"

    @staticmethod
    def validate_ph_no(number):
        if len(number) >= 8 and number.isdigit():
            return True
        else:
            return False
n_contacts = int(input("How many contacts do you want to add?: "))
for i in range(n_contacts):
    name = input("Enter your name: ")
    phone_no = input("Enter your phone number:")
    if PhoneBook.validate_ph_no(phone_no):
        PhoneBook(name,phone_number= phone_no)
    else:
        print(f"invalid phone number for {name} and phone number should be atleast 8 digits and should only contain digits")

c2 = PhoneBook('jhaa',8860764890)
c3 = PhoneBook('rahul',8860779048)
#print(PhoneBook.phone_directory)


# print(c1.show_contact())
# print(c2.show_contact())

PhoneBook.show_all_contact()

# print(PhoneBook.search_contact("Jhaa"))