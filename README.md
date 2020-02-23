# SankeyDiagramFinances
Sankey Diagram of the Details from your [22seven](https://www.22seven.com/) account. It allows the visualization of all spending groups and where money is coming in from and going to over a period of time.

## Overview

The aim of the [22seven](https://www.22seven.com/) platform is to provide the end user with an idea of how much they spend on different categories and to keep track of expenses over time.
The platform is uniquely constructed such that it is capable of securely acquiring the details of how you earn and spend money. It does this by getting access to your bank account and records the details of each transaction.

Conveniently, the site provides the ability for the user to download all of their historical data as a CSV file which contains all of the relevant details of each and every transation that the system has been able to record.

## Sankey Diagrams

This utility makes use of this capability in their system to gain some more insights in your spending patterns with the use of a [Sankey diagram](https://en.wikipedia.org/wiki/Sankey_diagram). The aim of the diagram is to make use of multiple _pipes_, where the width of each pipe represents the magnitude of the value.
In this case, the size of each pipe represents the amount of money that is allocated to a specific spending category.

## 22seven Data

The 22seven site provides the user with the ability to bulk export their data, this can be done by the following instruction.
This also assumes that you have been using the platform for a period of time and the system has gathered some historical transactional data.

* Logging into the platform with your own credentials.
* Navigate to the _TRANSACTIONS_ tab on the left of the screen (assuming the web interface).
* At the top of the _TRANSACTIONS_ tab, select _ALL_ in order to get the list of all historical transactions.
* On the top right of the screen, select _EXPORT_, this will prompt the user to download all of the historical data available.
* Save the CSV file in the _RawData_ folder in this repository.


## Installation and Usage

This system currently makes use of Python in order to manage and analyse the data.
The system has only been tested on 3.X of Python.

In order to run the script simply run:

```python Sankey.py```