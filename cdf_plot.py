#!/usr/bin/env python3

import numpy as np
from utils import *


def generate_dummy_data(classes, samples):
    np.random.seed(2025)

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

    # cdf plot
    fig, ax = plt.subplots()

    for i in range(classes):
        x, y = cdf_helper(data[i], bins=100)
        ax.plot(x, y,
                label=f'Class{i}',
                color=COLOR[i],
                linestyle=LINESTYLE[i],
                clip_on=False)

    # set axis labels
    ax.set_xlabel('Value')
    ax.set_ylabel('CDF')

    # put legend outside plot when no space, but put inside whenever possible
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    # save in SVG, PDF, and PNG formats
    save_figures(fig, 'examples/cdf')


if __name__ == '__main__':
    main()
