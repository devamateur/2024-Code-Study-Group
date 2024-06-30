def solution(cacheSize, cities):
    answer = 0
    st = []
    
    for city in cities:
        st.append(city.lower())
        
        # 캐시크키보다 작거나 같을때
        if len(st) <= cacheSize:
            # cache hit
            if st[-1] in st[:-1]:
                answer += 1
            # cache miss
            else:
                answer += 5
        
        # 캐시크기보다 클 때
        if len(st) > cacheSize:
            # cache hit
            if st[-1] in st[:-1]:
                answer += 1
                st.pop(st.index(st[-1]))
            # cache miss
            else:
                answer += 5
                st.pop(0)

    return answer