import pandas as pd
new_data = pd.read_excel("D:\Car_sales.xlsx", sheet_name="car")

# distinct count and group by sum
new_data["Manufacturer"].count()
# or
new_data.Manufacturer.count()
new_data.Manufacturer.size()
new_data.Manufacturer.nunique() #distinct count
# *****************************************************************************************************************************
n1=new_data.groupby(by=["Manufacturer"])
n1= new_data.groupby(by=["Manufacturer", "Model"])
# Or
# n1 = new_data.groupby(["Manufacturer","Latest_Launch" ])
n2 = new_data.groupby(["Manufacturer" ])

# * operations *****************after creating the group*****************************************************************************
n2 = new_data.groupby(["Manufacturer","Latest_Launch" ])
n3= n2[["Manufacturer","__year_resale_value","Sales_in_thousands"]].sum()
# addding count
n3["Manufacturer_count"] = n2.Manufacturer.size()
## adding Power_perf_factor mean
n3["Power_perf_factor"] = n2.Power_perf_factor.mean()
n3