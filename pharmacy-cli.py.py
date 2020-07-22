## Block

import random

print("Welcome to our online pharmacy!")

illness_type = ["1. Allergies", "2. Asthma", "3. Cold & Flu", "4. Cough & Phlegm", "5. Dry eyes", "6. Ear infection", "7. Headache", "8. Heartburn", "9. High fever", "10. Joint sprain", "11. Minor muscle/joint pain", "12. Pink eye", "13. Pregnancy vitamin B", "14. Runny nose", "15. Teething", "16. Toothache"]

for illness in illness_type:
    print(illness)

answer = input("In order for us to help you please type in the value of the choices that compensates to your illness from the list above.")


if int(answer) == 1:
    age = input("Please type the one that corresponds to your age range: ( 2-6 , 7-64 , 65+ )")

    if age == "2-6":
        print("drink 2.5 ml of ZYRTEC a day")

    elif age == "7-64":
        print("drink around 5 - 10 ml of ZYRTEC a day depending on severity")

    elif age == "65+":
        print("drink 5 ml of ZYRTEC a day")


elif int(answer) == 2:
    print("take 1 - 2 inhilations of VENTOLIN a day")


elif int(answer) == 3:
    age = input("Please type the one that corresponds to your age range: ( 1-2 , 3-7 , 8-12 , 13+ )")

    if age == "1-2":
        print("drink 2.5 ml of BRUFEN 3 times a day")

    elif age == "3-7":
        print("drink 5 ml of BRUFEN 3 times a day")

    elif age == "8-12":
        print("drink 10 ml of BRUFEN 3 times a day")

    elif age == "13+":
        print("take 1 - 2 tablets of FLUDREX no more than 8 tablets a day")


elif int(answer) == 4:
    age = input("Please type the one that corresponds to your age range: ( 0-6 , 7-12 , 13+ )")

    if age == "0-6":
        print("drink 2.5 ml of PROSPAN twice a day")

    elif age == "7-12":
        print("drink 5 ml of PROSPAN twice a day")

    elif age == "13+":
        print("drink 5 ml of PROSPAN 3 times a day")


elif int(answer) == 5:
    print("allow 1 - 2 drops from REFRESH TEARS into your eye when needed")


elif int(answer) == 6:
    print("allow 1 - 2 drops of APIGEN into the infected ear twice a day")


elif int(answer) == 7:
    age = input("Please type the one that corresponds to your age range: ( 10-15 , 16+ )")

    if age == "10-15":
        print("dissolve 1 tablet of PANADOL ACTIFAST into some warm water, no more than 3 times a day")

    elif age == "16+":
        print("dissolve 1 - 2 tablets of PANADOL ACTIFAST into some warm water, no more than 3 times a day")


elif int(answer) == 8:
    age = input("Please type the one that corresponds to your age range: ( adult )")

    if age == "adult":
        print("drink around 15 - 30 ml of GAVISCON LIQUID 4 times a day depending on intensity")

    else:
        print("Sorry we do not have a medicine for you")


elif int(answer) == 9:
    age = input("Please type the one that corresponds to your age range: (1-2 , 3-7 , 8-12 , 13+ )")

    if age == "1-2":
        print("drink 2.5 ml of BRUFEN 3 times a day")

    elif age == "3-7":
        print("drink 5 ml of BRUFEN 3 times a day")

    elif age == "8-12":
        print("drink 10 ml of BRUFEN 3 times a day")

    elif age == "13+":
        print("dissolve 1000mg of PARAFAST ET 1000 in some warm water twice a day")


elif int(answer) == 10:
    print("spray some FAST RELEIF SPRAY on desired area")


elif int(answer) == 11:
    print("adhere a patch of SALONPAS to the targeted area")


elif int(answer) == 12:
    print("allow 1 - 2 drops of APIGEN into the eye twice a day")


elif int(answer) == 13:
    print("take 1 tablet of FOLIAC ACID a day ")


elif int(answer) == 14:
    print("spray some STERIMAR SPRAY into your nostril")


elif int(answer) == 15:
    print("apply some DAD TEETHING GEL onto the teething site")


elif int(answer) == 16:
    print("dip a q-tip into SAVOY TOOTHACHE DROP then apply it to the pain site ")





def fun_fact (list_of_facts) :
    x = random.choice(list_of_facts)
    return x

facts= ["only 2 % of the entire population have green eyes", "your eyelashes last about 150 days", "Your blood has the same amount of salt in it as the ocean does", "babies are born with 300 bones - adults have 206", "the heart pumps at least 9450 liters of blood a day", "fingernails grow 4 times as fast as your toe nails", "around 8 % of the worlds population have blue eyes", "only 1 - 2 % of the population have grey eyes", "around 79 % of the entire population have brown eyes ", ]

point = fun_fact(facts)

print("fun fact: " + point)




ending = input("Thank you for using this website, may you please rate your experince using this online pharmacy on the scale of 1- 5.")

if int(ending) == 5:
    print("feel free to visit our website anytime!")

else:
    print("I am sorry to say that there was an error with the system")
    final_answer = input("please try again")


    if final_answer == "5":
        print("I am now reassured that you indeed pressed the wrong key")

    else:
        print("I am sorry to tell you that 1, 2, 3, & 4 do not work!")



















































