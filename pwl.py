import random

print("")
print('''
  _____           __          __           _ _      _     _    
 |  __ \          \ \        / /          | | |    (_)   | |   
 | |__) |_ _ ___ __\ \  /\  / /__  _ __ __| | |     _ ___| |_  
 |  ___/ _` / __/ __\ \/  \/ / _ \| '__/ _` | |    | / __| __| 
 | |  | (_| \__ \__ \\   /\  / (_) | | | (_| | |____| \__ \ |_  
 |_|   \__,_|___/___/ \/  \/ \___/|_|  \__,_|______|_|___/\__| 

                    +-+-+-+-+-+-+-+-+-+
                    |G|e|n|e|r|a|t|o|r|
                    +-+-+-+-+-+-+-+-+-+ 

                    Created by: v3ctr0n      
                    ''')
print("Company (1) or a single person (2) ?")
answer = input("Choose 1 or 2: ")

if answer == "1":
    answ = input("How many words to combine? (3 = default - up to 7): ")
    if answ == "3":
         name = input("Name of the company: ")
         othr_name = input("Other name for the company:")
         street = input("Street name: ")

         info_list_lower = [name.lower(), othr_name.lower(), street.lower()]
         info_list_upper = [name.capitalize(), othr_name.capitalize(), street.capitalize()]
         spc_char = ['@', '#', '&', '$', '*', '%', '/', '-', '_', '!', '~', '?', '123']
         fin_list = info_list_lower + info_list_upper + spc_char
         fin_list_let = info_list_lower + info_list_upper

         answ1 = input("Special characters (Y/N)? ")
         if answ1 == "Y":
             for i in range(200):
                 print (''.join(random.sample(fin_list, random.randint(2,4))))
         elif answ1 == "N":
             for i in range(200):
                 print (''.join(random.sample(fin_list_let, random.randint(2,3))))
         else:
             print("Error you fool")
            
    elif answ in range(4, 7):
        name = input("Name of the company: ")
        othr_name = input("Other name for the company:")
        street = input("Street name: ")
        other1 = input("Other: ")
        other2 = input("Other: ")
        other3 = input("Other: ")
        other4 = input("Other: ")

        info_list_lower = [name.lower(), othr_name.lower(), street.lower()]
        info_list_upper = [name.capitalize(), othr_name.capitalize(), street.capitalize()]
        spc_char = ['@', '#', '&', '$', '*', '%', '/', '-', '_', '!', '~', '?', '123']
        fin_list = info_list_lower + info_list_upper + spc_char
        fin_list_let = info_list_lower + info_list_upper


        answ1 = input("Special characters (Y/N)? ")
        if answ1 == "Y":
             for i in range(200):
                print (''.join(random.sample(fin_list, random.randint(2,4))))
        elif answ1 == "N":
             for i in range(200):
                print (''.join(random.sample(fin_list_let, random.randint(2,5))))
        else:
            print("Error you fool")

    else:
        print("Nope.")


    

elif answer == "2":
    answ = input("How many words to combine? (5 = default - up to 8): ")
    
    if answ == "5":

        first_name = input("First name of the person: ")
        surname = input("Surname of the person: ")
        year = input("Year of birth: ")
        family = input("Name of a family member: ")
        pet_name = input("Pet name: ")

        info_list_upper = [first_name.capitalize(), surname.capitalize(), year.capitalize(), family.capitalize() , pet_name.capitalize()]
        info_list_lower = [first_name.lower(), surname.lower(), year.lower(), family.lower() , pet_name.lower()]
        spc_char = ['@', '#', '&', '$', '*', '%', '/', '-', '_', '!', '~', '?', '123']
        fin_list = info_list_upper + info_list_lower + spc_char
        fin_list_let = info_list_lower + info_list_upper


        answ1 = input("Special characters (Y/N)? ")
        if answ1 == "Y":
             for i in range(300):
                 print (''.join(random.sample(fin_list, random.randint(2,6))))
        elif answ1 == "N":
             for i in range(300):
                 print (''.join(random.sample(fin_list_let, random.randint(2,5))))
        else:
             print("Error you fool")


    elif answ > "5":

        first_name = input("First name of the person: ")
        surname = input("Surname of the person: ")
        year = input("Year of birth: ")
        family = input("Name of a family member: ")
        pet_name = input("Pet name: ")
        other1 = input("Other: ")
        other2 = input("Other: ")
        other3 = input("Other: ")


        info_list_upper = [first_name.capitalize(), surname.capitalize(), year.capitalize(), family.capitalize() , pet_name.capitalize()]
        info_list_lower = [first_name.lower(), surname.lower(), year.lower(), family.lower() , pet_name.lower()]
        spc_char = ['@', '#', '&', '$', '*', '%', '/', '-', '_', '!', '~', '?', '123']
        fin_list = info_list_upper + info_list_lower + spc_char
        fin_list_let = info_list_lower + info_list_upper


        answ1 = input("Special characters (Y/N)? ")
        if answ1 == "Y":
             for i in range(300):
                print (''.join(random.sample(fin_list, random.randint(2,7))))
        elif answ1 == "N":
             for i in range(300):
                print (''.join(random.sample(fin_list_let, random.randint(2,5))))
        else:
            print("Error you fool")
    

else:
    print("Is typing 1 or 2 so hard?")