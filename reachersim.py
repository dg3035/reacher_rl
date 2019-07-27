
import roboschool
import gym
import numpy as np


class ReacherSim:
    
    #this function sets up the environment and instantiates a reacher with a random state
    def setup_environment(self):
        self.a = np.array([0.,0.])
        # setting up the environment
        self.env = gym.make('RoboschoolReacher-v1')
        self.env.seed(10)
        self.state = self.env.reset()


        #the loop will keep on running the reset function till it gets a reachable state
        while (self.if_target_reachable(self.state[0], self.state[1]) == False):
            self.state = self.env.reset()

    #     print("target reachable")

        return self.state, self.a, self.env
    
    #this function checks whether the goal is reachable
    def if_target_reachable(self,target_x, target_y):
        target = np.sqrt(target_x**2 + target_y**2)
        link_1 = 0.1
        link_2 = 0.11

        if target < np.sqrt(link_1**2 + link_2**2):
            return True

        else:
    #         print('target unreachable')
            return False
    
    #this function derives the inverse kinematics of the target x and y, giving joint theta values
    def inverse_kinematics(self, target_x, target_y):
        link_1 = 0.1
        link_2 = 0.11
        q2 =np.arccos((target_x**2 + target_y**2 - link_1**2 - link_2**2)/(2*link_1*link_2))
        q1 = np.arctan2(target_y,target_x)-np.arctan2((link_2*np.sin(q2)),(link_1+link_2*np.cos(q2)))
        return q1,q2 

