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

    # box plot
    fig, ax = plt.subplots()

    for i in range(classes):
        color = COLOR[i]
        bg_color = matplotlib.colors.to_rgba(color, alpha=0.2)
        lw = 2  # line width

        ax.boxplot(
            [data[i]], positions=[i],
            patch_artist=True,  # allow color customization
            showfliers=False,   # remove fliers
            widths=0.6,         # width of boxes
            capwidths=0.4,      # width of caps
            boxprops=dict(facecolor=bg_color, edgecolor=color, linewidth=lw),
            whiskerprops=dict(color=color, linewidth=lw),
            capprops=dict(color=color, linewidth=lw),
            medianprops=dict(color=color, linewidth=lw),
        )

    # set axis ticks and labels
    ax.set_xlabel('Class')
    ax.set_ylabel('Value')

    # save in SVG, PDF, and PNG formats
    save_figures(fig, 'examples/box')


if __name__ == '__main__':
    main()
