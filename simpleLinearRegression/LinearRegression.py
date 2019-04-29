

class LinearRegression(object):
    
    def __init__(self, independentVariable, dependentVariable):
        self.__x = independentVariable
        self.__y = dependentVariable
        self.__slope = self.getSlope()
        self.__yIntercept = self.getYintercept()
    
    def getLinearRegressionFunction(self):
        ''' return: y(x) = a + bx '''
        return lambda x: self.__yIntercept + self.__slope * x

    def getSlope(self):
        ''' return slope: b = r * (Sy/Sx) '''
        return 0
    def getYintercept(self):
        ''' return Yintercept: a = y' - bx' '''
        return self.getMean(self.__y) - (self.getSlope() * self.getMean(self.__x))
    
    def getPearsonCorrelationCoefficient(self):
        ''' r = sum((x-x')(y-y')) / sqrt(sum(x-x')^2 * sum(y-y')^2) '''
        return 0
    
    def getStandardDeviation(self, count, summation):
        ''' Sx = sqrt(sum(x-x')^2 / n-1) '''
        return 0

    def getMean(self, column):
        return 0
    
    def getCount(self, column):
        return 0
    
    def getSummation(self, column):
        return 0