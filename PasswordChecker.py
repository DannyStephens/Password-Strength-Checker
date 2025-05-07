PLengthScore = 0 #Password length score 1-5=1 6-8=2 9-11=3 12-15=4 16+=5
PComplexScore= 0 #Character variety (uppercase, lowercase, numbers, symbols)
PCommonScore= 0 #No common passwords - Implement list of common password to try
PRepeatedCScore= 0 #No repeated or sequential characters (like aaaa, 1234)

print("Password Strength Checker")
Password = input("Enter your password to see how strong it is:")
PLength = len(Password)

def LengthCheck():
  if PLength<=5:
    print("Password Length Insecure")
    PLengthScore = 1    
  
  elif 6 <= PLength <= 8:
      print("Password Length Weak")
      PLengthScore = 2      
  
  elif 9 <= PLength <= 11:
      print("Password Length Moderate")
      PLengthScore = 3      
  
  elif 12 <= PLength <= 15:
      print("Password Length Secure")
      PLengthScore = 4      
  
  elif PLength >= 16:
      print("Password Length Very Secure")
      PLengthScore = 5      
  
LengthCheck()
