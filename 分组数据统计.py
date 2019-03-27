

def fenzu(final_3_list):
    target_dict = {}
    for a, e, c in final_3_list:
        if a in target_dict:
            if target_dict[a][0] >e:
                target_dict[a] = [e, c]

        # if a in target_dict and target_dict[a][0] < e:
        #     continue
        target_dict[a] = [e, c]

    print(target_dict)

    group = {}
    for _, v in target_dict.items():
        if v[1] not in group:
            group[v[1]] = 1
        else:
            group[v[1]] += 1
    print(group)
    return group

final_3_list = [
                ('a', 1, 1),
                ('b', 1, 1),
                ('c', 1, 1),
                ('d', 1, 1),
                ('e', 1, 1),
                ('a', 2, 1),
                ('a', 3, 1),
                ('b', 2, 4),
                ('c', 1, 1),
                ('a', 5, 6),
]


# group = fenzu(final_3_list)
# print(group)
group = {}
target_dict = {'a': [5, 6], 'b': [2, 4], 'c': [1, 1], 'd': [1, 1], 'e': [1, 1]}
for k, v in target_dict.items():
    group_count = v[1]
    if group_count not in group:
        group[group_count] = 1
    else:
        group[group_count] += 1
print(group)


group = {
    '1': 0, '2': 0, '3': 0, '4': 0,
    '5': 0, '6': 0, '3': 0, '4': 0,
    '1': 0, '2': 0, '3': 0, '4': 0,
    '1': 0, '2': 0, '3': 0, '4': 0,
    '1': 0, '2': 0, '3': 0, '4': 0,
    '5': 0,
    '6': 0,
    '7': 0,
    '8': 0,
    '9': 0,
    '': 0,
    '1': 0,
    '1': 0,
    '1': 0,
    '1': 0,
}