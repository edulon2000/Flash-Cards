from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card= {}
to_learn  = {}
# ---- Flash cards ----
try:
    data = pandas.read_csv("flash-card-project-start\\data\\words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("flash-card-project-start\data\db.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn =data.to_dict(orient="records")
    

def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title,text = "English",fill = "black")    
    canvas.itemconfig(card_word,text = current_card["English"],fill = "black")
    canvas.itemconfig(canva_image, image = frontcard_img)
    flip_timer = window.after(3000,func=flip_card)

def is_know():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("flash-card-project-start\\data\\words_to_learn.csv",index=False)
    next_card()
        
def flip_card():
    canvas.itemconfig(canva_image,image = backcard_img)
    canvas.itemconfig(card_title,text = "Português",fill = "white")    
    canvas.itemconfig(card_word,text = current_card["Portugues"],fill = "white")
   
# ----UI----


window = Tk()
window.title("Flash card")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer = window.after(3000,func=flip_card)

canvas = Canvas(width=800, height=526,bg=BACKGROUND_COLOR, highlightthickness=0)
frontcard_img = PhotoImage(file="flash-card-project-start\\images\\card_front.png")
canva_image = canvas.create_image(400,263, image = frontcard_img)
backcard_img = PhotoImage(file="flash-card-project-start\\images\\card_back.png")

card_title = canvas.create_text(400,150, text="English",fill= "Black", font=("Ariel",40,"italic"))
card_word = canvas.create_text(400,263, text=" ",fill= "Black", font=("Ariel",60,"bold"))
canvas.grid(column=0,row=0,columnspan=2)


wrong_img = PhotoImage(file="flash-card-project-start\\images\\wrong.png")
wrong_button = Button(text="Wrong",highlightthickness=0,image=wrong_img,command=next_card)
wrong_button.grid(column=0,row=1,sticky="s")
wrong_button.config(padx=50,pady=50)

right_img = PhotoImage(file="flash-card-project-start\\images\\right.png")
right_button = Button(text="Right",highlightthickness=0,image=right_img,command=is_know)
right_button.grid(column=1,row=1,sticky="s")
right_button.config(padx=50,pady=50)


next_card()



window.mainloop()