validPassword = False
while validPassword == False:
  password = str(input("Enter a password: "))
  if len(password) < 8 or len(password) > 16:
    print("Invalid password!")
  elif password.islower() == True:
    print("Invalid password!")
  elif password.isalpha() == True:
    print("Invalid password!")
  else:
    print("Password accepted")
    validPassword = True