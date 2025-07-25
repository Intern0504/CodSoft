print("Welcome to our password generator 👑")
length=int(input("Enter the required lenght of the password: "))
letters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits="0123456789"
symbols="@!#$%^&*()_+"
all=letters+digits+symbols
word=input("Type any word (it will be used to mix password) : ")
password=""
index=0
for i in range(length):
    char=word[i%len(word)]
    index=(index + ord(char)+i)%len(all)
    password +=all[index]
print("Password generated : ",password)