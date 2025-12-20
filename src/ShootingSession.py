import math
class ShootingSession():
    """
        Define a shooting session.
        
        - distance : X meters (integer)
        - weapon : string
        - grouping_points : [(X,Y),...] (array of tuple of integer)
        - nb_shot_fired : positive integer
        - date : string
        - caliber (optional) : string
    """
    def __init__(self, distance, weapon, grouping_points=[(0,0)], nb_shot_fired=0, caliber=None, date=None):
        self.distance = distance
        self.weapon = weapon
        self.grouping_points = grouping_points
        self.nb_shot_fired = nb_shot_fired
        self.date = date
        
        # optional attribute
        self.caliber = caliber
        
    #-------- getters ----------
    def get_Distance(self):
        return self.distance
    def get_WeaponName(self):
        return self.weapon
    def get_GroupingPoints(self):
        return self.grouping_points
    def get_NbShots(self):
        return self.nb_shot_fired
    def get_caliber(self):
        if self.caliber == None:
            return "No caliber specified"
        else:
            return self.caliber
    def get_Date(self):
        return self.date
        
    #-------- setters ----------
    def set_Distance(self,distance):
        self.distance = distance
    def set_WeaponName(self, WeaponName):
        self.weapon = WeaponName
    def set_GroupingPoints(self, grouping_points):
        self.grouping_points = grouping_points
    def set_NbShots(self, nb_shot_fired):
        self.nb_shot_fired = nb_shot_fired
    def set_Caliber(self,caliber):
        self.caliber = caliber
    def set_Date(self,date):
        self.date = date

    """
        Return an array of euclidian distances from the grouping_points of each impact on the target
        
        Parameters =>
        - coord_impact : array of tuple of integer, representing the coordinates of each shots in the target
        len(coord_impact) <= self.nb_shot_fired
        
        Return =>
        [[Dist_1,Dist_2,...],[Dist_1,Dist_2,...],...]
    """
    def DistFromGroupingPoints(self, coord_impact):
        DistArray = []
        GlobalArray = [] # Global array of each impact distances from each grouping point 
        for i in range(len(self.grouping_points)):
            for X,Y in coord_impact:
                DistArray.append(math.sqrt((X - self.grouping_points[i][0])**2+(Y - self.grouping_points[i][1])**2))
            GlobalArray.append(DistArray)

        return GlobalArray
    
    
        


