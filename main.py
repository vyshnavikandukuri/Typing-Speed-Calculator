from time import *
import random as r


def mistake(par_test,user_test):
    error=0
    for i in range(len(par_test)):
        try:
            if par_test[i]!=user_test[i]:
                error+=1
        except:
            error+=1
    return error
    



def speed_time(time_start,time_end,userinput):
    time_delay=time_end - time_start
    time_Round=round(time_delay,2)
    speed=len(userinput)/time_Round
    return round(speed)
    
    
while True:
    ck=input("ready to test:yes/no : ")
    if ck=="yes":
        test=["The quick brown fox jumps over the lazy dog",
        "A journey of a thousand miles begins with a single step",
        "Typing fast requires accuracy, focus, and continuous practice",
        "Every moment is a fresh beginning if you choose to make it so",
        "Success is not final, failure is not fatal: It is the courage to continue that counts",
        "The sun sets in the west, bringing the day to a peaceful close",
        "Hard work beats talent when talent doesn’t work hard",
        "Good communication is as stimulating as black coffee, and just as hard to sleep after",
        "Opportunities don’t happen, you create them",
        "Reading improves your vocabulary and sharpens your mind"]


        test1=r.choice(test)
        print("      *****Typing Speed Calculator*****")
        print(test1)
        print()
        print()
        time1=time()
        test_input=input(" Enter : ")
        time2=time()


        print("Speed : ",speed_time(time1,time2,test_input)," w/sec")
        print("Error : ",mistake(test1,test_input))

    elif ck=="no":
        print("Thank you!!")
        break

    else:
        print("Wrong input!!!") 

        
    



