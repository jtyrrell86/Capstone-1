# Recreational Marijuana Legalization and Asthma Hospitalizations: Is their a correlation?
## Backround and Motivation {need to finish and cite}
According to the CDC asthma is one of the most common long term diseases impacting children, though it can also effect adults. When an Asthma attack occurs it can cause wheezing, breathlessness, chest tightness, and coughing {anything about more serious conditions or maybe my experience with Brett}. Asthma attacks are brought on by asthma triggers of which tobacco smoke is one of the most commmon triggers.

With states around the country, including Colorado, legalizing both medical and recreational marijuana I wanted to see if it's legalization had any measurable impacts asthma hospitalization rates.

## Data
In order to answer the above question I looked at the Colorado Department of Public Health and Environment (CDPHE) Asthma Hospitalization Data available on <a href="https://data-cdphe.opendata.arcgis.com/datasets/colorado-epht-asthma-hospitalization-data/data">CDPHE's Open Data website</a>. This data set includes county-level and state data on rates of hospitalizations, due to diagnosis of asthma, among Colorado residents between 2004- 2018. In addition it is also broken down gender and five different age groups. This data was published by the Colorado Environmental Public Health Tracking project. {include this or somthing more about how the rates calculated? citation?} Retail sale of recreational marijuana was allowed starting on January 1st, 2014 so I chose to look at data four years before and four years after legalization.

## Exploratory Data Analysis
### What Does the Statewide Trend Look Like?
After importing my data into pandas, and doing some basic cleaning, my first goal was to look at only statewide data for both genders and all age groups. I was was surprised that out of more than 20,000 rows this only returned 8 data points to look at, but the trend being shown was interesting an unintutive. Though the rate did jump slightly in 2014, when legalization occured, the overall trend between 2010 and 2017 was a sharp decrease as shown below.

[Figure 1.1]
    <div align="center">
        <img src="images/Statewide_Hospitalization_Rates_From_2010_2017_for_Both_Genders_and_All_Ages.png" width="" height="">
    </div>
<br>

## What About the Trend in Just One County?
As a comparison I also took a look at the rates for both gender and all ages in just Arapahoe county. I chose Arapahoe county because it's both one of the most populous counties in Colorado and the one I live in. As you can see below the trend is almost identical.

[Figure 1.2]
    <div align="center">
        <img src="images/Arapahoe_County_Hospitalization_Rates_From_2010_2017_for_Both_Genders_and_All_Ages.png" width="" height="">
    </div>
<br>

# What About the Trend for Males Aged 15 to 34?
As one final basic comparison I took a look at the rates for my specific age group. Again, the results are almost identical.

[Figure 1.3]
    <div align="center">
        <img src="images/Arapahoe_County_Hospitalization_Rates_From_2010_2017_for_Males_Aged_15_to_34.png" width="" height="">
    </div>
<br>


## Has Legalization of Recreational Marijuana had a Measurable Impact?
[Figure 1.4]
    <div align="center">
        <img src="images/Condenced_Distribution_of_Asthma_Hospitalization_Rates.png" width="" height="">
    </div>
<br>

## Lessons Learned
The authors of this data specific warn against making inferences from this data about environmental changes.

In the absence of more data looking at only data from those counties who reported rates for both genders and all age groups would present a more equal comparison.



## Sources
1) https://data-cdphe.opendata.arcgis.com/datasets/colorado-epht-asthma-hospitalization-data/data
2) https://www.cdc.gov/asthma/faqs.htm#attack1
3) https://www.colorado.gov/pacific/sites/default/files/13%20Amendment%2064%20LEGIS.pdf
