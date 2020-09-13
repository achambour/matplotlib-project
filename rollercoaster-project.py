import pandas as pd
import matplotlib.pyplot as plt

# load rankings data here:
wood_df = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
steel_df = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')

#number of rankings by year
wood_by_year = wood_df.groupby('Year of Rank').Name.nunique()
steel_by_year = steel_df.groupby('Year of Rank').Name.nunique()

# function to plot rankings over time for 1 roller coaster here:
def ranking_plot(roller_coaster, df, park_name):
  coaster_ranking = df[(df.Name == roller_coaster) & (df.Park == park_name)]
  #figure and plot
  fig = plt.figure()
  fig.add_subplot(1,1,1)
  ax = plt.subplot()
  plt.plot(coaster_ranking['Year of Rank'], coaster_ranking['Rank'])
  plt.xlabel('Year')
  plt.ylabel('Ranking')
  plt.title("{}'s ranking at {} for different years".format(roller_coaster, park_name))
  ax.invert_yaxis()
  plt.show()
  return None

#test with one rollercoaster
print(ranking_plot('El Toro', wood_df, 'Six Flags Great Adventure'))
plt.clf()

# function to plot rankings over time for 2 roller coasters here:

def ranking_plots(coaster1, coaster2, df, park_name1, park_name2):
  coaster1_ranking = df[(df.Name == coaster1) & (df.Park == park_name1)]
  coaster2_ranking = df[(df.Name == coaster2) & (df.Park == park_name2)]
  #figure and plot
  fig = plt.figure()
  fig.add_subplot(1,1,1)
  ax = plt.subplot()
  plt.plot(coaster1_ranking['Year of Rank'], coaster1_ranking['Rank'], label=coaster1)
  plt.plot(coaster2_ranking['Year of Rank'], coaster2_ranking['Rank'], label=coaster2)
  plt.xlabel('Year')
  plt.ylabel('Ranking')
  plt.title("{}'s and {}'s rankings at {} and {} for different years".format(coaster1, coaster2, park_name1, park_name2))
  plt.legend()
  ax.invert_yaxis()
  plt.show()
  return None

#test
print(ranking_plots('El Toro', 'Boulder Dash', wood_df, 'Six Flags Great Adventure', 'Lake Compounce'))
plt.clf()

# function to plot top n rankings over time here:

def top_rank(n, df):
  top_n_rankings = df[df.Rank <= n]
  #create figure
  fig = plt.figure()
  fig.add_subplot(1,1,1)
  ax = plt.subplot()
  for coaster in top_n_rankings['Name'].unique():
    coaster_rankings = top_n_rankings[top_n_rankings.Name == coaster]
    plt.plot(coaster_rankings['Year of Rank'], coaster_rankings['Rank'], label=coaster)
  ax.invert_yaxis()
  plt.legend()
  plt.show()
  return None

#test
print(top_rank(3, wood_df))
plt.clf()

# roller coaster data here:

coaster_df = pd.read_csv('roller_coasters.csv')
#print(coaster_df.head())

# function to plot histogram of column values here

def coaster_hist(df, column, min, max):
  #remove all missing values
  df.dropna()
  #remove outliers for heights
  heights = coaster_df[coaster_df['height'] <= 140]
  #figure
  fig = plt.figure()
  fig.add_subplot(1,1,1)
  #plot
  values = coaster_df[column]
  plt.hist(values, range(min, max))
  plt.show()
  return None

#test
print(coaster_hist(coaster_df, 'length', 400, 450))
plt.clf()

# function to plot inversions by coaster at a park here:

def coaster_inversions_chart(coaster_df, park_name):
  #subset of dataframe
  park_coasters = coaster_df[coaster_df['park'] == park_name]
  park_coasters = park_coasters.sort_values('num_inversions', ascending=False)
  coaster_names = park_coasters['name']
  number_inversions = park_coasters['num_inversions']
  #figure
  fig = plt.figure()
  fig.add_subplot(1,1,1)
  ax = plt.subplot()
  #plot
  plt.bar(range(len(coaster_names)), number_inversions)
  ax.set_xticks(range(len(coaster_names)))
  ax.set_xticklabels(coaster_names)
  plt.ylabel('No. inversions')
  plt.xticks(rotation=40)
  plt.show()
  return None

#test
#print(coaster_inversions_chart(coaster_df, 'Walibi Sud Ouest'))
plt.clf()


# function to plot pie chart of operating status here:

def pie_coaster(coaster_df):
  operating_coasters = coaster_df[coaster_df['status']=='status.operating']
  closed_coasters = coaster_df[coaster_df['status']=='status.closed.definitely']
  status_counts = [len(operating_coasters), len(closed_coasters)]
  plt.pie(status_counts, autopct='%0.1f%%', labels=['Operating','Closed'])
  plt.title = 'Operating vs Closed rollercoasters'
  plt.axis('equal')
  plt.show()

#test
print(pie_coaster(coaster_df))
plt.clf()

# function to create scatter plot of any two numeric columns here:
def coaster_scatter(coaster_df, column1, column2):
  #remove outliers
  coaster_df = coaster_df[coaster_df['height'] < 140]
  #figure
  fig = plt.figure()
  fig.add_subplot(1,1,1)
  ax = plt.subplot()
  #plot
  plt.scatter(coaster_df[column1], coaster_df[column2])
  plt.ylabel(column2)
  plt.xlabel(column1)
  plt.title('{} vs {} of rollercoasters'.format(column2, column1))
  plt.show()

#test
print(coaster_scatter(coaster_df, 'speed', 'height'))
plt.clf()


