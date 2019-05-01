import math


class LinearRegression(object):

    def __init__(self, independentVariable, dependentVariable):
        self.__x = independentVariable
        self.__y = dependentVariable

    def getLinearRegressionFunction(self):
        ''' return: y(x) = a + bx '''
        return lambda x: self.getYintercept() + self.getSlope() * x

    def getSlope(self):
        ''' return slope: b = r * (Sy/Sx) '''
        return self.getPearsonCorrelationCoefficient() * (self.getStandardDeviation(self.__y) / self.getStandardDeviation(self.__x))

    def getYintercept(self):
        ''' return Yintercept: a = y' - bx' '''
        return self.getMean(self.__y) - (self.getSlope() * self.getMean(self.__x))

    def getPearsonCorrelationCoefficient(self):
        ''' r = sum((x-x')(y-y')) / sqrt(sum(x-x')^2 * sum(y-y')^2) '''
        numerator = self.getSummation(
            self.getProduct(self.getDiff(self.__x), self.getDiff(self.__y)))
        denominator = math.sqrt(self.getSquaredSum(
            self.getDiff(self.__x)) * self.getSquaredSum(self.getDiff(self.__y)))
        return numerator / denominator

    def getStandardDeviation(self, arr):
        ''' return: Sx = sqrt(sum(x-x')^2 / n-1) '''
        value = self.getDiff(arr)
        squaredSum = self.getSquaredSum(value)
        return math.sqrt(squaredSum / (self.getCount(arr) - 1))

    def getMean(self, column):
        ''' Find mean value of an array '''
        return self.getSummation(column) / self.getCount(column)

    '''
        TODO: Evaluate and add the estimated error for the linear-regression equation
            Standard error = sqrt(sum(y^ - y)^2 / n - 2)
    '''

    def getCount(self, column):
        ''' return: # of elements. return length of x[] if x[] length is not greater than y[] length'''
        return len(self.__x) if len(self.__y) >= len(self.__x) else len(self.__y)

    def getSummation(self, column):
        ''' Sums all elements '''
        return math.fsum(column)

    def getDiff(self, column):
        ''' return: (x - x') as an array, and round its values to 2-decimals '''
        sum = []
        mean = self.getMean(column)
        for d in column:
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

    def setX(self, newX):
        ''' Set new value for X '''
        self.__x = newX

    def setY(self, newY):
        ''' Set new value for Y '''
        self.__y = newY

    def getX(self):
        ''' Return the value of X '''
        return self.__x

    def getY(self):
        ''' Return the value of Y '''
        return self.__y
