#coded by cybereagle2001

import time
import os
import base64
from pylab import * 
import numpy as np
import math as m
import getpass

def encrypt(data):
    os.system("clear")
    chaine=""
    for loop in data:
        message= loop
        message_bytes= message.encode('ascii')
        base64_bytes= base64.b64encode(message_bytes)
        base64_message= base64_bytes.decode('ascii')
        chaine+= base64_message+";"
    enc_data=open("data.txt","w")
    enc_data.write(chaine)
    enc_data.close()
    login()

def decrypt(loop):
    base64_message = loop
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    return message

def equa(dec_user):
    os.system("clear")
    print("\033[0;36m")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("*-*-*-Equation Resolution-*-*-*")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("""
            choose one option: 
               1) ax+b=0
               2) ax+b=c
               3) ax²+bx+c=0
               4) ax²+bx+c=d
               5) exp(x)=b
               6) √x+a = b
               7) cos(x)= b
               8) sin(x)= b
               
               00) go back 
    """)
    print("\033[0;37m")
    message= dec_user+"~$ "
    menu_equa= int(input(message))
    if (menu_equa == 1):
        a= float(input("write the first coeff: "))
        b= float(input("write the constant: "))
        if (a == 0):
            print("all reals are solutions")
        else:
            x= -b/a
            print("the solution is : ", -b/a)
        restart=input("click enter to continue (result will be deleted)")
        equa(dec_user)

    elif (menu_equa == 2):
        a= float(input("write the first coeff: "))
        b= float(input("write the constant: "))
        c= float(input("the second member of the equation : "))
        if (a == 0):
            print("All Real are solutions")
        else:
            x= (c-b)/a
            print("the solution is {0}".format(x))
        restart=input("click enter to continue (result will be deleted)")
        equa(dec_user)

    elif (menu_equa == 3):
        a= float(input("write the first coeff: "))
        b= float(input("write the second coeff: "))
        c= float(input("write the constant: "))
        coeff=[a,b,c]
        print("the solutions are: ",np.roots(coeff))
        restart=input("click enter to continue (result will be deleted)")
        equa(dec_user)

    elif (menu_equa == 4):
        a= float(input("write the first coeff: "))
        b= float(input("write the second coeff: "))
        c= float(input("write the constant: "))
        d=float(input("write the second member of the equation: "))
        coeff=[a,b,c-d]
        print("the solutions are: ",np.roots(coeff))
        restart=input("click enter to continue (result will be deleted)")
        equa(dec_user)

    elif (menu_equa == 5):
        b= float(input("write the second member: "))
        x= m.log(b)
        print("the solution of this equation is: ",x)
        restart=input("click enter to continue (result will be deleted)")
        equa(dec_user)

    elif (menu_equa == 6):
        a= float(input("first constant: "))
        b= float(input("second constant: "))
        x= m.pow(b-a,2)
        print("the solution is : ", x)
        restart=input("click enter to continue (result will be deleted)")
        equa(dec_user)

    elif (menu_equa == 7):
        b= float(input("write the second member: "))
        x= m.acos(b)
        print("the solution is : ",x)
        restart=input("click enter to continue (result will be deleted)")
        equa(dec_user)

    elif (menu_equa == 8):
        b= float(input("write the second member: "))
        x= m.asin(b)
        print("the solution is: ",x)
        restart=input("click enter to continue (result will be deleted)")
        equa(dec_user)
    
    elif (menu_equa == 00):
        math(dec_user)

def func_cos(dec_user):
    x= linspace(-2*pi, 2*pi, 30)
    y= cos(x)
    plot(x,y,"b:o",label="cos(x)")
    title("function cos(x)")
    legend()
    show()
    graph(dec_user)

def func_sin(dec_user):
    x= linspace(-2*pi, 2*pi, 30)
    y= sin(x)
    plot(x,y,"r--",label="sin(x)")
    title("function sin(x)")
    legend()
    show()
    graph(dec_user)

def func_ln(dec_user):
    x= linspace(0, 2*pi, 30)
    y= log(x)
    plot(x,y,"r--",label="log(x)")
    title("function log(x)")
    legend()
    show()
    graph(dec_user)

def func_exp(dec_user):
    x= linspace(-2*pi, 2*pi, 30)
    y= exp(x)
    plot(x,y,"r--",label="exp(x)")
    title("function exp(x)")
    legend()
    show()
    graph(dec_user)

def func_ax(dec_user):
    a= float(input("please what is the x coeffician: "))
    b= float(input("what is the value of the constant: "))
    x=  linspace(-2*pi, 2*pi, 30)
    y= a*x+b
    plot(x,y,"r--",label="ax+b")
    title("function ax+b")
    legend()
    show()
    graph(dec_user)

