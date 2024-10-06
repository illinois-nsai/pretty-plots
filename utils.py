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

# hatch style
HATCH = [
    None,
    '/',
    '\\',
    '.',
    'x',
    '-',
    '|',
    '+',
    '/.',
    '\\.',
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
