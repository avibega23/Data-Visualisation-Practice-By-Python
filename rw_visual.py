import matplotlib.pyplot as plt

from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()

point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values , rw.y_values, c = point_numbers ,edgecolor ="none",s=15)
# plt.scatter(rw.x_values,rw.y_values,s=10)
plt.show()