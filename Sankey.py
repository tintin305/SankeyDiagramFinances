import pandas as pd
import plotly
import plotly.graph_objs as go


d = pd.read_csv('my_transactions.csv')

# Simple graph of transaction amounts over time
# plotly.offline.plot({
#     "data": [go.Scatter(x= d['Date'], y=d["Amount"])],
#     "layout": go.Layout(title="hello world")
# }, filename= "simpleGraph.html")


# # Sample Sankey example for plotly
# data = dict(
#     type='sankey',
#     node = dict(
#       pad = 15,
#       thickness = 20,
#       line = dict(
#         color = "black",
#         width = 0.5
#       ),
#       label = ["A1", "A2", "B1", "B2", "C1", "C2"],
#       color = ["blue", "blue", "blue", "blue", "blue", "blue"]
#     ),
#     link = dict(
#       source = [0,1,0,2,3,3],
#       target = [2,3,3,4,4,5],
#       value = [8,4,2,8,4,2]
#   ))

# layout =  dict(
#     title = "Basic Sankey Diagram",
#     font = dict(
#       size = 10
#     )
# )

# fig = dict(data=[data], layout=layout)
# plotly.offline.plot(fig, validate=False, filename="SankeyOutput.html")

# Relevant columns
d = d.drop(["Date","Original Transaction Description","My Transaction Description", "Account", "Notes", "Pay month", "Split Transaction"], axis=1)
# print(d.head())

# print('\n' )
print(d.shape )




# Creating new dataframe for income items
isincome = d['Spending Group']=="Income"
income = d[isincome]
print(income.shape)
print(income.head())

# Get the sum of the amounts per category (within income)
incomeCategories = income.groupby('Category')['Amount'].sum()

print(incomeCategories.head())

sankey_source = list(income["Spending Group"])
sankey_target = list(income["Category"])
sankey_amount = list(income["Amount"])



# # Plan: 
# - Determine if amount is income or not
# - create two dataframes, one for income and one for spending (later extend to all spending groups)
# - Sum amounts in new dataframes according to Category (https://www.shanelynn.ie/summarising-aggregation-and-grouping-data-in-python-pandas/)  shows how to use groupby() command
# - use summed amounts to make a list to input into the Sankey code for the links
# - figure out how to make labels for the Sankey