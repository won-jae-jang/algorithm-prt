from bisect import bisect_left, bisect_right

def count_by_range(array, left, right):
    left_index = bisect_left(array, left)
    right_index = bisect_right(array, right)
    return right_index - left_index

def solution(words, queries):
    length = len(words)
    right_words = [[] for _ in range(length + 1)]
    reversed_words = [[] for _ in range(length + 1)]
    for word in words:
        right_words[len(word)].append(word)
        reversed_words[len(word)].append(word[::-1])
    
    for i in range(2, length + 1):
        right_words[i].sort()
        reversed_words[i].sort()
    
    result = []
    for query in queries:
        #접두사에 와일드카드 문자가 붙은 경우
        if query[0] == '?':
            query = query[::-1] #문자열 뒤집기
            left = query.replace('?', 'a')
            right = query.replace('?', 'z')
            result.append(count_by_range(reversed_words[len(query)], left, right))
        #접미사에 와일드 카드가 붙은 경우
        else:
            left = query.replace('?', 'a')
            right = query.replace('?', 'z')
            result.append(count_by_range(right_words[len(query)], left, right))    
            
    return result

solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
         ["fro??", "????o", "fr???", "fro???", "pro?"])