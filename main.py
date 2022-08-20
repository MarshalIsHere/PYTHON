real_pass ="password123" #this is the realpassword
pass_start = 0 #This is the initial attempt of a user
pass_max_try = 8 # This is the maximum attemp of a user
user_pass = "" #This field is for the user password input section
while real_pass != user_pass and pass_start != pass_max_try:
    user_pass = input("Enter the correct password : ")
    pass_start = pass_start + 1
    if user_pass == real_pass:
        print("You have succesfully entered your password.")
    else:
        print("Wrong Password : Try AGAIN PLEASE")

if pass_start == pass_max_try:
    print("\nSORRY \n YOur acoount is blocked\n PLEASE CONTACT CUSTOMER CARE")