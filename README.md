# POPOF
Priority Oriented Perspective On Finances

## Overview
A super simple in both philosophy and implementation python script that calculates finances based on a priority file of costs. Essentially the user has to categorize his costs and rank those categories in a csv file. The goal of popof is to be a modular calculator of costs based on their priority as each individual has priorities on spending money as well as that some costs are dependent on other costs and provide a useful perspective on ones finances. POPOF has 2 operation modes:
- Goal: Calculate the amount of money it takes to fulfill all cost needs
- Coverage: Calculate which costs can be satisfied based on an income amount

## Example input csv file
`# Base, Name, Cost, Period`  
`Survival, Water, 20, m`  
`Survival, Shelter, 400, m`  
`Survival, Electricity, 50, m`  
`Survival, Food, 15, d`  
`Communication, Internet, 30, m`  
`Communication, Telephone, 35, m`  
`Transportation, Car Gas, 5, d`  
`Grooming, Haircut, 15, m`  
`Services, Spotify, 7, m`  
`Services, Netflix, 10, m`  
`Maintenance, Car Wash, 15, m`  
`Hobbies, Skateboarding, 0, d`  
`Hobbies, Paint, 15, w`  

In the above example the priority in descending order is Survival, Communication, Transportation, Grooming, Services, Maintenance, Hobbies and their respective costs in the respective order that are found in the file. A well defined costs file is considered one that costs are properly categorized and categories are properly defined (a cost shouldn't be qualified to belong to more than 1 category). The scripts provides the user with the ability to define a cost by a period d: daily, w: weekly or m: monthly for the results to be as accurate as possible. The results are monthly.

## Usage
`python3 popof.py [OPTIONS]`

### Options
`-h, --help            				| Show this help message and exit`  
`-c COSTS, --costs COSTS			| Input csv file containing costs`  
`-s SAVINGS, --savings SAVINGS 		| Define goal for savings (Run GOAL mode)`  
`-i INCOME, --income INCOME 		| Define income (Run COVERAGE mode)`  

## Contributions
Contributions are more than welcome, especially for proposals about interesting/informative statistics regarding the results and the costs or different modes of operation!
