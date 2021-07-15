#############################################
#                                           #
#                                           #
#     Password Manager                      #
#                                           #
#                                           #
#############################################


loop_continue = False

def Search_for_a_password(loop_continue):
    matching = False
    print("""
            Eg:-
                Enter the link of the site :- www.github.com
            """)
    Search = input("Enter the link of the site :- ")

    try:
        Search_opener = open("psw/"+Search+".txt", "r")
        data = Search_opener.read()

        print(data)

    except:
        print("There is no Site name called" + Search + "in savings. Please Try again\n")
        ct = str(input("Do you want to continue [y/n]"))
        if st == "y" or "Y":
            loop_continue == True
        elif st == "n" or "N":
            loop_continue = False
        else:
            print("\nThere is no option")


def Save_a_password(loop_continue):
    Sitename = str(input("Enter the Website  :- "))
    Username = str(input("Enter the Username :- "))
    Password = str(input("Enter the Password :- "))

    saver = open("psw/"+Sitename+".txt", "w")
    saver.write(Sitename+"\n")
    saver.write(Username+"\n")
    saver.write(Password+"\n")
    ct = str(input("Do you want to continue [y/n]"))
    if ct == "y" or "Y":
        loop_continue = True
    elif ct == "n" or "N":
        loop_continue = False
    else:
        print("\nThere is no option")

    if loop_continue:
        main(loop_continue)


def main(loop_continue):

    print("""
            1. Search for a password
            2. Save a password
    """)

    print("type 1 to search for a password or type 2 to save a password\n")


    What_To_do = int(input("Enter what to do :- "))

    try:
        if What_To_do == 1:
            Search_for_a_password(loop_continue)
        if What_To_do == 2:
            Save_a_password(loop_continue)
        if  What_To_do > 2:
            print("\nThere is no option\n")
            main(loop_continue)
        else:
            print("\nThere is no option\n")
            main(loop_continue)
        if What_To_do == str(What_To_do):
            print("\nThere is no option\n")
            main(loop_continue)
    except:
        print("\nThere is no option\n")
        main(loop_continue)

main(loop_continue)

if loop_continue:
    main(loop_continue)
