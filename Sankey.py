# TODO Provide a user selectable date range
# TODO Determine if amount is income or not
# TODO create two dataframes, one for income and one for spending (later extend to all spending groups)
# TODO Sum amounts in new dataframes according to Category (https://www.shanelynn.ie/summarising-aggregation-and-grouping-data-in-python-pandas/)  shows how to use groupby() command
# TODO use summed amounts to make a list to input into the Sankey code for the links
# TODO figure out how to make labels for the Sankey

import pandas as pd
import plotly
import plotly.graph_objs as go
import datetime


def createItems(data, uniqueGroups):

    # Each category is now stored in a dict where each dict name is given by: 'Category_categoryName'
    categories = {}

    for uniqueCategory in uniqueGroups:
        isUniqueCategory = data['Spending Group'] == uniqueCategory
        categoryName = uniqueCategory
        categories['{}'.format(categoryName)] = data[isUniqueCategory]

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

    return None


def loadData():

    # Read in csv from 22Seven
    data = pd.read_csv('RawData/my_transactions.csv')

    # Format the 'Date' column as a datetime.
    data['Date'] = pd.to_datetime(data['Date'])

    return data


def generateSankey(data):

    # Relevant columns (remove unneeded columns)
    data.drop(["Date", "Original Transaction Description", "My Transaction Description", "Account", "Notes", "Pay month", "Split Transaction"], axis=1, inplace=True)

    # Create list of the different spending groups (these can be created by the user beforehand)
    uniqueGroups = list(data['Spending Group'].unique())



    # Create dataframes for each category
    # Using a dict to store the different categories
    categories = {}
    categories = createItems(data, uniqueGroups)

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


    return None

def extractDateRange(data, startDate, endDate):

    # Create the mask that will be the selected date range. (https://stackoverflow.com/questions/29370057/select-dataframe-rows-between-two-dates)
    dateRange = (data['Date'] > startDate) & (data['Date'] <= endDate)

    # Take the selected date range.
    data = data.loc[dateRange]

    return data


if __name__ == "__main__":

    data = loadData()



    # This function allows for the selection of a date range. Format is YYYY, MM, DD
    startDate = datetime.date(2018, 10, 10)
    endDate = datetime.date(2020, 1, 1)
    data = extractDateRange(data, startDate, endDate)


    generateSankey(data)