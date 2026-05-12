from data_T1 import _all_payLoads
import numpy as np
data_1, data_2, data_3, data_4, data_5 = _all_payLoads

#Write your code here and print the results
#T1.1
image1 = data_1.astype(np.uint16)
image2 = data_2.astype(np.uint16)
result_1 = (image1 + image2) / 2.0
print("result_1: ")
print(result_1)
#T1.2
total_loss = np.float64(data_3)
record = np.float64(0.0)
for update in data_4:
    y = np.float64(update) - record
    t = total_loss + y
    record = (t - total_loss) - y
    total_loss = t
print("\nresult_2 :")
print(total_loss)
#T1.3
x = np.float64(data_5)
result_3 = 2.0 * (np.sin(x / 2.0) ** 2) / (x ** 2)
print("\nresult_3 :")
print(result_3)
