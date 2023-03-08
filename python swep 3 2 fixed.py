from tkinter import *

import random
Korean=["Kimbab","Kimchi-fried rice","Bulgogi"]
Japanese=["Sushi","Ramen","Udon","Domburi"]
Chinese=["Beijing Duck","Dumpling","Pork fried rice"]
def recommendation():
    country=whitebox.get()
    if country == "korean":
        food=random.choice(Korean)
    elif country == "Korean":
        food=random.choice(Korean)
    elif country == "KOREAN":
        food.random.choice(Korean)
    elif country == "chinese":
        food=random.choice(Chinese)
    elif country == "Chinese":
        food=random.choice(Chinese)
    elif country == "CHINESE":
        food=random.choice(Chinese)
    elif country == "japanese":
        food=random.choice(Japanese)
    elif country == "Japanese":
        food=random.choice(Japanese)
    elif country == "JAPANESE":
        food.random.choice(Japanese)
    text3.config(text="Try "+food+"!")
     
window = Tk()
window.title("Menu Recommendation")
window.geometry("5000x5000")

text1 = Label(window,text="Welcome to Menu Recommendation")
text1.pack()

text2 = Label(window,text="A A.I. will ask youc a question. Please answer it!")
text2.pack()

text3 = Label(window,text="Which do you like? (Enter Korean/Chinese/Japanese)")
text3.pack()

whitebox=Entry(window)
whitebox.pack()

button1=Button(window, text="Recommend",command=recommendation)
button1.pack()

window.mainloop()
