import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from math import sqrt
from cleaning import all_ages_both_genders_statewide, all_ages_both_genders_arapahoe_county, child_both_genders_arapahoe_county, male_young_adult_to_adult_arapahoe_county, calc_pre_len_mean_variance_std, calc_post_len_mean_variance_std


def all_ages_both_genders_statewide_plot(data):
    '''
    Generates a plot showing asthma hospitalizations using statewide data,
    for both genders, and all age groups.
    '''
    fig, ax = plt.subplots(dpi=150)
    plt.plot(data["YEAR"], data["RATE"])
    plt.grid()
    plt.axvline(x=2014, ls="--", color="green", label="Recreational Marijuana Legalization")
    plt.title("Statewide Hospitalization Rates From 2010- 2017 \n for Both Genders and All Ages")
    plt.xlabel("Year")
    plt.ylabel("Asthma Hospitalization Rate per 10,000 People")
    plt.legend(loc="best", fontsize="x-small")
    plt.savefig("../images/Statewide_Hospitalization_Rates_From_2010_2017_for_Both_Genders_and_All_Ages.png")
    return plt

def all_ages_both_genders_arapahoe_county_plot(data):
    '''
    Generates a plot showing asthma hospitalizations using data for Arapahoe county,
    for both genders, and all age groups.
    '''
    fig, ax = plt.subplots(dpi=150)
    plt.plot(data["YEAR"], data["RATE"])
    plt.grid()
    plt.axvline(x=2014, ls="--", color="green", label="Recreational Marijuana Legalization")
    plt.title("Arapahoe County Hospitalization Rates From 2010- 2017 \n for Both Genders and All Ages")
    plt.xlabel("Year")
    plt.ylabel("Asthma Hospitalization Rate per 10,000 People")
    plt.legend(loc="best", fontsize="x-small")
    plt.savefig("../images/Arapahoe_County_Hospitalization_Rates_From_2010_2017_for_Both_Genders_and_All_Ages.png")
    return plt

def child_both_genders_arapahoe_county_plot(data):
    '''
    Generates a plot showing asthma hospitalizations using data for Arapahoe county,
    for both genders, and for children betweeen 0-4.
    '''
    fig, ax = plt.subplots(dpi=150)
    plt.plot(data["YEAR"], data["RATE"])
    plt.grid()
    plt.axvline(x=2014, ls="--", color="green", label="Recreational Marijuana Legalization")
    plt.title("Arapahoe County Hospitalization Rates From 2010- 2017 \n for Children Aged 0- 4")
    plt.xlabel("Year")
    plt.ylabel("Asthma Hospitalization Rate per 10,000 People")
    plt.legend(loc="best", fontsize="x-small")
    plt.savefig("../images/Arapahoe_County_Hospitalization_Rates_From_2010_2017_for_Children_Aged_0_to_4.png")
    return plt

def male_young_adult_to_adult_arapahoe_county_plot(data):
    '''
    Generates a plot showing asthma hospitalizations using data for Arapahoe county,
    for males between 15-34.
    '''
    fig, ax = plt.subplots(dpi=150)
    plt.plot(data["YEAR"], data["RATE"])
    plt.grid()
    plt.axvline(x=2014, ls="--", color="green", label="Recreational Marijuana Legalization")
    plt.title("Arapahoe County Hospitalization Rates From 2010- 2017 \n for Males Aged 15- 34")
    plt.xlabel("Year")
    plt.ylabel("Asthma Hospitalization Rate per 10,000 People")
    plt.legend(loc="best", fontsize="x-small")
    plt.savefig("../images/Arapahoe_County_Hospitalization_Rates_From_2010_2017_for_Males_Aged_15_to_34.png")
    return plt

def distribution_of_asthma_hospitalization_rates_plot(data1, data2):
    '''
    Plots the pdf of both the pre-legalization and post-legalization data for comparison.
    it's also shows the mean of both samples.
    '''
    pre_len, pre_mean, pre_variance, pre_std = data1
    post_len, post_mean, post_variance, post_std = data2

    pre_norm_dist = stats.norm(pre_mean, pre_std)
    post_norm_dist = stats.norm(post_mean, post_std)
    
    fig, ax = plt.subplots(dpi=150)
    pre_x = np.linspace(pre_mean - 3*pre_std, pre_mean + 3*pre_std, 100)
    post_x = np.linspace(post_mean - 3*post_std, post_mean + 3*post_std, 100)
    plt.grid()
    plt.title("Distribution of Asthma Hospitalization Rates")
    plt.xlabel("Asthma Hospitalization Rate per 10,000 People")
    plt.ylabel("PDF")
    plt.axvline(x=pre_mean, ls="--", color="red", label=f"Pre- Mean: {round(pre_mean, 2)}")
    plt.axvline(x=post_mean, ls="--", color="blue", label=f"Post- Mean: {round(post_mean, 2)}")
    plt.plot(pre_x, pre_norm_dist.pdf(pre_x), linewidth=2, color="red", label="Pre- Legalization")
    plt.plot(post_x, post_norm_dist.pdf(post_x), linewidth=2, color="blue", label="Post- Legalization")
    plt.legend(loc="best")
    plt.savefig("../images/Condenced_Distribution_of_Asthma_Hospitalization_Rates.png")


if __name__ == "__main__":
    all_ages_both_genders_statewide_plot(all_ages_both_genders_statewide())
    all_ages_both_genders_arapahoe_county_plot(all_ages_both_genders_arapahoe_county())
    child_both_genders_arapahoe_county_plot(child_both_genders_arapahoe_county())
    male_young_adult_to_adult_arapahoe_county_plot(male_young_adult_to_adult_arapahoe_county())
    distribution_of_asthma_hospitalization_rates_plot(calc_pre_len_mean_variance_std(), calc_post_len_mean_variance_std())
