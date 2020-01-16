import matplotlib.pyplot as plt
import numpy as np 

params = {'legend.fontsize': 'x-large',
          'figure.figsize': (15, 5),
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large'}
plt.rcParams.update(params)

graph = ({'delta_1':{'value': [], 'real_value': [], 'i_value' : []},
        'delta_2':{'value': [], 'real_value': [], 'i_value' : []},
        'delta_3':{'value': [], 'real_value': [], 'i_value' : []},
        'delta_4':{'value': [], 'real_value': [], 'i_value' : []},
        'delta_5':{'value': [], 'real_value': [], 'i_value' : []},
        'delta_6':{'value': [], 'real_value': [], 'i_value' : []}})
deltas = ['delta_1', 'delta_2', 'delta_3', 'delta_4', 'delta_5', 'delta_6']
i = -1
i_counter = 0
with open("../1_a") as f: # open the file for reading
    for line in f: # iterate over each line
        if line[0] == 'C':
            i += 1
            counter = 0
        elif line[0] == 't':
            current_data = line.split()
            graph[deltas[i]]['i_value'].append(float(current_data[2]))
            i_counter += 1
        elif line[0] == 'y':
            current_data = line.split()
            graph[deltas[i]]['value'].append(float(current_data[2]))
            graph[deltas[i]]['real_value'].append(float(current_data[4]))

counter = 0
for j in deltas:
    plt.figure(counter)
    plt.plot(graph[deltas[counter]]['i_value'],graph[deltas[counter]]['value'],'r-')
    #plt.hold(True)
    plt.plot(graph[deltas[counter]]['i_value'],graph[deltas[counter]]['real_value'],'g-')
    plt.grid()
    plt.xlabel('tiempo [s]', fontsize=20)
    plt.ylabel('y (rojo) , y_real (verde)')
    plt.title('Funcion original y aproximada vs Tiempo', fontsize=26)
    counter += 1
plt.show()
    

