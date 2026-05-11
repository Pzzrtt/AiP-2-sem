import re

regul = re.compile(r'(?P<ip>\d.+) -- \[(?P<data>.*?)\] "(?P<metode>\w+) (?P<path>.*?) (?P<protokol>.*?)" (?P<status>\d+) (?P<size>\d+) "(?P<name>.*?)"')

ips = []
status_all = []
paths = []
total_size = 0
total_requests = 0


for line in open('logs.txt'):
    matchs = regul.match(line)
    if matchs:
        reg = matchs.groupdict()
        ips.append(reg['ip'])
        status_all.append(reg['status'])
        paths.append(reg['path'])
        total_size += int(reg['size'])
        total_requests += 1


ips = sorted(ips)
ipp = set()
for i in ips:
    ipp.add(i)

res_ip = {}
for i in ipp:
    x = ips.count(i)
    res_ip[i] = x

print("Топ-5 IP-адресов:")
c = 1
sort_res_ip = sorted(res_ip.items(), key=lambda x: x[1], reverse=True)
for ip, count in sort_res_ip:
    if c > 5:
        break
    else:
        c += 1
        print(f'{ip} - {count} запроосов {round(count / total_requests * 100, 2)}%')
    

status_all = sorted(status_all)
status_all_set = set()
for i in status_all:
    status_all_set.add(i)

status_all_res_d = {}
for i in status_all_set:
    x = status_all.count(i)
    status_all_res_d[i] = x

print("\nСтатус-коды:")
sort_status_all_res_d = sorted(status_all_res_d.items(), key=lambda x: x[1], reverse=True)
for stat, count in sort_status_all_res_d:
    print(f'{stat} - {count} запроосов {round(count / total_requests * 100, 2)}%')


paths = sorted(paths)
paths_set = set()
for i in paths:
    paths_set.add(i)

paths_d = {}
for i in paths_set:
    x = paths.count(i)
    paths_d[i] = x

print("\nСамые популярные пути:")
p = 1
paths_d = sorted(paths_d.items(), key=lambda x: x[1], reverse=True)
for url, count in paths_d:
    if p > 5:
        break
    else:
        p += 1
        print(f'{url} - {count} запроосов {round(count / total_requests * 100, 2)}%')


print('\nОбщий размер всех запросов:')
print(total_size)