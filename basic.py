import random
random.seed(15) # I like the number 15

class Doc:
    def __init__(self,name, tags):
        self.name = "doc-" + str(name)
        self.tags = tags
    
    def __str__(self):
        return self.name + ",tags: " + str(self.tags)
    
    def __repr__(self):
        return self.name


def initalize():
    # a list of 100 random words I generated from https://www.randomlists.com/random-words?dup=false&qty=100
    tag_list = ["connect","rate","enormous","optimal","lackadaisical","explode","furtive","maniacal","subtract","inexpensive","fall","wreck","hideous","birth","field","narrow","sense","ripe","suggestion","linen","well-groomed","divide","wandering","prickly","sink","plug","succeed","contain","doll","peel","needless","discover","locket","religion","cold","dramatic","first","zebra","visitor","remarkable","bridge","apple","juvenile","rhyme","striped","expect","men","hair","quirky","dream","minister","well-off","believe","curious","hard-to-find","fog","panoramic","true","stone","rejoice","tire","hallowed","laborer","jumpy","difficult","stranger","dangerous","appear","stormy","secretary","land","greet","jelly","tank","knowing","annoying","listen","drunk","verdant","sleep","collar","mindless","interest","erect","horrible","acoustic","yawn","makeshift","magic","arrive","spray","meeting","guiltless","third","expert","bells","squeal","phobic","bare","stay"]

    docs = []
    size = random.randint(10000,100000) # |D| roughly between 10^4 and 10^5
    for i in range(size):
        # each document has rougly 2-7 tags
        tags = random.sample(tag_list, random.randint(2,7))
        docs.append(Doc(i,tags))
    return docs, tag_list,

# problem = initalize()
# head_10 = problem[0][:10]
# for i in head_10:
#     print(i)


def brute_force(docs,tags,q):
    result = []
    for d in docs:
        is_subset = True
        for tag in d.tags:
            if not (tag in q):
                is_subset = False
                break
        if is_subset:
            result.append(d)

    return result

simple_tags = ["1", "2", "3", "4","5","6"]
simple_docs = [Doc(1,["1","2","3"]),Doc(2,["1","3","5"]),Doc(3,["2","4","5"]),Doc(4,["2","3","6"]),Doc(5,["2","5"])]
simple_q = ["1","2","3","5"]

simple_ans = brute_force(simple_docs, simple_tags, simple_q)
print(simple_ans) # should be [doc-1, doc-2, doc-5]


print("----------------------------")

    
problem = initalize()
q = random.sample(problem[1], random.randint(10,40))
ans = brute_force(problem[0], problem[1], q)

print("There are " + str(len(ans)) + " documents have tags under q")

# let's check it's correct
print("q: " + str(q))
selected = random.sample(ans, 5)
for i in selected:
    print(i)
