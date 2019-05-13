#Your task is to find the path through the field which has the lowest cost to go through.

#As input you will receive:
#1) a toll_map matrix (as variable t) which holds data about how expensive it is to go through the given field coordinates
#2) a start coordinate (tuple) which holds information about your starting position
#3) a finish coordinate (tuple) which holds information about the position you have to get to

#As output you should return:
#1) the directions list


#Implementation of Dijsktra's algorithm
import bisect

def cheapest_path(t, start, finish):
    rows = len(t)
    cols = len(t[0])
    visited=[[0 for j in range(cols)] for i in range(rows)]
    dist = {}
    prior = {}
    dist[start] = 0
    frontier = [(start, 0)]
    finish_neighbors = [(finish[0], finish[1] + 1), (finish[0], finish[1] - 1), (finish[0] + 1, finish[1]),
                        (finish[0] - 1, finish[1])]

    finish_neighbors = [f for f in finish_neighbors if f[0] >= 0 and f[0] < rows and f[1] >= 0 and f[1] < cols]

    while (len(frontier) > 0):
        current1 = frontier.pop(0)
        current = current1[0]
        curr_dist = current1[1]
        visited[current[0]][current[1]]==1
        if current == finish or (len(finish_neighbors) == 0):
            break

        try:
            finish_neighbors.remove(current)
        except:
            pass

        temp = [(current[0], current[1] + 1), (current[0], current[1] - 1), (current[0] + 1, current[1]),
                (current[0] - 1, current[1])]
        temp = [f for f in temp if f[0] >= 0 and f[0] < rows and f[1] >= 0 and f[1] < cols]

        for neighbor in temp:
            old_dist = dist.get(neighbor, float('Inf'))
            if curr_dist + t[current[0]][current[1]] < old_dist:
                try:
                    frontier.remove((neighbor, old_dist))
                except:
                    pass
                new_dist = curr_dist + t[current[0]][current[1]]
                dist[neighbor] = new_dist
                prior[neighbor] = current
                if visited[neighbor[0]][neighbor[1]]==0:
                   if len(frontier) == 0:
                        frontier = [(neighbor, new_dist)]
                   else:
                        keys = [k[1] for k in frontier]
                        curr_index = bisect.bisect_left(keys, new_dist)
                        frontier[curr_index:curr_index] = [(neighbor, new_dist)]

    out = []
    current = finish
    while (current != start):
        (x, y) = prior.get(current)
        if (x < current[0]):
            out = ["down"] + out
        elif (x > current[0]):
            out = ["up"] + out
        elif (y < current[1]):
            out = ["right"] + out
        else:
            out = ["left"] + out
        current = (x, y)

    return out  # directions

def main():
    t=[[1, 9, 1], [2, 9, 1], [2, 1, 1]]
    start=(0,0)
    finish=(0,1)
    print(cheapest_path(t, start, finish))

if __name__=="__main__":
    main()

