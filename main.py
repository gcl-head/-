from pypinyin import lazy_pinyin
from copy import deepcopy


def get_idioms():
    file = open('idiom.txt', 'r')
    idiom = file.readlines()
    for (index, i) in enumerate(idiom):
        idiom[index] = i.strip()
    return idiom


def find_next_idioms(idiom):
    tail = lazy_pinyin(idiom[-1])[0]
    if tail == target_head:
        return {target}
    re = set()
    if tail in tails:
        return re
    for i in idioms:
        if lazy_pinyin(i[0])[0] == tail:
            re.add(i)
    tails.add(tail)
    return re


def get_route(idiom, route):
    # idiom 当前成语
    # route 加入了当前成语的成语接龙路径
    next_idioms = find_next_idioms(idiom)
    # print(next_idioms)
    if len(next_idioms) == 0:
        return
    if target in next_idioms:
        next_route = deepcopy(route)
        next_route.append(target)
        routes.append(next_route)
        for rou in next_route:
            print(rou+' ', end='')
        print()
        return
    for i in next_idioms:
        next_route = deepcopy(route)
        next_route.append(i)
        get_route(i, next_route)


idioms = get_idioms()  # 成语库
tails = set()  # 成语尾部拼音
routes = []  # 成语接龙路径
target = '一个顶俩'  # 目标成语
target_head = lazy_pinyin(target[0])[0]

if __name__ == '__main__':
    input_idiom = input('请输入成语：')
    # input_idiom = '头头是道'
    get_route(input_idiom, [])
    routes.sort(key=lambda elem: len(elem))
    result = open('result.txt', 'w')
    for r in routes:
        for rr in r:
            result.write(rr + ' ')
        result.write('\n')
    result.close()
    # print(routes)
