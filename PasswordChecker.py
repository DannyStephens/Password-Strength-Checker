import string

PLengthScore = 0
PComplexScore = 0
PCommonScore = 0
PRepeatedCScore = 0

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
    if any(c.isupper() for c in Password):
        score += 1
    if any(c.isdigit() for c in Password):
        score += 1
    if any(c in string.punctuation for c in Password):
        score += 1

    PComplexScore = score
    print(f"Password Complexity Score: {score}/4")

def CommonCheck():
    global PCommonScore
    min_score = 5
    with open(r'/content/drive/MyDrive/Passwords.txt', 'r') as fp:
        lines = fp.readlines()
        for row in lines:
            clean_row = row.strip()
            if Password == clean_row:
                min_score = 0
                PCommonScore = 1
                break
            else:
              if Password in clean_row:
                  min_score = min(min_score, 1)
                  PCommonScore = 2
                  break
              else:
                PCommonScore = 3
    print(f"Password Commonness Score: {PCommonScore}/3")

def RepeatCheck():
    global PRepeatedCScore
    RCount = 1
    prev_char = ""

    for i, c in enumerate(Password):
        if c == prev_char:
            RCount += 1
            if RCount >= 4:
                print("Password Repeated Characters Score: 1/4")
                PRepeatedCScore = 1
                return
        else:
            RCount = 1

        if i >= 3 and Password[i-3] == Password[i-1] and Password[i-2] == Password[i]:
            print("Password Repeated Characters Score: 2/4")
            PRepeatedCScore = 2
            return

        prev_char = c

    if RCount == 3:
        print("Password Repeated Characters Score: 3/4")
        PRepeatedCScore = 3
    else:
        print("Password Repeated Characters Score: 4/4")
        PRepeatedCScore = 4



LengthCheck()
ComplexCheck()
CommonCheck()
RepeatCheck()

total_score = PLengthScore + PComplexScore + PCommonScore + PRepeatedCScore
max_score = 5 + 4 + 3 + 4
print(f"\nTotal Password Strength Score: {total_score}/{max_score}")



