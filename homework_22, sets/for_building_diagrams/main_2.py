from matplotlib_venn import venn3
import matplotlib.pyplot as plt
import random


days = set()
i = 1
while i != 31:
    days.add(f"day_{i}")
    i += 1


raining = set()
cold = set()
windy = set()

while len(raining) != 5:
    day = random.choice(list(days))
    if day not in cold and day not in windy:
        raining.add(day)

while len(windy) != 2:
    day = random.choice(list(days))
    if day not in cold and day not in raining:
        windy.add(day)

# raining ∩ windy ∩ cold = 1
while len(raining) != 6:
    day = random.choice(list(days))
    if day not in raining and day not in cold and day not in windy:
        raining.add(day)
        cold.add(day)
        windy.add(day)

# raining ∩ windy = 5

while len(raining) != 10 and len(windy) != 7:
    day = random.choice(list(days))
    if day not in raining and day not in windy and day not in cold:
        raining.add(day)
        windy.add(day)

# raining ∩ cold = 3
while len(raining) != 12 and len(cold) != 3:
    day = random.choice(list(days))
    if day not in raining and day not in windy and day not in cold:
        raining.add(day)
        cold.add(day)

# windy ∩ cold = 2

while len(windy) != 8 and len(cold) != 4:
    day = random.choice(list(days))
    if day not in raining and day not in windy and day not in cold:
        windy.add(day)
        cold.add(day)

sunny = days - cold - windy - raining
print(sunny)
fig = plt.figure()


v = venn3([windy, raining, cold], ('windy', 'raining', 'cold'))
plt.show()

