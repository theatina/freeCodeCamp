import copy
import random
from copy import deepcopy
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    balls = [ [ colour for c in range(val) ] for colour,val in kwargs.items()]
    self.contents = [ c for b in balls for c in b]
    self.tot_balls=len(self.contents)
  
  def draw(self, ball_num):
    # random.shuffle(self.contents)
    if ball_num>self.tot_balls:
      balls_drawn=self.contents
      self.tot_balls=0
      self.contents=[]
    else:
      balls_drawn=random.sample(self.contents, ball_num)
      self.tot_balls=self.tot_balls-ball_num
      for b in balls_drawn:
        self.contents.remove(b)
    return balls_drawn
    

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  exp_balls= [ [ colour for c in range(val) ] for (colour,val) in expected_balls.items()]
  exp_ball_list=[ c for b in exp_balls for c in b]
  
  expected_happened=0
  for i in range(num_experiments):
    temp_hat=deepcopy(hat)
    balls_drawn=temp_hat.draw(num_balls_drawn)

    b_in_drawn=0
    for b in exp_ball_list:
      if b in balls_drawn:
        b_in_drawn+=1
        balls_drawn.remove(b)
  
    if b_in_drawn==len(exp_ball_list):
      expected_happened+=1
  
  prob=expected_happened/num_experiments
  
  return prob

h1=Hat(blue=3,red=2,green=6)
# print(h1.draw(2))
p=experiment(h1,{"blue":2,"green":1},4,100)
print(p)