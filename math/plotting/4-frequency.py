#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

def frequency():

    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)
    plt.figure(figsize=(6.4, 4.8))

    plt.xlabel('Grades')
    plt.ylabel('Number of Students')
    plt.title('Project A')
    plt.xticks([0, 10,20,30,40,50,60,70,80,90,100])
    plt.ylim(0, 30)
    plt.xlim(0, 100)
    plt.hist(range = (0, 100), bins = 10, x = student_grades, edgecolor = 'black')
    plt.show()
