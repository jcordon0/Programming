# -*- coding: utf-8 -*-
def StoredPasswords(password):
    
    checkPass = ['123456','123456789','12345','qwerty','password','12345678','111111','123123','1234567890','1234567','qwerty123',
                '000000','1q2w3e','aa12345678','abc123','password1','1234','qwertyuiop','123321','password123','1q2w3e4r5t',
                'iloveyou','654321','666666','987654321','123','123456a','qwe123','1q2w3e4r','7777777','1qaz2wsx','123qwe',
                'zxcvbnm','121212','asdasd','a123456','555555','dragon','112233','123123123','monkey','11111111','qazwsx',
                '159753','asdfghjkl','222222','1234qwer','qwerty1','123654','123abc']
    
    found = "\nYour password was found in the database. Please consider changing it.\n"
    notFound = "\nYour password was not found in the database.\n"
 # Instructed checkpass to append the password into its list   
    if password in checkPass:
        print(found, "\nFrom my database, The index for your password is: ",checkPass.index(password),"\n")
        checkPass.append(password)
        print(checkPass)
        print("\n*Appended to database*\n") 
# Return checked password to userpass function
        return(getUserPass)
    else:
        checkPass.append(password)
        print(checkPass)
        print(notFound,"*Appended to database*\n") 
    
def getUserPass():
 #gather input from user to pass to storedpasswords function   
    password = input("Please enter a Password that contains the following:\n"\
                      "\nlower & upper case letters-\nNumbers-\nSymbols-\nAccepted: ! @ % ^ & * ( )"\
                      "\nExcluded: # $ _ - + =\nAt least 8 characters long-\n")
#passing values to and from functions    
    valid_password(password)
    StoredPasswords(password)
    
def valid_password (password):
# created a list of incorrect characters to compare passed password to 
#length, uppercase, lowercase, digit are false and instructed to look for those parameters in the password string   
    accepted = ['!','@','%','^','&','*','(',')']
    symbol = False
    length = False
    uppercase = False
    lowercase = False
    digit = False

    if len(password) >= 8:
        length = True
# This codes calls the string searches and executes them          
    for ch in password:
        if ch.isupper():
            uppercase = True
        if ch.islower():
            lowercase = True
        if ch.isdigit():
            digit = True  
        if ch in accepted:
            symbol = True
 #if conditions are met password is checked against all previous checks and returns is_valid if pass           
    if length and uppercase and lowercase and digit and accepted:
        is_valid = True
        print("\nYour password meets the requirments\n") 
    else:
        is_valid = False
        input("\nYour password is invalid. Try again\n")
        
def main():
    getUserPass()
    
if __name__ =='__main__':
    main() 