from flask import Flask, escape, request, render_template
import os, copy, random
import config
from navigation import collections, processedcollections

app = Flask(__name__)


@app.route('/<collection>')
@app.route('/', defaults = {'collection': '~super'})
def view(collection):

    boring_mode = request.args.get('boring')
    if boring_mode is None or not "1" in boring_mode:
        boring_mode = False
    else:
        boring_mode = True

    collection = escape(collection)
    if not collection in processedcollections:
        return 'No such collection.'

    files = []
    for path in processedcollections[collection]:
        for file in sorted(os.listdir(os.path.join('pics', path))):
            files.append(os.path.join('pics', path, file))
    if not boring_mode:
        random.shuffle(files)

    randtext = random.choice(open('texts.txt').read().splitlines()).split('||')

    return render_template('view.html', collection=collection, collections=collections, files=files, randtext=randtext, random=random, boring_mode=boring_mode, config=config)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)


