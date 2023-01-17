import datetime


file_name = str(datetime.datetime.now())
with open(file_name, 'w') as f:
    f.write('hi')
