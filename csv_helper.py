#CSV manipulation helper functions


def get_headers(s):
    s = s[:s.find("\n")]
    g = s.split(",")
    return g
    
def get_data(s):
    s = s[s.find("\n")+1:]
    data = s.split("\n")
    i = 0
    while i < len(data):
        data[i] = data[i].split(",")
        i += 1
    return data
    
def make_dict(data):
    d = {}
    for x in data:
        y = x[0]
        x.remove(y)
        d[y] = x
    return d

def combine_dict(dict, headers):
    temp_dict = {}
    for x in dict:
        g = dict[x]
        i = 0
        while i < len(g):
            temp_dict[headers[i]] = g[i]
            i += 1
        year_dict[x] = temp_dict
        dict = {}
    return dict
