

class LinearRegression(object):
    
    def __init__(self, independentVariable, dependentVariable):
        self.__x = independentVariable
        self.__y = dependentVariable
        pass
    
    def getLinearRegressionFunction(self):
        ''' y(x) = a + bx '''
        return 0

    def getSlope(self):
        ''' b = r * (Sy/Sx) '''
        return 0
    
    def getYintercept(self):
        ''' a = y' - bx' '''
        return 0
    
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