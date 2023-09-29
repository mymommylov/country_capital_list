from tkinter import *
import random

root = Tk()
root.title("Country Capitals")
root.geometry("400x400")

country_name = Entry(root)
country_name.place(relx = 0.5, rely = 0.2, anchor = CENTER)

capital_name = Entry(root)
capital_name.place(relx = 0.5, rely = 0.3, anchor = CENTER)

capital_list = Label(root)
country_list = Label(root)
capital_random = Label(root)
country_random = Label(root)

country_list1 = []
capital_list1 = []
def input_data():
    country = country_name.get()
    country_list1.append(country)
    country_list["text"] = "Country Name : " + str(country_list1)
    
    capital = capital_name.get()
    capital_list1.append(capital)
    capital_list["text"] = "Capital Name : " + str(capital_list1)

def random1():
    length = len(country_list1)
    random_no = random.randint(0, length-1)
    index = country_list1[random_no]
    country_random["text"] = "Random Country : " + str(index)
    
    length1 = len(capital_list1)
    random_no1 = random.randint(0, length1-1)
    index1 = capital_list1[random_no1]
    capital_random["text"] = "Random Capital : " + str(index1)
    
btn = Button(root, text = "Display Country & Capital Name", command = input_data, bg = "blue", fg = "white")
btn.place(relx = 0.5, rely = 0.4, anchor = CENTER)

country_list.place(relx = 0.5, rely = 0.5, anchor = CENTER)
capital_list.place(relx = 0.5, rely = 0.6, anchor = CENTER)
    
btn1 = Button(root, text = "Display Country & Capital Name Randomly", command = random1, bg = "blue", fg = "white")
btn1.place(relx = 0.5, rely = 0.7, anchor = CENTER)

country_random.place(relx = 0.5, rely = 0.8, anchor = CENTER)
capital_random.place(relx = 0.5, rely = 0.9, anchor = CENTER)

root.mainloop()