import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 1000)                     # от -10 до 10 сделать 100 точек
y = 5*x**2+10*x - 30                       # y - тоже много точек




# 𝑓(𝑥)=5𝑥^2+10𝑥−30
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel("x")                              # подпись у горизонтальной оси х
ax.set_ylabel("y")                              # подпись у вертикальной оси y
ax.legend()                          
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('blue')
ax.spines['top'].set_color('blue')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
fig.savefig('1.png')  
# plot the function

plt.plot(x, y, 'r')


# show the plot
plt.show()

import numpy as np
import matplotlib.pyplot as plt
 
y = lambda x: 5*x**2+10*x - 30    
xs = np.linspace(-10, 10, 100)
plt.plot(xs, [y(x) for x in xs])
plt.show()