import csv
import re

def true_name_contact(cont):
    person = ' '.join([cont[i] for i in range(3)]).split()
    for id, val in enumerate(person):
        cont[id] = val

def true_phone_contact(cont):
    pattern = re.compile(r"(\+7|8){1}\s*\(*(\d{3})\)*\s*-*(\d{3})-*(\d{2})-*(\d{2})\s*\(*(доб\.)*\s*(\d{4})*\)*")
    subst_pattern = r"+7(\2)\3-\4-\5 \6\7"
    cont[5] = pattern.sub(subst_pattern, cont[5])

def contact_to_dict(cont_dict, cont):
    name = cont[0] + ' ' + cont[1]
    if name not in cont_dict.keys():
        cont_dict[name] = [cont[i] for i in range(2, 7)]
    else:
        cont_dict[name] = [cont[i] if cont[i] != '' else cont_dict[name][i-2] for i in range(2, 7)]

def dict_to_list(cont_dict):
    res = []
    for key, val in contacts_dict.items():
        res.append(key.split() + val)
    return res

if __name__ == '__main__':
    with open("phonebook_raw.csv", encoding='utf-8', errors='ignore') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    contacts_dict = {}
    for cont in contacts_list:
        true_name_contact(cont)
        true_phone_contact(cont)
        contact_to_dict(contacts_dict, cont)

    with open("phonebook.csv", "w", encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(dict_to_list(contacts_dict))