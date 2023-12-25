import random
import string

print("Welcome to the PyPassword Generator!")

length = int(input("Enter the length of password: "))  

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower + upper + num + symbols

password = "".join(random.sample(all,length)) 

print(f"The generated password is: {password}")