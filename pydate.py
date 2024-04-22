from datetime import datetime
formatted_date = datetime.strptime("12/2/2022", '%m/%d/%Y').strftime('%Y-%m-%d')

print(formatted_date)