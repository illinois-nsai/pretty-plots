#!/usr/bin/env python3

import numpy as np
from utils import *


def generate_dummy_data(classes):
    np.random.seed(2025)

    # shape of x: (1, classes)
    x = np.arange(classes)

    # shape of y_mean and y_err: (1, classes)
    y_mean = 100 * np.random.rand(classes) + 50
    y_err = 100 * np.random.rand(classes) / 3

    return x, y_mean, y_err


def main():
    # generate dummy data
    classes = 10
    x, y_mean, y_err = generate_dummy_data(classes)

    # bar plot
    fig, ax = plt.subplots()

    for i in range(classes):
        ax.bar(x[i], y_mean[i], yerr=y_err[i],
               label=f'Class{i}',
               color=f'C{i}',
               hatch=HATCH[i],
               edgecolor='0.1',  # edge color (grayscale 0.1)
               linewidth=1,      # edge width
               error_kw=dict(ecolor='black', lw=2, capsize=8, capthick=2),
               clip_on=False)

    # set axis ticks and labels
    ax.set_xticks(x)
    ax.set_xlabel('Class')
    ax.set_ylabel('Height')

    # put legend outside plot when no space, but put inside whenever possible
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    # save in SVG, PDF, and PNG formats
    save_figures(fig, 'examples/bar')


if __name__ == '__main__':
    main()
