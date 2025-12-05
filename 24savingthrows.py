# 24savingthrows.py by Saumitra Dikhit
import random


def savingthrows():
    # DC of 5, normal
    print("Saving Throws (DC of 5, normal):")
    d1 = random.randint(1,20)
    print(d1)
    if(d1 >= 5): print(d1, ", success")
    else: print(d1, ", fail")

    # DC of 5, advantage
    print("Saving Throws (DC of 5, advantage):")
    d1 = random.randint(1,20)
    d2 = random.randint(1,20)
    print(d1,", ", d2)
    if (d1 > 5 and d1 > d2): print(d1, ", success")
    elif (d2 > 5 and d2 > d1): print (d2, ", success")
    elif (d1 > 5 and d1 == d2): print (d1, ", success")
    else: print("fail")

    # DC of 5, disadvantage
    print("Saving Throws (DC of 5, disadvantage):")
    d1 = random.randint(1,20)
    d2 = random.randint(1,20)
    print(d1, ", ", d2)
    if (d1 < d2 and d1 > 5): print (d1, ", success")
    if (d2 < d1 and d2 > 5): print (d2, ", success")
    if (d1 == d2 and d1 > 5): print (d1, ", success ")

    # Probability Table DC of 5
    print("Probability of success (DC 5 Normal): 0.8")
    print("Probability of success (DC 5 Advantage): 0.96")
    print("Probability of success (DC 5 Disadcantage): 0.64")

    # DC of 10, normal
    print("Saving Throws (DC of 10, normal):")
    d1 = random.randint(1,20)
    print(d1)
    if(d1 >= 10): print(d1, ", success")
    else: print(d1, ", fail")

    # DC of 10, advantage
    print("Saving Throws (DC of 10, advantage):")
    d1 = random.randint(1,20)
    d2 = random.randint(1,20)
    print(d1,", ", d2)
    if (d1 > 10 and d1 > d2): print(d1, ", success")
    elif (d2 > 10 and d2 > d1): print (d2, ", success")
    elif (d1 > 10 and d1 == d2): print (d1, ", success")
    else: print("fail")

    # DC of 5, disadvantage
    print("Saving Throws (DC of 10, disadvantage):")
    d1 = random.randint(1,20)
    d2 = random.randint(1,20)
    print(d1, ", ", d2)
    if (d1 < d2 and d1 > 10): print (d1, ", success")
    if (d2 < d1 and d2 > 10): print (d2, ", success")
    if (d1 == d2 and d1 > 10): print (d1, ", success ")
    else: print("fail")

    # Probability Table DC of 10
    print("Probability of success (DC 10 Normal): 0.55")
    print("Probability of success (DC 10 Advantage): 0.7975")
    print("Probability of success (DC 10 Disadcantage): 0.3025")


    # DC of 15, normal
    print("Saving Throws (DC of 15, normal):")
    d1 = random.randint(1,20)
    print(d1)
    if(d1 >= 15): print(d1, ", success")
    else: print(d1, ", fail")

    # DC of 15, advantage
    print("Saving Throws (DC of 15, advantage):")
    d1 = random.randint(1,20)
    d2 = random.randint(1,20)
    print(d1,", ", d2)
    if (d1 > 15 and d1 > d2): print(d1, ", success")
    elif (d2 > 15 and d2 > d1): print (d2, ", success")
    elif (d1 > 15 and d1 == d2): print (d1, ", success")
    else: print("fail")

    # DC of 15, disadvantage
    print("Saving Throws (DC of 15, disadvantage):")
    d1 = random.randint(1,20)
    d2 = random.randint(1,20)
    print(d1, ", ", d2)
    if (d1 < d2 and d1 > 15): print (d1, ", success")
    if (d2 < d1 and d2 > 15): print (d2, ", success")
    if (d1 == d2 and d1 > 15): print (d1, ", success ")
    else: print(d1, ", ", d2, ", fail")

    # Probability Table DC of 15
    print("Probability of success (DC 15 Normal): 0.3")
    print("Probability of success (DC 15 Advantage): 0.51")
    print("Probability of success (DC 15 Disadcantage): 0.09")

savingthrows()
