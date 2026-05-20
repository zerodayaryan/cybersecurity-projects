alphabets = [' ' ,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
text = input("Enter text ").lower()
key = int(input("Enter key length "))
cipher=''
special=['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
numbers=str([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
index=0
for char in text:
   if char in special or char in numbers:
    cipher+=char
   else:
    index = (alphabets.index(char) + int(key)) % len(alphabets)
    cipher+=alphabets[index]

print("cipher text = ",cipher)
