import datetime as dt

# %m	Номер месяца [01,12]
# %d	День месяца [01,31]
d = dt.datetime.strptime(input(), '%m %d')
print((d - dt.timedelta(1)).strftime('%m.%d'), (d + dt.timedelta(1)).strftime('%m.%d'))