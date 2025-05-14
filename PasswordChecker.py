#ADD BIGGER PASSWORD LIST
#ADD PREDICTION OF HOW LONG TO CRACK


import string
import getpass

PLengthScore = 0
PComplexScore = 0
PCommonScore = 0
PRepeatedCScore = 0
Game = 1

print("Password Strength Checker")
while Game == 1:
  Password = getpass.getpass("Enter your password to see how strong it is: ")
  PLength = len(Password)

  def LengthCheck():
      global PLengthScore
      if PLength <= 5:
          PLengthScore = 1
      elif 6 <= PLength <= 8:
          PLengthScore = 2
      elif 9 <= PLength <= 11:
          PLengthScore = 3
      elif 12 <= PLength <= 15:
          PLengthScore = 4
      elif PLength >= 16:
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

  def CommonCheck():
      global PCommonScore
      min_score = 5
      print("Opening text file")
      with open(r'/content/drive/MyDrive/rockyou.txt', 'r', encoding='ISO-8859-1') as fp:
          lines = fp.readlines()
          for row in lines:
              clean_row = row.strip()
              if Password == clean_row:
                  min_score = 0
                  PCommonScore = 1
                  break
              else:
                  PCommonScore = 2

  def RepeatCheck():
      global PRepeatedCScore
      RCount = 1
      prev_char = ""

      for i, c in enumerate(Password):
          if c == prev_char:
              RCount += 1
              if RCount >= 4:
                  # 4 characters repeated
                  PRepeatedCScore = 1
                  return
          else:
              RCount = 1

          if i >= 3 and Password[i-3] == Password[i-1] and Password[i-2] == Password[i]:
              PRepeatedCScore = 2
              #similar characters repeated twice e.g. asas
              return

          prev_char = c

      if RCount == 3:
          # 3 characters repeated
          PRepeatedCScore = 3
      else:
          # no repeats
          PRepeatedCScore = 4


  LengthCheck()
  ComplexCheck()
  CommonCheck()
  RepeatCheck()


  PLengthScore = PLengthScore*0.4
  PComplexScore = PComplexScore*0.45
  PRepeatedCScore = PRepeatedCScore*0.15

  print(f"Password Commonness Check: {PCommonScore}/2")

  print(f"Password Length Score: {PLengthScore}/2")
  print(f"Password Complexity Score: {PComplexScore}/1.8")
  print(f"Password Repeated Characters Score: {PRepeatedCScore}/0.6")

  total_score = PLengthScore + PComplexScore + PRepeatedCScore
  max_score = 2 + 1.8 + 0.6

  if PCommonScore == 1:
    print("PASSWORD SECURITY: VERY WEAK - COMMON PASSWORD USED - EASILY BRUTEFORCABLE - NO SCORE APPLICABLE")
  elif total_score < 1.5 and PCommonScore == 2:
      print("PASSWORD SECURITY: VERY WEAK")
      print(f"Password Score: {total_score}/{max_score}")
  elif 1.5 <= total_score < 2.5 and PCommonScore == 2:
      print("PASSWORD SECURITY: WEAK")
      print(f"Password Score: {total_score}/{max_score}")
  elif 2.5 <= total_score < 3.5 and PCommonScore == 2:
      print("PASSWORD SECURITY: OK")
      print(f"Password Score: {total_score}/{max_score}")
  elif 3.5 <= total_score < 4 and PCommonScore == 2:
      print("PASSWORD SECURITY: GOOD")
      print(f"Password Score: {total_score}/{max_score}")
  elif 4 <= total_score < 4.4 and PCommonScore == 2:
      print("PASSWORD SECURITY: SECURE")
      print(f"Password Score: {total_score}/{max_score}")

