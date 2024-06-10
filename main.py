import os             # operating sys  # for file handeling
from datetime import datetime
import json

def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

class ExceptionHandeling:

    def check_char(self, message):
            while True:
                data = input(message)
                if data.isalpha() :
                    return data
                else:
                    print("==>> Erorr: \n\t Invalid Input \n\t use only Letters")

    def check_IntLen(self, message, feildName = ''):
        if feildName == 'cnic':
            while True:
                data = input(message)
                if data == "0":
                    return 0
                elif len(data) == 13 :
                    if data.isnumeric():
                        return data
                    else:
                        print("==>> Erorr: \n\t Invalid Input \n\t use only Digits")
                else:
                    print("==>> Erorr: \n\t Invalid Input \n\t use only 13 Digits")
        elif feildName == 'atmPin':
            while True:
                data = input(message)
                if data == "0":
                    return 0
                elif len(data) == 4 :
                    if data.isnumeric():
                        return data
                    else:
                        print("==>> Erorr: \n\t Invalid Input \n\t use only Digits")
                else:
                    print("==>> Erorr: \n\t Invalid Input \n\t use only 4 Digits")
        elif feildName == "cardNum":
            while True:
                data = input(message)
                if data == "0":
                    return 0
                elif len(data) == 16 :
                    if data.isnumeric():
                        return data
                    else:
                        print("==>> Erorr: \n\t Invalid Input \n\t use only Digits")
                else:
                    print("==>> Erorr: \n\t Invalid Input \n\t use only 16- Digits")
        elif feildName == "bills":
            while True:
                data = input(message)
                if data == "0":
                    return 0
                elif len(data) == 12 :
                    if data.isnumeric():
                        return data
                    else:
                        print("==>> Erorr: \n\t Invalid Input \n\t use only Digits")
                else:
                    print("==>> Erorr: \n\t Invalid Input \n\t use only 12-Digits")
        else:
            while True:
                data = input(message)
                if data == "0":
                    return 0
                elif len(data) == 14 :
                    if data.isnumeric():
                        return data
                    else:
                        print("==>> Erorr: \n\t Invalid Input \n\t use only Digits")
                else:
                    print("==>> Erorr: \n\t Invalid Input \n\t use only 14- Digits")

    def check_Int(self, message):
        while True:
            try:
                value = int(input(message))
                if value >= 0:  
                    return value
                else:
                    clear_screen()
                    print("==>> Error: \n\t Invalid Input \t You Cannot put Negative Amount")
            except ValueError:                  # Catch only ValueError
                clear_screen()
                print("==>> Error: \n\t Invalid Input")
            
    def check_date(self, message):
        while True:
            data = input(message)
            if len(data) == 5 :
                if data[0].isnumeric() and data[1].isnumeric() and data[2] == "/" and data[3].isnumeric() and data[4].isnumeric() :
                        return data
            elif len(data) == 8 :
                if data[0].isnumeric() and data[1].isnumeric() and data[2] == "/" and data[3].isnumeric() and data[4].isnumeric() and data[5] == "/" and data[6].isnumeric() and data[7].isnumeric():
                        return data
            else:   
                    print("==>> Erorr: \n\t Invalid Input \n\t use The Right format (DD/MM/YY Note: use MM/YY for expiray dates)")

    def check_Index(self, message, listLen):
         while True:
            data = self.check_Int(message)
            if data <= listLen :
                return data
            print("==>> Erorr: \n\t Invalid Input \n\t use only From Below.")

    def check_UserName(self, message, feildName =''):
        while True:
            data = input(message)
            temp = list(data)
            if data == "0":
                return 0
            elif len(temp) == 0:
                print("==>> Erorr: \n\t Invalid Input \n\t There is NO input Please Write The Name.")
                continue
            if feildName == "benificery":
                if len(data) < 3:
                    print("==>> Erorr: \n\t Invalid Input \n\t User Name is too small.")
                    continue
                if len(data) > 20:
                    print("==>> Erorr: \n\t Invalid Input \n\t User Name is too large.")
                    continue
                if ' ' in temp[0] or ' ' in temp[-1]:
                    print("==>> Erorr: \n\t Invalid Input \n\t There Should not be SPACES in the START or in the END.")
                    continue
                flag = False
                for x in  range(1,len(temp)-1):
                    if temp[x] == ' ':
                        if temp[x+1] == ' ':
                            flag = True
                            break    
                if flag:
                    print("==>> Erorr: \n\t Invalid Input \n\t Two consective spaces not allowed")
                    continue        
            
            if ' ' in temp and feildName != "benificery":
                print("==>> Erorr: \n\t Invalid Input \n\t Enter User Name without spaces.")
                continue
            if len(data) < 4 and feildName != "benificery":
                print("==>> Erorr: \n\t Invalid Input \n\t User Name is too small.")
                continue
            elif len(data) > 10 and feildName != "benificery":
                print("==>> Erorr: \n\t Invalid Input \n\t User Name is too large.")
                continue
            return data

    def check_Password(self, message):
        while True:
            flag = False
            data = input(message)
            temp = list(data)
            if data == "0":
                return 0
            elif len(data) < 5 :
                print("==>> Erorr: \n\t Invalid Input \n\t Password is too small.")
                continue
            elif len(data) > 12:
                print("==>> Erorr: \n\t Invalid Input \n\t Password is too large.")
                continue
            if ' ' in temp[0] or ' ' in temp[-1]:
                print("==>> Erorr: \n\t Invalid Input \n\t There Should not be SPACES in the START or in the END.")
                continue
            for x in  range(1,len(temp)-1):
                if temp[x] == ' ':
                    if temp[x+1] == ' ':
                        flag = True
                        break
            if flag:
                print("==>> Erorr: \n\t Invalid Input \n\t Two consective spaces not allowed")
                continue
            return data
  

