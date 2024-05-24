from hypothesis_testing import *
from PearsonsR import *

def test(sample, population):
    return reject(t_test(len(sample), 0.05, 2), test_stat(sample, population))

numFatalFed = [65,34,49,31,116,97,76,63,63,48,536,84,114,82,194,88,19,161,14,19,218,146,101,202,92,14,36,8,44]
numFatalSt = [35,31,97,91,39,115,149,101,42,63,146,11,137,20,39,43,72,70,60,375,67]
rateFatalFed = [17.7,7.3,6.9,6.7,6.4,6.1,5.7,5.5,5.4,5.2,4.8,4.3,4,3.5,3.4,3.3,3.2,3.1,3.1,2.7,2.7,2.5,2.5,2.4,2.4,2.2,2.1,1.7,1.4]
rateFatalSt = [12.2,8.9,6.6,4.9,4.8,4.2,3.8,3.8,3.6,3.5,3.5,3.5,3.4,3.4,3,2.6,2.6,2.6,2.3,2.3,2.2]
numInjFed = [13300,19800,30600,39000,33400,26600,24300,203200,41200,72900,155300,60300,21200,113600,7900,124900,74800,146300,80900,43800,69700]
numInjSt = [6500,9700,45600,48900,19900,77900,66200,65100,32400,36200,75900,9900,105500,13700,27700,42900,51900,67500,54400,345400,89300]
rateInjFed = [5,4.1,2.3,3.6,3.6,3.2,3.9,2.7,3.3,4,3.9,3.3,5.6,3.2,2.8,3.2,2.8,2.5,3.1,3.9,3.1]
rateInjSt = [3.5,4.6,4.5,4.1,3.9,3.9,2.7,3.5,4.1,3,2.9,5,4,3.8,3.4,3.9,3.1,3.8,3.2,3.5,4.8]

#print("Reject number of fatalities: " + str(test(numFatalSt, numFatalFed)))
#print("Reject rate of fatalities: " + str(test(rateFatalSt, rateFatalFed)))
#print("Reject number of injuries: " + str(test(numInjSt, numInjFed)))
#print("Reject rate of injuries: " + str(test(rateInjSt, rateInjFed)))

yearsInspect = [31, 45, 49, 50, 57, 58, 60, 68, 79, 80, 81, 82, 82, 94, 98, 101, 103, 104, 104, 107, 108, 108, 110, 111, 111, 112, 112, 118, 119, 122, 123, 123, 124, 125, 126, 128, 131, 135, 136, 137, 138, 173, 175, 179, 184, 191, 206, 237, 238, 521]
rateFatal = [2.6, 3.4, 3.6, 2.2, 2.6, 8.9, 3.5, 3.5, 3.4, 3.2, 3, 3.8, 3.8, 4.3, 6.6, 12.2, 1.7, 4, 4.2, 2.1, 2.7, 2.6, 5.7, 17.7, 3.5, 5.5, 3.1, 3.3, 2.2, 3.5, 2.4, 1.4, 4.9, 3.4, 2.3, 5.2, 6.1, 7.3, 4.8, 2.5, 2.5, 6.9, 3.1, 2.3, 2.4, 4.8, 6.4, 5.4, 2.7, 6.7]
numInspectors = [75,63,44,111,58,11,104,9,20,8,22,48,30,24,26,9,7,36,39,24,9,48,16,8,24,14,53,26,7,28,67,33,39,57,30,9,19,7,98,74,49,7,5,216,105,9,16,9,60]
popByInspectors = [51986.68,157097.5397,62363.54545,62135.65766,92700.74138,66403.90909,93744.96154,69565.55556,69740.2,165966.125,129698.8636,170522.5,215129.9333,200649.5,118315,64033.88889,150660.1429,158887.7778,167633.4103,149772.7917,177258.2222,122645.6667,180328.5625,87647,196556.4167,213129.7143,217904.2075,231706.4231,189176,185451.6786,132014.0597,201909.2424,112470.4103,223984.5263,218499.2667,205922.5556,200990.2105,143397.5714,266168.1735,174087.973,202070,265267.4286,183035.8,175688.8889,186408.8762,231923.2222,287560.75,328018.2222,321630.3667]
rateFatal2 = [2.6, 3.4, 3.6, 2.2, 2.6, 8.9, 3.5, 3.5, 3.4, 3.2, 3, 3.8, 3.8, 4.3, 6.6, 12.2, 1.7, 4, 4.2, 2.1, 2.7, 2.6, 5.7, 17.7, 3.5, 5.5, 3.1, 3.3, 2.2, 3.5, 2.4, 1.4, 4.9, 3.4, 2.3, 5.2, 6.1, 7.3, 4.8, 2.5, 2.5, 6.9, 3.1, 2.3, 2.4, 4.8, 6.4, 5.4, 2.7]
yearsInspect2 = [31, 45, 49, 50, 57, 58, 60, 68, 79, 80, 81, 82, 82, 94, 98, 101, 103, 104, 104, 107, 108, 108, 110, 111, 111, 112, 112, 118, 119, 122, 123, 123, 124, 125, 126, 128, 131, 135, 136, 137, 138, 173, 175, 179, 184, 191, 206, 237, 238]

