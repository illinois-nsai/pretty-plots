# Pretty Plots

This repository contains scripts for plotting "publication-quality" figures
with the `matplotlib` library in Python.
[Example outputs](#examples) are shown below.

## Usage

The following usage is tested on Ubuntu 24.04.

1. Install required Python packages:

    ```shell
    pip install -r requirements.txt
    ```

    * Pass `--break-system-packages` to the above command if you are comfortable with installing the required packages system-wide. Otherwise, create a Python [virtual environment](https://docs.python.org/3/library/venv.html).

2. Confirm that the "Times New Roman" font is installed on your system:

    ```shell
    $ python3
    >>> import matplotlib.font_manager as fm
    >>> fm.findfont('Times New Roman')
    ```

    * If the font is not found on Ubuntu, run:
        ```shell
        # install Times New Roman through Microsoft Core Fonts
        sudo apt install ttf-mscorefonts-installer

        # clear matplotlib's cache
        rm -r ~/.cache/matplotlib
        ```

        Restart the Python interpreter and try to find the font again.
        Expected output is
        `/usr/share/fonts/truetype/msttcorefonts/Times_New_Roman.ttf`.

    * Alternatively, install LaTeX and set `'text.usetex': True` in `utils.py`.
      LaTeX fonts such as "Times New Roman" and "Computer Modern" should now be
      available. However, text rendering will be slower.

3.  Edit figure parameters in `utils.py` as needed,
    and run the desired plotting script (e.g., `./line_plot.py`).


## Example figures

### Line plot

![line plot](examples/line.png)

### Scatter plot

![scatter plot](examples/scatter.png)

### Bar plot

![bar plot](examples/bar.png)

### CDF plot

![CDF plot](examples/cdf.png)

### Box plot

![box plot](examples/box.png)

### Violin plot

![violin plot](examples/violin.png)
