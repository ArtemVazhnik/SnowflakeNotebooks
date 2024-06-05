# The Snowpark package is required for Python Worksheets. 
# You can add more packages by selecting them using the Packages control and then importing them.

import snowflake.snowpark as snowpark
from snowflake.snowpark.functions import col
import pandas as pd
import matplotlib.pyplot as plt

def main(session: snowpark.Session): 
    # Your code goes here, inside the "main" handler.
    tableName = 'TEMP.HOME_SALES.HOME_SALES'
    dataframe = session.table(tableName)#.filter(col("language") == 'python')

    df = dataframe.to_pandas()

    # Print a sample of the dataframe to standard output.
    # dataframe.show()

    # # return df
    # plt.figure(figsize=(30, 5))
    # ax = df.plot(kind='bar')
    # plt.title('First click position (pos == -1 means no clicks)')
    # plt.xlabel('Position')
    # plt.ylabel('Percent')
    # plt.xticks(rotation=0)
    # plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # # Добавление подписей над столбцами
    # for i in ax.patches:
    #     ax.text(i.get_x() + i.get_width() / 2, i.get_height() + 0.5, 
    #             '{:.1f}%'.format(i.get_height()), ha='center', va='bottom')
    
    # plt.show()
    return dataframe
