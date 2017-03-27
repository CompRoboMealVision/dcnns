#!/usr/bin/env python2.7

from label_image import label_image
import sys
import matplotlib.pyplot as plt
import numpy as np

def plot_bar_graph(labels, scores, bins):

    fig, ax = plt.subplots()
    ind = np.arange(bins)
    width = 0.35
    labels = labels[0:bins]
    heights = scores[0:bins]
    rects = ax.bar(ind, heights, width)
    ax.set_xticks(ind)
    ax.set_xticklabels((labels))

if __name__ == '__main__':
    # change this as you see fit
    image_path = sys.argv[1]
    labels, scores = label_image(image_path)
    plot_bar_graph(labels, scores, 5)
    plt.show()