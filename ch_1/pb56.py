day = int(input('Enter days -> '))

year = day // 365
rday = day%365

month = rday//30
total_days = rday%30
print('year ',year,' month ',month,' days ',total_days)