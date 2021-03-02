import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) &
        (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    df_line = df

    fig, ax = plt.subplots(figsize=(20, 5))
    line, = ax.plot(df_line, color='red')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
  df_line = df

  fig, ax = plt.subplots(figsize=(20, 5))
  line, = ax.plot(df_line, color='red')
  ax.set_xlabel('Date')
  ax.set_ylabel('Page Views')
  ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    

    # Save image and return fig (don't change this part)
  fig.savefig('line_plot.png')
  return fig


def draw_bar_plot():
    df_bar = df.copy()
    df_bar = df_bar.resample('M').mean()
      
    months = ['January', 'February', 'March', 'April', 
            'May', 'June', 'July', 'August', 
            'September', 'October', 'November', 'December']
    labels = [i for i in range(2016, 2020)]    

      
      # Create Wide Format Dataframe to be used for plotting
    data_dict={'Year': labels}
    for j , month in enumerate(months):
      month_data = []
      for i in labels:
        try:
          month_data.append(df_bar['{}-{}'.format(i, j+1)].iloc[0]['value'])
        except KeyError:
          month_data.append(0)
      data_dict[j] = month_data
      
    df_bar = pd.DataFrame(data_dict)
    df_bar.columns = ["Year"] + months


      #begin plotting process
    pos = list(range(len(df_bar['Year'])))
    width = 0.05

    fig, ax = plt.subplots(figsize=(7, 7))
    for q in range(12):
      plt.bar([p + width*q for p in pos], df_bar[months[q]], width)

    ax.set_ylabel('Average Page Views')
    ax.set_xticks([p + 5 *width for p in pos])
    ax.set_xticklabels(df_bar['Year'])
    ax.set_xlabel('Years')

    plt.legend(months, title='Months')
    plt.xticks(rotation=90)

    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig = plt.figure(figsize=(20, 5))

    ax1 = plt.subplot(1, 2, 1)
    sns.boxplot(y=df_box['value'], x=df_box['year'])

    ax1.set_ylabel('Page Views')
    ax1.set_xlabel('Year')
    ax1.set_title('Year-wise Box Plot (Trend)')


    ax2 = plt.subplot(1, 2, 2)
    sns.boxplot(y=df_box['value'], x=df_box['month'], order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

    ax2.set_ylabel('Page Views')
    ax2.set_xlabel('Month')
    ax2.set_title('Month-wise Box Plot (Seasonality)')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