class DataRecord:
    
    def __init__(self):         #contructor
        self.customersDetails = {}     # customersDetils (atribbute of class DataRecord)
        self.organizationsDetails = {}
        self.registerationDetails = {}
        self.benificeryDetails = {}
        self.otherBanksDetails = {}
        self.donationsDetails = {}
        self.ransactionHistoryDetails = {}
                
    def saveFile(self):
        with open('Records.json', 'w') as file:         #save file
            json.dump(self.customersDetails, file, indent=4)

    def loadFile(self):
        with open('Records.json', 'r') as file:
            self.customersDetails = json.load(file)
    
    def saveOrganizationFile(self):
        with open('Organizations.json', 'w') as file:
            json.dump(self.organizationsDetails, file, indent=4)

    def loadOrganizationFile(self):
        with open('Organizations.json', 'r') as file:
            self.organizationsDetails = json.load(file)

    def saveRegisterationFile(self):
            with open('Register.json', 'w') as file:
                json.dump(self.registerationDetails, file, indent=4)

    def loadRegistrationFile(self):
        with open('Register.json', 'r') as file:
            self.registerationDetails = json.load(file)
        # print(self.registerationDetails)

    def loadBenificeryFile(self):
        with open('Benificeries.json', 'r') as file:
            self.benificeryDetails = json.load(file)

    def saveBenificeryFile(self):
        with open('Benificeries.json', 'w') as file:
            json.dump(self.benificeryDetails, file, indent=4)

    def loadOtherBanksFile(self):
        with open('OtherBanks.json', 'r') as file:
            self.otherBanksDetails = json.load(file)

    def loadDonationsFile(self):
        with open('Donations.json', 'r') as file:
            self.donationsDetails = json.load(file)

    def saveDonationsFile(self):
        with open('donations.json', 'w') as file:
            json.dump(self.donationsDetails, file, indent=4)

    def loadTransactionHistoryFile(self):
        with open('TransactionHistory.json', 'r') as file:
            self.transactionHistoryDetails = json.load(file)

    def saveTransactionHistoryFile(self):
        with open('TransactionHistory.json', 'w') as file:
            json.dump(self.transactionHistoryDetails, file, indent=4)

    def saveOtherBanksFile(self):
        with open('OtherBanks.json', 'w') as file:
            json.dump(self.otherBanksDetails, file, indent=4)

    def displayData(self):   # remove
        for user, details in self.customersDetails.items():
            print(f"User Name: {user}")
            for key, value in details.items():
                print(f"  {key}: {value}")

    def recordUpdation(self, accNum, userName):  # Balancing (current balance) in records & register file
        balance = self.registerationDetails[accNum]["balance"]
        self.customersDetails[userName]["balance"] = balance
        return balance
    
    def recordUpdationForReciever(self, accNum):
        for key in self.customersDetails.keys():
            if accNum == self.customersDetails[key]["accNum"]:
                self.customersDetails[key]["balance"] = self.registerationDetails[accNum]["balance"]

    def fetchUserAccNum(self, userName=''): # userName is a variable declared in this method (fetchUserAccNum)
        return self.customersDetails[userName]["accNum"]
    
    def checkUser(self, transferName):  #remove
        if transferName in self.customersDetails.keys():
            return True
        return False
        
    def fetchAccInfo(self, userName):
        data = self.customersDetails[userName]
        print(f"User Name: {userName}\n")
        for key, value in data.items():  # items can be keys or values
            if key == "cardNum" or key == "atmPin" or key=="cnic":
                continue   # go back to for loop
            print(f"{key}: {value}\n")

    def fetchRecords(self):
        return self.customersDetails

    def setUserTransactionHistory(self, userName, accNum):
        if userName not in self.transactionHistoryDetails.keys():
            self.transactionHistoryDetails[userName] = {
                                                        "accNum": accNum,
                                                        "To": {}
                                                        }

    def fetchAccTransactionHistory(self, userName):
        print(f"User Name: {userName}\n\nAcount Number: {self.transactionHistoryDetails[userName]["accNum"]}\n")
        if not self.transactionHistoryDetails[userName]["To"]:
            print("\n\tYou Dont have Any Transaction Your List Is Empty.")
        data = self.transactionHistoryDetails[userName]["To"]
        for key, value in data.items():
            print(f"\nName: {value[1]}\t\tAccount: {value[2]}\t\tAmount: {value[0]}\tTime: {key}")


class Verify:

    def __init__(self):
        self.handleException = ExceptionHandeling()

        self.records = None
        self.register = None
        self.users = None
        
    def setRecords(self, records):
        self.records = records

    def setRegister(self, register, users):
        self.register = register
        self.users = users

    def verifyLogin(self, message, username='', feildName=''):
        if feildName == "userName":
            while True:
                data = input(message)
                if data == "0":
                    return data
                elif data in self.records.keys():
                    return data
                else:
                    clear_screen()
                    print("==>>Invalid Username")
        if feildName == "password" :
            while True:
                data = input(message)
                if data == "0":
                    return data
                elif data == self.records[username]["password"]:
                    return data
                elif data == "1":
                    return 1
                else:
                    clear_screen()
                    print(f"User Name: {username}")
                    print("==>>Invalid Password\n\nIf You Dont remember Press 1 to reset OR 0 to return\n\n")

    def registraion(self, message, feildName='', accNum=''):

        if feildName == "accNum":
            while True:
                flag = False
                data = self.handleException.check_IntLen(message, feildName)
                if data == 0:
                    return 0
                elif data in self.register.keys():
                    for key in self.records.keys():
                        if data == self.records[key]["accNum"]:
                            flag = True
                            break
                    if flag :
                        print("\n==>>Invalid Account Number \n It is Already Registerd In E-Banking\n")
                        continue
                    return data
                else:
                    print("\n==>>Invalid Account Number \n It is not present in the Bank Records\n")

        elif feildName == "cardNum":
            while True:
                data = self.handleException.check_IntLen(message, feildName)
                if data == 0:
                    return 0
                elif data in self.register[accNum][feildName]:
                    return data
                else:
                    print(f"\n==>>Invalid Card Number \n It does not match against your given Account Number: {accNum}\n")
        
        elif feildName == "atmPin":
            while True:
                data = self.handleException.check_IntLen(message, feildName)
                if data == 0:
                    return 0
                elif data in self.register[accNum][feildName]:
                    return data
                else:
                    print("\n==>>Invalid ATM-PIN \n It is not present in the Bank Records\n")

        elif feildName == "cnic":
            while True:
                data = self.handleException.check_IntLen(message, feildName)
                if data == 0:
                    return 0, 0
                elif data in self.register[accNum][feildName]:
                    balance = self.register[accNum]["balance"]
                    return data, balance
                else:
                    print("\n==>>Invalid CNIC \n It is not present in the Bank Records\n")

    def userNameVerification(self, message):
        while True:
            data = self.handleException.check_UserName(message)
            if data == 0:
                return 0
            elif data in self.users:
                print("\n==>>ERROR \n\t User Name Already In Use")
            else:
                return data
    
    def passwordVerification(self, message):
        return self.handleException.check_Password(message)
    
    def fetchBalance(self, userName):
        return self.records[userName]["balance"]

    def fetchNewPassword(self, userName):
        while True:
            newPassword = self.handleException.check_Password("\n Write Your NEW Password\n\n ==>>")
            if newPassword == 0:
                return self.records, 1
            elif newPassword == self.records[userName]["password"]:
                clear_screen()
                print("==>>You CANNOT Write same Password As Before\n\nPress any button to continue OR 0 to return")
                continue
            confrimPassword = self.handleException.check_Password("\n Write again same password to CONFRIM Password\n\n ==>>")
            if newPassword == confrimPassword:
                self.records[userName]["password"] = newPassword
                return self.records , 1
            else:
                clear_screen()
                print("==>>Invalid Password\n\n Password DONOT match with the confrim password")

    def passwordReset(self, userName):
        while True:
            accData = self.handleException.check_IntLen("Give Your 14-Digit Account Number\n\n==>>")
            if accData == 0:
                clear_screen()
                return self.records, 0
            if accData == self.records[userName]["accNum"]:
                while True:
                    cardData = self.handleException.check_IntLen("Give Your 16-Digit Card Number\n\n==>>", 'cardNum')
                    if cardData == self.records[userName]["cardNum"]:
                        while True:
                            cnicData = self.handleException.check_IntLen("Give Your 13-Digit CNIC\n\n==>>", "cnic")
                            if cnicData == self.records[userName]["cnic"]:
                                return self.fetchNewPassword(userName)
                            else:
                                print(f"\n==>>Invalid CNIC \n It does not match to this User Name: {userName}\n")
                    else:
                        print(f"\n==>>Invalid Card Number \n It does not match to this User Name: {userName}\n")
            else:
                print(f"\n==>>Invalid Account Number \n It does not match to this User Name: {userName}\n")


