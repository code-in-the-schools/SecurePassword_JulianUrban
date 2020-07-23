validPassword = False
while validPassword == False: #code loops while there is an invalid password
  password = str(input("Enter a password: ")) #the user enters a password
  if len(password) < 8 or len(password) > 16: #is the password between 8 and 16 characters?
    print("Invalid password!")
  elif password.islower() == True and password.isupper() == False: #is the password in all lowercase? It needs to have uppercase and lowercase
    print("Invalid password!")
  elif password.isalpha() == True: #is the password only letters? It needs to have numbers and/or special characters
    print("Invalid password!")
  else: #The password is valid if the other if statements are false
    print("Password accepted")
    validPassword = True