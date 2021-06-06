#CSV manipulation helper functions


def get_headers(s):
    s = s[:s.find("\n")]
    g = s.split(",")
    return g

def splitcomma(s):
    newl = list(s.split(','))
    return newl

def get_data(s):
    headerend = s.find('\n')
    s = s[headerend:]
    s = s.strip()
    line = s.split('\n')
    data = list(map(splitcomma, line))
    return data

def make_dict(data):
    d = {}
    for lists in data:
        i = 1
        values = lists[0]
        d[values] = []
        while i < len(lists):
            d[values].append(int(lists[i]))
            i += 1
    return d

def make_dict_moves(data):
    d = {}
    for lists in data:
        i = 1
        values = lists[0]
        d[values] = []
        while i < len(lists):
            d[values].append(lists[i])
            i += 1
    return d

def combine_dict(dict, headers):
    headersnomove = headers[1:]
    for key in dict.keys():
        i = 0
        newdict = {}
        while i < len(headersnomove):
            newdict[headersnomove[i]] = dict[key][i]
            i += 1
        dict[key] = newdict
    return dict
