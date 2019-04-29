import math

class LinearRegression(object):
    
    def __init__(self, independentVariable, dependentVariable):
        self.__x = independentVariable
        self.__y = dependentVariable
        self.__xDiff = self.getDiff(self.__x)
        self.__yDiff = self.getDiff(self.__y)
        #self.__slope = self.getSlope()
        #self.__yIntercept = self.getYintercept()
    
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
        numerator = self.getSummation(self.getProduct(self.__xDiff, self.__yDiff))
        denominator = math.sqrt(self.getSquaredSum(self.__xDiff) * self.getSquaredSum(self.__yDiff)) 
        return numerator / denominator
    
    def getStandardDeviation(self, arr):
        ''' FIXME: Sx = sqrt(sum(x-x')^2 / n-1) '''
        value = self.getDiff(arr)
        squaredSum = self.getSquaredSum(value)
        return math.sqrt(squaredSum / (self.getCount(arr) - 1))

    def getMean(self, column):
        ''' Find mean value of an array '''
        return self.getSummation(column) / self.getCount(column)
    
    def getCount(self, column):
        ''' Get number of elements'''
        return len(column)
    
    def getSummation(self, column):
        ''' Sums all elements '''
        return math.fsum(column)

    def getDiff(self, column):
        ''' return: sum(x - x') as an array, and round it to decimals '''
        sum = []
        mean = self.getMean(column)
        for d in column:
            #  (x - x') for all elements, and append each to sum[]
            sum.append(round(d - mean, 2))
        return sum 

    def getSquaredSum(self, column):
        ''' Square each element, then sum them togather '''
        sum = 0
        for a in column:
            sum += math.pow(a, 2)
        return sum
    
    def getProduct(self, x, y):
        ''' Get product of the two arrays, and round it to 2-decimals '''
        product = []
        for a in range(self.getCount(x)):
            product.append(round(x[a] * y[a], 2))
        
        return product
