#!/usr/bin/env python3

import numpy as np
from utils import *


def generate_dummy_data(classes, samples):
    np.random.seed(2025)

    # shape of x: (1, classes)
    x = np.arange(classes)

    # shape of data: (classes, samples)
    data = np.zeros((classes, samples))
    for i in range(classes):
        data[i] = np.random.normal(i + 1, (i + 1) / 5, samples)

    return data


def main():
    # generate dummy data
    classes = 10
    samples = 1000
    data = generate_dummy_data(classes, samples)

    # violin plot
    fig, ax = plt.subplots()

    for i in range(classes):
        violin = ax.violinplot([data[i]], positions=[i])
        config = violin['bodies'][0]
        config.set_facecolor(f'C{i}')
        config.set_edgecolor(f'C{i}')

    # customize the markers for medians
    for i in range(classes):
        median = np.median(data[i])
        ax.scatter(i, median,
                   color=f'C{i}',
                   marker='o',
                   s=30)

    # set axis ticks and labels
    ax.set_xticks(np.arange(classes))
    ax.set_xlabel('Class')
    ax.set_ylabel('Value')

    # save in SVG, PDF, and PNG formats
    save_figures(fig, 'example_violin')


if __name__ == '__main__':
    main()
