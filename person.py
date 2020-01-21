class GameObject:

    def __init__(self, x, y, vx, vy):
        self._x = x
        self._y = y
        self._vx = vx
        self._vy = vy
        self._ax = 0
        self._ay = 0

    def getx(self):
        return self._x

    def gety(self):
        return self._y

    def getvx(self):
        return self._vx

    def getvy(self):
        return self._vy

    def getax(self):
        return self._ax

    def getay(self):
        return self._ay
        
    def setx(self, x):
        self._x = x
    
    def sety(self, y):
        self._y = y

    def setvx(self, vx):
        self._vx =  vx
    
    def setvy(self, vy):
        self._vy = vy

    def setax(self, ax):
        self._ax = ax
    
    def setay(self, ay):
        self._ay = ay


