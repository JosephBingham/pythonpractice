
data = input()
sum = 0
for i in xrange(0,len(data)):
	sum += data(i)

mean = (1.0/len(data)) * sum

newsum = 0
for i in xrange(0,len(data)):
	newsum += (data(i) - mean)**2

s = ((1.0/len(data)-1)*newsum)**.5


median = data(len(data)/2) if len(data)%2 == 0 else .5*(data(len(data)/2)+data(len(data)+1))
newdata = []
#mad = median(abs(data(i) - median(data))
for i in xrange(0, len(data)):
	newdata.add(data(i) - median)
median = newdata(len(newdata)/2) if len(newdata)%2 == 0 else .5*(newdata(len(newdata)/2)+newdata(len(newdata)+1))

