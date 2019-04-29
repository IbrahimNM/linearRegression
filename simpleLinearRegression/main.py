from LinearRegression import LinearRegression

x = [17,13,12,15,16,14,16,16,18,19]
y = [94,73,59,80,93,85,66,79,77,91]
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