class Registraion: 
    def __init__(self):
        # self.handleException = ExceptionHandeling()
        self.verify = Verify()
        
        self.customersDetails = None

    def setRegister(self, register, customersDetails, users):
        self.verify.setRegister(register, users)
        self.verify.setRecords(customersDetails)
        self.customersDetails = customersDetails

    def dataInput(self):

        accNum = self.verify.registraion("Write your 14-digit account number == >>", 'accNum')
        if accNum == 0:
            return self.customersDetails, 0
        cardNum = self.verify.registraion('Write your 16-digit card number ==>>', 'cardNum', accNum)
        if cardNum == 0:
            return self.customersDetails, 0
        atmPin = self.verify.registraion("Write your 4-digit ATM pin == >>", 'atmPin', accNum)
        if atmPin == 0:
            return self.customersDetails, 0
        cnic, balance = self.verify.registraion("Write your 13-digit CNIC number ==>>", "cnic", accNum)
        if cnic == 0:
            return self.customersDetails, 0

        userName = self.verify.userNameVerification("User Name: ")
        if userName == 0:
            return self.customersDetails, 0
        password = self.verify.passwordVerification("Password: ")
        if password == 0:
            return self.customersDetails, 0
        
        print("done")
        
        self.customersDetails[userName] = {
                                            "password" : password,
                                            "accNum" : accNum,
                                            "cardNum" : cardNum,
                                            "atmPin" : atmPin,
                                            "cnic" : cnic,
                                            "balance" : balance
                                        }
        clear_screen()
        print("Account Created")
        return self.customersDetails, 1


class LogIn:

    def __init__(self):
        self.verifyData = Verify()
        self.userName = None
        
    def setRecordsInVerify(self, records):
        self.verifyData.setRecords(records)


    def logins(self):
        self.userName = self.verifyData.verifyLogin("User Name: ", feildName="userName")
        if self.userName == "0":
            return 0, self.userName
        password = self.verifyData.verifyLogin("Password: ", username=self.userName, feildName="password")
        if password == "0":
            return 0, self.userName
        elif password == 1:
            return 1, self.userName

        print("Access Granted")
        return 2, self.userName

    def fetchLogin(self):
        balance = self.verifyData.fetchBalance(self.userName)
        return self.userName, balance

    def changePassword(self, userName):
        return self.verifyData.fetchNewPassword(self.userName)

    def resetPassword(self, userName):
        return self.verifyData.passwordReset(userName)


class CurrentUser:
    
    def __init__(self):
        self.currentUser = None
        self.currentBalance = None

    def setCurrentUser(self, userName, balance):
        self.currentUser = userName
        self.currentBalance = balance

    def updateBalance(self, balance):
        self.currentBalance = balance


