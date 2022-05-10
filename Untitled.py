#!/usr/bin/env python
# coding: utf-8

# In[17]:


import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(1,10,100)
y1 = (5-2*x)/3
y2 = (5.1-2*x)/3.1

y3 = (5.001-2*x)/3
y4 = (5.1-2*x)/3.1

plt.plot(x,y1,x,y2,x,y3,x,y4)


plt.title("Graficas")
plt.legend(('y1','y2','y3','y4'), loc='upper left')
plt.xlabel('x')
plt.ylabel('y', fontsize=20)
plt.show()


# In[10]:


x = np.linspace(1,10,100)
y1 = (2-2*x)/3
y2 = (1.999-1.999*x)/3

y3 = (2-2*x)/3
y4 = (2-1.999*x)/3

plt.plot(x,y1,x,y2,x,y3,x,y4)


plt.title("Graficas")
plt.legend(('y1','y2','y3','y4'), loc='upper left')
plt.xlabel('x')
plt.ylabel('y', fontsize=20)
plt.show()


# In[ ]:


max = 100
for k in range(max+1):
    for i in range(1,n+1):
        sum = 0
        for j in range(1,i):
            sum = sum + 

