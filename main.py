import re
import csv
import pprint

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

result_list, phone, name, organisation, position, email, result_dict = [], [], [], [], [], [], {}
buff = ""
for i in range(1, len(contacts_list)):
    res = (re.findall(r'\d+\s*', ''.join(contacts_list[i])))
    phone.append((''.join(res)).replace(' ', ""))

    buff = ""
    for j in range(3):
        if len(contacts_list[i][j]) > 1:
            buff += " " + contacts_list[i][j]
    name.append((buff))
    organisation.append(contacts_list[i][3])
    position.append(contacts_list[i][4])
    email.append(contacts_list[i][6])

for i in range(len(phone)):
    if phone[i]:
        phone[i] = '+7' + '(' + phone[i][1:4] + ')' + phone[i][3:]

    if len(phone[i]) > 15:
        phone[i] = phone[i][0:15] + ' доб.' + phone[i][15:]
# print(phone)

result_list = zip(name, organisation, position, phone, email)
result_list = list(result_list)
# print(result_list)

for i in range(len(result_list)):
    result_dict[" ".join(result_list[i][0].split()[0:2])] = {'last_name': " ".join(result_list[i][0].split()[0:1])}
    result_dict[" ".join(result_list[i][0].split()[0:2])].update(
        {'first_name': " ".join(result_list[i][0].split()[1:2])})
    result_dict[" ".join(result_list[i][0].split()[0:2])].update({'surname': " ".join(result_list[i][0].split()[2:3])})
    result_dict[" ".join(result_list[i][0].split()[0:2])].update({'organization': result_list[i][1]})
    result_dict[" ".join(result_list[i][0].split()[0:2])].update({'position': result_list[i][2]})
    result_dict[" ".join(result_list[i][0].split()[0:2])].update({'phone': result_list[i][3]})
    result_dict[" ".join(result_list[i][0].split()[0:2])].update({'email': result_list[i][4]})


with open("phonebook.csv", "w", encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=",")
    datawriter.writerows(result_dict)

pprint.pprint(result_dict)