def funx_axx(dec_user):
    a=float(input("the first coeffician: "))
    b= float(input("the second coeffican: "))
    c= float(input("the function canstant: "))
    x= linspace(-2*pi,2*pi)
    y=a*pow(x,2)+b*x+c
    plot(x,y,"r--",label="ax²+bx+c")
    title("function ax²+bx+c")
    legend()
    show()
    graph(dec_user)

def func_tan(dec_user):
    x= linspace(-2*pi, 2*pi, 30)
    y= tan(x)
    plot(x,y,"r--",label="tan(x)")
    title("function tan(x)")
    legend()
    show()
    graph(dec_user)


def graph(dec_user):
    os.system("clear")
    print("\033[0;33m")
    print("----------------------------")
    print("----------------------------")
    print("----- choose function ------")
    print("----------------------------")
    print("----------------------------")
    print(""" 
               1) cos(x)
               2) sin(x)
               3) ln(x)
               4) exp(x)
               5) ax+b
               6) ax²+bx+c
               7) tan(x)
               00) go back
    """)
    print("\033[0;37m")
    x=int(input("choose one option (1 - 7): "))
    if (x == 1):
        func_cos(dec_user)
    elif (x == 2):
        func_sin(dec_user)
    elif(x == 3):
        func_ln(dec_user)
    elif(x == 4):
        func_exp(dec_user)
    elif (x == 5):
        func_ax(dec_user)
    elif (x == 6):
        funx_axx(dec_user)
    elif (x == 7):
        func_tan(dec_user)
    elif (x == 00):
        math(dec_user)
    else:
        graph(dec_user)

def math(dec_user):
    os.system("clear")
    print("""
        ::::::::::::::::::::::::::::::::::
        ::::::::::::::::::::::::::::::::::   
    """)
    print("        :::::::::: hello ",dec_user,"::::::::::")
    print("""
        ::::::::::::::::::::::::::::::::::
        ::::::::::::::::::::::::::::::::::
    """)
    print("chose one option(1,2): ")
    print(" 1) equation resolution")
    print(" 2) function graphs")
    message= dec_user+"~$ "
    menu= int(input(message))
    if (menu == 1):
        equa(dec_user)
    elif (menu == 2):
        graph(dec_user)
    else:
        math(dec_user)

def login():
    os.system("clear")
    print(""" 
        ****************************
        ****************************
        ******** CandyMath *********
        ****************************
        ****************************
            """)
    user= input("username: ")
    passw= getpass.getpass("password: ")
    enc_data= open("data.txt","r")
    a= enc_data.read()
    enc_list= list(a.split(";"))
    dec_pass= decrypt(enc_list[5])
    dec_user= decrypt(enc_list[2])
    i=0
    if (user == dec_user):
        if (passw == dec_pass):
            math(dec_user)
        else:
            os.system("clear")
            print("Credential Error")
            print("username or password not found")
            time.sleep(3)
            login()
    else:
        os.system("clear")
        print("Credential Error")
        print("username or password not found")
        time.sleep(3)
        login()

def signup():
    os.system("clear")
    print("\033[0;32m")
    print("""  
               ////////////////////////////////
               ////////////////////////////////
               //////// Hello new user ////////
               ////////////////////////////////
               ////////////////////////////////""")
    print("\033[0;37m")
    print("\n please answer these questions: ")
    name= input("name : ")
    surname= input("surname: ")
    username= input("username: ")
    nationality= input("nationality: ")
    phone= input("phone number: ")
    password= getpass.getpass("password: ")
    co_password= getpass.getpass("confirm your password: ")
    i =0
    while ((co_password != password)):
        i=i+1
        if (i == 5):
            print("\033[0;31m")
            print("//////////// Warning ////////////")
            print("\033[0;37m")
            print(" this is your password: ",password)
            time.sleep(2)
        co_password=getpass.getpass("please confirm your password:(again):  ")
    data=[name,surname,username,nationality,phone,password]
    print(data)
    encrypt(data)

def main():
    print("\033[0;31m")
    print("******************************")
    print("******************************")
    print("** please choose one option **")
    print("******************************")
    print("******************************")
    print("\033[0;37m")
    print("1) sign up")
    print("2) login ")
    log= int(input("please choose one option: (1/2): "))
    while((log != 1) and (log != 2)):
        log= int(input("please choose one option: (1/2): "))
    if (log == 1):
        signup()
    elif (log == 2):
        login()

main()
