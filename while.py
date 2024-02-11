# ps = str(input("придумайте пароль:   "))
# psw  = str(input("\n\n\n\n\n\n\nкакой парол?   "))
# while psw != ps:
#     print("ERROR PASSWARD")
#     psw  = str(input("какой пароль?   "))
# print("вход в систему")
# lg = str(input("придумайте логин:   "))
# ps = int(input("придумайте пароль:   "))
# log  = str(input("\n\n\n\n\n\n\nкакой логин?   "))
# while log != lg:
#     print("ERROR LOGIN")
#     log  = str(input("какой логин?   "))
# psw = int(input("\n\n\n\n\n\n\n\nкакой пароль ?  "))
# while psw != ps:
#     print("\n\n\n\n\n\nERROR PASSWARD ")
#     psw = int(input("какой пароль ?  "))
# print("выполняется вход")
# lg = str(input("придумайте логин:   "))
# ps = int(input("придумайте пароль:   "))
# log  = str(input("\n\n\n\n\n\n\nкакой логин?   "))
# psw = int(input("\n\n\n\n\n\n\n\nкакой пароль ?  "))
# while log != lg or psw != ps:
#     print("\n\n\n\n\n\n\nERROR RASSWARD or LOGIN")
#     log  = str(input("какой логин?   "))
#     psw = int(input("какой пароль ?  "))
lg = str(input("придумайте логин:   "))
ps = int(input("придумайте пароль:   "))
log  = str(input("\n\n\n\n\n\n\nкакой логин?   "))
psw = int(input("\n\n\n\n\n\n\n\nкакой пароль ?  "))
while log != lg or psw != ps :
    print("all ancorect ")
    if log != lg:
        print ("login error ")
        log  = str(input("какой логин?   "))  
    elif psw != ps:
        print("passward error")
        psw = int(input("какой пароль ?  "))     
print(" all corect")
      
    
    
    
