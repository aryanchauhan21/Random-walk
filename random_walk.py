from random import choice


class RandomWalk():
    def __init__(self, points):
        self.points = points
        self.x_list = [0]
        self.y_list = [0]

    def points_generator(self):

        while len(self.x_list) < self.points:

            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_path_length = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_path_length = y_direction * y_distance

            if y_path_length == 0 and x_path_length == 0:
                continue

            x_point = self.x_list[-1] + x_path_length
            y_point = self.y_list[-1] + y_path_length

            self.x_list.append(x_point)
            self.y_list.append(y_point)

