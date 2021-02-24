import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from math import sqrt
from data.cleaning import statewide_high_level_filter

def statewide_high_level_line_plot(data):
    fig, ax = plt.subplots(dpi=150)
    plt.plot(gender_filter["YEAR"], gender_filter["RATE"])
    plt.axvline(x=2014, ls="--", color="green", label="Recreational Marijuana Legalization")
    plt.title("Statewide Hostpitilization Rates From 2010- 2018 for Both Genders and All Ages")
    plt.xlabel("Year")
    plt.ylabel("Asthma Hospitalization Rate")
    plt.legend(loc="best", fontsize="x-small")
    plt.savefig("../images/Statewide_Hostpitalization_Rates_From_2010_2018_for_Both_Genders_and_All_Ages.png")
    return plt

if __name__ == "__main__":
    statewide_high_level_line_plot(statewide_high_level_filter())
