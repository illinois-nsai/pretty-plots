#!/usr/bin/env python3

import numpy as np
from utils import *


def generate_dummy_data(classes):
    np.random.seed(2025)

    # shape of x and y: (1, classes)
    x = np.random.rand(classes)
    y = np.random.rand(classes)

    return x, y


def main():
    # generate dummy data
    classes = 10
    x, y = generate_dummy_data(classes)

    # scatter plot
    fig, ax = plt.subplots()

    for i in range(classes):
        ax.scatter(x[i], y[i],
                   color=f'C{i}',
                   marker=MARKER[i],
                   clip_on=False)

        # labels are (6 pt, 6 pt) away from the points
        ax.annotate(f'Class{i}',
                    xy=(x[i], y[i]),
                    xytext=(6, 6),
                    textcoords='offset points')

    # set axis labels
    ax.set_xlabel('Metric X')
    ax.set_ylabel('Metric Y')

    # save in SVG, PDF, and PNG formats
    save_figures(fig, 'examples/scatter')


if __name__ == '__main__':
    main()