class Transfer:

    def __init__(self):
        self.handleException = ExceptionHandeling()
    
        self.userName = None
        self.customersDetails = None
        self.register = None
        self.otherBanks = None
        self.transactionHistory = None
        
    def setData(self, userName, customersDetails='', register='', otherBanks='', transactionHistory=''):
        self.userName = userName
        self.customersDetails = customersDetails
        self.register = register
        self.otherBanks = otherBanks
        self.transactionHistory = transactionHistory
        
    def transferMoney(self, accNum, transferAccNum, transferName):
        if transferAccNum in self.register.keys():
            while True:
                amount = self.handleException.check_Int(f"How much MONEY you want to send to {transferName.capitalize()} \t\t Your Current Balance: {self.register[accNum]["balance"]}\n\nPress 00 To Return ==>>")
                if amount == 00:
                    clear_screen()
                    return self.register, transferAccNum, self.transactionHistory, True
                if amount <= self.register[accNum]["balance"]:
                    self.register[accNum]["balance"] -= amount
                    self.register[transferAccNum]["balance"] += amount
                    clear_screen()
                    print("Transfer Successfull")
                    print(f"\n\nTransferd Funds \n\nFrom:\n\n Name: {self.userName.capitalize()}\t\t Account Number: {accNum}\n Balance: {self.register[accNum]["balance"]}\n\nTo:\n\n Name: {transferName.capitalize()}\t\t Account Number: {transferAccNum}\n\n\tAmount: {amount}\t\t Time: {datetime.now()}")
                    # key = f"{datetime.now()}"
                    self.transactionHistory[self.userName]["To"][f"{datetime.now()}"] = [amount, transferName.capitalize(), transferAccNum]
                    # self.transactionHistory[self.userName]["To"][key].append(amount, transferAccNum)
                    ex = input("\n\n Press Any Button To Return")
                    clear_screen()
                    return self.register, transferAccNum, self.transactionHistory, True
                else:
                    print(f"==>> Erorr: \n\t Not Enough Balance \n\n\t\t Your Balance Is ==>>  {self.register[accNum]["balance"]}")
        elif transferAccNum in self.otherBanks:
            while True:
                amount = self.handleException.check_Int(f"How much MONEY you ant to send to {transferName.capitalize()} \t\t Your Current Balance: {self.register[accNum]["balance"]}\n\nPress 00 To Return ==>>")
                if amount == 00:
                    clear_screen()
                    return self.register, transferAccNum, self.transactionHistory, False

                if amount <= self.register[accNum]["balance"]:
                    self.register[accNum]["balance"] -= amount
                    self.otherBanks[transferAccNum] += amount
                    clear_screen()
                    print("Transfer Successfull")
                    print(f"\n\nTransferd Funds \n\nFrom:\n\n Name: {self.userName.capitalize()}\t\t Account Number: {accNum}\n Balance: {self.register[accNum]["balance"]}\n\nTo:\n\n Name: {transferName.capitalize()}\t\t Account Number: {transferAccNum}\n\n\tAmount: {amount}\t\t Time: {datetime.now()}")
                    # key = f"{datetime.now()}"
                    self.transactionHistory[self.userName]["To"][f"{datetime.now()}"] = [amount, transferName.capitalize(), transferAccNum]
                    # self.transactionHistory[self.userName]["To"][key].append(amount, transferAccNum)
                    ex = input("\n\n Press Any Button To Return")
                    clear_screen()
                    return self.register, transferAccNum, self.transactionHistory, False
                else:
                    print(f"==>> Erorr: \n\t Not Enough Balance \n\n\t\t Your Balance Is ==>>  {self.register[accNum]["balance"]}")
            
    def payBenificerySameBank(self, transferAccNum, userName, register, accNum):
        while True:
            amount = self.handleException.check_Int(f"How much MONEY you ant to send to {userName.capitalize()}\t\t Your Current Balance: {self.register[accNum]["balance"]} \n\nPress 00 To Return ==>>")
            if amount == 00:
                clear_screen()
                return self.register, transferAccNum, self.transactionHistory

            if amount <= self.register[accNum]["balance"]:
                self.register[accNum]["balance"] -= amount
                self.register[transferAccNum]["balance"] += amount
                clear_screen()
                print("Transfer Successfull")
                print(f"\n\nTransferd Funds \n\nFrom:\n\n Name: {self.userName.capitalize()}\t\t Account Number: {accNum}\n Balance: {self.register[accNum]["balance"]}\n\nTo:\n\n Name: {userName.capitalize()}\t\t Account Number: {transferAccNum}\n\n\tAmount: {amount}\t\t Time: {datetime.now()}")
                # key = f"{datetime.now()}"
                self.transactionHistory[self.userName]["To"][f"{datetime.now()}"] = [amount, userName.capitalize(), transferAccNum]
                # self.transactionHistory[self.userName]["To"][key].append(amount, transferAccNum)
                ex = input("\n\n Press Any Button To Return")
                clear_screen()
                return self.register, transferAccNum, self.transactionHistory
            else:
                print(f"==>> Erorr: \n\t Not Enough Balance \n\n\t\t Your Balance Is ==>>  {self.register[accNum]["balance"]}")

    def payBenificeryOtherBanks(self, transferAccNum, userName, otherBanks, accNum):
        while True:
            amount = self.handleException.check_Int(f"How much MONEY you ant to send to {userName.capitalize()}\t\t Your Current Balance: {self.register[accNum]["balance"]} \n\nPress 00 To Return ==>>")
            if amount == 00:
                clear_screen()
                return self.register, otherBanks, self.transactionHistory

            if amount <= self.register[accNum]["balance"]:
                self.register[accNum]["balance"] -= amount
                otherBanks[transferAccNum] += amount
                clear_screen()
                print("Transfer Successfull")
                print(f"\n\nTransferd Funds \n\nFrom:\n\n Name: {self.userName.capitalize()}\t\t Account Number: {accNum}\n Balance: {self.register[accNum]["balance"]}\n\nTo:\n\n Name: {userName.capitalize()}\t\t Account Number: {transferAccNum}\n\n\tAmount: {amount}\t\t Time: {datetime.now()}")
                # key = f"{datetime.now()}"
                self.transactionHistory[self.userName]["To"][f"{datetime.now()}"] = [amount, userName.capitalize(), transferAccNum]
                # self.transactionHistory[self.userName]["To"][key].append(amount, transferAccNum)
                ex = input("\n\n Press Any Button To Return")
                clear_screen()
                return self.register, otherBanks, self.transactionHistory
            else:
                print(f"==>> Erorr: \n\t Not Enough Balance \n\n\t\t Your Balance Is ==>>  {self.register[accNum]["balance"]}")

    def payBills(self, transferName, genre, accNum, organizationsDetails):

        while True:
            accId = self.handleException.check_IntLen(f"Write Your {transferName} Bill ID To Pay Your Bill\n\n==>>", 'bills')
            if accId == 0:
                clear_screen()
                return self.register, organizationsDetails, self.transactionHistory

            elif accId in organizationsDetails[genre][transferName].keys():
                if organizationsDetails[genre][transferName][accId] == 0:
                    clear_screen()
                    ex = input(f"\n Your Bill Against Acount Id {accId} is Already paid \n\n Totall Amount to be paid is 0 \n\n Press any button to return")
                    return self.register, organizationsDetails, self.transactionHistory

                billAmount = organizationsDetails[genre][transferName][accId]
                clear_screen()
                while True:
                    
                    choice = input(f"Your Totall Bill of {transferName} Bill ID: {accId}Be Paid is\n\n\t ==>>Amount:{billAmount}\n\nPress Y to PAY and N to cancel\n\n==>>")
                    if choice.lower() == 'y':
                        if billAmount <= self.register[accNum]["balance"]:
                            self.register[accNum]["balance"] -= billAmount
                            organizationsDetails[genre][transferName]["totall_amount_ever_paid"] += billAmount
                            organizationsDetails[genre][transferName][accId] = 0

                            print(f"\n\nBill Paid: \n\nFrom:\n\n Name: {self.userName.capitalize()}\t\t Account Number: {accNum}\n Balance: {self.register[accNum]["balance"]}\n\nTo:\n\n Organization Name: {transferName.capitalize()}\t\t Account ID: {accId}\n\n\tAmount: {billAmount}\t\t Time: {datetime.now()}")
                            self.transactionHistory[self.userName]["To"][f"{datetime.now()}"] = [billAmount, transferName, accId]
                            ex = input("\n\n Press Any Button To Return")
                            clear_screen()
                            return self.register, organizationsDetails, self.transactionHistory
                        else:
                            clear_screen()
                            print(f"==>> Erorr: \n\t Not Enough Balance \n\n\t\t Your Balance Is ==>>  {self.register[accNum]["balance"]}")
                            
                    elif choice.lower() == 'n':
                        return self.register, organizationsDetails, self.transactionHistory
                    else:
                        clear_screen()
                        print("==>> Erorr: \n\t Invalid Input \n\t choose from below 2 only\n\n")
                
            else:
                print(f"==>> Erorr: \n\t Invalid Input \n\t This Account ID {accId} does not exsist\n\n")
    
    def payDonations(self, transferName, transferType, accNum, donations):
        while True:
            amount = self.handleException.check_Int(f"How much MONEY you want to Donate to {transferName.capitalize()} as a {transferType}\t\t Your Current Balance: {self.register[accNum]["balance"]}\n\nPress 00 To Return ==>>")
            if amount == 00:
                clear_screen()
                return self.register, donations, self.transactionHistory, 0
            if amount <= self.register[accNum]["balance"]:
                self.register[accNum]["balance"] -= amount
                donations[transferName][transferType] += amount
                clear_screen()
                print("Transfer Successfull")
                print(f"\n\nTransferd Funds \n\nFrom:\n\n Name: {self.userName.capitalize()}\t\t Account Number: {accNum}\n Balance: {self.register[accNum]["balance"]}\n\nTo:\n\n\t The Amount of {amount} is paid to {transferName} as a {transferType}\t\t Time: {datetime.now()}")
                # key = f"{datetime.now()}"
                self.transactionHistory[self.userName]["To"][f"{datetime.now()}"] = [amount, transferName, transferType]
                # self.transactionHistory[self.userName]["To"][key].append(amount, f"{transferName}  [{transferType}]")
                ex = input("\n\n Press Any Button To Return")
                clear_screen()
                return self.register, donations, self.transactionHistory, 1
            else:
                print(f"==>> Erorr: \n\t Not Enough Balance \n\n\t\t Your Balance Is ==>>  {self.register[accNum]["balance"]}")


