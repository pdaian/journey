import copy
from config import collections

def resolve_recursive(collections):
    done = True
    for collection in collections:
        toresolve = set()
        for path in collections[collection]:
            if path in collections:
                # If collection contains path that is itself collection, expand out full file paths
                # We only process nodes that are sinks each round, to ensure sorts propagate across the DAG
                is_sink = True
                for subpath in collections[path]:
                    if subpath in collections:
                        is_sink = False
                if is_sink:
                    toresolve.add(path)
                    done = False
        for path in toresolve:
            for subpath in collections[path]:
                # expand subpaths while preserving order
                collections[collection].insert(collections[collection].index(path), subpath)
            collections[collection].remove(path)
    if not done:
        resolve_recursive(collections)

collections['~super'] = []
for collection in collections:
    if 'private' in collection:
        continue
    for path in collections[collection]:
        if not path in collections['~super']:
            collections['~super'].append(path)

processedcollections = copy.deepcopy(collections)
resolve_recursive(processedcollections)
print(processedcollections)
print(processedcollections.keys())
