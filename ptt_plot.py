from datetime import datetime 
import matplotlib.pyplot as plt 

with open("ptt.txt",'r',encoding='utf-8') as f:
    ptt_lines = f.readlines()

x_time, y_ptt = [], []
for line in ptt_lines:
    data = line.split()
    x_time.append(data[0])
    y_ptt.append(float(data[1]))

x_date_format = [datetime.strptime(d, '%Y/%m/%d').date() for d in x_time]

plt.figure(figsize=(10, 6))

plt.title('Ptt')
plt.plot(x_date_format, y_ptt, 'o-')
plt.xlabel('Time')
plt.ylabel('Ptt')

plt.savefig('ptt.png', bbox_inches='tight')
plt.show()