def do(string):
    res = []
    for s in set(string):
        counter = 0
        for ss in string:
            if s == ss:
                counter += 1
        res.append(f'{s} = {counter}')
    return res


def power(s):
    result = {}
    for ss in s:
        result[ss] = result.get(ss, 0)+1
    for k, s in result.items():
        print(k, s)


power('aaabbbstrr')
