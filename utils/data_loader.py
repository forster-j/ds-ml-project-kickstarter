# Libraries

import os, json, re
import pandas as pd 
from sklearn.preprocessing import LabelEncoder



######### functions for pre-processing ####################################################################

def extract_year_date_month(df, column):
    '''Takes a column, converts it to datetime, and creates new columns with day, month and year
    The new columns are named:
        - column_weekday
        - column_month
        - column_year
    '''
    
    # Convert column in df to datetime
    df[column] = pd.to_datetime(df[column], unit='s')

    # extract the day, month, and year components
    df[column + '_' + 'weekday'] = df[column].dt.weekday
    df[column + '_' + 'month'] = df[column].dt.month
    #df[column + '_' + 'year'] = df[column].dt.year

    return df


def duration(df, column1, column2):
    '''Returns the duration in days between 2 columns with datetime and puts it into a new colum
        - column1: start date
        - column2: end date
    '''
    df['duration_days'] = (df[column2] - df[column1]).dt.days

    return df

def convert_to_usd(df):
    return round(df['goal'] * df['static_usd_rate'],2)




######### Load the data ########################################################## 

directory = 'Kickstarter_data/'
data = pd.DataFrame()
relevant_columns = ['category', 'country', 'state', 'static_usd_rate', 'goal', 'launched_at', 'deadline', 'creator']

for file in sorted(os.listdir(directory)):
    df_temp = pd.read_csv(directory+file)
    data = pd.concat([data, df_temp[relevant_columns]], ignore_index=True)


##### Cleaning ########################################

## drop duplicates
    
data = data.drop_duplicates(ignore_index =True)   
data = data.drop('creator', axis=1)    


## Get the categories from the 'category

cat_data = data["category"].apply(json.loads)
cat_data = pd.DataFrame(cat_data.tolist())
data['slug'] = cat_data['slug']
data = data.drop("category", axis=1)
data["slug"] = data["slug"].apply(lambda x: re.split(r'/', x)[0])

le = LabelEncoder()
data['slug'] = le.fit_transform(data['slug'])

## Work on the 'state' column

data = data[data['state'] != 'live'].reset_index(drop=True)
data['state'] = data['state'].apply(lambda x: 1 if x == 'successful' else 0)


## Work on the time-related columns 'launched_at' and 'deadline'

data['launched_at'] = pd.to_datetime(data['launched_at'], unit='s')
data['deadline'] = pd.to_datetime(data['deadline'], unit='s')

data = extract_year_date_month(data, 'launched_at')
data = duration(data, 'launched_at', 'deadline')

data = data.drop(['launched_at', 'deadline'], axis=1)

## Work on 'goal' column 

data['goal_in_usd'] = data.apply(convert_to_usd, axis=1)
data = data.drop(['static_usd_rate', 'goal'], axis=1)
data = data[data['goal_in_usd'] < 1000000].reset_index(drop=True)

## Work on 'country' column

data["north_america"] = data["country"].apply(lambda x: 1 if x in ['US', 'CA'] else 0)
data = data.drop('country', axis=1)



#save Dataframe in csv_file
data.to_csv('data/cleaned_data.csv', index=False)