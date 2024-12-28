import pandas as pd
def sundays_of_year(year):
    start_date = f'{year}-01-01'
    end_date = f'{year}-12-31'
    dates = pd.date_range(start=start_date, end=end_date)
    return dates[dates.dayofweek == 6]
print("Sundays:", sundays_of_year(2024))
