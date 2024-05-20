import numpy as np
import pandas as pd
import os
import csv

data_source = pd.read_excel(r"F:\Data Analytics\youtube_dashboard\Global_YouTube_Statistics.xlsx")
df = pd.DataFrame(data_source)

print(data_source)