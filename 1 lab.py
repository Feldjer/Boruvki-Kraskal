top = 0
new_massive = []
global_list = []
mas_edge = []
mas = []
string = massive = ""

def delete_dubler(fragment, massive):
    global new_massive
    count = 0
    fragment = [fragment[1], fragment[0], fragment[2]]
    for i in massive:
        if i == fragment:
            new_massive = massive[0:count] + massive[count+1:]
            break
        count += 1
    return new_massive

while True:
    string = input()
    if "32767" in string:
        massive += string
        break
    elif " " in string:
        massive = massive + string + " "
    else:
        count = int(string)
massive = massive.split(" ")
for i in range(len(massive)):
    if int(massive[i]) == count:
        break
    else:
        link = int(massive[i]) - 1
        gap = int(massive[i+1]) - int(massive[i])
        mas.append(massive[link:link+gap])

for i in range(len(mas)):
    mas_edge.append(i+1)

for i in mas:
    top += 1
    stop = 0
    for j in i:
        stop += 1
        if stop == 2:
            lister.append(int(j))
            global_list.append(lister)
            stop = 0
        else:
            lister = [top, int(j)]
global_list = sorted(global_list, key=lambda edge: edge[2])

for i in range(len(global_list)//2):
    global_list = delete_dubler(global_list[i], global_list)

summa = 0
mas_edge_print = []
for i in range(len(mas_edge)):
    mas_edge_print.append([])

mas = []
top_first = False
top_second = False
for i in global_list:
    flagPass = False
    if i[0] in mas_edge:
        mas_edge.remove(i[0])
        top_first = True
    if i[1] in mas_edge:
        mas_edge.remove(i[1])
        top_second = True
    if top_first and top_second:
        mas.append([i[0], i[1]])
        summa += i[2]
        top_first = False
        top_second = False
    elif top_first:
        for j in mas:
            if i[1] in j:
                j.append(i[0])
                summa += i[2]
                top_first = False
                top_second = False
    elif top_second:
        for j in mas:
            if i[0] in j:
                j.append(i[1])
                summa += i[2]
                top_first = False
                top_second = False
    else:
        flagPass = True
    if not flagPass:
        mas_edge_print[i[0]-1].append(i[1])
        mas_edge_print[i[1]-1].append(i[0])
    if not mas_edge:
        break

if len(mas) > 1:
    count = len(mas) - 1
    counter = 0
    for i in global_list:
        control_first_final = 0
        control_first = 0
        control_second_final = 0
        control_second = 0
        for j in mas:
            control_first += 1
            if i[0] in j:
                control_first_final = control_first
            control_second += 1
            if i[1] in j:
                control_second_final = control_second
        if control_first_final != control_second_final:
            summa += i[2]
            counter += 1
            mas_edge_print[i[0]-1].append(i[1])
            mas_edge_print[i[1]-1].append(i[0])
            mas.append(mas[control_first_final-1] + mas[control_second_final-1])
            mas.remove(mas[control_first_final-1])
            if control_second_final != 1:
                mas.remove(mas[control_second_final-2])
            else:
                mas.remove(mas[control_second_final-1])
        if count == counter:
            break

string = ""
for i in mas_edge_print:
    i.sort()
    for j in i:
        string = string + str(j) + " "
    string = string + "0 \n"
string = string + str(summa)

print(string)
