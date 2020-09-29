
from tkinter import *
import tkinter as tk
import random 
import time 
import datetime 
  

# creating root object and image
root_stong = tk.Tk()

# defining size of window 
root_stong .geometry("1200x600") 
# setting up the title of window 
root_stong.title("Message Encryption and Decryption") 
logo = tk.PhotoImage(file="python_logo_small7.gif")
w1 = tk.Label(root_stong , image=logo).pack()

Tops = Frame(root_stong, width = 1600,height =700) 
Tops.pack() 
f1 = Frame(root_stong, width = 800, height = 700) 
f1.pack()
# ============================================== 
#                  TIME 
# ==============================================

localtime = time.asctime(time.localtime(time.time()))
                       
  
lblInfo = Label(Tops, font=('arial', 20, 'bold'), 
             text = localtime, fg = "Black", 
                           bd = 10, anchor = "center")
                          
lblInfo.grid(row = 0, column = 0) 

rand = StringVar()
Id  = StringVar()
Msg = StringVar() 
key = StringVar() 
mode = StringVar() 
Result = StringVar() 

# exit function 
def qExit(): 
  root.destroy() 

# Function to reset the window 
def Reset(): 
  rand.set("")
  Id.set("")
  Msg.set("") 
  key.set("") 
  mode.set("") 
  Result.set("") 


# reference 
lblReference = Label(f1, font = ('arial', 16, 'bold'),text = "NAME :", bd = 16, anchor = "w") 
        
lblReference.grid(row = 0, column = 0)

lblReference = Label(f1, font = ('arial', 16, 'bold'),text = "ID No:", bd = 16, anchor = "w") 
        
lblReference.grid(row = 0, column = 2) 

txtReference = Entry(f1, font = ('arial', 16, 'bold'),textvariable = rand, bd = 10, insertwidth = 4) 
            
txtReference.grid(row = 0, column = 1)
txtReference = Entry(f1, font = ('arial', 16, 'bold'),textvariable = Id, bd = 10, insertwidth = 4) 
            
txtReference.grid(row = 0, column = 3) 


# labels 
lblMsg = Label(f1, font = ('arial', 16, 'bold'),text = "MESSAGE :", bd = 16, anchor = "w") 
    
lblMsg.grid(row = 1, column = 0) 

txtMsg = Entry(f1, font = ('arial', 16, 'bold'),textvariable = Msg, bd = 10, insertwidth = 4) 
        
txtMsg.grid(row = 1, column = 1) 

lblkey = Label(f1, font = ('arial', 16, 'bold'),text = "KEY :", bd = 16, anchor = "w")
      
lblkey.grid(row = 2, column = 0) 

txtkey = Entry(f1, font = ('arial', 16, 'bold'),textvariable = key, bd = 10, insertwidth = 4) 
        
txtkey.grid(row = 2, column = 1) 

lblmode = Label(f1, font = ('arial', 16, 'bold'),text = "MODE[e for encrypt, d for decrypt] :",bd = 16, anchor = "w") 
                
lblmode.grid(row = 3, column = 0) 

txtmode = Entry(f1, font = ('arial', 16, 'bold'),textvariable = mode, bd = 10, insertwidth = 4) 
          
txtmode.grid(row = 3, column = 1) 

lblService = Label(f1, font = ('arial', 16, 'bold'),text = "RESULT :", bd = 16, anchor = "w") 
      
lblService.grid(row = 2, column = 2) 

txtService = Entry(f1, font = ('arial', 16, 'bold'),textvariable = Result, bd = 10, insertwidth = 4) 
            
txtService.grid(row = 2, column = 3) 

# Vigenère cipher 
import base64 

# Function to encode 
def encode(key, clear): 
  enc = [] 
  for i in range(len(clear)): 
    key_c = key[i % len(key)] 
    enc_c = chr((ord(clear[i]) + ord(key_c)) % 256) 
    enc.append(enc_c) 
  return base64.urlsafe_b64encode("".join(enc).encode()).decode() 

# Function to decode 
def decode(key, enc): 
  dec = [] 
  enc = base64.urlsafe_b64decode(enc).decode() 
  for i in range(len(enc)): 
    key_c = key[i % len(key)] 
    dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)   
    dec.append(dec_c) 
  return "".join(dec) 


def Ref(): 
  #print("Message= ", (Msg.get())) 
  clear = Msg.get() 
  k = key.get() 
  m = mode.get() 
  if (m == 'e'):
                Result.set(encode(k, clear)) 
  else:
                Result.set(decode(k, clear)) 

# Show message button 
btnTotal = Button(f1, padx = 16, pady = 8, bd = 16, fg = "black",font = ('arial', 16, 'bold'), width = 10,text = "Show Result", bg = "green",command = Ref).grid(row = 7, column = 1) 

# Reset button 
btnReset = Button(f1, padx = 16, pady = 8, bd = 16,fg = "black", font = ('arial', 16, 'bold'),width = 10, text = "Reset", bg = "powder blue",command = Reset).grid(row = 7, column = 2) 

# Exit button 
btnExit = Button(f1, padx = 16, pady = 8, bd = 16,fg = "black", font = ('arial', 16, 'bold'),width = 10, text = "Exit", bg = "red",command = qExit).grid(row = 7, column = 3) 

# keeps window alive 
root_stong.mainloop()
