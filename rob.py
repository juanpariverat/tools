#este codigo para hablar con rob inteligencia artificial
from random import choice
user_name = raw_input("Como te llamas: ")
print("Hola me llamo rob estoy para servirte " +  user_name)

rob_saludos = ["", "hola", "rob_hola2"]
# rob_saludos2 = ["Hola", "ok", "hola rob", "va", "perfecto", "gracias", "ok rob"]
rob_comoestas_user = ["excelente", "muy bien", "bien"]
rob_comoestas = ["como estas rob", "como estas", "como andas"]
user = raw_input("")
if user in rob_saludos:
    print(choice(rob_saludos) + user_name)
    user_saludo =  raw_input("")
    if user_saludo in rob_saludos:
        print (choice(rob_saludos) + '  ' +  user_name)
else :
    print("what...")


user_comoestas = raw_input("")
if user_comoestas in rob_comoestas:
    print (choice(rob_comoestas_user) + " " + user_name + ", que nesecitas")
else:
    rob_comoestas_user.append(user_comoestas)
    print (choice(rob_comoestas_user)+ " "  + user_name)
user_respuestas = raw_input("")


def escribe ():
    escribe = []
    escuchar= raw_input("Dime algo: ")
    escribe.append(escuchar)
    print(str(escribe))
    if escribe in rob_comoestas:
        print(rob_comoestas_user + " y tu ")

escribe()