class DisplayData:

    def __init__(self):
        self.handleException = ExceptionHandeling()

    displayOptions = {
            "initial ask" :{ 
                                "1" : "1: Register",
                                "2" : "2: Login",
                            },
            "after logins" :{ 
                                "transfer" : "1: Transfer",
                                "bills" : "2: Bills",
                                "donations" : "3: Donations",
                                "transaction history" : "4: Transaction History",
                                "bioData" : "5: Account Information"
                            },
            "diff bank acc" : {
                                "1" : "1: Allied Bank Limited (ABL)",
                                "2" : "2: Bank of Punjab (BOP)",
                                "3" : "3: Askari Bank",
                                "4" : "4: Bank Alfalah Limited (BAFL)",
                                "5" : "5: Bank Al-Habib Limited (BAHL)",
                                },
            "bills"         : {
                                "1: Internet" : {
                                                "1" : "1: Strom Fiber",
                                                "2" : "2: NAYA-Tel",
                                                "3" : "3: Fiber-Link",
                                                "3" : "4: Connect",
                                                },
                                "2: Electricity" : {
                                                "1" : "1: K-Electric",
                                                "2" : "2: LESCO",
                                                "3" : "3: IESCO",
                                                "3" : "4: Fesco",
                                                },
                                "3: Gas" :  {
                                                "1" : "1: SUI-Southern Gas Company",
                                                "2" : "2: SUI-Northern Gas Company",
                                            },
                                "4: Telephone" : {
                                                "1" : "1: PTCL",
                                            },
                                 },
            "donations"         : {
                                "1: Ithad Foundation" : {'1':'1: Sadqa','2':'2: Zakat'},
                                "2: Edhi Welfare" : {'1':'1: Sadqa','2':'2: Zakat'},
                                "3: Alkhidmat Foundation" : {'1':'1: Sadqa','2':'2: Zakat'},
                                "4: JDC Foundation" : {'1':'1: Sadqa','2':'2: Zakat'},
                                "5: Shaukat Khanam Memorial" : {'1':'1: Sadqa','2':'2: Zakat'},
                                "basic options" : {'1':'1: Sadqa','2':'2: Zakat'}
                                },

        }

    pickDisplayOptions = {
        "initial ask" :{ 
                            "1" : "1: Register",
                            "2" : "2: Login",
                        },
        "after logins" :{ 
                            "transfer" : "1: Transfer",
                            "bills" : "2: Bills",
                            "donations" : "3: Donations",
                        },
        "diff bank acc" : {
                            "1" : "1: Allied Bank Limited (ABL)",
                            "2" : "2: Bank of Punjab (BOP)",
                            "3" : "3: Askari Bank",
                            "4" : "4: Bank Alfalah Limited (BAFL)",
                            "5" : "5: Bank Al-Habib Limited (BAHL)",
                            },
        "bills"         : {
                            "Internet" : {
                                            "1" : "strom-fiber",
                                            "2" : "naya-tel",
                                            "3" : "fiber-link",
                                            "4" : "connect",
                                            },
                            "Electricity" : {
                                            "1" : "K-Electric",
                                            "2" : "LESCO",
                                            "3" : "IESCO",
                                            "3" : "Fesco",
                                            },
                            "Gas" :  {
                                            "1" : "SUI-Southern Gas Company",
                                            "2" : "SUI-Northern Gas Company",
                                        },
                            "Telephone" : {
                                            "1" : "PTCL",
                                        },
                                },
            "donations"         : {
                                "Ithad Foundation" : {'1':'1: Sadqa','2':'2: Zakat'},
                                "Edhi Welfare" : {'1':'1: Sadqa','2':'2: Zakat'},
                                "Alkhidmat Foundation" : {'1':'1: Sadqa','2':'2: Zakat'},
                                "JDC Foundation" : {'1':'1: Sadqa','2':'2: Zakat'},
                                "Shaukat Khanam Memorial" : {'1':'1: Sadqa','2':'2: Zakat'},
                                "basic options" : {'1':'Sadqa','2':'Zakat'}
                                },

        }

    def makeList(self):
        afterLogins = list(self.displayOptions["after logins"].keys())
        afterLoginsList = afterLogins

    def records(self, customers_details):
        records = customers_details

    def run_dict(self, feildName=''):
        if feildName == "initialAsk":
            return [value for value in self.displayOptions["initial ask"].values()]
        elif feildName == "after logins":
            return [value for value in self.displayOptions["after logins"].values()]
        elif feildName == "diff bank acc":
            return [value for value in self.displayOptions["diff bank acc"].values()]
        elif feildName == "bills":
            return [key for key in self.displayOptions["bills"].keys()]
        elif feildName == "donations":
            return [key for key in self.displayOptions["donations"].keys() if key != "basic options"]
        elif feildName == "1: Internet":
            return [value for value in self.displayOptions["bills"]["1: Internet"].values()]
        elif feildName == "2: Electricity":
            return [value for value in self.displayOptions["bills"]["2: Electricity"].values()]
        elif feildName == "3: Gas":
            return [value for value in self.displayOptions["bills"]["3: Gas"].values()]
        elif feildName == "4: Telephone":
            return [value for value in self.displayOptions["bills"]["4: Telephone"].values()]
        elif feildName == "donationKind":
            return [value for value in self.displayOptions["donations"]["basic options"].values()]

    def bills(self, feildName, feildName1):
        companyName = list(self.pickDisplayOptions["bills"][feildName].values())            # billing company stormfiber etc
        choice = self.handleException.check_Index(f"{"\n".join(self.run_dict(feildName1))}\n ==>", len(companyName))
        if choice == 0:
            temp = temp1 = 0
            return temp, temp1
        temp = companyName[choice-1]
        return temp, feildName
        
    def billChoice(self):
        billingChoice = list(self.pickDisplayOptions["bills"].keys())   #  shows Bill type Like internet, electricity etc
        choice = self.handleException.check_Index(f"{"\n".join(self.run_dict(feildName="bills"))}\n ==>>", len(billingChoice))
        if choice == 0:
            temp = temp1 = 0
            return temp, temp1
        temp = billingChoice[choice-1]
        tempList = list(self.displayOptions["bills"].keys())
        temp1 = tempList[choice-1]
        return temp, temp1

    def donationChoice(self):
        while True:
            donationChoice = list(self.pickDisplayOptions["donations"].keys())   #  shows donations type Like alkhidmat/JDCetc
            choice = self.handleException.check_Index(f"{"\n".join(self.run_dict(feildName="donations"))}\n ==>>", len(donationChoice))
            if choice == 0:
                temp = temp1 = 0
                return temp, temp1
            temp = donationChoice[choice-1]
            donationKindList = list(self.pickDisplayOptions["donations"]["basic options"].values())
            while True:
                donationKind = self.handleException.check_Index(f"{"\n".join(self.run_dict(feildName="donationKind"))}\n\n ==>>", len(donationKindList))
                if donationKind == 0:
                    clear_screen()
                    break
                temp1 = donationKindList[donationKind-1]
                return temp, temp1


