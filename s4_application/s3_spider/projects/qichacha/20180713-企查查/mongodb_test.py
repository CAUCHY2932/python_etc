
import pymongo


MONGO_URL='localhost'

client = pymongo.MongoClient(MONGO_URL, connect=False)
for item in [str(x) for x in range(3)]:
    
    MONGO_DB=item
    db = client[MONGO_DB]
    for item2 in [str(y) for y in range(3)]:
        MONGO_TABLE=item2
        for item3 in [str(z) for z in range(3)]:
            item3={item3:item3}
            db[MONGO_TABLE].insert(item3)
