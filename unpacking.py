l1 = ["a","b","c","d"]

w,x,y,z = l1 #unpacking all the item in list and adding them in w,x,y,z respectivly
print(w,x,y,z)

config = ("name","123","https//www.com")
username,password,url = config #unpacking tuple and adding them in respective username,password,url
print(username,password,url)

config = ("name","123","https//www.com")
*dummy,url = config # last one will be added to url and renaming first 2 will be add to dummy
print(url)

fruits = ['apple','juice','water','banana']
apple,_,_,banana = fruits
fruits1 = ['apple','juice','water','banana']
firstfruit,*l,lastfruit = fruits1
print(apple,banana)
print(firstfruit,lastfruit,l)