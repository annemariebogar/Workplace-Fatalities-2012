import statistics
import math

data = [110, 118, 125, 132, 140, 123, 129, 115, 128, 137, 119, 121, 126, 134, 131, 122, 135, 116, 133, 127, 130, 138, 114, 136, 124]
confidence_level = .95
n = len(data)
mean = statistics.mean(data)
standard_deviation = statistics.stdev(data)
standard_error = standard_deviation / math.sqrt(n)
alpha = 1-confidence_level
print("n = " + str(n))
print("mean = " + str(mean))
print("standard deviation = " + str(standard_deviation))
print("standard error = " + str(standard_error))
if n < 30:
    print("needs t-score with a degree of freedom of {} and half alpha of {:.3f}".format(n-1, alpha/2))
else:
    print("needs Z-score with half alpha of {:.3f}".format(n-1, alpha/2))
critical = 2.064
margin_error = critical * standard_error
print("margin of error = " + str(margin_error))
print("confidence interval = [" + str(mean - margin_error) + "] [" + str(mean + margin_error) + "]")
