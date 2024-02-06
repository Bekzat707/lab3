movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]



def oces(movies):
    name=input("Name:")
    for i in movies:
        if(name==i["name"]):
            if(i["imdb"]>5.5):
                print("True")

oces(movies)



def sublist(movies):
    name=input("Name:")
    for i in movies:
        if(name==i["name"]):
            if(i["imdb"]>5.5):
                print(i)

sublist(movies)



def category(movies):
    category=input("Category:")
    for i in movies:
        if category==i["category"]:
            print(i["name"])

category(movies)



def average_for_name(list,movies):
    array=list
    sum=0
    for i in movies:
        for j in array:
            if i["name"]==j:
                sum+=i["imdb"]
    
    print("Average IMDB-",sum/len(array))

array=["We Two","Exam"]
average_for_name(array,movies)



def average_for_category(list,movies):
    array=list
    sum=0
    s=0
    for i in movies:
        for j in array:
            if i["category"]==j:
                sum+=i["imdb"]
                s+=1
    
    print("Average IMDB-",sum/s)

array=["Romance","Action"]
average_for_category(array,movies)
