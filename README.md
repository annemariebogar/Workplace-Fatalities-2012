# **2012 Workplace Fatalities by State**
**Author:** Anne Marie Bogar<br/>
**Active Project Dates:** February 25 - March 10, 2024<br/>

## Summary
The goal of the project is to use visualizations in Power BI to explore a dataset about workplace fatalities in each state in the year 2012. 
The graphs, filters and interactivity help the audience detect correlations and gain interesting insights into the relationships between the different features in the dataset. 
Statistical analysis, such as logistic regression and hypothesis testing, is used to confirm the findings in the graphs.

## Data
The data is from a CSV file containing information about workplace fatalities in each state in the year 2012. 
The information contained in the file for each state consists of:
1. The total number of workplace fatalities in 2012
2. The rate of workplace fatalities in 2012
3. The state’s rank in terms of workplace fatalities for 2012
4. The total number of workplace injuries and/or illnesses in 2012
5. The rate of workplace injuries and/or illnesses in 2012
6. The penalties, or average amount of dollars the state was fined, in 2013
7. The state rank for penalty amounts in 2013
8. The number of inspectors in the state for conducting workplace inspections
9. The number of years it takes to inspect each workplace once
10. Whether the program that inspects the workplaces is state-run or federal-run

## Questions Explored

|                | Average Number of Fatalities, 2012 | Average Rate of Fatalities, 2012 |
| :------------- | :--------------------------------: | :------------------------------: |
| Federal mean   |             97.03448276            |           4.420689655            |
| State mean     |             85.85714287            |           4.176190476            |
| State stdev    |             77.69510005            |           2.4130690476           |
| Test statistic |             -0.659256583           |           -0.464319806           |
| Critical value |                -2.086              |              -2.086              |
| Rejection of H0|        Failed to be rejected       |       Failed to be rejected      |

One of the questions explored was whether having a state-run program versus a federal-run program made a difference in terms of fatalities and injuries/illnesses. Based on the visualizations on the “Fatalities per Program” page, there does not appear to be any significant difference between state-run and federal-run programs in either the rate of fatalities nor in the number of fatalities. Due to the fact that there are more states that use a federal program than a state program, the graphs refer to the average number and rate of fatalities. A summation rather than an average would lead to a higher percentage for the federal program and therefore an inaccurate comparison. The graphs did show a slightly larger percentage of fatalities in federal-run programs, so a hypothesis test with a 95% confidence level was conducted to determine whether the difference was significant enough to declare that state-run programs result in less fatalities. The results, shown above in Table 1, fail to reject the null hypothesis that both types of programs result in similar numbers and rates of fatalities.

|                | Average Number of Injuries/Illnesses, 2012 | Average Rate of Injuries/Illnesses, 2012 |
| :------------- | :----------------------------------------: | :--------------------------------------: |
| Federal mean   |                 66809.52381                |               3.480952381                |
| State mean     |                 61547.61905                |               3.771428571                |
| State stdev    |                 70629.67237                |               0.62220805                 |
| Test statistic |                -0.341401511                |               2.139363403                |
| Critical value |                   -2.086                   |                  2.086                   |
| Rejection of H0|            Failed to be rejected           |                 Rejected                 |

Another question explored was how each state ranked in terms of numbers and rates for both fatalities and injuries/illnesses. California led in terms of numbers for both fatalities and injuries/illnesses, although California did not have the highest per-capita rate for either due to its large population. Per-capita rates of injuries in Maine and fatalities in North Dakota are both inflated due to their significantly smaller population sizes. The maximum and minimum rates of injuries and fatalities were found in states with federal-run programs, while the maximum and minimum numbers were found in states with state-run programs. This further supports the idea that there is no significant difference to be found between the two. A hypothesis test with a 95% confidence level was run to determine whether there was a difference between state and federal programs in terms of injuries/illnesses numbers and rates. As seen above in Table 2, the null hypothesis that both types of programs result in similar numbers of injuries/illnesses failed to be rejected; however, the difference in average rates of injuries/illnesses was significant enough to reject the assumption that the two program types are the same.
<br/><br/>
A third question explored was the relationship between the fatality rate, the years of inspection, and the number of inspectors. The scatter graph and bar chart used to analyze the relationship between fatality rates and the number of years to inspect each workplace once did not seem to imply a correlation, so Pearson’s R was calculated and found to be 0.12232858307027374. To analyze the relationship between the number of inspectors and the fatality rates and years of inspection, the population of each state was divided by the number of inspectors in each state to determine how many state residents corresponded to one inspector. This took into account the population size of the states, as the same number of inspectors in two differently-sized states would most likely result in different outcomes. In the scatter plot comparing the rate of fatalities to the number of inspectors (or more precisely, the number of residents per inspector), there was no evident correlation, and upon further calculations, Pearson’s R confirmed this suspicion with a coefficient of -0.15469112002936752. With the exception of a few outliers (North Dakota, Wyoming and Alaska all had fairly high rates of fatalities compared to the ratio of residents to inspectors) the states formed a flat trend line. In contrast, the correlation between the number of years to inspect each workplace once and the number inspectors per-capita was quite strong, with a Pearson’s R of 0.76312840475276. Not surprisingly, the number of years decreased as the ratio of residents to inspectors decreased, and the number of years increased as the ratio increased. Another interesting takeaway from the graphs is that the average number of years was approximately 60% higher for the federal program and similarly, the average number of inspectors per-capita was also approximately 60% higher for the federal program.

