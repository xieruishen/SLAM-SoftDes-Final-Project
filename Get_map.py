from PIL import Image
import rospy

from std_msgs.msg import Header, String
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import PoseStamped, PoseWithCovarianceStamped, PoseArray, Pose, Point, Quaternion
from nav_msgs.srv import GetMap
from copy import deepcopy

import tf
from tf import TransformListener
from tf import TransformBroadcaster
from tf.transformations import euler_from_quaternion, rotation_matrix, quaternion_from_matrix
from random import gauss

import math
import time

import numpy as np
from numpy.random import random_sample

class OccupancyGrid:
    def __init__(self):



    def get_grid_with_occcupied(self):
        map = self.map
        # build up a numpy array of the coordinates of each grid cell in the map
        Grid = np.zeros((map.info.width * map.info.height, 2))
        total_occupied = 0
        count1 = 0
        for i in range(map.info.width):
            for j in range(map.info.height):
                ind = i + j * map.info.width
                if map.data[ind] > 0:
                    total_occupied += 1
                Grid[count1, 0] = float(i)
                Grid[count1, 1] = float(j)
                count1 += 1

        # build up a numpy array of the coordinates of each occupied grid cell in the map
        Occupied = np.zeros((total_occupied, 2))
        count2 = 0
        for i in range(map.info.width):
            for j in range(map.info.height):
                ind = i + j * map.info.width
                if map.data[ind] > 0:
                    Occupied[count2, 0] = float(i)
                    Occupied[count2, 1] = float(j)
                    count2 += 1
        return Grid, Occupied


class Map:
    def __init__(self,filename):
        self.map_img = filename

    def convert_pgm_to_png(self):
        im = Image.open("filename")
        im.save('map.png')



if __name__ == '__main__':
    grid = OccupancyGrid()
    Grid, Occupied =grid.get_grid_with_occupied()