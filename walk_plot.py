import matplotlib.pyplot as m
from random_walk import RandomWalk
while True:
    man = RandomWalk(5000)
    List = list(range(5000))
    man.points_generator()
    m.scatter(man.x_list, man.y_list,s=15, c=List, cmap=m.cm.Greens, edgecolors='none')
    m.title('Random path taken my a man')
    m.scatter(0, 0, c='blue', edgecolors='none', s=100)
    m.scatter(man.x_list[-1], man.y_list[-1], c='red', edgecolors='none', s=100)
    m.show()
    ans = input('wanna continue y/n ? ')
    if ans == 'n':
        break