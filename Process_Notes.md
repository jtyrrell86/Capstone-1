






* I choose this data because I thought looking at asthma hospitalization rates over a 9 year span pre and post recreational legalization would be informative as to it's impact on these rates.
* As part of my initial analysis I filtered my data to include:
1. Only Statewide entires
2. 2010- 2018
3. All age groups
4. Both genders
* When I looked at the resulting data a realized a potential issue was that these filters only returned 8 rows, one for each year.
* I then graphed this data on a basic plot and noticed that their was a spike in 2014, but then the genral trend was down.
* I Then decided to get a better idea of how much data I had. After doing a .info() I noticed a large percentage of the entries were (~5000 were null). In addition I did a .describe and noticed the min, 25% and 50% were zero.
* I then decided to to see how many entries were had a rate of zero and it turned out almost 8500 were (more then 50% of the data)
* I then looked at how many potential counties this represented and it looked as though 57 of 62 counites may have no data
* After realizing that a majority of counties were missing data I suspected the statewide data may be inaccurate. As such I decided to look at a county with more complete data, Arapapoh county.
* Again, I only had 8 rows, but the general trend of the data was identical to the statewide data.
* Lastly, I decided to to look at data only for males aged 15- 34. This data was much more erratic.