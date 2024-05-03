def get_values(s):
    g = s.split()
    q = []
    for a in g:
        q.append(int(a))
    return q
print(get_values('90 99 97 89'))

def get_vals_list(s):
    g = s.split('\n')
    q = []
    for a in g:
        q.append('[' + a + ']')
    return q
print(get_vals_list("""90 99 97 89
91 94 99 89
81 94 100 100
90 99 79 81
50 79 49 41
90 99 94 94"""))

def get_averages(s):
    g = s.split(',')
    q = []
    for a in g:
        q.append(sum(a))
    return q
print(get_averages([[90, 99, 97, 89],
  [91, 94, 99, 89],
  [81, 94, 100, 100],
  [90, 99, 79, 81],
  [50, 79, 49, 41],
  [90, 99, 94, 94]]))