|                                                |      Pearson’s R       |
| :--------------------------------------------- | :--------------------: |
| Penalty amount by Rate of Fatalities           |   0.12412747181729103  |
| Penalty amount by Number of Fatalities         |   0.3668455170303696   |
| Penalty amount by Rate of Injuries/Illnesses   |  -0.08697389849178325  |
| Penalty amount by Number of Injuries/Illnesses |   0.5608114855541665   |

The final question explored was the relationship between the penalties, in the form of monetary fees, imposed on each state and how these fees corresponded to the numbers and rates of fatalities and injuries/illnesses. Upon examination of the graphs, there appears to be no real correlation between the penalty amounts, which the Pearson’s R for each graph in Table 3 above corroborates. The R coefficient is slightly higher for the number of fatalities and number of injuries/illnesses, but this can be attributed to California being an outlier in terms of the penalty amount. The penalty amount does not seem to be based on any of these statistics, as the amount is relatively the same across the board, regardless of rate or number, except for California which has an unusually high penalty amount. One interesting insight that these graphs highlighted is that the federal program tends to impose a higher penalty fee than the state program, regardless of statistics. In fact, the average federal penalty fee is roughly 60% higher than that of the state programs.

## Power BI Features
The graphs used in the report are pie charts, bar graphs, scatter graphs, maps, and gauges. The pie charts were used to demonstrate the difference between the state-run and federal-run programs in terms of average numbers of fatalities, average rates of fatalities, average number of years to inspect each workplace once, average number of residents to inspectors, and average penalty amounts. A bar graph was used to analyze the relationship between the rate of fatalities and the number of years to inspect each workplace once, as well as a scatter graph with a trend line. The scatter graphs were used to explore the correlation between the number of residents per inspector and the rate of fatalities and the number of years to inspect each workplace once, as well as the correlation between the penalty amount imposed and numbers and rates of fatalities and injuries/illnesses. Trend lines were used to illustrate how much of a correlation there was, although they were a bit influenced by outliers. Gauges were used to show the statistics of each state and where they fell in terms of the maximum and minimum numbers. And maps were used to visualize which states used a federal-run program and which states used a state-run program.
<br/><br/>
In addition to charts, cards were used to display information on which states had the minimum and maximum number and rate of fatalities and injuries/illnesses. Buttons were also used to switch between bookmarks to show different variations of charts exploring the same statistics. Slicers were used to filter between program types and states. Conditional coloring was used on the gauges. And finally, tooltips were used to display more information about the data points in the graphs.
<br/><br/>
To further analyze the data, a column was added with state population from 2012 from the US census website, and another column was added using a DAX formula dividing the state population by the number of inspectors in the state to take into account the population size of the state when determining if the number of inspectors affects the fatality rate or the number of years to inspect each workplace once. DAX was also used to calculate measures to display the state names with the maximum and minimum rates and numbers of fatalities and injuries/illnesses. For example, the DAX formula for determining the state with the maximum number of fatalities is:
<br/><br/>
**FatalMaxState = CALCULATE( VALUES( ‘Fatalities 2012’[State] ),
<br/>FILTER( ALL( ‘Fatalities 2012’[Number of Fatalities, 2012] ) ),
<br/>‘Fatalities 2012’[Number of Fatalities, 2012] = MAX( ‘Fatalities 2012’[Number of Fatalities, 2012] ) ) )**

## Future Improvements

Given more time and greater available resources, I would add more datapoints to the data set to get more insight and to seek further correlations. For example, I used the state population to determine the ratio of inspectors to workers, but as the entire population of a state does not work at these workplaces, I would have preferred to use the number of workers in the state that work at these workplaces or even the number of workplaces in the state. These features would better represent the ratio to compare whether there actually was a correlation.
<br/><br/>
I would also like to review at the guidelines and regulations for each state’s programs. With the currently available context, the penalty amounts appear arbitrary and do not seem to be based on existing fatality or injury/illness data. It would be interesting to investigate what basis exists for the penalties and how they are levied.
<br/><br/>
With a larger dataset and more regulatory context, I would perform a deeper analysis on the states with the lowest per-capita rates of fatalities and injuries to see what specific steps they are taking to keep the numbers low. For instance, what is their ratio of inspectors to workers? How do they determine penalty fees and amounts? What size is their budget and how are they spending the money? A report from past years to determine what has changed and how these changes have impacted the rates would also help in understanding how to keep fatality and injury/illness rates low. This information could influence planning of how to change other states’ programs (whether federal or state run) to reduce their rates of fatalities and injuries/illnesses.
<br/><br/>
Finally, I would like to view the datasets post-2012 to see if any progress has been made. The states that have made the most progress in reducing the fatality and injury/illness rates would be studied to determine what steps they took, which strategies worked and which ones did not, and then using this information, a plan would be devised to be implemented in other states.
