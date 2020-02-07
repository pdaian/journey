import copy, os
from config import collections, custom_sorts

def expand_sinks(collections):
    for collection in collections:
        is_sink = True
        should_expand = False
        for path in collections[collection]:
            if path in collections:
                # only expand sinks (collections that point to other collections)
                is_sink = False
            if os.path.isdir(os.path.join('pics', path)):
                # only expand paths that contain a directory
                should_expand = True
        if is_sink and should_expand:
            files = []
            for path in collections[collection]:
                if os.path.isdir(os.path.join('pics', path)):
                    for file in sorted(os.listdir(os.path.join('pics', path))):
                            files.append(os.path.join('pics', path, file))
                else:
                    files.append(path)
            if collection in custom_sorts:
                sort_function = custom_sorts[collection]
                files = sorted(files, key=sort_function)
                print("Sorted", collection, "by", sort_function)
            print("Expanded", collection)
            collections[collection] = files

def resolve_recursive(collections):
    expand_sinks(collections)
    done = True
    for collection in collections:
        toresolve = []
        for path in collections[collection]:
            if path in collections:
                # If collection contains path that is itself collection, expand out full file paths
                # We only process nodes that are sinks each round, to ensure sorts propagate across the DAG
                is_sink = True
                for subpath in collections[path]:
                    if subpath in collections:
                        is_sink = False
                        break
                if is_sink:
                    toresolve.append(path)
                    done = False
        for path in toresolve:
            for subpath in collections[path]:
                # expand subpaths while preserving order
                collections[collection].insert(collections[collection].index(path), subpath)
            collections[collection].remove(path)
        if len(toresolve) > 0:
            print("Processed", collection, toresolve)
    if not done:
        resolve_recursive(collections)
    else:
        expand_sinks(collections)

collections['~super'] = []
for collection in collections:
    if 'private' in collection:
        continue
    for path in collections[collection]:
        if not path in collections['~super']:
            collections['~super'].append(path)

processedcollections = copy.deepcopy(collections)
resolve_recursive(processedcollections)
