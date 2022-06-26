def solution(N, stages):
    ppl = [0]*(N+1)
    
    for s in stages:
        ppl[s-1]+=1
    
    for i in range(N):
        if sum(ppl[i:])==0:
            ppl[i] = [i, 0]
        else:
            ppl[i] = [i,ppl[i]/sum(ppl[i:])]
    print(ppl)
    ppl = ppl[:-1]   
    ppl.sort(key=lambda x:(-x[1],x[0]))
    print(ppl)
    answer=[p[0]+1 for p in ppl]

    return answer