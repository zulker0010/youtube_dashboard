import numpy as np
import pandas as pd

data_source = pd.read_excel(r"F:\Data Analytics\youtube_dashboard\Global_YouTube_Statistics.xlsx")

columns_to_drop = ['Title',
                    'uploads',
                    'Abbreviation', 
                    'channel_type',
                    'video_views_rank', 
                    'country_rank', 
                    'channel_type_rank',
                    'video_views_for_the_last_30_days',
                    'lowest_monthly_earnings',
                    'highest_monthly_earnings',
                    'lowest_yearly_earnings',
                    'subscribers_for_last_30_days',
                    'created_year', 
                    'created_month',
                    'created_date',
                    'Gross tertiary education enrollment (%)',
                    'Population',
                    'Unemployment rate', 
                    'Urban_population',
                    'Latitude', 
                    'Longitude']
 
data_source.drop(columns=columns_to_drop, inplace = True)

data_source['Youtuber'] = data_source['Youtuber'].astype(str) 
data_source['category'] = data_source['category'].astype(str)
data_source['Country'] = data_source['Country'].astype(str) 
data_source['rank'] = data_source['rank'].astype(int)
data_source['subscribers'] = data_source['subscribers'].astype(int)
data_source['highest_yearly_earnings'] = data_source['highest_yearly_earnings'].astype(int)

df_cleaned = data_source.style.hide(axis='index')
df_cleaned.to_excel('df_cleaned.xlsx')

df = pd.read_excel('df_cleaned.xlsx')
df

df_selected_country = df[df.Country == 'United States'].sort_values(by = 'video views', ascending= False)

def country_stats(most_popular_channel, most_viewed_category, highest_paid, input_df, input_country):
    df_selected_country_stats = input_df[input_df['Country'] == input_country].reset_index()



#most_popular channel (most viewed)
def format_num(num):
    if num > 1000000000:
        if not num % 1000000000:
            return f'{num//1000000000}B'
        return f'{round(num/1000000000, 1)}B'
    return f'{num/100000000}M'



