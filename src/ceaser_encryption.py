alphabets = [' ' ,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
text = input("Enter text ").lower()
key = int(input("Enter key length "))
cipher=''
for char in text:
    index = (alphabets.index(char) + int(key)) % len(alphabets)
    cipher+=alphabets[index]


print("cipher text = ",cipher)
