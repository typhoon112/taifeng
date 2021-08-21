import json
with open("zjwater2010_2020.json") as f:
    d = json.load(f)
s = set()
for k, v in d.items():
    c = 0
    for t in v:
        for x in t:
            if x == -1:
                c += 1
                break
    if c >= 4:
        s.add(k)
for k in s:
    del d[k]
for k, v in d.items():
    h = [len(list(filter(lambda x: x == -1, t))) == 0 for t in v]
    l = len(v)
    for t in v:
        m = dict()
        for i, b in enumerate(h):
            if not b:
                c = 0
                n = [0] * 5
                for p in [-2, -1, 1, 2]:
                    if 0 <= i + p < l and h[i + p]:
                        c += 1
                        for j in range(5):
                            n[j] += v[i + p][j]
                for j in range(5):
                    n[j] /= c
                m[i] = n
        for i, n in m.items():
            v[i] = n
with open("zjwater.json", "w") as f:
    json.dump(d, f)