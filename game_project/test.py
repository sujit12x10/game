from collections import OrderedDict

dict = {
    'SRH': {'total_matches': 12, 'wins': 8, 'losses':4},
    'RCB': {'total_matches': 12, 'wins': 7, 'losses':4},
    'KKR': {'total_matches': 12, 'wins': 9, 'losses':4},
        }

d_asc = OrderedDict(sorted(dict.items(), key=lambda kv:kv[1]['wins'], reverse=True))
print(d_asc)


