from LinearRegression import LinearRegression

x = [1400, 1600, 1700, 1875, 1100, 1550, 2350, 2450, 1425, 1700]
y = [245,312,279,308,199,219,405,324,319,255]
current = LinearRegression(x,y)
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
print 'Product of (x - x\')*(y - y\'): ', current.getProduct(current.getDiff(x), current.getDiff(y))
print 'Y: ', current.getYintercept()
print 'Slope: ', current.getSlope() 
func = current.getLinearRegressionFunction()
print 'Function: ', current.getLinearRegressionFunction()
print 'f(15): ', func(15)
print 'X: ', current.getX()
print 'Y: ', current.getY()