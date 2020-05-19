import sys
sys.path.insert(0, './src')

from src.lsb_stegno import lsb_encode, lsb_decode
from src.n_share import generate_shares, compress_shares

# Main Function         
if __name__ == "__main__":

    a = int(input("Press 1 for Encoding\nPress 2 for Decoding\nEnter choice: ")) 
    if (a == 1): 
        print("Encoding...")
        data = lsb_encode() 
        print("Generating shares...")
        generate_shares(data)
        print("COMPLETED")
          
    elif (a == 2): 
        print("Compressing shares...")
        compress_shares()
        print("Decoded message: " + lsb_decode("images/compress.png") + "\nCOMPLETED")
    else: 
        raise Exception("Enter correct input") 
