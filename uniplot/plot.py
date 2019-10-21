import matplotlib.pyplot as plt

def plot_bar_show(d):
    ## A list of numbers as long as the elements in d
    r = range(0, len(d))
    ## Prepare a figure
    plt.figure()

    ## Add bars, one at each x position, with the values of d
    plt.bar(r, d.values())
    ## Add labels to the x-axis, with the keys of d
    plt.xticks(r, d.keys())
    ## Squash everything up so there is no white space
    plt.tight_layout()
    ## Show the graph
    plt.show()
