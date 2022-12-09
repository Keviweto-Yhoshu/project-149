# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 19:25:40 2022

@author: Keviweto
"""

from tkinter import*
import random

root=Tk()

root.title("Random Words")
root.geometry("500x500")

label_random = Label(root)
label_random.place(relx=0.5,rely=0.6)



def ran():
    alphabets=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    print(alphabets)
    alpha_list = alphabets
    random_no1 = random.randint(0,25)
    print(random_no1)
    random_no2 = random.randint(0,25)
    print(random_no2)
    random_no3 = random.randint(0,25)
    print(random_no3)
    random_no4 = random.randint(0,25)
    print(random_no4)
    random_no5 = random.randint(0,25)
    print(random_no5)
    
    random_alpha1 = alpha_list[random_no1]
    random_alpha2 = alpha_list[random_no2]
    random_alpha3 = alpha_list[random_no3]
    random_alpha4 = alpha_list[random_no4]
    random_alpha5 = alpha_list[random_no5]
    
    label_random["text"] = random_alpha1 + random_alpha2 + random_alpha3 + random_alpha4 + random_alpha5
    
    

btn= Button(root, text="word",bg="yellow",command=ran)
btn.place(relx=0.5, rely=0.4, anchor=CENTER)

root.mainloop()
    
    