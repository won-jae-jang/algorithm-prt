from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)
        
    answer = len(dist) + 1
    for friends in permutations(dist, len(dist)):
        for start in range(length):
            count = 1
            distance = weak[start] + friends[count - 1]
            for i in range(start + 1, start + length):
                if weak[i] <= distance:
                    continue
                else:
                    count += 1
                    if count > len(dist):
                        break
                    distance = weak[i] + friends[count - 1]
                    
            answer = min(answer, count)
    if answer > len(dist):
        return -1
    else:
        return answer
    
            
solution(12, [1, 5, 6, 10], [1, 2, 3, 4])