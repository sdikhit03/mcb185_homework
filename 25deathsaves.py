# 25deathsaves.py by Saumitr Dikhit
import random

def deathsaves():
    failure = 0
    success = 0
    while True:
        roll = random.randint(1,20)
        if roll == 1:
            failure += 2
        elif roll < 10:
            failure += 1
        elif roll == 20:
            return "revive"
        else:
            success += 1
        
        if failure >= 3:
            return "die"
        if success == 3:
            return "stable"

died = 0
stabilized = 0
revived = 0

for x in range(10000):
    result = deathsaves()
    if result == "die":
        died += 1
    elif result == "stable":
        stabilized += 1
    elif result == "revive":
        revived += 1

print("Probability of dying: " + str(died / 10000))
print("Probability of stabilizing: " + str(stabilized / 10000))
print("Probability of reviving: " + str(revived / 10000))