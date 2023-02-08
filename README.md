# Tagged-Document-Lookup
This is a project topic provided when applying for Queen's Mu lab interview

Here's the Problem
Tagged Document Lookup

Imagine you have a set of documents D and a set of tags T that can be associated with them. 
You can assume that |D| is around 10^4 to 10^5 and |T| is roughly 100. 
For each document d ∈ D, the tags for that document, t_d ⊆ T, has a size of roughly 2-7.

Unlike the normal document retrieval setting, we don’t want the set of documents that match a single given tag. Rather, given a set of tags q ⊆ T (with |q| anywhere from 10 to 40), we would like to return all documents that have all of their tags in the set:
    query(D,T,q)={d|t_d ⊆ q}
For this question, you don’t really need to be concerned with what’s in the documents, or what the tags actually are (treat 
D and T as just two sets of objects). The task for this problem is to implement the query procedure.


# Result
running measure.py the first time
I get this result
When n is: 100
Basic solution time: 0.3513009920134209
Smart solution time: 0.3202114140149206
When n is: 200
Basic solution time: 2.4467377639957704
Smart solution time: 0.763522985012969
When n is: 500
Basic solution time: 2.354874929005746
Smart solution time: 1.2695786299882457
When n is: 1000
Basic solution time: 9.498742081021192
Smart solution time: 6.216420765005751