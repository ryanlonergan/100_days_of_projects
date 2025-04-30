from tkinter import *
from PIL import Image, ImageTk
import requests


def get_quote():
    response = requests.get(url='https://stoic.tekloon.net/stoic-quote')
    response.raise_for_status()

    data = response.json()
    quote = data['data']['quote'] + ' - ' + data['data']['author']

    canvas.itemconfig(quote_text, text=quote)


window = Tk()
window.title("Stoic Quotes")
window.config(padx=50, pady=50)


canvas = Canvas(width=400, height=514)
background_img = PhotoImage(file="background.png")
canvas.create_image(250, 307, image=background_img)
quote_text = canvas.create_text(250, 307, text="Stoic Quote Goes HERE", width=250, font=("Consolas", 20, "bold"),
                                fill="white")
canvas.grid(row=0, column=0)

image = Image.open("marcus_aurelius.png")
image_resized = image.resize((200, 200))

img = ImageTk.PhotoImage(image_resized)

stoic_button = Button(image=img, highlightthickness=0, borderwidth=0, command=get_quote)
stoic_button.grid(row=1, column=0)

get_quote()

window.mainloop()
