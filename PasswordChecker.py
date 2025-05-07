import string

PLengthScore = 0  # Password length score 1-5=1 6-8=2 9-11=3 12-15=4 16+=5
PComplexScore = 0  # Character variety (uppercase, lowercase, numbers, symbols)
PCommonScore = 0   # No common passwords - Implement list of common passwords
PRepeatedCScore = 0  # No repeated or sequential characters (like aaaa, 1234)

print("Password Strength Checker")
Password = input("Enter your password to see how strong it is: ")
PLength = len(Password)

def LengthCheck():
    global PLengthScore
    if PLength <= 5:
        print("Password Length Score 1/5")
        PLengthScore = 1    
    elif 6 <= PLength <= 8:
        print("Password Length Score 2/5")
        PLengthScore = 2      
    elif 9 <= PLength <= 11:
        print("Password Length Score 3/5")
        PLengthScore = 3      
    elif 12 <= PLength <= 15:
        print("Password Length Score 4/5")
        PLengthScore = 4      
    elif PLength >= 16:
        print("Password Length Score 5/5")
        PLengthScore = 5     

def ComplexCheck():
    global PComplexScore
    score = 0
    if any(c.islower() for c in Password):
        score += 1
    elif any(c.isupper() for c in Password):
        score += 1
    elif any(c.isdigit() for c in Password):
        score += 1
    elif any(c in string.punctuation for c in Password):
        score += 1

    PComplexScore = score
    print(f"Password Complexity Score: {score}/4")

LengthCheck()
ComplexCheck()
