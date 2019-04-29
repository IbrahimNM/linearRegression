from LinearRegression import LinearRegression

x = [17,13,12,15,16,14,16,16,18,19]
y = [94,73,59,80,93,85,66,79,77,91]
current = LinearRegression(x,y)
print current
print 'Summation: ', current.getSummation(x)
print 'Count:', current.getCount(x)
print 'Mean: ', current.getMean(x)
print 'xDiff: ', current.getDiff(x)
print 'yDiff: ', current.getDiff(y)
