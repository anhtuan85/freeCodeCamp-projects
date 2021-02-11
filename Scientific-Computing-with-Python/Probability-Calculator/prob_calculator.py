import copy
import random
# Consider using the modules imported above.

class Hat:

    def __init__(self,**kargs):
        self.contents = list()
        for i in kargs:
            self.contents+= [i]*kargs[i]
        self._contents = self.contents.copy()

    def draw(self, num):
        if len(self.contents)<num:
            return self.contents
        drawn = [self.contents.pop(random.randint(0,len(self.contents)-1)) for i in range(num)]
        return drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0
    for i in range(num_experiments):
        drawn = hat.draw(num_balls_drawn)
        successful_experiments+= all(expected_balls[i]<=drawn.count(i) for i in expected_balls)
        hat.contents = hat._contents.copy()
    return successful_experiments/num_experiments
