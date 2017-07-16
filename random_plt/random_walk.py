from random import choice


def get_step():
    distance = choice([0, 1, 2, 3, 4])
    choose = choice([-1, 1])
    return distance * choose


class RandomWalk:
    def __init__(self, num_points=10000):
        self.num_points = num_points

        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            # x
            x_step = get_step()

            # y
            y_step = get_step()

            if x_step == 0 and y_step == 0:
                continue

            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
