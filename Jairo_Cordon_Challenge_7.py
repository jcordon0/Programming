# -*- coding: utf-8 -*-
def StoredPasswords(checkPass):
    
    password_tuple = ('123456','123456789','12345','qwerty','password','12345678','111111','123123','1234567890','1234567','qwerty123',
                '000000','1q2w3e','aa12345678','abc123','password1','1234','qwertyuiop','123321','password123','1q2w3e4r5t',
                'iloveyou','654321','666666','987654321','123','123456a','qwe123','1q2w3e4r','7777777','1qaz2wsx','123qwe',
                'zxcvbnm','121212','asdasd','a123456','555555','dragon','112233','123123123','monkey','11111111','qazwsx',
                '159753','asdfghjkl','222222','1234qwer','qwerty1','123654','123abc')
    
    found = "\nYour password is too common. Please consider changing it."
    notFound = "\nYou have a strong password."
    
    if checkPass in password_tuple:
        print("\nFrom my database, The index for your password is:",password_tuple.index(checkPass))
        checkPass = found
        print(checkPass)
    else:
        checkPass = notFound
        print(checkPass)
    return
def getUserPass():
    
    user_name = input("Hello,\nPlease enter a Username:\n")
    checkPass = input("Please enter a Password:\n")
    StoredPasswords(checkPass)
    print(checkPass)
    
def main():
    getUserPass()
    
if __name__ =='__main__':
    main() 