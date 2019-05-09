from numpy import sqrt
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
from matplotlib.collections import PatchCollection
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes, mark_inset# make font huge for beamer
font = {'weight' : 'bold',
        'size'   : 22}
matplotlib.rc('font', **font)

def visualize(x, y, name):
    fig, ax = plt.subplots(figsize=(10, 10))
    inside = x ** 2 + y ** 2 <= 1.0
    ax.scatter(x[inside], y[inside], c='green', s=3, marker='^')
    ax.scatter(x[~inside], y[~inside], c='red', s=3)
    estimate = sum(inside) / len(inside) * 4
    ax.set_title(
        "Approximating $\pi$ with {} samples as {:f}".format(name, estimate),
        y=1.08)
    p = PatchCollection([Wedge((0, 0), 1, 0, 360)], alpha=0.1)
    ax.add_collection(p)
    axins = zoomed_inset_axes(ax, 2.5, loc=3)  # zoom = 6
    axins.axis([1.4, 1.1, 1.4, 1.1])
    axins.scatter(x[inside], y[inside], c='green', s=50, marker='^')
    axins.scatter(x[~inside], y[~inside], c='red', s=50)
    p = PatchCollection([Wedge((0, 0), 1, 0, 360)], alpha=0.1)
    axins.add_collection(p)
    axins.set_xlim(1 / sqrt(2), 1 / sqrt(2) + 0.2)  # Limit the region for zoom
    axins.set_ylim(1 / sqrt(2) - 0.2, 1 / sqrt(2))
    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])

    plt.xticks(visible=False)  # Not present ticks
    plt.yticks(visible=False)
    #
    ## draw a bbox of the region of the inset axes in the parent axes and
    ## connecting lines between the bbox and the inset axes area
    mark_inset(ax, axins, loc1=2, loc2=4, fc="none", ec="0.5", linewidth=3)
