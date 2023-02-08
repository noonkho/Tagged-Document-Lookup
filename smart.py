import random
import math

random.seed(15) # I like the number 15

# Generate a list of primes from https://stackoverflow.com/questions/1628949/to-find-first-n-prime-numbers-in-python
# Seems like this is O(n^2) but we don't consider this part
def prime(i, primes):
    for prime in primes:
        if not (i == prime or i % prime):
            return False
    primes.add(i)
    return i

def historic(n):
    primes = set([2])
    i, p = 2, 0
    while True:
        if prime(i, primes):
            p += 1
            if p == n:
                return primes
        i += 1

# Test if the functions above work or not
# primes = historic(10)
# print(primes)
# print(type(primes))
# print(len(primes))

class Doc:
    def __init__(self,name, tags_primes):
        self.name = "doc-" + str(name)
        self.tags = [i[0] for i in tags_primes]
        self.product = math.prod([i[1] for i in tags_primes])
    
    def __str__(self):
        return self.name + ", prod=" + str(self.product) + " ,tags: " + str(self.tags)
    
    def __repr__(self):
        return self.name
    

def initalize():
    # a list of 100 random words I generated from https://www.randomlists.com/random-words?dup=false&qty=100
    tag_list = ["connect","rate","enormous","optimal","lackadaisical","explode","furtive","maniacal","subtract","inexpensive","fall","wreck","hideous","birth","field","narrow","sense","ripe","suggestion","linen","well-groomed","divide","wandering","prickly","sink","plug","succeed","contain","doll","peel","needless","discover","locket","religion","cold","dramatic","first","zebra","visitor","remarkable","bridge","apple","juvenile","rhyme","striped","expect","men","hair","quirky","dream","minister","well-off","believe","curious","hard-to-find","fog","panoramic","true","stone","rejoice","tire","hallowed","laborer","jumpy","difficult","stranger","dangerous","appear","stormy","secretary","land","greet","jelly","tank","knowing","annoying","listen","drunk","verdant","sleep","collar","mindless","interest","erect","horrible","acoustic","yawn","makeshift","magic","arrive","spray","meeting","guiltless","third","expert","bells","squeal","phobic","bare","stay"]
    primes = sorted(list(historic(len(tag_list)))) # should be 100 primes

    tags_prime_list = list(zip(tag_list, primes))

    docs = []
    size = random.randint(10000,100000) # |D| roughly between 10^4 and 10^5
    for i in range(size):
        # each document has rougly 2-7 tags
        tags_primes = random.sample(tags_prime_list, random.randint(2,7))
        docs.append(Doc(i,tags_primes))
    return docs, tags_prime_list


def smart(docs,tags,q): # should be O(n)
    result = []
    q_prod = math.prod([i[1] for i in q])
    for d in docs:
        if q_prod % d.product == 0:
            result.append(d)

    return result


simple_tags = [("1",2), ("2",3), ("3",5), ("4",7), ("5",11),("6",13)]
simple_docs = [Doc(1,[("1",2),("2",3),("3",5)]),Doc(2,[("1",2),("3",5),("5",11)]),Doc(3,[("2",3),("4",7),("5",11)]),
                Doc(4,[("2",3),("3",5),("6",13)]),Doc(5,[("2",3),("5",11)])]
simple_q = [("1",2), ("2",3), ("3",5), ("5",11)]

simple_ans = smart(simple_docs, simple_tags, simple_q)
print(simple_ans) # should be [doc-1, doc-2, doc-5]

print("----------------------------")

problem = initalize()
q = random.sample(problem[1], random.randint(10,40))
ans = smart(problem[0], problem[1], q)

print("There are " + str(len(ans)) + " documents have tags under q")

# let's check it's correct
print("q: " + str([i[0] for i in q]))
selected = random.sample(ans, 5)
for i in selected:
    print(i)