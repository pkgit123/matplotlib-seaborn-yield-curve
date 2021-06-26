import pandas as pd

pd.set_option("display.max_columns", 999)

%matplotlib inline

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as md

import seaborn as sns

print('Seaborn version: ', sns.__version__)


%%time

# Scrape treasury yield curve
str_year = '2018'
str_yield = f'https://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/TextView.aspx?data=yieldYear&year={str_year}'    # Year
df_yield_curve = pd.read_html(str_yield)[1]

# convert date from str
df_yield_curve['Date'] = pd.to_datetime(df_yield_curve['Date'], format = '%m/%d/%y')

print(f'Dataframe shape: {df_yield_curve.shape} \n')
print(f'Dataframe columns: {df_yield_curve.columns} \n')

df_yield_curve.head()


# select subset of columns
ls_cols_select = ['Date', '2 yr', '5 yr', '10 yr', '30 yr']

# create new dataframe with select columns
df_yield_curve_select = df_yield_curve[ls_cols_select]
df_yield_curve_select = df_yield_curve_select.set_index('Date')

print(f'Dataframe shape: {df_yield_curve_select.shape} \n')
print(f'Dataframe columns: {df_yield_curve_select.columns} \n')

df_yield_curve_select.head()


# ==================================================================================================
# Line plot, including adjusting x-axis density
# https://stackoverflow.com/questions/63218645/lowering-the-x-axis-value-density-for-dates-on-a-seaborn-line-plot-updated
# ==================================================================================================

fig, ax = plt.subplots(figsize = (8, 5))

sns.lineplot(ax = ax, data=df_yield_curve_select)

# specify the position of the major ticks 
ax.xaxis.set_major_locator(md.MonthLocator(bymonthday = 1))
# specify the format of the labels as 'year-month-day'
ax.xaxis.set_major_formatter(md.DateFormatter('%Y-%m-%d'))
# (optional) rotate by 90° the labels in order to improve their spacing
plt.setp(ax.xaxis.get_majorticklabels(), rotation = 90)

# put a title
plt.title(f"`Treasury yields in Year: {str_year}`")

# Rotates X-Axis Ticks by 90-degrees
plt.xticks(rotation = 90) 

# Put the legend out of the figure
plt.legend(title=f"Legend: Term", bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

plt.show()
print()
