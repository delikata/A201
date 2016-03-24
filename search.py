from collections import defaultdict

input1 = '''Jack and Jill went up the hill to fetch a pail of water.
All work and no play makes Jack and Jill a dull couple.
The Manchester United Junior Athletic Club (MUJAC) karate team was super good at kicking.
The MUJAC playmaker actually kinda sucked at karate.'''

with open('255H.searchengine.input') as file:
    input2 = ''.join(file.readlines())

def common(input, n):
    dict = defaultdict(set)
    word = ''
    for i in input:
        for x in xrange(len(i) - n + 1):
            dict[i[x:x + n]].add(i)
    return dict

def search(input):
    input = set([filter(str.isalnum, x).lower() for x in input.strip().splitlines()])
    out = []
    prefixes = sorted([[-len(j), i, j] for i, j in common(input, 5).iteritems()])
    for i in xrange(len(prefixes)):
        if not input:
            break
        if not len(input.intersection(prefixes[i][2])):
            continue
        word = prefixes[i][1]
        to_remove = set([j for j in input if word in j])
        input.difference_update(to_remove)
        for p in prefixes:
            p[2].difference_update(to_remove)
            p[0] = -len(p[2])
        prefixes[i + 1:] = sorted(prefixes[i + 1:])
        out += [word]
    print len(out)
    return out

print search(input1)
print search(input2)
