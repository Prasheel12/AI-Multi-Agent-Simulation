import math


class movement(object):
    def __init__(self, x=0.0, y=0.0):
        if isinstance(x, tuple) or isinstance(x, list):
            self.x = x[0]
            self.y = x[1]
        else:
            self.x = x
            self.y = y

    def __str__(self):
        return "(%s, %s)"%(self.x, self.y)

    #Tuple return from vector
    def toTuple(self):
        return (self.x, self.y)

    @staticmethod
    def deg_to_rad(degree):
        return degree * math.pi / 180.0

    @staticmethod
    def rad_to_deg(radian):
        return radian * 180.0 / math.pi

    @staticmethod
    def from_points(P1, P2):
        return movement(P2[0] - P1[0], P2[1] - P1[1])

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def magnitudeSquared(self):
        return self.x**2 + self.y**2

    #Vector is turned into unit vector
    def normalize(self):
        magnitude = self.magnitude()
        try:
            xnorm = self.x / magnitude
        except ZeroDivisionError:
            xnorm = 0.0
        try:
            ynorm = self.y / magnitude
        except ZeroDivisionError:
            ynorm = 0.0

        return movement(xnorm, ynorm)

    #Returns x vector
    def xcomp(self):
        return movement(self.x, 0)

    #Returns y component
    def ycomp(self):
        return movement(0, self.y)

    #Returns vector right hand normal to self
    def rhnorm(self):
        return movement(self.y, -self.x)

    #Returns vector left hand normal to self
    def lhnorm(self):
        return movement(-self.y, self.x)

    def __add__(self, rhs):
        return movement(self.x + rhs.x, self.y + rhs.y)

    def __sub__(self, rhs):
        return movement(self.x - rhs.x, self.y - rhs.y)

    def __neg__(self):
        return movement(-self.x, -self.y)

    def __mul__(self, scalar):
        return movement(self.x * scalar, self.y * scalar)

    def __div__(self, scalar):
        return movement(self.x /scalar, self.y / scalar)

    #Check to see if other has same elements as self
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

    #Gets distance to point
    def get_distance_to(self, p):
        dx = self.x - p.x
        dy = self.y - p.y
        return math.sqrt(dx*dx + dy*dy)

    #Returns dot product
    def dot(self, rhs):
        return self.x*rhs.x + self.y*rhs.y

    #Project input vector onto self
    def projection(self, vec):
        dp = self.dotpro(vec)
        mag = self.magnitude()
        projx = (dp / mag**2) * self.x
        projy = (dp / mag**2) * self.y
        return movement(projx, projy)

    #Get angle between input vector and self
    def angle(self, vec):
        anorm = self.normalize()
        bnorm = vec.normalize()
        dp = anorm.dotpro(bnorm)
        return math.acos(dp)

    #To rotate self
    def rotate(self, angle):
        rad = self.deg_to_rad(angle)
        x = self.x * math.cos(rad) - self.y * math.sin(rad)
        y = self.x * math.sin(rad) + self.y * math.cos(rad)
        self.x = x
        self.y = y

    #Get the cross product
    def crossproduct(self, vec):
        return self.x*vec.y - self.y*vec.x
