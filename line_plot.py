#!/usr/bin/env python3

import numpy as np
from utils import *


def generate_dummy_data(classes, samples):
    np.random.seed(2025)

    # shape of x: (1, samples)
    x = np.arange(2000, 2000 + samples)

    # shape of y: (classes, samples)
    y = np.zeros((classes, samples))
    for i in range(classes):
        y[i] = np.random.rand(samples) + i

    return x, y


def main():
    # generate dummy data
    classes = 10
    samples = 5
    x, y = generate_dummy_data(classes, samples)

    # line plot
    fig, ax = plt.subplots()

    for i in range(classes):
        ax.plot(x, y[i],
                label=f'Class{i}',
                color=f'C{i}',
                linestyle=LINESTYLE[i],
                marker=MARKER[i],
                clip_on=False)

    # set axis labels
    ax.set_xlabel('Year')
    ax.set_ylabel('Value')

    # put legend outside plot when no space, but put inside whenever possible
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    # save in SVG, PDF, and PNG formats
    save_figures(fig, 'example_line')


if __name__ == '__main__':
    main()