#pearsonsR(x, y)
#r = 0.12232858307027374
#print("Pearsons R for years v rate: " + str(pearsonsR(yearsInspect, rateFatal)))

#r = 0.76312840475276
#print("Pearsons R for years v num of inspectors: " + str(pearsonsR(popByInspectors, yearsInspect)))

#r = -0.15469112002936752
#print("Pearsons R for rate v num of inspectors: " + str(pearsonsR(popByInspectors, rateFatal2)))

numFatal = [43,137,42,67,70,31,146,11,20,19,39,149,101,84,97,35,8,114,115,36,19,72,76,65,63,63,161,88,14,82,92,44,91,194,60,48,97,34,536,146,101,49,14,375,202,39,116,63,218,31]
rateInj = [3.9,4,4.1,4.8,3.8,4.6,2.9,5,3.8,5.6,3.4,2.7,3.5,3.3,4.5,3.5,4,3.9,3.9,3.1,3.6,3,3.2,3.3,3.1,3.1,4.1,3.9,3.2,3.9,3.6,5,2.7,3.2,2.8,4.1,2.8,3.5,2.5,3.9,2.3,3.2]
numInj = [42900,105500,32400,89300,67500,9700,75900,9900,13700,21200,27700,66200,65100,41200,45600,6500,72900,77900,43800,51900,33400,36200,113600,60300,80900,69700,48900,155300,54400,24300,39000,13300,203200,124900,74800,19800,7900,345400,146300,19900,3060,26600]
penaltiesInj = [363,542,2133,791,768,889,996,1008,964,2083,1053,726,727,1803,790,1777,2207,1054,1735,685,1971,492,2156,1931,2151,1929,3254,1916,891,2565,1872,1983,2187,1876,2061,1798,2406,6422,2016,998,1765,2569]
penaltiesFatal = [363,542,2133,791,768,889,996,1008,964,2083,1053,726,727,1803,790,1777,2023,2207,1054,1735,1449,685,1971,3045,492,1515,2156,1931,2243,1649,2151,1929,3254,1916,891,2565,1872,1983,2187,1876,2061,1798,2406,6422,2016,998,1765,2569,1821,2346]

#r = 0.12412747181729103
print("Pearsons R for fatal rate v penalties: " + str(pearsonsR(rateFatal, penaltiesFatal)))

#r = -0.08697389849178325
print("Pearsons R for inj rate v penalties: " + str(pearsonsR(rateInj, penaltiesInj)))

#r = 0.3668455170303696
print("Pearsons R for fatal num v penalties: " + str(pearsonsR(numFatal, penaltiesFatal)))

#r = 0.5608114855541665
print("Pearsons R for inj num v penalties: " + str(pearsonsR(numInj, penaltiesInj)))