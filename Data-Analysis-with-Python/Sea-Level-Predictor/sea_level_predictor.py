import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
  
    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    line1 = linregress(df['Year'], y = df['CSIRO Adjusted Sea Level'])
    slope, intercept, r_value, p_value, std_err = line1

    years_extended = df['Year'].append(pd.Series(range(2014, 2050)), ignore_index=True)
    # print(years_extended)

    plt.plot(years_extended, years_extended*slope + intercept, color="black")

    # Create second line of best fit
    mask = df['Year']>=2000
    line2 = linregress(df['Year'][mask], y = df['CSIRO Adjusted Sea Level'][mask])
    slope, intercept, r_value, p_value, std_err = line2
    years_reduced = years_extended[years_extended>=2000]
    plt.plot(years_reduced, years_reduced*slope + intercept, color="green")
    print(years_reduced*slope + intercept)
    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.xticks([1850.0, 1875.0, 1900.0, 1925.0, 1950.0, 1975.0, 2000.0, 2025.0, 2050.0, 2075.0])

    # plt.show()
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()