import pandas as pd
import json, re

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
    '''Returns the duration in days between 2 columns with datetime and puts it into a new colum.
        - column1: start date
        - column2: end date
    '''
    df['duration_days'] = (df[column2] - df[column1]).dt.days

    return df

def convert_to_usd(df):
    ''' Converts a column 'goal' into $USD by multiplying it with corresponding exchange rates from a column 'static_usd_rate'
        The result is rounded to 2 decimal places.
        - df: dataframe containing the columns
    '''
    df['goal'] = round(df['goal'] * df['static_usd_rate'],2)

    return df

def extract_category(df):
    ''' From json-string entry in column category, extract entry slug and take string in front of '/' in order
        to get the campaigns category that is written into the column 'slug'. 
    ''' 
    cat_data = pd.DataFrame(df["category"].apply(json.loads).tolist())
    df['slug'] = cat_data['slug']
    df["slug"] = df["slug"].apply(lambda x: re.split(r'/', x)[0])

    return df

def state_to_binary(df):
    ''' Modifies the column state containing the entries live/successful/failed/canceled/suspended to a binary column, 
        dropping rows with state 'live', setting the entry 'successful' to 1 and the others to 0. 
    '''
    df = df[df['state'] != 'live'].reset_index(drop=True)
    df['state'] = df['state'].apply(lambda x: 1 if x == 'successful' else 0)
    return df


def north_america(df):
    '''Checks a dataframe column with alpha 2 country code an returns the dataframe with an additional column
       'north_america' containing 1 if the country is USA (US) or Canada (CA) and therefore in north america 
       and 0 in any other case. 
    '''
    df["north_america"] = df["country"].apply(lambda x: 1 if x in ['US', 'CA'] else 0)
    return df

def unrealistic_goal(df):
    '''Exclude projects with goals above 1000000 as they will most likely fail and in the majority
       of cases are unrealistic. 
    '''
    df = df[df['goal'] < 1000000].reset_index(drop=True)
    return df