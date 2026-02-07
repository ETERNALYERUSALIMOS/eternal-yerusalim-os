from googlesearch import search
for q in ["масляные духи BESTPARFUM", "купить масляные духи"]:
    print(q, list(search(q, num=5)))
