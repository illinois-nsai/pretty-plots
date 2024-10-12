import numpy as np

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# default figure parameters
plt.rcParams.update({
    'text.usetex': False,
    'font.family': 'serif',
    'font.serif': 'Times New Roman',
    'font.size': 16,
    'legend.fontsize': 16,
    'axes.labelsize': 16,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'lines.linewidth': 2,
    'lines.markersize': 10,
    'svg.fonttype': 'none',
})

# color palette
import seaborn as sns
sns.set_palette('deep')  # or 'muted', 'colorblind'

# colors
COLOR = [
    'C0',  # '#4c72b0'
    'C1',  # '#dd8452'
    'C2',  # '#55a868'
    'C3',  # '#c44e52'
    'C4',  # '#8172b3'
    'C5',  # '#937860'
    'C6',  # '#da8bc3'
    'C7',  # '#8c8c8c'
    'C8',  # '#ccb974'
    'C9',  # '#64b5cd'
]

# hatch style
HATCH = [
    None,
    '/',
    '\\',
    '.',
    'x',
    '-',
    'o',
    '+',
    '//',
    '\\\\',
]

# line style
LINESTYLE = [
    'solid',
    'dotted',
    'dashed',
    'dashdot',
    (0, (5, 5)),              # dashed
    (0, (1, 1)),              # densely dotted
    (0, (5, 1)),              # densely dashed
    (0, (3, 1, 1, 1)),        # densely dashdotted
    (5, (10, 3)),             # long dash with offset
    (0, (3, 1, 1, 1, 1, 1)),  # densely dashdotdotted
]

# marker style
MARKER = [
    'o',
    '^',
    's',
    'v',
    'd',
    '<',
    '>',
    'D',
    'H',
    'p',
]


def cdf_helper(data, bins=None):
    '''
    Helper function to compute CDF probabilities.

    :param data: array of data points (shape: (1, N))
    :param bins: 1) None (raw/exact CDF), or 2) number of bins (binned CDF), or
                 3) right edges of bins (binned CDF); first bin: (-inf, bins[0])
    '''

    samples = len(data)
    if samples == 0:
        raise ValueError('No data points to compute CDF')
    data = np.array(data)

    if bins is None:
        sorted_data = np.sort(data)
        cdf_probs = (1 + np.arange(samples)) / samples
        return sorted_data, cdf_probs
    else:
        if type(bins) == int:
            bins = np.linspace(data.min(), data.max(), bins)
        else:  # assume bins is a sorted list of bin edges
            bins = np.array(bins)

        cdf_probs = np.zeros(len(bins))
        for i, bin_edge in enumerate(bins):
            cdf_probs[i] = np.sum(data <= bin_edge)
        cdf_probs /= samples

        return bins, cdf_probs


def save_figures(fig, file_stem):
    '''
    Save the figure in SVG, PDF, and PNG formats. Close the figure afterwards.
    '''

    for ext in ['svg', 'pdf', 'png']:
        file_name = f'{file_stem}.{ext}'

        if ext == 'png':
            fig.savefig(file_name, bbox_inches='tight', dpi=150)
        else:
            fig.savefig(file_name, bbox_inches='tight')

        print(f'Saved {file_name}')

    plt.close(fig)
