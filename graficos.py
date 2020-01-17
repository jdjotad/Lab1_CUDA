import matplotlib.pyplot as plt
import numpy as np
from math import log

params = {'legend.fontsize': 'x-large',
          'figure.figsize': (16, 8),
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large'}
plt.rcParams.update(params)
graph = {"CPU":{"x": [], "y": []}, "GPU":{"x": [], "y": []}, "HYBRID":{"x": [], "y": []}}
graph_2 = {"CPU":{"x": [], "y": []}, "GPU":{"x": [], "y": []}, "GPU_BLOCK":{"x": [], "y": []}}
counter = 0
with open("1_a_time") as f: # open the file for reading
    for line in f: # iterate over each line
        data = line.split()
        for i in data:
            if counter == 0:
                graph["CPU"]["x"].append(float(i))
                counter = 1
            else:
                graph["CPU"]["y"].append(float(i))
                counter = 0

with open("1_b_time") as f: # open the file for reading
    for line in f: # iterate over each line
        data = line.split()
        for i in data:
            if counter == 0:
                graph["GPU"]["x"].append(float(i))
                counter = 1
            else:
                graph["GPU"]["y"].append(float(i))
                counter = 0

with open("1_c_time") as f: # open the file for reading
    for line in f: # iterate over each line
        data = line.split()
        for i in data:
            if counter == 0:
                graph["HYBRID"]["x"].append(float(i))
                counter = 1
            else:
                graph["HYBRID"]["y"].append(float(i))
                counter = 0
line_n = -1
with open("2_time") as f: # open the file for reading
    for line in f: # iterate over each line
        data = line.split()
        line_n += 1
        if line_n == 0:
            for i in data:
                if counter == 0:
                    graph_2["CPU"]["x"].append(float(i))
                    counter = 1
                else:
                    graph_2["CPU"]["y"].append(float(i))
                    counter = 0
        elif line_n == 1:
            for i in data:
                if counter == 0:
                    graph_2["GPU"]["x"].append(float(i))
                    counter = 1
                else:
                    graph_2["GPU"]["y"].append(float(i))
                    counter = 0

plt.figure(0)
#[log(y,10) for y in graph["CPU"]["x"]]
plt.plot(graph["CPU"]["x"],graph["CPU"]["y"],'ro', label = 'CPU')
plt.plot(graph["CPU"]["x"],graph["CPU"]["y"],'r-', alpha = 0.3)
plt.plot(graph["GPU"]["x"],graph["GPU"]["y"],'go', label = 'GPU')
plt.plot(graph["GPU"]["x"],graph["GPU"]["y"],'g-', alpha = 0.3)
plt.plot(graph["HYBRID"]["x"],graph["HYBRID"]["y"],'bo', label = 'HYBRID')
plt.plot(graph["HYBRID"]["x"],graph["HYBRID"]["y"],'b-', alpha = 0.3)
plt.grid()
plt.xlabel('$\Delta_t$', fontsize=20)
plt.ylabel('Tiempo [ms]')
plt.title('Tiempo vs $\Delta_t$', fontsize=26)
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.savefig('grafico_1.png', orientation='portrait')


plt.figure(1)
#[log(y,10) for y in graph["CPU"]["x"]]
plt.plot(graph_2["CPU"]["x"],graph_2["CPU"]["y"],'ro', label = 'CPU')
plt.plot(graph_2["CPU"]["x"],graph_2["CPU"]["y"],'r-', alpha = 0.3)
plt.plot(graph_2["GPU"]["x"],graph_2["GPU"]["y"],'go', label = 'GPU')
plt.plot(graph_2["GPU"]["x"],graph_2["GPU"]["y"],'g-', alpha = 0.3)
#plt.plot(graph_2["HYBRID"]["x"],graph["HYBRID"]["y"],'bo', label = 'HYBRID')
#plt.plot(graph_2["HYBRID"]["x"],graph["HYBRID"]["y"],'b-', alpha = 0.3)
plt.grid()
plt.xlabel('$m$', fontsize=20)
plt.ylabel('Tiempo [ms]')
plt.title('Tiempo vs m', fontsize=26)
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.savefig('grafico_2.png', orientation='portrait')

#plt.show()
