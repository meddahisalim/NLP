import scipy
from scipy.stats import kstest,shapiro


print(scipy.__doc__)

m = 11 
std = 4.73

data = [5,8,9,15,18]

# for x in points:
#     cdf = norm.cdf(x ,loc=m, scale=std)
#     print(cdf)

# print(kstwo.cdf(0.95,5))


D , p_value = kstest(data,'norm',args=(m,std))
D1 , p_value1 = shapiro(data)
print(D)
print(p_value)
print(D1)
print(p_value1)
