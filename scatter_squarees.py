import matplotlib.pyplot as plt

x_values = list(range(1,50000))
y_values = [x**2 for x in x_values]


plt.scatter(x_values,y_values,edgecolor ='none',s =100)

plt.title("Squuare Numbers",fontsize = 24)
plt.xlabel("Value",fontsize = 14)
plt.ylabel("Square OF Value",fontsize = 14)

#settings the tick labels
plt.tick_params(axis = 'both',which = 'major',labelsize = 14)
plt.axis([0,5,0,5000])

plt.show()
