
def checkPass():
    password=input("Enter a password:")
    count=0
    hasLower = False
    hasUpper = False
    hasSpecial = False
    isCommon = False
    isPassStrng = False
    special = ["@","$","!","#","%","^","/","*"]
    commonPass=["abc", 'abc123']
    #check password length, uppercase and lowercase
    for char in password:
        count+=1
        if char.isupper() :
            hasUpper = True
        if char.islower() :
            hasLower = True
    if hasUpper == False or hasLower == False:
        print("Include uppercase and lower case")
    if count < 8 or count > 16:
        print("Make sure the password is between 8 and 16 characters")

    
    #check special character
    for specials in special:
        if specials in password:
            hasSpecial = True
            break
    if hasSpecial == False:
        print("Include special character in password")

    #check for common pass
    for common in commonPass:
        if common == password:
            print("this is a common password")
            isCommon=True

    if hasLower==True and hasUpper==True and hasSpecial==True and isCommon == False and count>8 and count<16:
        print("pass is strong")
    else:
        print("Reenter the password")
        checkPass()

checkPass()
