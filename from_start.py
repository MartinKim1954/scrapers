# item = '수유등'
item = '신생아욕조'
now_string = "2020.09.02"
# now_string = "2020.09.03"

file = 'open_date_' + item + '.txt'
f = open(file, 'r')
file_read = f.readlines()
f.close()

for i in range(len(file_read)):
    file_read[i] = file_read[i].replace("\n", "")


total_months_list = []
total_days_list = []

for i in range(len(file_read)):
    year = int(now_string[:4]) - int(file_read[i][:4])
    month = int(now_string[5:7]) - int(file_read[i][5:7])
    day = int(now_string[8:10]) - int(file_read[i][8:10])
    days = round(day, 2)
    total_months = str((year*12)+month)
    total_days = str((year*12*365)+(month*30.42)+days)
    total_months_list.append(total_months)
    total_days_list.append(total_days)

months_txt_name = 'months_from_start_' + item + '.txt'
days_txt_name = 'days_from_start_' + item + '.txt'


f = open(months_txt_name, 'w')
for i in range(len(total_months_list)):
    data = f'{total_months_list[i]}\n'
    f.write(data)
f.close()

f = open(days_txt_name, 'w')
for i in range(len(total_days_list)):
    data = f'{total_days_list[i]}\n'
    f.write(data)
f.close()
