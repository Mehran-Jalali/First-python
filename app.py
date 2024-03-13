print('Hi there')
n = 5
while n > 0 :
    print (n)
    n = n - 1
print("well done")        
# make fun stuff 
# we give 50 peoples 100$ each and they should give 1$ every time I request so 
import random
random.seed()

#we wanna show in graphic bar so we should install the source library for example matplotlib so
# in cmd type : py -m pip install matplotlib
from matplotlib import pyplot as plt

people = []

for i in range(0,50):
    people.append(100)

#  if you increse the times you will see some peoples that have 0$ and they will quit the game:
for requestTime in range(0,10000):
    for person1 in range(0,50):
        person2 = random.randrange(0,50)
        while people[person2] == 0:
            person2 = random.randrange(0,50)

        if people[person1] != 0:
            people[person2] = people[person2] + 1
            people[person1] = people[person1] - 1

print(plt.bar(range(0,50) ,people))
