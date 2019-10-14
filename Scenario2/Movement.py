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
        return "(%s, %s)" % (self.x, self.y)

    def toTuple(self):
        '''Returns the vector as a tuple'''
        return (self.x, self.y)

    @staticmethod
    def degreeToRad(degree):
        # Function to convert degrees to radians
        return degree * math.pi / 180.0

    @staticmethod
    def radianToDeg(radian):
        # Convert Radians to degrees
        return radian * 180.0 / math.pi

    @staticmethod
    def move(P1, P2):
        # create a movement object
        return movement(P2[0] - P1[0], P2[1] - P1[1])

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def magnitudeSquared(self):
        return self.x ** 2 + self.y ** 2

    def normalize(self):
        # Convert vector to a unit vector
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

    def xComponent(self):
        # Returns x component of input
        return movement(self.x, 0)

    def yComponent(self):
        # Returns y component of input
        return movement(0, self.y)

    def rhnorm(self):
        # Returns the right hand normal
        return movement(self.y, -self.x)

    def lhnorm(self):
        # Returns the left hand normal
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
        return movement(self.x / scalar, self.y / scalar)

    def __eq__(self, other):
        '''Return True if other has same elements as self'''
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def getDistance(self, p):
        # Return distance to the point
        dx = self.x - p.x
        dy = self.y - p.y
        return math.sqrt(dx * dx + dy * dy)

    def dotProduct(self, rhs):
        # Returns the dot product
        return self.x * rhs.x + self.y * rhs.y

    def projection(self, vec):
        # Project the input vector onto itself
        dp = self.dotpro(vec)
        mag = self.magnitude()
        projx = (dp / mag ** 2) * self.x
        projy = (dp / mag ** 2) * self.y
        return movement(projx, projy)

    def angle(self, vec):
        # gets the angle between vectors
        anorm = self.normalize()
        bnorm = vec.normalize()
        dp = anorm.dotpro(bnorm)
        return math.acos(dp)

    def rotate(self, angle):
        rad = self.degreeToRad(angle)
        x = self.x * math.cos(rad) - self.y * math.sin(rad)
        y = self.x * math.sin(rad) + self.y * math.cos(rad)
        self.x = x
        self.y = y

    def crossproduct(self, vec):
        return self.x * vec.y - self.y * vec.x
