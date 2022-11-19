homerseklet= [0,12,13,9,2,7]
csokken = []

i = 0
while i < len(homerseklet)-1:
    if homerseklet[i+1]  <= homerseklet[i]-3:
        print(f"oktober  {i+2}" )
        print(homerseklet[i+1])
    i += 1

# az első olyan napot írja ki amikor 3-mal csökken a hőmérséklet

i= 0
while i < len(homerseklet)-1 and homerseklet[i]-homerseklet[i+1] <= 3 :
    i += 1
#ciklus vége
