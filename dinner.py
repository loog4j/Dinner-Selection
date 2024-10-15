#define dining options with a variable
dining_options = ("Canes", "Pizza", "Chick-fil-a", "other")
kenzies_choice = input(f"Would you like {dining_options}? Please type one.")

if kenzies_choice == "Canes":
    print("Okay I will pick up Canes")
elif kenzies_choice == "Pizza":
    print("Please text Dallin which Pizza place you would like to eat from:\n")
elif kenzies_choice == "Chick-fil-a":
    print("Okay I will pick up a #1 without pickles")
else:
    print("We will discuss when I get home")
