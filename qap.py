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
    max_tens = [math.ceil(max(col) / 10.0) * 10 for _, col in data.items()]
    return [x / sum(max_tens) for x in max_tens]


# Quantitative abundance plots
def qap_build(input_data):
    fig, axes = plt.subplots(
        ncols=len(list(input_data)),
        sharey=True,
        figsize=(1 * len(list(input_data)) + 2, 8),
        gridspec_kw={'width_ratios': create_subplot_ratios(input_data)}
    )
    for i in range(len(list(input_data))):
        species_name = input_data.iloc[:, i].name
        abundances = input_data.iloc[:, i].values
        heights = input_data.index.values
        ax = axes[i]
        ax.plot(abundances, heights, marker='.', linestyle='-', linewidth=0, color='black')
        ax.fill_betweenx(heights, abundances, color='#206599')
        ax.set_xlabel('%')
        ax.set_title(species_name, y=1.1, rotation = 85)
        style_axes(i, ax, abundances, heights)

    fig.tight_layout()
    return fig