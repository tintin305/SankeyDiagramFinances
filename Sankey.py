import pandas as pd
import plotly
import plotly.graph_objs as go


d = pd.read_csv('my_transactions.csv')

# Relevant columns
# d = d.drop(["Date","Original Transaction Description","My Transaction Description", "Account", "Notes", "Pay month", "Split Transaction"], axis=1)

# Creating new dataframe for income items
# isincome = d['Spending Group']=="Income"
# income = d[isincome]


# # Simple graph of transaction amounts over time
# plotly.offline.plot({
#     "data": [go.Scatter(x= d['Date'], y=d["Amount"])],
#     "layout": go.Layout(title="hello world")
# })


# Sample Sankey example for plotly
data = dict(
    type='sankey',
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(
        color = "black",
        width = 0.5
      ),
      label = ["A1", "A2", "B1", "B2", "C1", "C2"],
      color = ["blue", "blue", "blue", "blue", "blue", "blue"]
    ),
    link = dict(
      source = [0,1,0,2,3,3],
      target = [2,3,3,4,4,5],
      value = [8,4,2,8,4,2]
  ))

layout =  dict(
    title = "Basic Sankey Diagram",
    font = dict(
      size = 10
    )
)

fig = dict(data=[data], layout=layout)
plotly.offline.plot(fig, validate=False)


# print(d.head())

# data_trace = dict(
#     type='sankey',
#     domain = dict(
#       x =  [0,1],
#       y =  [0,1]
#     ),
#     orientation = "h",
#     valueformat = ".0f",
#     node = dict(
#       pad = 10,
#       thickness = 30,
#       line = dict(
#         color = "black",
#         width = 0.5
#       ),
#       label =  refugee_df['Category'].dropna(axis=0, how='any'),
#       color = refugee_df['Color']
#     ),
#     link = dict(
#       source = refugee_df['Source'].dropna(axis=0, how='any'),
#       target = refugee_df['Target'].dropna(axis=0, how='any'),
#       value = refugee_df['Value'].dropna(axis=0, how='any'),
#   )
# )

# layout =  dict(
#     title = "Refugee movement through Manus and Nauru, via <a href='http://www.bryanbrussee.com/sankey.html'>Bryan Brussee</a>",
#     height = 772,
#     width = 950,
#     font = dict(
#       size = 10
#     ),    
# )


# fig = dict(data=[data_trace], layout=layout)
# py.iplot(fig, validate=False)
