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
data_source['video views'] = data_source['video views'].astype(int)
data_source['video views'] = data_source['video views'].abs()


df_cleaned = data_source.style.hide(axis='index')
df_cleaned.to_excel('df_cleaned.xlsx')

from gauth_script import df

#df_selected_country = df[df.Country == 'United States'].sort_values(by = 'video views', ascending= False)

#dynamic stats within country
    #find channel with max views
def most_viewed_channel(input_country):
     country_df = df[df['Country'] == input_country]
     max_view_index = country_df['video views'].idxmax()
     max_view_count = country_df.loc[max_view_index]
     channel_name = max_view_count['Youtuber']
     view_count = max_view_count['video views']
     return channel_name, view_count 
     

    #find channel with max earnings
def highest_earning_channel(input_country):
     country_df = df[df['Country'] == input_country]
     max_earnings_index = country_df['highest_yearly_earnings'].idxmax()
     max_earning = country_df.loc[max_earnings_index]
     channel_name = max_earning['Yotuber']
     highest_earning = max_earning['highest_yearly_earnings']
     return (highest_earning, channel_name)



#most_popular channel number conversion (most viewed)
def format_num(num):
       if num > 1000000000:
            if not num % 1000000000:
                return f'{num//1000000000}B'
            return f'{round(num/1000000000, 1)}B'
       return f'{num/100000000}M' 