class Benificery:
    def __init__(self):
        self.handleException = ExceptionHandeling()

        self.userName = None
        self.register = None
        self.otherBanks = None
        self.benificery = None

    def setData(self, userName, register='', otherBanks='', benificery=''):
        self.userName = userName
        self.register = register
        self.otherBanks = otherBanks
        self.benificery = benificery

    def addBenificerySameBank(self):
        while True:
            accNum = self.handleException.check_IntLen("Write your 14-digit account number == >>")
            if accNum == 0:
                return self.benificery, accNum, None, 0
            if accNum in self.benificery[self.userName].keys():
                clear_screen()
                print(f"\n==>>Invalid Account Number\n This Account Number Is Already Set For Other Account In Your Benificery List\nUnder The User Name: {self.benificery[self.userName][accNum]}")
                continue
            elif accNum in self.register.keys():
                while True:
                    userName = self.handleException.check_UserName("Enter Any User Name For Your New Benificery Account\n\n==>>", "benificery")
                    if userName == 0:
                        return self.benificery, accNum, None, 0
                    elif userName == self.benificery[self.userName].values():
                        tempAccNum = [key for key, value in self.benificery[self.userName].items() if value == userName]
                        clear_screen()
                        print(f"\n==>>Invalid User Name \n This User Name Is Already Set For Other Account In Your Benificery List.\nUnder The Account Number: {tempAccNum}")
                        continue
                    self.benificery[self.userName][accNum] = userName
                    print("User Added In Your Benificery List")
                    return self.benificery, accNum, userName, 1
            else:
                print("\n==>>Invalid Account Number\n This Account Number Is Not Registerd In This Bank.\n")

    def addBenificeryOtherBank(self):
        while True:
            accNum = self.handleException.check_IntLen("Write your 14-digit account number == >>")
            if accNum == 0:
                return self.otherBanks, self.benificery, accNum, None, 0
            if accNum not in self.benificery[self.userName].keys():
                while True:
                    userName = self.handleException.check_UserName("Enter Any User Name For Your New Benificery Account\n\n==>>", "benificery")
                    if userName == 0:
                        return self.otherBanks, self.benificery, accNum, None, 0
                    elif userName in self.benificery[self.userName].values():
                        tempAccNum = [key for key, value in self.benificery[self.userName].items() if value == userName]
                        clear_screen()
                        print(f"\n==>>Invalid User Name \n This User Name Is Already Set For Other Account In Your Benificery List\nUnder The Account Number: {tempAccNum}")
                        continue
                    self.benificery[self.userName][accNum] = userName
                    print("User Added In Your Benificery List")
                    if accNum not in self.otherBanks.keys():
                        self.otherBanks[accNum] = 0
                    return self.otherBanks, self.benificery, accNum, userName, 1
            else:
                clear_screen()
                print(f"\n==>>Invalid Account Number\n This Account Number Is Already Set For Other Account In Your Benificery List\nUnder The User Name: {self.benificery[self.userName][accNum]}")

    def fetchBenificeries(self):
        while True:
            if self.userName not in self.benificery.keys():
                self.benificery[self.userName] = {}
            temp = list(self.benificery[self.userName].values())
            tempDisplay = (f"{i}-{value}" for i,value in enumerate(temp, start=2) )
            options = (f"1: Add New Beneficiary Account\n\n\n\t\t*** Already Present Account***\n{"\n".join(tempDisplay)}\n\n=> Press 1 for adding New Beneficiary")
            choice = self.handleException.check_Int(f"{options}\n ==>>")
            clear_screen()
            if choice > len(temp)+1:
                clear_screen()
                print("==>> Erorr: \n\t Invalid Input \n\t choose from below options only\n\n")
                continue

            if choice == 0:
                accNum = userName = 0
                return accNum, userName
            elif choice == 1:
                accNum = userName = 1
                return accNum, userName
            else:
                choice -= 2
                userName = temp[choice]
                accNum = ''.join([key for key, value in self.benificery[self.userName].items() if value == userName])
                return accNum, userName


