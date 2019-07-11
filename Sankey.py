# TODO Provide a user selectable date range
# TODO Determine if amount is income or not
# TODO create two dataframes, one for income and one for spending (later extend to all spending groups)
# TODO Sum amounts in new dataframes according to Category (https://www.shanelynn.ie/summarising-aggregation-and-grouping-data-in-python-pandas/)  shows how to use groupby() command
# TODO use summed amounts to make a list to input into the Sankey code for the links
# TODO figure out how to make labels for the Sankey

import pandas as pd
import plotly
import plotly.graph_objs as go


def createItems(d, uniqueGroups):

    # Each category is now stored in a dict where each dict name is given by: 'Category_categoryName'
    categories = {}

    for uniqueCategory in uniqueGroups:
        isUniqueCategory = d['Spending Group'] == uniqueCategory
        categoryName = uniqueCategory
        categories['{}'.format(categoryName)] = d[isUniqueCategory]

    return categories


def sumAmounts(categories):

    sumCategories = {}
    categoryNames = categories.keys()

    # Categories is a dict, so extracting the category names and data with this for loop
    for category, data in categories.items():  
        specifiedCategory = data.groupby('Category')['Amount'].sum()
        sumCategories['{}'.format(category)] = specifiedCategory

    # This changes the dataframe to a series

    return sumCategories


def printCategories(incomeCategories, expenseCategories, recurringCategories, investmentCategories):
    print('Income')
    print(incomeCategories)

    print('Expenses')
    print(expenseCategories)

    print('Recurring Expenses')
    print(recurringCategories)

    print('Investments')
    print(investmentCategories)
    return

# Read in csv from 22Seven
d = pd.read_csv('my_transactions.csv')

# Relevant columns (remove unneeded columns)
d = d.drop(["Date", "Original Transaction Description", "My Transaction Description", "Account", "Notes", "Pay month", "Split Transaction"], axis=1)

# Create list of the different spending groups (these can be created by the user beforehand)
uniqueGroups = list(d['Spending Group'].unique())



# Create dataframes for each category
# Using a dict to store the different categories
categories = {}
categories = createItems(d, uniqueGroups)

# Get the sum of the amounts per category
summedCategories = sumAmounts(categories)


incomeCategories = (summedCategories['Income'])

# Create list of the different spending categories (these can be created by the user beforehand)
categories = incomeCategories.keys()

# make source, target, amount and label lists for the sankey diagram 
# SECTION 1: Income to middle
sankey_source = list(range(0, len(incomeCategories)))

sankey_amount = []
sankey_target = []
sankey_label = []
sankey_colour = []
for i in range(0, len(incomeCategories)):
    # print(incomeCategories[i])
    sankey_label.append(categories[i])
    sankey_amount.append(incomeCategories[i])
    sankey_target.append(len(incomeCategories))
    sankey_colour.append("blue")

sankey_label.append('Middle')
sankey_colour.append("green")

# print(sankey_source)
#  Repeat for outgoing groups

# SECTION 2: Middle to spending groups

otherCategories = list(summedCategories.keys())
otherCategories.remove('Income')
otherCategories.remove('Transfer')
otherCategories.remove('Invest-save-repay')

targetCounter = len(incomeCategories)+1


# make source, target, amount and label lists for the sankey diagram 
#  Loop through the spending groups
for i in range(0, len(otherCategories)):
    print(otherCategories[i])

    sankey_source.append(len(incomeCategories))
    sankey_label.append(otherCategories[i])
    sankey_amount.append(-sum(summedCategories[otherCategories[i]]))
    sankey_target.append(targetCounter)
    sankey_colour.append("blue")

    # SECTION 3: Spending groups to categories within each spending group
    sankeyCategories = (summedCategories[otherCategories[i]])
    categories = summedCategories[otherCategories[i]].keys()

    sourceCounter = targetCounter
    targetCounter = targetCounter + 1

    for k in range(0, len(sankeyCategories)):
      print(sankeyCategories[i])

      sankey_source.append(sourceCounter)
      sankey_label.append(categories[k])
      sankey_amount.append(-sankeyCategories[k])
      sankey_target.append(targetCounter)
      targetCounter = targetCounter +1
      sankey_colour.append("yellow")




    

# Sample Sankey example for plotly adapted for income only
data = dict(
    type='sankey',
    node=dict(
      pad=15,
      thickness = 20,
      line = dict(
        color = "black",
        width = 0.5
      ),
      label = sankey_label,
      color = sankey_colour
    ),
    link = dict(
      source = sankey_source,
      target = sankey_target,
      value = sankey_amount
  ))

layout =  dict(
    title = "Basic Sankey Diagram of just incomes",
    font = dict(
      size = 10
    )
)

fig = dict(data=[data], layout=layout)
plotly.offline.plot(fig, validate=False, filename="SankeyIncomeOutput.html")



# #  Repeat for outgoing expenses

# otherCategories = list(summedCategories.keys())
# otherCategories.remove('Income')
# otherCategories.remove('Transfer')

# sankeyCategories = (summedCategories[otherCategories[2]])

# # Create list of the different spending categories (these can be created by the user beforehand)
# categories = sankeyCategories.keys()

# # make source, target, amount and label lists for the sankey diagram 
# sankey_source = []

# sankey_amount = []
# sankey_target = []
# sankey_label = ["middle"]
# sankey_colour = ["red"]
# for i in range(0, len(sankeyCategories)):
#     print(sankeyCategories[i])

#     sankey_source.append(0)
#     sankey_label.append(categories[i])
#     sankey_amount.append(-sankeyCategories[i])
#     sankey_target.append(i+1)
#     sankey_colour.append("blue")

    
# # Sample Sankey example for plotly adapted for income only
# data = dict(
#     type='sankey',
#     node=dict(
#       pad=15,
#       thickness = 20,
#       line = dict(
#         color = "black",
#         width = 0.5
#       ),
#       label = sankey_label,
#       color = sankey_colour
#     ),
#     link = dict(
#       source = sankey_source,
#       target = sankey_target,
#       value = sankey_amount
#   ))

# layout =  dict(
#     title = "Basic Sankey Diagram of just one spending category",
#     font = dict(
#       size = 10
#     )
# )

# fig = dict(data=[data], layout=layout)
# plotly.offline.plot(fig, validate=False, filename="SankeySpendingOutput.html")
