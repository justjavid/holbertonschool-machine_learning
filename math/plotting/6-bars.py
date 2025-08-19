#!/usr/bin/env python3
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

def bars():
    np.random.seed(5)
    fruit = np.random.randint(0, 20, (4,3))
    plt.figure(figsize=(6.4, 4.8))

    x = ['Farrah', 'Fred', 'Felicia']
    plt.bar(x, fruit[0], color = 'r', width=0.5)
    plt.bar(x, fruit[1], bottom=fruit[0], color = 'yellow', width=0.5)
    plt.bar(x, fruit[2], bottom=fruit[0] + fruit[1], color = "#ff8000", width=0.5)
    plt.bar(x, fruit[3], bottom=fruit[0]+fruit[1]+fruit[2], color = "#ffe5b4", width=0.5)

    plt.legend(['apples', 'bananas', 'oranges', 'peaches'])
    plt.ylabel('Quantity of Fruit')
    plt.ylim(0, 80)
    plt.title('Number of Fruit per Person')
    plt.show()

bars()