import pandas as pd
import numpy as np
data = {
    'ord_no': [70001.0,np.nan,70002.0,70004,np.nan,70005,np.nan,70010,70003,70012,np.nan,70013],
    'purch_amt': [150.5,270.65,65.26,110.5,948.5,2400.6,5760,1983.43,2480.4,250.45,75.29,3045.6],
    'ordr_date': ["2012-10-05","2012-10-06",np.nan,"2012-10-07","2012-10-08","2012-10-09","2012-10-22","2012-10-10","2012-10-15","2012-10-21","2012-10-16","2012-10-30"],
    'cust_id': [3002,3001,3001,3003,3002,3001,3001,3004,3003,3002,3001,3001],
    'sales_id': [5002,5003,5001,np.nan,5002,5001,5001,np.nan,5003,5002,5003,np.nan]
}
df = pd.DataFrame(data)
missing_values = df.isna()
print("Missing values (True indicates a missing value):")
print(missing_values)
