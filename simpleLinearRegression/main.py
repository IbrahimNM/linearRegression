from LinearRegression import LinearRegression

x = [1,2,3,4,5,6,7,8]
y = [11,22,33,44,55,66,77,88]


current = LinearRegression(x, y)
print current
print 'Summation of x: ', current.getSummation(x)
print 'Summation of y: ', current.getSummation(y)
print 'Number of digits in x:', current.getCount(x)
print 'Number of digits in y:', current.getCount(y)
print 'Mean of x: ', current.getMean(x)
print 'Mean of y: ', current.getMean(y)
print 'xDiff (x - x\'): ', current.getDiff(x)
print 'yDiff: (y - y\')', current.getDiff(y)
print 'StandardDiff of x: ', current.getStandardDeviation(x)
print 'StandardDiff of y: ', current.getStandardDeviation(y)
print 'Product of (x - x\')*(y - y\'): ', current.getProduct(
    current.getDiff(x), current.getDiff(y))
print 'Y: ', current.getYintercept()
print 'Slope: ', current.getSlope()
func = current.getLinearRegressionFunction()
print 'Function: ', current.getLinearRegressionFunction()
print 'f(15): ', func(15)
print 'X: ', current.getX()
print 'Y: ', current.getY()
