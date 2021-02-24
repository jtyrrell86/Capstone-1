import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from math import sqrt

asthma_data = pd.read_csv("../data/Colorado_EPHT_Asthma_Hospitalization_Data.csv")

def statewide_high_level_filter(raw_data):
    # Filters the data for only statewide rates for both genders, all ages, and between 2010- 2018.
    county_filter = asthma_data[asthma_data["COUNTY"] == "Statewide"]
    date_filter = county_filter[county_filter["YEAR"] >= 2010]
    age_filter = date_filter[date_filter["AGE"] == "All ages"]
    gender_filter= age_filter[age_filter["GENDER"] == "Both genders"]
    gender_filter[["COUNTY", "RATE", "YEAR", "GENDER", "AGE"]].to_csv("../data/statewide_high_level_data.csv")


if __name__ == "__main__":

    print(statewide_high_level_filter(asthma_data))