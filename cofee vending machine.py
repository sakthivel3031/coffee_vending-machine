#print("****************************************************************************")
ch=int(input("press 1 to continue.....: "))
while(ch==1):
    print("C...cofee\nT....coffee\ns...soups...\nh...Hot_soups\n")
    choice=input("enter your choice: ")
    if(choice.lower()=="c"):
        print("1....Espresso cofee\n2....Cappuccino cofee\n3....Latee cofee")
        cg=int(input())
        if (cg==1):
            print("Welcome to CCD")
            print("Enjoy to Espresso coffee")
        elif(cg==2):
            print("Welcome to CCD")
            print("Enjoy to cappuccino cofee")
        elif(cg==3):
            print("Welcome to CCD")
            print("Enjoy to Latee coffee")
        else:
            print("INVALID OUTPUT")
    elif(choice.lower()=="t"):
        print("1.plain tea\n2.assam tea\n3.ginger tea\n4.cardamon tea \n5.masala tea \n6.lemon tea\n7.green tea\n8.organic darjeeling tea")
        ca=int(input())
        if(ca==1):
            print("Welcome to CCD")
            print("Enjoy to plain tea")
        elif(ca==2):
            print("Welcome to CCD")
            print("Enjoy to assam tea")
        elif(ca==3):
            print("Welcome to CCD")
            print("Enjoy to ginger tea")
        elif(ca==4):
            print("Welcome to CCD")
            print("Enjoy to cardemon tea")
        elif(ca==5):
            print("Welcome to CCD")
            print("Enjoy to masala tea")
        elif(ca==6):
            print("Welcome to CCD")
            print("Enjoy to lemon tea")
        elif(ca==7):
            print("Welcome to CCD")
            print("Enjoy to green tea")
        elif(ca==8):
            print("Welcome to CCD")
            print("Enjoy to organic darjeeling  tea")
        else:
            print("INVALID OUTPUT")
    elif(choice.lower()=="s"):
        print("1.hot and sour soup\n2.veg corn soup\n3.tomato soup\n4.spiecy tomato soup\n5.beverges")
        cr=int(input())
        if(cr==1):
            print("Welcome to CCD")
            print("Enjoy to hot and sour soup")
        elif(cr==2):
            print("Welcome to CCD")
            print("Enjoy to veg corn soup")
        elif(cr==3):
            print("Welcome to CCD")
            print("Enjoy to tomato soup")
        elif(cr==4):
            print("Welcome to CCD")
            print("Enjoy to spiecy tomato soup")
        elif(cr==5):
            print("Welcome to CCD")
            print("Enjoy to beverges")
        else:
            print("INVALID OUTPUT")
    elif(choice.lower()=="h"):
        print("1.bdam drink\n2.badam-pista drink")
        ct=int(input("enter your choice :"))
        if(ct==1):
            print("Welcome to CCD")
            print("Enjoy to Badam drink")
        elif(ct==2):
            print("Welcome to CCD")
            print("Enjoy to Badam-pista drink")
        else:
            print("INVALID OUTPUT")
    else:
        print("INVALID OUTPUT")
        
        
    