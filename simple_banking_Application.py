balance = 0.0
kyc_documents = {}

def check_balance():
    print(f"Your current balance is {balance}$")
    print("===============================")

def deposit(amount):
    global balance
    if amount > 0 :
        balance += amount
        print(f"{amount}$ deposit successfully !!!")
        print("------------------------------------------------------------------------")
    else:
        print("cannot deposit negative or zero amount")
        print("===============================")

def withdraw(amount):
    global balance
    if amount <= 0 :
        print("cannot withdraw negative or zero amount")
        print("===============================")
    elif amount > balance:
        print("Cannot withdraw,insufficient funds!")
        print("===============================")
    else:
        balance -= amount
        print(f"{amount}$ withdraw successfully!!!")
        print("------------------------------------------------------------------------")
def update_kyc(docs):
    global kyc_documents
    kyc_documents.update(docs)

def check_kyc():
    if len(kyc_documents) == 0:
        print("Kyc not done yet")
        print("-----------------")
    else:
        for doc in kyc_documents:
            print(f"{doc} : {kyc_documents[doc]}")

if __name__ == "__main__":
    print("===============================")
    print("     Welcome to ABC Bank        ")
    print("===============================")
    while True:
        print("1. check the balance ")
        print("2. deposit an amount ")
        print("3. withdraw an amount ")
        print("4. check kyc")
        print("5. update kyc")
        print("6. Quit")
        choice = input("enter your choice(1-6)")
        print("===============================")
        if choice == '1':
            check_balance()
        elif choice == '2':
            amount = float (input("enter the amount you want to deposit: "))
            deposit(amount)
        elif choice == '3':
            amount = float(input("enter the amount you want to withdraw:"))
            withdraw(amount)
        elif choice == '4':
            check_kyc()
        elif choice == '5':
            kyc_docs = {}
            n_documents = int(input("Enter the number of documents you want to add "))
            for i in range(n_documents):
                key = input("Enter the document type: ")
                value = input("Enter the document number: ")
                kyc_docs[key] = value
            update_kyc(kyc_docs)
            print("kyc updated successfully ")
            print("-----------------")

        elif choice == '6':
            print("quiting,hava a nice day")
            break
        else:
            print("Invalid choice,try again!")
            print("===============================")
    print()
    print("Thank you for using ABC Banking  ")