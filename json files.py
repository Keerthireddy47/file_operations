import json
import pprint

f=open("C:\\Users\\hp\\OneDrive\\Desktop\\imdb_movies.json")
movies_data=json.load(f)
f.close()
# pprint.pprint(movies_data)
d={}
# dict={"director":1}
# dict+=1
for rec in movies_data:
    if rec['director'] not in d:
        d[rec['director']] = 1
        
    else:    
        d[rec['director']] += 1
max= max(d.items(), key=lambda x: x[1])[1]
for rec_one in d:
    if d[rec_one] == max:
        print(rec_one)
        

#in dictionaries we can take value from key d={'x':1,'y':2} if we want 1 we can use d(x)
d={}
d[(1,2,3)] = 1
print(d)

import json
f=open("C:\\Users\\hp\\OneDrive\\Desktop\\imdb_movies.json")
movies_data=json.load(f)
f.close
new_dict = {}
for rec in movies_data:
    for j in rec['genre']:
        # rec['genre']=j.strip()
        if j.strip() not in new_dict:
            new_dict[j.strip()] = 1
        else:
            new_dict[j.strip()] +=1
max=max(new_dict.items(),key=lambda x:x[1])
print(max)


import json
f=open("C:\\Users\\hp\\OneDrive\\Desktop\\imdb_movies.json")
movies_data=json.load(f)
f.close()
d={}
for rec in movies_data:
    movie_name=rec['name']
    score=float(rec['imdb_score'])
    if movie_name not in d:
        d[movie_name] = score
data1=sorted(d.items(),key=lambda x: x[1],reverse=False)
print(data1[0])


import json
f=open("C:\\Users\\hp\\OneDrive\\Desktop\\imdb_movies.json")
movies_data= json.load(f)
f.close()
d=[]
for i in range(0,101):
    d.append(movies_data[i])
max=max(d,key=lambda x:x["99popularity"])
print(f"best director from top 100 movies is {max["director"]} and the rating is {max["99popularity"]}")


import json
f=open("C:\\Users\\hp\\OneDrive\\Desktop\\imdb_movies.json")
movies_data= json.load(f)
f.close()
d=[]
for i in range(0,11):
    d.append(movies_data[i])
max=max(d,key=lambda x:x["imdb_score"])
print(max)