class Main:

    def __init__(self):              # Constructor:
        self.records = DataRecord()   # Self.records = DisplayRecord()    -->  records (object),  DataRecord (Class)
        self.display = DisplayData()
        self.handleException = ExceptionHandeling()
        self.logIn = LogIn()
        self.currentUser = CurrentUser()
        self.transfer = Transfer()
        self.register = Registraion()
        self.benificery = Benificery()

        clear_screen()
        self.firstStep()
        # self.secondStep()

    def setEssentials(self):
        
        self.records.loadFile()
        self.records.loadBenificeryFile()
        self.records.loadOtherBanksFile()
        self.records.loadRegistrationFile()
        self.records.loadOrganizationFile()
        self.records.loadDonationsFile()
        self.records.loadTransactionHistoryFile()
        self.logIn.setRecordsInVerify(self.records.customersDetails)
        
    def firstStep(self):

        self.setEssentials()   # setting up essential data(loading/fetching/setting)
        while True:
            options = "\n".join(self.display.run_dict(feildName="initialAsk"))       # ask weather register or login
            choice = self.handleException.check_Int(f"{options}\n ==>>")
            clear_screen()

            if choice == 0:
                break

            elif choice == 1:
                self.records.loadRegistrationFile()   # remove
                self.register.setRegister(self.records.registerationDetails, self.records.customersDetails, self.records.fetchRecords()) 
                self.records.customersDetails, flag = self.register.dataInput()   # customer e-banking registration process
                if flag == 0:
                    continue
                self.records.saveFile() 
                self.records.loadFile() 
                
            elif choice == 2:
                while True:
                    back, tempuserName = self.logIn.logins()   # customer will login

                    if back == 0:    # exit from current step ...breaks loop
                        break
                    elif back == 1:
                        self.records.customersDetails, flag = self.logIn.resetPassword(tempuserName)
                        if flag == 0:
                            continue
                        self.records.saveFile()
                        self.records.loadFile()
                        print("\n==> Now Try Again With New Password\n\n")
                        continue

                    

                    userName, balance = self.logIn.fetchLogin()
                    self.currentUser.setCurrentUser(userName, balance)  # set customer name and balance for permenant display and other use
                    self.records.setUserTransactionHistory(userName, self.records.fetchUserAccNum(userName))
                    clear_screen()

                    self.transfer.setData(self.currentUser.currentUser, self.records.customersDetails, self.records.registerationDetails, self.records.otherBanksDetails, self.records.transactionHistoryDetails)               # setting up data in transfer class for all purposes
                    self.currentUser.updateBalance(self.records.recordUpdation(self.records.fetchUserAccNum(self.currentUser.currentUser),self.currentUser.currentUser))        # updating/balancing record in rigester and record file
                    
                    self.records.saveFile()
                    print(f"Wellcome {self.currentUser.currentUser}")

                    # self.display.records(self.records.customersDetails) # remove idk y im doing this
                
                    while True:    
                        print(f"\n\nName: {self.currentUser.currentUser}\t\t Balance: {self.currentUser.currentBalance}\n\n") #display user name & balance

                        options = "\n".join(self.display.run_dict(feildName="after logins"))   # ask after login (transfer/bill/donations etc)
                        choice = self.handleException.check_Int(f"{options}\n ==>>")
                        clear_screen()

                        if choice == 0:        # exit from current step ...breaks loop
                            break

                        elif choice == 1:   # selecting transfering option
                            
                            self.benificery.setData(self.currentUser.currentUser, self.records.registerationDetails, self.records.otherBanksDetails, self.records.benificeryDetails)    # setting data in benificery class for transfering process

                            while True:
                                print(f"Name: {self.currentUser.currentUser}\t\t Balance: {self.currentUser.currentBalance}\n\n")

                                tempAccNum, tempUserName = self.benificery.fetchBenificeries()  # ask for trasnfer options (new or old)
                                clear_screen()

                                if tempAccNum == 0:         # exit from current step ...breaks loop
                                    break

                                elif tempAccNum != 1:   # transfering process if receiver is not new
                                    self.records.registerationDetails, recieverAccNum, self.records.transactionHistoryDetails, flag = self.transfer.transferMoney(self.records.fetchUserAccNum(self.currentUser.currentUser), tempAccNum, tempUserName)   # transfering money
        
                                    self.currentUser.updateBalance(self.records.recordUpdation(self.records.fetchUserAccNum(self.currentUser.currentUser),self.currentUser.currentUser))        # updating/balancing record in rigester and record file
                                    if flag:
                                        self.records.recordUpdationForReciever(recieverAccNum)
                                    self.records.saveTransactionHistoryFile()
                                    
                                    self.records.saveFile()  
                                    self.records.saveRegisterationFile()
                                    self.records.saveOtherBanksFile()

                                    continue

                                options = (f"\n1: This Bank\n\n2: Some Other Bank")   # ask if the receiver is new
                                choice = self.handleException.check_Int(f"{options}\n ==>>")
                                clear_screen()

                                if choice == 0:     # exit from current step ...will not breaks loop
                                    continue

                                elif choice == 1:   # if the reciever is in our bank
                                    
                                    self.records.benificeryDetails, tempAccNum, tempUserName, flag = self.benificery.addBenificerySameBank()#adding new benif...
                                    if flag == 0:
                                        clear_screen()
                                        continue

                                    self.records.registerationDetails, recieverAccNum, self.records.transactionHistoryDetails = self.transfer.payBenificerySameBank(tempAccNum, tempUserName, self.records.registerationDetails, self.records.fetchUserAccNum(self.currentUser.currentUser))  # Transfering funds after adding

                                    self.currentUser.updateBalance(self.records.recordUpdation(self.records.fetchUserAccNum(self.currentUser.currentUser),self.currentUser.currentUser))        # updating/balancing record in rigester and record file
                                    self.records.recordUpdationForReciever(recieverAccNum)
                                    self.records.saveTransactionHistoryFile()
                                    self.records.saveFile() 
                                    self.records.saveBenificeryFile()    
                                    self.records.saveRegisterationFile()
                                    

                                    continue

                                elif choice == 2:   # if the reciever is not in our bank (will be add in other bank file)

                                    self.records.otherBanksDetails, self.records.benificeryDetails, tempAccNum, tempUserName, flag = self.benificery.addBenificeryOtherBank()         #adding new benificeries

                                    if flag == 0:
                                        clear_screen()
                                        continue
                                    
                                    self.records.registerationDetails, self.records.otherBanksDetails, self.records.transactionHistoryDetails = self.transfer.payBenificeryOtherBanks(tempAccNum, tempUserName, self.records.otherBanksDetails, self.records.fetchUserAccNum(self.currentUser.currentUser))    # Transfering funds after adding

                                    self.currentUser.updateBalance(self.records.recordUpdation(self.records.fetchUserAccNum(self.currentUser.currentUser),self.currentUser.currentUser))     # updating/balancing record in rigester and record file...
                                    self.records.saveTransactionHistoryFile()
                                    self.records.saveFile() 
                                    self.records.saveRegisterationFile()
                                    self.records.saveBenificeryFile() 
                                    self.records.saveOtherBanksFile()       
                                                    

                                    continue
                                
                                else:
                                    clear_screen()
                                    print("==>> Erorr: \n\t Invalid Input \n\t choose from below 2 only\n\n")
                                    continue


                        elif choice == 2:       # transfering billing option
                            while True:
                                self.records.loadOrganizationFile()
                                print(f"Name: {self.currentUser.currentUser}\t\t Balance: {self.currentUser.currentBalance}\n\n")
                                print("\nChose what do you want to do : \n")         # its showing internet electercity etc
                                
                                feildName, feildName1 = self.display.billChoice()
                                if feildName == 0 and feildName1 == 0:
                                    clear_screen()
                                    break 
                                clear_screen()
                                while True:
                                    self.transfer.setData(self.currentUser.currentUser)
                                    print(f"Name: {self.currentUser.currentUser}\t\t Balance: {self.currentUser.currentBalance}\n\n")
                                    transferName, genre = self.display.bills(feildName, feildName1)
                                    
                                    clear_screen()
                                    if transferName == 0 and genre == 0:
                                        break
                                    clear_screen()

                                    print(f"Name: {self.currentUser.currentUser}\t\t Balance: {self.currentUser.currentBalance}\n\n")

                                    self.transfer.setData(self.currentUser.currentUser, self.records.customersDetails, self.records.registerationDetails, self.records.otherBanksDetails, self.records.transactionHistoryDetails) 
                                    
                                    self.records.registerationDetails, self.records.organizationsDetails, self.records.transactionHistoryDetails = self.transfer.payBills(transferName, genre, self.records.fetchUserAccNum(self.currentUser.currentUser), self.records.organizationsDetails)

                                    self.currentUser.updateBalance(self.records.recordUpdation(self.records.fetchUserAccNum(self.currentUser.currentUser),self.currentUser.currentUser))     # updating/balancing record in rigester and record file...
                                    self.records.saveTransactionHistoryFile()
                                    self.records.saveFile() 
                                    self.records.saveRegisterationFile()
                                    self.records.saveOrganizationFile()

                                    break

                                clear_screen()
                                
                        elif choice == 3:               # pay donations
                            while True:
                                transferName, transferType = self.display.donationChoice()
            
                                if transferName == 0:
                                    break 
                                
                                self.records.registrationDetails, self.records.donationsDetails, self.records.transactionHistoryDetails, flag = self.transfer.payDonations(transferName, transferType, self.records.fetchUserAccNum(self.currentUser.currentUser), self.records.donationsDetails)
                                if flag == 0:
                                    clear_screen()
                                    break
                                userName, balance = self.logIn.fetchLogin()
                                self.currentUser.setCurrentUser(userName, balance)

                                self.currentUser.updateBalance(self.records.recordUpdation(self.records.fetchUserAccNum(self.currentUser.currentUser),self.currentUser.currentUser))
                                self.records.saveTransactionHistoryFile()
                                self.records.saveFile()
                                self.records.saveDonationsFile()
                                
                                break
                                
                            clear_screen()
                        elif choice == 4:
                            self.records.fetchAccTransactionHistory(self.currentUser.currentUser)
                            ex = input("\n\n Press Any Button To Return")
                            clear_screen()
                            continue

                        elif choice == 5:   # display account information
                            while True:
                                self.records.fetchAccInfo(self.currentUser.currentUser)
                                choice = self.handleException.check_Int("Press 1 to change password and 0 to return\n\n==>>")

                                if choice == 0:             # exit from current step ...breaks loop
                                    clear_screen()
                                    break
                                if choice == 1:             # customer changes password
                                    self.records.customersDetails = self.logIn.changePassword(self.currentUser.currentUser)
                                    self.records.saveFile()
                                    clear_screen()
                                    continue
                                else:
                                    clear_screen()
                                    print("==>> Erorr: \n\t Invalid Input \n\t choose from below 2 only\n\n")
                                    continue
                        else:
                            clear_screen()
                            print("==>> Erorr: \n\t Invalid Input \n\t choose from below 5 only\n\n")
                            continue
                            

            else:
                clear_screen()
                print("==>> Erorr: \n\t Invalid Input \n\t choose from below 2 only\n\n")

        print("\n\t\tTHANKS FOR USING OUR SERVICES\n\t\t\t *** GOODBYE ***")
      
if __name__ == "__main__":
    main_instance = Main()  
    