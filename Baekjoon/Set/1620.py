n,m = map(int, input().split())
pokemon = dict()
pokemonN = dict()

for i in range(1,n+1):
    ii = input()
    pokemon[ii]=i
    pokemonN[i]=ii
for _ in range(m):
    ii = input()
    if ii.isdigit():
        print(pokemonN[int(ii)])
    else:
        print(pokemon[ii])