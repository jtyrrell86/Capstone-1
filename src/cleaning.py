import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from math import sqrt

asthma_data = pd.read_csv("../data/Colorado_EPHT_Asthma_Hospitalization_Data.csv")

def remove_uneeded_columns(raw_data):
    # Removes all, but the five columns i'm using
    return raw_data[["COUNTY", "RATE", "YEAR", "GENDER", "AGE"]]


def all_ages_both_genders_statewide():
    # Filters the data for only statewide rates for both genders, all ages, and between 2010- 2017.
    data = remove_uneeded_columns(asthma_data)
    all_ages_both_genders_statewide = data[(data["COUNTY"] == "Statewide") &
                                           ((data["YEAR"] >= 2010) & (data["YEAR"] <= 2017)) &
                                           (data["AGE"] == "All ages") &
                                           (data["GENDER"] == "Both genders")]
    return all_ages_both_genders_statewide
 
def all_ages_both_genders_arapahoe_county():
    # Filters the data for only Arapahoe County rates for both genders, all ages, and between 2010- 2017.
    data = remove_uneeded_columns(asthma_data)
    all_ages_both_genders_arapahoe_county = data[(data["COUNTY"] == "Arapahoe") &
                                                        ((data["YEAR"] >= 2010) & (data["YEAR"] <= 2017)) &
                                                        (data["AGE"] == "All ages") &
                                                        (data["GENDER"] == "Both genders")]
    return all_ages_both_genders_arapahoe_county

def child_both_genders_arapahoe_county():
    # Filters the data for only Arapahoe County rates for males age 15-34 and between 2010- 2017.
    data = remove_uneeded_columns(asthma_data)
    child_both_genders_arapahoe_county = data[(data["COUNTY"] == "Arapahoe") &
                                              ((data["YEAR"] >= 2010) & (data["YEAR"] <= 2017)) &
                                              (data["AGE"] == "0-4 years old") &
                                              (data["GENDER"] == "Both genders")]
    return child_both_genders_arapahoe_county

def male_young_adult_to_adult_arapahoe_county():
    # Filters the data for only Arapahoe County rates for males age 15-34 and between 2010- 2017.
    data = remove_uneeded_columns(asthma_data)
    male_young_adult_to_adult_arapahoe_county = data[(data["COUNTY"] == "Arapahoe") &
                                                     ((data["YEAR"] >= 2010) & (data["YEAR"] <= 2017)) &
                                                     (data["AGE"] == "15-34 years old") &
                                                     (data["GENDER"] == "Male")]
    return male_young_adult_to_adult_arapahoe_county

def remove_zeroes_and_nans():
    data = remove_uneeded_columns(asthma_data)
    # Removes 8,448 rows where RATE was zero
    minus_rate_zero = data[data["RATE"] != 0]
    # Removes rows where RATE is NaN
    minus_rate_nan = minus_rate_zero.dropna(subset=["RATE"])
    # Removes rows where AGE is NaN
    minus_age_nan = minus_rate_nan.dropna(subset=["AGE"])
    return minus_age_nan

def four_years_pre_legalization():
    # From the remove zeroes and nans data this generates my pre legalization sample used for the calculations below
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
    # From the remove zeroes and nans data this generates my post legalization sample used for the calculations below
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
    # Using both my pre and post samples this performs a Welches two tailed t-test
    data1 = four_years_pre_legalization()
    data2 = four_years_post_legalization()
    stat, p_value1 = stats.ttest_ind(data1["RATE"], data2["RATE"], equal_var=False)
    return stat, p_value1

if __name__ == "__main__":

    # print(all_ages_both_genders_statewide())
    # print(all_ages_both_genders_arapahoe_county())
    # print(child_both_genders_arapahoe_county())
    # print(male_young_adult_to_adult_arapahoe_county())
    # print(remove_zeroes_and_nans())
    # print(four_years_post_legalization())
    # print(calc_pre_len_mean_variance_std())
    # print(calc_post_len_mean_variance_std())
    print(two_sided_ttest())