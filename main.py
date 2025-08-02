import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.title("StoryBoard")
window.geometry("400x400")

story = "Echoing Well. Whispering woods. Legends hint at power."

def madeWish():
  global story
  canvas.itemconfig(container, image=op1A)
  story = "Wish spoken. Price unknown."
  storyLabel["text"] = story
  option1.pack_forget()
  option2.pack_forget()
  option1A.pack()
  option1B.pack()

def observed():
  global story
  canvas.itemconfig(container, image=op2)
  story = "No magic. But something is missed."
  storyLabel["text"] = story
  option1.pack_forget()
  option2.pack_forget()
  option2A.pack()
  option2B.pack()

def seekPrice():
  global story
  canvas.itemconfig(container, image=op1AI)
  story = "Wish granted. Burden shared. Community blossoms in echo’s wake"
  storyLabel["text"] = story
  option1A.pack_forget()
  option1B.pack_forget()
  restartButton.pack()
  
def hopeBest():
  global story
  canvas.itemconfig(container, image=op1AI)
  story = "Wish granted. Burden shared. Community blossoms in echo’s wake"
  storyLabel["text"] = story
  option1A.pack_forget()
  option1B.pack_forget()
  restartButton.pack()
  
def quietW():
  global story
  canvas.itemconfig(container, image=op2AI)
  story = "No magic cast. But truth uncovered. The well gave its gift slowly."
  storyLabel["text"] = story
  option2A.pack_forget()
  option2B.pack_forget()
  restartButton.pack()

def chillW():
  global story
  canvas.itemconfig(container, image=op2AII)
  story = "Magic unseen, but not absent. The village holds echoes of kindness."
  storyLabel["text"] = story
  option2A.pack_forget()
  option2B.pack_forget()
  restartButton.pack()
def restart():
  global story
  canvas.itemconfig(container, image=start)
  story = "You meet a woman on the way to a Replit meetup IRL"
  storyLabel["text"] = story
  restartButton.pack_forget()
  option1.pack()
  option2.pack()
  

start = ImageTk.PhotoImage(Image.open("images/op1.jpg"))
op1A = ImageTk.PhotoImage(Image.open("images/op1a.jpg"))
op1B = ImageTk.PhotoImage(Image.open("images/op1b.jpg"))
op1AI = ImageTk.PhotoImage(Image.open("images/op1Ai.jpg"))

op2 = ImageTk.PhotoImage(Image.open("images/op2.jpg"))
op2A = ImageTk.PhotoImage(Image.open("images/op2a.jpg"))
op2B = ImageTk.PhotoImage(Image.open("images/op2b.jpg"))
op2AI = ImageTk.PhotoImage(Image.open("images/op2Ai.jpg"))
op2AII = ImageTk.PhotoImage(Image.open("images/op2aii.jpg"))


canvas = tk.Canvas(window, width = 300, height = 200)
canvas.pack()
container = canvas.create_image(100,100,image = start)


storyLabel = tk.Label(text=story)
storyLabel.pack()

option1 = tk.Button(text="Make a wish", command=madeWish)
option1.pack()
option1A = tk.Button(text="Seek the price", command= seekPrice)
option1B = tk.Button(text="Hope for the best", command=hopeBest)

option2 = tk.Button(text="Observe from a distance", command=observed)
option2.pack()
option2A = tk.Button(text = "Search woods for clues", command= quietW)
option2B = tk.Button(text = "Return to village", command=chillW)

restartButton = tk.Button(text="Restart", command=restart)

tk.mainloop()
