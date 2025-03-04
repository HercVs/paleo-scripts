import matplotlib.pyplot as plt
import numpy as np
import math

def style_axes(subplot_n, ax, data, y_axis):
    ax.set_facecolor('#EFFFFF')
    ax.grid(True, which='major', axis='both', linestyle=':', color='black', linewidth=0.5)
    ax.spines['bottom'].set_linewidth(2)
    ax.spines['bottom'].set_color('black')
    ax.spines['right'].set_visible(False)
    ax.set_xticks(np.arange(0, 100.1, 10))
    ax.set_xticks(np.arange(0, 100.1, 5), minor=True)
    ax.tick_params(axis='x', which='major', length=10, width=2, color='black')
    ax.tick_params(axis='x', which='minor', length=5, width=1, color='black')
    ax.set_xlim(0, math.ceil(max(data) / 10.0) * 10)
    
    if subplot_n == 0: # Customize y axis - only for 1st subplot
        ax.spines['left'].set_linewidth(2)
        ax.spines['left'].set_color('black')
        ax.set_ylabel('Column Height (cm)')
        ax.set_yticks(y_axis)
        ax.tick_params(axis='y', which='major', length=10, width=2, color='black')
        ax.tick_params(axis='y', which='minor', length=5, width=1, color='black')
    else: # Hide y border and ticks on subplots after 1st
        ax.spines['left'].set_visible(False)
        ax.tick_params(axis='y', which='both', length=0)


def create_subplot_ratios(data):
    max_tens = [math.ceil(max(arr) / 10.0) * 10 for arr in data]
    return [x / sum(max_tens) for x in max_tens]


################################################################################
# Example data
input_data = [[10, 20, 30, 50, 60, 80, 90, 110, 150, 170, 210, 250],
              [11, 8, 21, 10, 35, 57, 19, 32, 0, 14, 26, 48], 
              [4, 23, 10, 41, 34, 3, 20, 21, 84, 53, 15, 11], 
              [5.3, 30, 0, 11, 35, 43, 10, 1, 4.3, 23, 32, 11],
              [4, 3, 0, 1, 4, 3, 0, 1, 4, 3, 5, 1]]
input_data_dict = { # Should eventually read dicts to pull sp names
    "height": [10, 20, 30, 50, 60, 80, 90, 110, 150, 170, 210, 250],
    "Sp1": [1, 8, 1, 10, 5, 7, 9, 2, 0, 4, 6, 8],
    "Sp2": [4, 3, 0, 1, 4, 3, 0, 1, 4, 3, 4, 1]
}

height_column = 0 # TODO In given excel/csv, height column is assumed 1st


################################################################################
# Quantitative abundance plots
heights = input_data.pop(height_column)
fig, axes = plt.subplots(ncols=len(input_data),
                         sharey=True,
                         figsize=(8, 6),
                         gridspec_kw={'width_ratios': create_subplot_ratios(input_data)})

for i in range(len(input_data)):
    arr = np.array(input_data[i])
    ax = axes[i]
    ax.plot(arr, heights, marker='.', linestyle='-', linewidth=0, color='black')
    ax.fill_betweenx(heights, arr, color='#206599')
    ax.set_xlabel('%')
    ax.set_title('sp')
    style_axes(i, ax, arr, heights)

plt.tight_layout()
plt.show()