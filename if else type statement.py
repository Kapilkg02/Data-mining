import pandas as pd
new_data = pd.read_excel("D:\Car_sales.xlsx", sheet_name="car")

# if else statement
# there are multiple ways to apply if else, i ll put only three efffective ways to do so.

import numpy as np
test1.head(10)
condition_list = [(test1.imp_cscore>=500)&(test1.imp_cscore<550),
                 (test1.imp_cscore>=550)&(test1.imp_cscore<650),
                 (test1.imp_cscore>=650)&(test1.imp_cscore<750),
                 (test1.imp_cscore==800)|(test1.imp_cscore>850)]
Choice_list = ["bad","ok","good","give_loan"]
test1["decision"] = np.select(condition_list,Choice_list,default = "on hold")
test1[:][test1.imp_cscore > 800]

# *******************************Via function***********************************************************

def scoring(n):
    if 500<=n<600: score = "bad"
    elif 600<=n<700: score = "good"
    elif 700<=n<800: score = "give loan"
    else: score = "on hold"
    return score

def scoring2(n):
    if 500<=n<600: score = test1.est_income/test1.hold_bal
    elif 600<=n<700: score = test1.RiskScore * test1.imp_crediteval
    elif 700<=n<800: score = test1.RiskScore + test1.hold_bal
    else: score = test1.hold_bal
    return score

test1["score1"] = test1.imp_cscore.apply(scoring)
test1[["score1","imp_cscore"]]

test2 = test1
test2["new_score"] = test1.imp_cscore.apply(scoring2)
test2[["score1","imp_cscore","new_score"]]


# *************************************where statement***************************************************
# multiple where condition or nested condition

import numpy as np
n3 = new_data
n3["t1"] = np.where(n3.Sales_in_thousands <2 , "too low",
                   np.where(n3.Sales_in_thousands < 6 ,"low" ,
                           np.where(n3.Sales_in_thousands < 10, "Good",
                                   np.where(n3.Sales_in_thousands < 16, "high", "very high"))))

n3["t2"] = np.where(n3.Sales_in_thousands <2 ,n3.__year_resale_value * 10,
                   np.where(n3.Sales_in_thousands < 6 ,n3.__year_resale_value * n3.Sales_in_thousands,
                           np.where(n3.Sales_in_thousands < 10, n3.__year_resale_value/100 ,
                                   np.where(n3.Sales_in_thousands < 16, n3.__year_resale_value+1500, n3.__year_resale_value/n3.Sales_in_thousands))))
n3[["Manufacturer" , "Sales_in_thousands" ,"__year_resale_value",  "t1" , "t2"]]
