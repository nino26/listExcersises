# spam = ['apples','bananas','tofu','cats']
#
# def combo(item):
#     combo=''
#     for value in item:
#         if combo=='':
#             combo = value
#             continue
#         combo = combo + ','+value
#
#     return combo
#
#
# print(combo(spam))


#Below program plays Heads or Tails 100 times and counts the streaks
# one streak is 6 straight Heads or Tails

import random

spam = []
t=0
h=0
numberOfStreaks = 0
for experimentNumber in range(10000):
    #code that creats a list of 100 heads or tails values.
    if len(spam) > 100: #limits the toos to 100
        break
    else:
        x = random.randint(0,1) #Toss
        if x == 0:
            spam.append('T')
            #checking for the streak
            if t < 6:
                t+=1
            elif h ==6:
                numberOfStreaks +=1
                #resetting tail streak value when streak is completed
                t=0
            else:
                t=0

        else:
            spam.append('H')
            if h < 6:
                h+=1
            elif h == 6:
                numberOfStreaks += 1
                #resetting head streak value when streak is completed
                h=0
            else:
                h=0



#  Prints the results
print(spam)
print(numberOfStreaks)

#[retty cool]
