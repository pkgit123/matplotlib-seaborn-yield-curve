# ==================================================
# Filename:     scrape-yield-curve-gca-version.py
# Description:  Re-write the code to use plt.gca() rather than ax
# ==================================================

import pandas as pd

pd.set_option("display.max_columns", 999)

%matplotlib inline

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as md

import seaborn as sns

print('Seaborn version: ', sns.__version__)

import matplotlib.dates as md
import matplotlib.dates as mdates

# Scrape treasury yield curve
str_year = '2018'
str_yield = f'https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value={str_year}'

df_yield_curve = pd.read_html(str_yield)[0]

# convert date from str
df_yield_curve['Date'] = pd.to_datetime(df_yield_curve['Date'], format = '%m/%d/%Y')

print(f'Dataframe shape: {df_yield_curve.shape} \n')
print(f'Dataframe columns: {df_yield_curve.columns} \n')

df_yield_curve.head()

# select subset of columns
ls_cols_select = ['Date', '2 Yr', '5 Yr', '10 Yr', '30 Yr']

# create new dataframe with select columns
df_yield_curve_select = df_yield_curve[ls_cols_select]
df_yield_curve_select = df_yield_curve_select.set_index('Date')

print(f'Dataframe shape: {df_yield_curve_select.shape} \n')
print(f'Dataframe columns: {df_yield_curve_select.columns} \n')

df_yield_curve_select.head()

# ==================================================================================================
# Line plot, including adjusting x-axis density
# https://stackoverflow.com/questions/63218645/lowering-the-x-axis-value-density-for-dates-on-a-seaborn-line-plot-updated
# Matplotlib x-axis density. https://stackoverflow.com/questions/13052844/matplotlib-how-to-decrease-density-of-tick-labels-in-subplots
# Matplotlib x-axis formatting. https://stackoverflow.com/questions/9627686/plotting-dates-on-the-x-axis-with-pythons-matplotlib
# ==================================================================================================

data=df_yield_curve_select


fig, ax = plt.subplots(figsize = (8, 5))

sns.lineplot(ax = ax, data=data)

# set x-axis formatting
interval=1
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(bymonthday = interval))


# put a title
plt.title(f"`Treasury yields in Year: {str_year}`")

# Rotates X-Axis Ticks by 90-degrees
plt.xticks(rotation = 90) 

# Put the legend out of the figure
plt.legend(title=f"Legend: Term", bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)



def visualize_year_rates(str_year):
    '''
    Visualize Treasury interest rates from a single year.
    '''
    
    # Scrape treasury yield curve
    str_yield = f'https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value={str_year}'
    df_yield_curve = pd.read_html(str_yield)[0]
    
    # convert date from str
    df_yield_curve['Date'] = pd.to_datetime(df_yield_curve['Date'], format = '%m/%d/%Y')
    
    # select subset of columns
    ls_cols_select = ['Date', '2 Yr', '5 Yr', '10 Yr', '30 Yr']

    # create new dataframe with select columns
    df_yield_curve_select = df_yield_curve[ls_cols_select]
    df_yield_curve_select = df_yield_curve_select.set_index('Date')
    
    print(str_year)
    print(df_yield_curve.shape)
    print(df_yield_curve_select.shape)
    
    # ==================================================================================================
    # Line plot, including adjusting x-axis density
    # https://stackoverflow.com/questions/63218645/lowering-the-x-axis-value-density-for-dates-on-a-seaborn-line-plot-updated
    # ==================================================================================================
    
    try:
        
        fig, ax = plt.subplots(figsize = (8, 5))

        sns.lineplot(ax = ax, data=df_yield_curve_select)

        # set x-axis formatting
        interval=1
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        plt.gca().xaxis.set_major_locator(mdates.MonthLocator(bymonthday = interval))

        # put a title
        plt.title(f"Treasury Yields in Year: `{str_year}`")

        # Rotates X-Axis Ticks by 90-degrees
        plt.xticks(rotation = 90) 

        # Put the legend out of the figure
        plt.legend(title=f"Legend: Term", bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

        plt.show()
        print()
        
    except:
        print(f'Error visualizing year: {str_year}')
    
    return df_yield_curve
  
  
  
_ = visualize_year_rates('2018')
_ = visualize_year_rates('2019')
_ = visualize_year_rates('2020')
_ = visualize_year_rates('2021')
_ = visualize_year_rates('2022')
