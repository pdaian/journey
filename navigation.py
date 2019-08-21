import copy
from config import collections

def resolve_recursive(collections):
    for collection in collections:
        toresolve = set()
        for path in collections[collection]:
            if path in collections:
                toresolve.add(path)
        for path in toresolve:
            collections[collection].remove(path)
            collections[collection] += collections[path]
        if len(toresolve) > 0:
            return resolve_recursive(collections)

collections['~super'] = set()
for collection in collections:
    if 'private' in collection:
        continue
    for path in collections[collection]:
        collections['~super'].add(path)
collections['~super'] = list(collections['~super'])

processedcollections = copy.deepcopy(collections)
resolve_recursive(processedcollections)
