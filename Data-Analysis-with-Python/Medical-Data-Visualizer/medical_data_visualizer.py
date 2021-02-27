import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")
# Add 'overweight' column
BMI = df["weight"]/((df["height"]/100)**2)
overweight = []
for bmi in BMI:
  if bmi > 25:
    overweight.append(1)
  else:
    overweight.append(0)
df['overweight'] = overweight

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholestorol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
a = df.loc[:,['cholesterol','gluc']] > 1
df.loc[:,['cholesterol','gluc']] = a.astype(int)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat  = pd.melt(df,id_vars=['cardio'],value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])



    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the collumns for the catplot to work correctly.
    cardio0 = df_cat[df_cat.cardio ==0].variable.groupby(df_cat.value).value_counts()
    cardio0 = cardio0.reset_index(name='total')
    cardio0['cardio'] = 0
    cardio1 = df_cat[df_cat.cardio ==1].variable.groupby(df_cat.value).value_counts()
    cardio1 = cardio1.reset_index(name='total')
    cardio1['cardio'] = 1

    df_cat = cardio0.append(cardio1)

    # Draw the catplot with 'sns.catplot()'
    g = sns.catplot(x='variable',y='total',hue='value', order=sorted(['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']),data=df_cat,col='cardio',kind='bar')
    fig= g.fig
    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    clean_cond1 = np.where((df['ap_lo'] > df['ap_hi']))[0]
    clean_cond2 = np.where(df['height'] < df['height'].quantile(0.025))[0]
    clean_cond3 = np.where(df['height'] > df['height'].quantile(0.975))[0]
    clean_cond4 = np.where(df['weight'] < df['weight'].quantile(0.025))[0]
    clean_cond5 = np.where(df['weight'] > df['weight'].quantile(0.975))[0]
    clean_cond = np.unique(np.concatenate([clean_cond1,clean_cond2,clean_cond3,clean_cond4,clean_cond5]))
    df_heat = df.drop(clean_cond)

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=np.bool))



    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(11, 9))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, mask=mask, vmax=.3, center=0,annot=True, fmt='.1f',
            square=True, linewidths=.5, cbar_kws={"shrink": .5})


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
