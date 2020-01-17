import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
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
        else:
            for i in data:
                if counter == 0:
                    graph_2["GPU_BLOCK"]["x"].append(int(i))
                    counter = 1
                else:
                    graph_2["GPU_BLOCK"]["y"].append(float(i)/1000)
                    counter = 0
ordered_list_y = []
ordered_list_x = []
for i in range(len(graph_2["GPU_BLOCK"]["x"])):
    if i == 0:
        ordered_list_y.insert(0, graph_2["GPU_BLOCK"]["y"][i])
        ordered_list_x.insert(0, graph_2["GPU_BLOCK"]["x"][i])
    else:
        for j in range(len(ordered_list_x)):
            if graph_2["GPU_BLOCK"]["x"][i] < ordered_list_x[j]:
                ordered_list_y.insert(j, graph_2["GPU_BLOCK"]["y"][i])
                ordered_list_x.insert(j, graph_2["GPU_BLOCK"]["x"][i])
                break
            elif (j == len(ordered_list_x) - 1):
                ordered_list_y.insert(j+1, graph_2["GPU_BLOCK"]["y"][i])
                ordered_list_x.insert(j+1, graph_2["GPU_BLOCK"]["x"][i])
graph_2["GPU_BLOCK"]["x"] = ordered_list_x
graph_2["GPU_BLOCK"]["y"] = ordered_list_y
    

plt.figure(0)
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
plt.plot(graph_2["CPU"]["x"],graph_2["CPU"]["y"],'ro', label = 'CPU')
plt.plot(graph_2["CPU"]["x"],graph_2["CPU"]["y"],'r-', alpha = 0.3)
plt.plot(graph_2["GPU"]["x"],graph_2["GPU"]["y"],'go', label = 'GPU')
plt.plot(graph_2["GPU"]["x"],graph_2["GPU"]["y"],'g-', alpha = 0.3)
plt.grid()
plt.xlabel('$m$', fontsize=20)
plt.ylabel('Tiempo [ms]')
plt.title('Tiempo vs m', fontsize=26)
plt.xscale('log')
plt.yscale('log')
plt.xticks(graph_2["CPU"]["x"] + graph_2["GPU"]["x"])
plt.legend()
plt.savefig('grafico_2.png', orientation='portrait')


plt.figure(2)
plt.plot(graph_2["GPU_BLOCK"]["x"],graph_2["GPU_BLOCK"]["y"],'ro', label = 'Iteracion block_size')
plt.plot(graph_2["GPU_BLOCK"]["x"],graph_2["GPU_BLOCK"]["y"],'r-', alpha = 0.3)
plt.grid()
plt.xlabel('block_size', fontsize=20)
plt.ylabel('Tiempo [s]')
plt.title('Tiempo vs block_size', fontsize=26)
plt.xticks(graph_2["GPU_BLOCK"]["x"])
plt.yticks(graph_2["GPU_BLOCK"]["y"])
plt.legend()
plt.savefig('grafico_2_block_size.png', orientation='portrait')

#plt.show()
