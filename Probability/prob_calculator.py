
import copy
import random
# Consider using the modules imported above.

class Hat:
    # contents = []
    def __init__(self,**colours):
        self.contents = []
        for col,amount in colours.items():
            for i in range(amount):
                self.contents.append(col)

    def draw(self,num: int):
        """returns a list of balls drawn(and removed) randomly from contents"""

        if num >= len(self.contents): return self.contents

        balls = []
        for i in range(num):
            colour = self.contents.pop(random.randint(0,len(self.contents)-1))
            balls.append(colour)
        
        return balls


def experiment(hat: Hat, expected_balls=dict, num_balls_drawn=1, num_experiments=1):
    """returns the probability of drawing expected_balls from the hat object"""

    hat_clone = copy.copy(hat)
    m = 0 # the number of times expexted_balls are drawn
    for _ in range(num_experiments):
        hat_clone.contents = hat.contents[:]
        balls_drawn = hat_clone.draw(num_balls_drawn)
        balls_present = []
        for ball, amount in expected_balls.items():
            # '1' means the expected ball and its quantity was drawn
            if balls_drawn.count(ball) >= amount: balls_present.append(1)
            else: balls_present.append(0)
        # if balls_present has no 0's, the expected balls are all present in their desired quantities
        if sum(balls_present) == len(balls_present): m += 1

    return m/num_experiments

# print(copy.__doc__)
# hat1 = Hat(blue=3,red=2,green=6)
# p1 = experiment(hat=hat1, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000)
# print(p1) # 0.272

# hat2 = Hat(yellow=5,red=1,green=3,blue=9,test=1)
# p2 = experiment(hat=hat2, expected_balls={"yellow":2,"blue":3,"test":1}, num_balls_drawn=20, num_experiments=100)
# print(p2) # 1.0

