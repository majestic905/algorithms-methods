n, W = map(int, input().split())
costs = [list(map(int, input().split())) for _ in range(n)]
costs.sort(key=lambda x: x[0]/x[1], reverse=True)
costs, weights = zip(*costs)

cost, i = 0, 0
while W > 0 and i < n:
    if W >= weights[i]:
        cost += costs[i]
        W -= weights[i]
    else:
        cost += costs[i]/weights[i]*W
        W = 0
    i += 1

print('%.3f' % cost)