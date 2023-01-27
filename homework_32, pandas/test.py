import pandas as pd
import names
import random

gpa = [round(random.uniform(40.0, 100.0), 2) for i in range(15)]


admission_to_exam = []
for value in gpa:
    if value <= 50:
        admission_to_exam.append(False)
    admission_to_exam.append(True)

print(admission_to_exam)