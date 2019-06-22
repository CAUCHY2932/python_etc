import random
import matplotlib.pyplot as plt
position =0
walk= [position]

steps= 1000

for i in range(steps):
    steps= 1 if random.randint(0,1) else -1
    position +=steps
    walk.append(position)

plt.plot(walk[:100])

plt.show()