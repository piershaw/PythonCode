#
#  Created by Pier Shaw on 01/09/2017
#  Copyright © 2014 Pier Shaw. All rights reserved.
#  Simple Python 2D array no Modules needed
#  piershaw@gmail.com
#

class Python2DArray(object):
    def __init__(self):
        super().__init__()
        self.array2D = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]

    def add(self,row,col,item):
        self.array2D[row].insert(col,item)

    def getArray2d(self):
           return self.array2D


my2dArray = Python2DArray()
my2dArray.add(0,0,"AAAAA")
my2dArray.add(0,1,"BBBBB")
my2dArray.add(1,0,"CCCCC")
my2dArray.add(1,1,"DDDDD")
my2dArray.add(2,0,"EEEEE")

print("my2dArray print at Index : " + " row " + str(my2dArray.getArray2d()[1][1]))
