import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from math import sqrt

asthma_data = pd.read_csv("../data/Colorado_EPHT_Asthma_Hospitalization_Data.csv")

def remove_uneeded_columns(raw_data):
    # Removes all, but the five columns i'm using
    return raw_data[["COUNTY", "RATE", "YEAR", "GENDER", "AGE"]]


def statewide_high_level_filter():
    # Filters the data for only statewide rates for both genders, all ages, and between 2010- 2018.
    data = remove_uneeded_columns(asthma_data)
    county_filter = data[data["COUNTY"] == "Statewide"]
    date_filter = county_filter[county_filter["YEAR"] >= 2010]
    age_filter = date_filter[date_filter["AGE"] == "All ages"]
    gender_filter= age_filter[age_filter["GENDER"] == "Both genders"]
    # gender_filter.to_csv("../data/statewide_high_level_data.csv")
    return gender_filter
 
def high_level_filter_arapahoe_county():
    # Filters the data for only Arapahoe County rates for both genders, all ages, and between 2010- 2018.
    data = remove_uneeded_columns(asthma_data)
    county_filter_arapahoe = data[data["COUNTY"] == "Arapahoe"]
    date_filter_arapahoe = county_filter_arapahoe[county_filter_arapahoe["YEAR"] >= 2010]
    age_filter_arapahoe = date_filter_arapahoe[date_filter_arapahoe["AGE"] == "All ages"]
    gender_filter_arapahoe = age_filter_arapahoe[age_filter_arapahoe["GENDER"] == "Both genders"]
    return gender_filter_arapahoe

def high_level_filter_arapahoe_county_males():
    # Filters the data for only Arapahoe County rates for males age 15-34 and between 2010- 2018.
    data = remove_uneeded_columns(asthma_data)
    county_filter_arapahoe = data[data["COUNTY"] == "Arapahoe"]
    date_filter_arapahoe = county_filter_arapahoe[county_filter_arapahoe["YEAR"] >= 2010]
    age1_filter_arapahoe = date_filter_arapahoe[date_filter_arapahoe["AGE"] == "15-34 years old"]
    male_filter_arapahoe = age1_filter_arapahoe[age1_filter_arapahoe["GENDER"] == "Male"]
    return male_filter_arapahoe

def remove_zeroes_and_nans():
    data = remove_uneeded_columns(asthma_data)
    # Removes 8,448 rows where RATE was zero
    minus_rate_zero = data[data["RATE"] != 0] # Removes 8448 rows
    # Removes rows where RATE is NaN
    minus_rate_nan = minus_rate_zero.dropna(subset=["RATE"])
    # Removes rows where AGE is NaN
    minus_age_nan = minus_rate_nan.dropna(subset=["AGE"])
    return minus_age_nan

def four_years_pre_legalization():
    scrubbed_data = remove_zeroes_and_nans()
    four_years_pre_legalization = scrubbed_data[(scrubbed_data["YEAR"] <= 2013) & 
                                 (scrubbed_data["YEAR"] >= 2010) &
                                 (scrubbed_data["COUNTY"] != "Statewide") &
                                 (scrubbed_data["GENDER"] != "Both genders") &
                                 (scrubbed_data["AGE"] != "All ages")]
    return four_years_pre_legalization

def calc_pre_len_mean_variance_std():
    pre_data = four_years_pre_legalization()
    pre_len = len(pre_data["RATE"])
    pre_mean = pre_data["RATE"].mean()
    pre_variance = pre_data["RATE"].var()
    pre_std = sqrt(pre_variance)
    return pre_len, pre_mean, pre_variance, pre_std

def four_years_post_legalization():
    scrubbed_data = remove_zeroes_and_nans()
    four_years_post_legalization = scrubbed_data[(scrubbed_data["YEAR"] <= 2017) & 
                                 (scrubbed_data["YEAR"] >= 2014) &
                                 (scrubbed_data["COUNTY"] != "Statewide") &
                                 (scrubbed_data["GENDER"] != "Both genders") &
                                 (scrubbed_data["AGE"] != "All ages")]
    return four_years_post_legalization

def calc_post_len_mean_variance_std():
    post_data = four_years_post_legalization()
    post_len = len(post_data["RATE"])
    post_mean = post_data["RATE"].mean()
    post_variance = post_data["RATE"].var()
    post_std = sqrt(post_variance)
    return post_len, post_mean, post_variance, post_std

def two_sided_ttest():
    data1 = four_years_pre_legalization()
    data2 = four_years_post_legalization()
    stat, p_value1 = stats.ttest_ind(data1["RATE"], data2["RATE"], equal_var=False)
    return stat, p_value1


if __name__ == "__main__":

    # print(remove_zeroes_and_nans())
    # print(high_level_filter_arapahoe_county_males())
    # print(four_years_post_legalization())
    print(calc_pre_len_mean_variance_std())
    print(calc_post_len_mean_variance_std())
    print(two_sided_ttest())