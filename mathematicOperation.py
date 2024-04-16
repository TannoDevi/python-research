minimum_height = 120
user_height = int(input("What is your height"))
user_age = int(input("How old are you"))
user_photo = input("Do you want to tke photo")
if user_age < 12:
    print("ticket price is 5$")
elif user_age < 18:
    print("ticket price is 7$")
elif user_age > 18:
    print("ticket price is 12$")
else:
    print("photo taken 3$")