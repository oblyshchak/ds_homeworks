from matplotlib_venn import venn3
import matplotlib.pyplot as plt
import names
import random


students = set()
while len(students) != 37:
    add_st = names.get_last_name()
    students.add(add_st)
print(len(students))
m = set()
ch = set()
ph = set()

while len(m) != 3:
    new_st = random.choice(list(students))
    if new_st not in ch and new_st not in ph:
        m.add(new_st)

while len(ch) != 8:
    new_st = random.choice(list(students))
    if new_st not in m and new_st not in ph:
        ch.add(new_st)

while len(ph) != 7:
    new_st = random.choice(list(students))
    if new_st not in m and new_st not in ch:
        ph.add(new_st)

while len(m) != 7:
    new_st = random.choice(list(students))
    if new_st not in m and new_st not in ch and new_st not in ph:
        ph.add(new_st)
        ch.add(new_st)
        m.add(new_st)

while len(m) != 10 and len(ph) != 14:
    new_st = random.choice(list(students))
    if new_st not in m and new_st not in ch and new_st not in ph:
        m.add(new_st)
        ph.add(new_st)

while len(m) != 15 and len(ch) != 17:
    new_st = random.choice(list(students))
    if new_st not in m and new_st not in ch and new_st not in ph:
        m.add(new_st)
        ch.add(new_st)

while len(ph) != 16 and len(ch) != 19:
    new_st = random.choice(list(students))
    if new_st not in m and new_st not in ch and new_st not in ph:
        ph.add(new_st)
        ch.add(new_st)

print(m&ph)
fig = plt.figure()


v = venn3([m, ch, ph], ('math', 'chemistry', 'physics'))
plt.show()
