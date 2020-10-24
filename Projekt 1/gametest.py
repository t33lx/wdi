import json

nick=input("nick: ")
counter=input("counter: ")
counter=int(counter)

bestscores={}
with open('ranks.txt', 'w') as f:
    json.dump(bestscores,f)
with open('ranks.txt') as f:
    data=json.load(f)
bestscores.update(data)
bestscores.update({nick : counter})
with open('ranks.txt', 'w') as f:
    json.dump(bestscores,f)

with open('ranks.txt') as f:
    data=json.load(f)
print(data)