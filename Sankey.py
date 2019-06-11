import pandas as pd
import plotly
import plotly.graph_objs as go

def createItems(d, uniqueCategories):

  categories = []

  for uniqueCategory in uniqueCategories:
    isUniqueCategory = d['Spending Group']==uniqueCategory
    categories.append(d[isUniqueCategory])

  return categories

def sumAmounts(categories):

  sumCategories = []

  for category in categories:
    specifiedCategory = category.groupby('Category')['Amount'].sum()
    sumCategories.append(specifiedCategory)

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

# Relevant columns
d = d.drop(["Date","Original Transaction Description","My Transaction Description", "Account", "Notes", "Pay month", "Split Transaction"], axis=1)

# Create list of the different categories (these can be created by the user beforehand)
uniqueCategories = list(d['Spending Group'].unique())

# These should not be hard coded like this. The system should pick up which categories are within the file. The user may have made their own categories and removed others.
# Create dataframes for items
categories = []
categories = createItems(d, uniqueCategories)


# Get the sum of the amounts per category
summedCategories = sumAmounts(categories)
print(summedCategories)


# Get the unique categories
# print(summedCategories[1]['Category'])
# categories = summedCategories['Category']
# print(categories)

# print(incomeCategories[categories[1]])

# make source, target, amount and label lists for the sankey diagram 
income_source =list(range(0, len(categories)))
print(income_source)


income_amount = []
income_target = []
income_label = []
income_colour = []
for i in range(0, len(categories)):
    # print(categories[i])
    income_label.append(categories[i])
    income_amount.append(incomeCategories[categories[i]])
    income_target.append(len(categories))
    income_colour.append("blue")


# print(income_source)
# print(income_amount)
# print(income_target)
# print(income_label)



# print(len(income_source))
# print(len(income_amount))
# print(len(income_target))
# print(len(income_label))


# Sample Sankey example for plotly adapted for income only
data = dict(
    type='sankey',
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(
        color = "black",
        width = 0.5
      ),
      label = income_label,
      color = income_colour
    ),
    link = dict(
      source = income_source,
      target = income_target,
      value = income_amount
  ))

layout =  dict(
    title = "Basic Sankey Diagram of just incomes",
    font = dict(
      size = 10
    )
)

fig = dict(data=[data], layout=layout)
plotly.offline.plot(fig, validate=False, filename="SankeyIncomeOutput.html")


# isExpenses = d['Spending Group']=="Day-to-day"
# expenses = d[isExpenses]


# pandasPrint(expenses.head())

# expensesCategories = expenses.groupby("Category")["Amount"].sum()

# pandasPrint(expensesCategories)


sankey_source = list(income["Spending Group"])
sankey_target = list(income["Category"])
sankey_amount = list(income["Amount"])



# # Plan: 
# - Determine if amount is income or not
# - create two dataframes, one for income and one for spending (later extend to all spending groups)
# - Sum amounts in new dataframes according to Category (https://www.shanelynn.ie/summarising-aggregation-and-grouping-data-in-python-pandas/)  shows how to use groupby() command
# - use summed amounts to make a list to input into the Sankey code for the links
# - figure out how to make labels for the Sankey