print("Welcome to the age calculator!")
print("")
print("What animal do you choose?")
animal = str(input("Cat or dog? "))
animal = animal.lower()
if animal == "cat":
    answer_cat = int(input("How old is your cat? "))
    age = 0
    if answer_cat == age:
        print("Your cat's age in human years is " + str(age))
    elif answer_cat == 1:
        age = 7
        print("Your cat's age in human years is " + str(age))
    elif answer_cat == 2:
        age = 13
        print("Your cat's age in human years is " + str(age))
    elif answer_cat == 3:
        age = 20
        print("Your cat's age in human years is " + str(age))
    elif answer_cat == 4:
        age = 26
        print("Your cat's age in human years is " + str(age))
    elif answer_cat == 5:
        age = 33
        print("Your cat's age in human years is " + str(age))
    elif answer_cat == 6:
        age = 40
        print("Your cat's age in human years is " + str(age))
    elif answer_cat == 7:
        age = 44
        print("Your cat's age in human years is " + str(age))
    elif answer_cat == 8:
        age = 48
        print("Your cat's age in human years is " + str(age))
    elif answer_cat == 9:
        age = 52
        print("Your cat's age in human years is " + str(age))
    elif answer_cat == 10:
        age = 56
        print("Your cat's age in human years is " + str(age))
    elif answer_cat == 11:
        age = 60
        print("Your cat's age in human years is " + str(age))
    elif answer_cat == 12:
        age = 64
        print("Your cat's age in human years is " + str(age))
    elif answer_cat == 13:
        age = 68
        print("Your cat's age in human years is " + str(age))
    elif answer_cat == 14:
        age = 72
        print("Your cat's age in human years is " + str(age))
    elif answer_cat == 15:
        age = 76
        print("Your cat's age in human years is " + str(age))
    elif answer_cat == 16:
        age = 80
        print("Your cat's age in human years is " + str(age))
    elif answer_cat == 17:
        age = 84
        print("Your cat's age in human years is " + str(age))
    elif answer_cat == 18:
        age = 88
        print("Your cat's age in human years is " + str(age))
    elif answer_cat == 19:
        age = 92
        print("Your cat's age in human years is " + str(age))
    elif answer_cat == 20:
        age = 96
        print("Your cat's age in human years is " + str(age))
    elif answer_cat == 21:
        age = 100
        print("Your cat's age in human years is " + str(age))
    elif answer_cat == 22:
        age = 104
        print("Your cat's age in human years is " + str(age))
    elif answer_cat == 23:
        age = 108
        print("Your cat's age in human years is " + str(age))
    elif answer_cat == 24:
        age = 112
        print("Your cat's age in human years is " + str(age))
    elif answer_cat == 25:
        age = 116
        print("Your cat's age in human years is " + str(age))
    elif answer_cat > 25:
        age = 116
        print("Your cat's age in human years is more than " + str(age))
    else:
        print("You lie at me!")
    print("")
