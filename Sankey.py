import pandas as pd
import plotly
import plotly.graph_objs as go

def createItems(d):
    # Creating new dataframe for income items
  isIncome = d['Spending Group']=="Income"
  income = d[isIncome]

  # Creating new dataframe for Day-to-day items
  isExpense = d['Spending Group']=='Day-to-day'
  expense = d[isExpense]

  # Creating new dataframe for recurring items
  isRecurring = d['Spending Group']=='Recurring'
  recurring = d[isRecurring]

  # Creating new dataframe for recurring items
  isInvestment = d['Spending Group']=='Investments'
  investment = d[isInvestment]
  return income, expense, recurring, investment

def sumAmounts(income, expense, recurring, investment):
  incomeCategories = income.groupby('Category')['Amount'].sum()
  expenseCategories = expense.groupby('Category')['Amount'].sum()
  recurringCategories = recurring.groupby('Category')['Amount'].sum()
  investmentCategories = investment.groupby('Category')['Amount'].sum()

  return incomeCategories, expenseCategories, recurringCategories, investmentCategories

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

# Create dataframes for items
income, expense, recurring, investment = createItems(d)

# Get the sum of the amounts per category
incomeCategories, expenseCategories, recurringCategories, investmentCategories = sumAmounts(income, expense, recurring, investment)

printCategories(incomeCategories, expenseCategories, recurringCategories, investmentCategories)

# Get the unique categories
categories = income.Category.unique()

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