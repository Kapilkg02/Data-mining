import pandas as pd
new_data = pd.read_excel("D:\Car_sales.xlsx", sheet_name="car")

##*******************************************************************************************************
# adding a new column as flag of  yes or not , 1 or 0

import numpy as np

n3["H_sale"] = np.where(n3.Sales_in_thousands > 15 , 1 ,0)
n3["S_flag"] = np.where(n3.Sales_in_thousands > 15 , "yes" ,"No")
n3
#multiple condition ;

n3["high_sale"] = np.where((n3.Sales_in_thousands > 15) & (n3.Manufacturer == "Audi") , 1 ,0)
n3["sale_flag"] = np.where((n3.Sales_in_thousands > 15 ) | (n3.dist >.65), "yes" ,"No")
n3

# multiple where condition or nested condition
n3["t1"] = np.where(n3.Sales_in_thousands <2 , "too low",
                   np.where(n3.Sales_in_thousands < 6 ,"low" ,
                           np.where(n3.Sales_in_thousands < 10, "Good",
                                   np.where(n3.Sales_in_thousands < 16, "high", "very high"))))
n3