elif animal == "dog":
    weight = float(input("Weight of dog: "))
    age = 0
    if weight == 0:
        print("Your dog's age in human years is " + str(age))
    elif (weight > 0 and weight <= 4.5359237):
        # weight 0 - 4.5359237
        answer_dog = int(input("How old is your dog? "))
        age = 0
        if answer_dog == age:
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 1:
            age = 15
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 2:
            age = 23
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 3:
            age = 28
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 4:
            age = 31
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 5:
            age = 35
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 6:
            age = 38
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 7:
            age = 42
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 8:
            age = 45
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 9:
            age = 49
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 10:
            age = 52
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 11:
            age = 56
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 12:
            age = 59
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 13:
            age = 63
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 14:
            age = 66
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 15:
            age = 70
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 16:
            age = 74
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 17:
            age = 78
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 18:
            age = 82
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 19:
            age = 86
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 20:
            age = 90
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 21:
            age = 94
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 22:
            age = 98
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 23:
            age = 102
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 24:
            age = 106
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 25:
            age = 110
            print("Your dog's age in human years is " + str(age))
        elif answer_dog > 25:
            age = 110
            print("Your dog's age in human years is more than " + str(age))
        else:
            print("Use only natural numbers!")
    elif(weight > 4.5359237 and weight <= 9.0718474):
    # weight 4.5359238 - 9.0718474
        answer_dog = int(input("How old is your dog? "))
        age = 0
        if answer_dog == age:
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 1:
            age = 15
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 2:
            age = 23
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 3:
            age = 28
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 4:
            age = 32
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 5:
            age = 36
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 6:
            age = 40
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 7:
            age = 44
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 8:
            age = 48
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 9:
            age = 52
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 10:
            age = 56
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 11:
            age = 60
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 12:
            age = 64
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 13:
            age = 68
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 14:
            age = 72
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 15:
            age = 76
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 16:
            age = 80
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 17:
            age = 84
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 18:
            age = 88
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 19:
            age = 92
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 20:
            age = 96
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 21:
            age = 100
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 22:
            age = 104
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 23:
            age = 108
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 24:
            age = 112
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 25:
            age = 115
            print("Your dog's age in human years is " + str(age))
        elif answer_dog > 25:
            age = 115
            print("Your dog's age in human years is more than " + str(age))
        else:
            print("Try once more!")
    elif(weight > 9.0718474 and weight <= 22.6796185):
    # weight 9.0718475 - 22.6796185
        answer_dog = int(input("How old is your dog? "))
        age = 0
        if answer_dog == age:
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 1:
            age = 15
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 2:
            age = 24
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 3:
            age = 29
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 4:
            age = 34
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 5:
            age = 38
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 6:
            age = 42
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 7:
            age = 47
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 8:
            age = 51
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 9:
            age = 56
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 10:
            age = 60
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 11:
            age = 65
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 12:
            age = 69
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 13:
            age = 74
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 14:
            age = 78
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 15:
            age = 83
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 16:
            age = 87
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 17:
            age = 92
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 18:
            age = 96
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 19:
            age = 101
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 20:
            age = 105
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 21:
            age = 109
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 22:
            age = 113
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 23:
            age = 117
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 24:
            age = 121
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 25:
            age = 125
            print("Your dog's age in human years is " + str(age))
        elif answer_dog > 25:
            age = 125
            print("Your dog's age in human years is more than " + str(age))
        else:
            print("It's impossible!")
    elif(weight > 22.6796185 and weight <= 40.8233133):
    # weight 22.6796186 - 40.8233133
        answer_dog = int(input("How old is your dog? "))
        age = 0
        if answer_dog == age:
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 1:
            age = 14
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 2:
            age = 22
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 3:
            age = 29
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 4:
            age = 34
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 5:
            age = 40
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 6:
            age = 45
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 7:
            age = 50
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 8:
            age = 55
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 9:
            age = 61
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 10:
            age = 66
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 11:
            age = 72
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 12:
            age = 77
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 13:
            age = 82
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 14:
            age = 88
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 15:
            age = 93
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 16:
            age = 99
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 17:
            age = 104
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 18:
            age = 109
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 19:
            age = 115
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 20:
            age = 121
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 21:
            age = 126
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 22:
            age = 130
            print("Your dog's age in human years is " + str(age))
        elif answer_dog > 22:
            age = 130
            print("Your dog's age in human years is more than " + str(age))
        else:
            print("Ha Ha! Try harder :)")
    elif weight > 40.8233133:
    # weight 40.8233134 - ...
        answer_dog = int(input("How old is your dog? "))
        age = 0
        if answer_dog == age:
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 1:
            age = 12
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 2:
            age = 20
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 3:
            age = 28
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 4:
            age = 35
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 5:
            age = 42
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 6:
            age = 49
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 7:
            age = 56
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 8:
            age = 64
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 9:
            age = 71
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 10:
            age = 78
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 11:
            age = 86
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 12:
            age = 93
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 13:
            age = 101
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 14:
            age = 108
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 15:
            age = 115
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 16:
            age = 123
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 17:
            age = 130
            print("Your dog's age in human years is " + str(age))
        elif answer_dog == 18:
            age = 135
            print("Your dog's age in human years is " + str(age))
        elif answer_dog > 18:
            age = 135
            print("Your dog's age in human years is more than " + str(age))
        else:
            print("Not this time friend!")
    else:
        print("Try again")
else:
    return("Choose cat or dog only")