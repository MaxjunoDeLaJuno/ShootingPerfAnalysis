class ShootingSession():
    """
        Define a shooting session.
        
        - distance : X meters (integer)
        - weapon_name : string
        - target_point : [(X,Y),...] (array of tuple of integer)
        - nb_shot_fired : positive integer
        - caliber (optional) : string
    """
    def __init__(self, distance, weapon_name, target_points, nb_shot_fired=0, caliber=None):
        self.dist = distance
        self.weapon = weapon_name
        self.grouping_p = target_points
        self.nb_shot = nb_shot_fired
        
        # optional attribute
        self.caliber = caliber
        
    #-------- getters ----------
    def get_Distance(self):
        return self.dist
    def get_WeaponName(self):
        return self.weapon
    def get_GroupingPoints(self):
        return self.grouping_p
    def get_NbShots(self):
        return self.nb_shot
    def get_caliber(self):
        if self.caliber == None:
            return "No caliber specified"
        else:
            return self.caliber
        
    #-------- setters ----------
    def set_Distance(self,distance):
        self.dist = distance
    def set_WeaponName(self, WeaponName):
        self.weapon = WeaponName
    def set_GroupingPoints(self, grouping_p):
        self.grouping_p = grouping_p
    def set_NbShots(self, nb_shot):
        self.nb_shot = nb_shot
    def set_caliber(self,caliber):
        self.caliber = caliber


   