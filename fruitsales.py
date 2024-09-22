# add your code here
import pandas as pd

fruit_sales = pd.DataFrame({'Apples': [35, 21],
                            'Bananas': [41, 34]},
                          index=['2017 Sales', '2018 Sales'])
fruit_sales.to_csv("fruit.csv")
