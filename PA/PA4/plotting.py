import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import itertools
import time


def plot(sets, colors=[], time = 10):
  # extract real part
  if colors == []:
    colors = itertools.cycle(["r", "b", "g"])
  else:
    colors = itertools.cycle(colors)
  i = 0
  x_min = min([z.real for z in sets[0]])
  x_max = max([z.real for z in sets[0]])
  y_min = min([z.imag for z in sets[0]])
  y_max = max([z.imag for z in sets[0]])
  for S in sets:
    x = [ele.real for ele in S]
    # extract imaginary part
    y = [ele.imag for ele in S]

    x_min = min([min(x), x_min])
    x_max = max([max(x), x_max])
    y_min = min([min(y), y_min])
    y_max = max([max(y), y_max])

    # plot the complex numbers
    plt.scatter(x, y, color=next(colors))
    i += 1
  plt.ylabel('Imaginary')
  plt.xlabel('Real')
  plt.xlim(x_min - 2, x_max + 2)
  plt.ylim(y_min - 2, y_max + 2)
  plt.axvline(x=0, c="black", label="Real axis")
  plt.axhline(y=0, c="black", label="Imaginary axis")
  plt.ion()
  plt.show()

  print(f"Plot is on display. Closing plot in {time} seconds...")
  for remaining in range(time, 0, -1):
      print(f"{remaining}", end= ' ') 
      plt.pause(1)
  plt.close()
  
