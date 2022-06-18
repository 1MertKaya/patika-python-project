l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
l2 = []

def flatten(x):
    for _ in x:
        if isinstance(_, list):
            flatten(_)
        else:
            l2.append(_)

flatten(l)

print(l2)