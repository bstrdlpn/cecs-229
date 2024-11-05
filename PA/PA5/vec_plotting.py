import matplotlib.pyplot as plt

def plot(vec_lst: list):
    max_x = 0.5
    min_x = -0.5
    max_y = 0.5
    min_y = -0.5

    fig, ax = plt.subplots()
    colors = ['k', 'r', 'b', 'c', 'm', 'y', 'g']
    names = ['black', 'red', 'blue', 'cyan', 'magenta', 'yellow', 'green']
    color_dic = dict(zip(colors, names))
    i = 0
    for v in vec_lst:
        c = colors[i]
        print(f"Plotting in {color_dic[c].upper()}: v = {v} ")
        x, y = v[0], v[1]
        ax.quiver(0, 0, x, y, angles='xy', scale_units='xy', scale=1, color=c)
        i+= 1 % len(colors)
        max_x = max(x, max_x)
        min_x = min(x, min_x)
        max_y = max(y, max_y)
        min_y = min(y, min_y)


    # Set the x-limits and y-limits of the plot
    ax.set_xlim([min_x - 1, max_x + 1])
    ax.set_ylim([min_y - 1, max_y + 1])

    # Show the plot along with the grid
    plt.grid()
    plt.show()