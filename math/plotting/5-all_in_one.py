#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

def all_in_one():

    y0 = np.arange(0, 11) ** 3

    mean = [69, 0]
    cov = [[15, 8], [8, 15]]
    np.random.seed(5)
    x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
    y1 += 180

    x2 = np.arange(0, 28651, 5730)
    r2 = np.log(0.5)
    t2 = 5730
    y2 = np.exp((r2 / t2) * x2)

    x3 = np.arange(0, 21000, 1000)
    r3 = np.log(0.5)
    t31 = 5730
    t32 = 1600
    y31 = np.exp((r3 / t31) * x3)
    y32 = np.exp((r3 / t32) * x3)

    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)

    fig, axs = plt.subplot_mosaic([
        ["left1", "right1"],
        ["left2","right2"],
        ["down", "down"]
    ], figsize = (8, 6)
    )

    axs["left1"].plot(np.arange(0, 11), y0, 'r-')
    axs["left1"].set_xlim((0, 10))

    axs["right1"].set_xlabel('Height (in)')
    axs["right1"].set_ylabel('Weight (lbs)')
    axs["right1"].set_title("Men's Height vs Weight")
    axs["right1"].scatter(x1, y1, c = 'magenta')

    axs["left2"].set_xlim(0, 28650)
    axs["left2"].set_yscale('log')
    axs["left2"].set_xlabel('Time (years)')
    axs["left2"].set_ylabel('Fraction Remaining')
    axs["left2"].set_title('Exponential Decay of C-14')
    axs["left2"].plot(x2, y2)

    axs["right2"].set_xlabel('Time (years)')
    axs["right2"].set_ylabel('Fraction Remaining')
    axs["right2"].set_title('Exponential Decay of Radioactive Elements')
    axs["right2"].set_xlim(0, 20000)
    axs["right2"].set_ylim(0, 1)
    axs["right2"].plot(x3, y31, 'r--', label = 'C-14')
    axs["right2"].plot(x3, y32, 'g-', label = 'Ra-226')
    axs["right2"].legend(loc = 'upper right')
    
    axs["down"].set_xlabel('Grades')
    axs["down"].set_ylabel('Number of Students')
    axs["down"].set_title('Project A')
    axs["down"].set_xticks([0, 10,20,30,40,50,60,70,80,90,100])
    axs["down"].set_ylim(0, 30)
    axs["down"].set_xlim(0, 100)
    axs["down"].hist(range = (0, 100), bins = 10, x = student_grades, edgecolor = 'black')

    plt.tight_layout()
    plt.show()

all_in_one()

