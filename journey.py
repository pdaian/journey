from flask import Flask, escape, request, render_template
import os, copy, random
import config
from navigation import collections, processedcollections

app = Flask(__name__)

def has_in(collection):
    hin = []
    for c in collections[collection]:
        if c in collections:
            hin.append(c)
    return hin

def is_in(collection):
    iin = []
    for c in collections:
        if collection in collections[c] and not "private" in c:
            iin.append(c)
    return iin

@app.route('/<collection>')
@app.route('/', defaults = {'collection': '~super'})
def view(collection):

    order_mode = request.args.get('order')
    if order_mode is None or not "1" in order_mode:
        order_mode = False
    else:
        order_mode = True

    collection = escape(collection)
    if not collection in processedcollections:
        return 'No such collection.'

    files = []
    for path in processedcollections[collection]:
        try:
            for file in sorted(os.listdir(os.path.join('pics', path))):
                files.append(os.path.join('pics', path, file))
        except:
            print("ERROR! FAILED TO PROCESS %s!" % (path))
    if not order_mode:
        random.shuffle(files)

    # process swiggle thumbnails, remove banned files
    for file in copy.deepcopy(files):
        if ".th." in file or not file.split(".")[-1] in config.allowed_extensions:
            #files.remove(file.replace(".th.", "."))
            files.remove(file)

    randtext = random.choice(open('texts.txt').read().splitlines()).split('||')

    return render_template('view.html', collection=collection, collections=collections, files=files, randtext=randtext, random=random, order_mode=order_mode, config=config, has_in=has_in(collection), is_in=is_in(collection))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)


