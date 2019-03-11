from src.utils import get_split_line
import numpy as np
import matplotlib.pyplot as plt


def main():
    file = open('../data/data.csv', 'r')
    ListOfAllLines = []
    for line in file:
        ListOfAllLines.append(line)
    x = []
    y = []
    z = []
    w = []
    for line in ListOfAllLines:
        if line[0] == 'M':
            split_line = get_split_line(line)
            x.append(float(split_line[1]))
            y.append(float(split_line[2]))
        elif line[0] == 'F':
            split_line = get_split_line(line)
            z.append(float(split_line[1]))
            w.append(float(split_line[2]))
    counts_x, bin_edges_x = np.histogram(x, bins=100)
    counts_y, bin_edges_y = np.histogram(y, bins=100)
    counts_z, bin_edges_z = np.histogram(z, bins=100)
    counts_w, bin_edges_w = np.histogram(w, bins=100)
    column_width = np.min(bin_edges_x[1:] - bin_edges_x[:-1])
    plt.bar(0.5*(bin_edges_x[1:] +bin_edges_x[:-1]),  counts_x, label='men\'s age', alpha=0.5, width=column_width)
    column_width = np.min(bin_edges_z[1:] - bin_edges_z[:-1])
    plt.bar(0.5*(bin_edges_z[1:] +bin_edges_z[:-1]),  counts_z, label='women\'s age', alpha=0.5, width=column_width)
    plt.legend(loc=0)
    plt.savefig('age_distribution.png')
    plt.close()
    column_width = np.min(bin_edges_y[1:] - bin_edges_y[:-1])
    plt.bar(0.5*(bin_edges_y[1:] +bin_edges_y[:-1]),  counts_y, label='men\'s height', alpha=0.5, width=column_width)
    column_width = np.min(bin_edges_w[1:] - bin_edges_w[:-1])
    plt.bar(0.5*(bin_edges_w[1:] +bin_edges_w[:-1]),  counts_w, label='women\'s height', alpha=0.5, width=column_width)
    plt.legend(loc=0)
    plt.savefig('height_distribution.png')
    file.close()
main()
