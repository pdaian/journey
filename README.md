# Journey

Journey is a script to display your photos in a randomized order, at randomized sizes.
Journey also randomized backgrounds, with automatically geometrically generated patterns
that fade into each other to compliment the atmosphere of photo browsing.

A demo of Journey is available [here](http://trip.pdaian.com/), a demo of Journey in
boring mode is available [here](http://trip.pdaian.com/?boring=1).

It supports hierarchical, recursively nested tags/albums (albums that contain albums).
It also supports private collections (any collection whose name contains the word 
`private` will not be discoverable by default).

The lowest primitive in Journey is folders, which contain photos.  To get started,
copy ``sample_config.py`` to ``config.py`` and modify the collections parameter
to map album names to folders.

The configuration also allows you to change the display style of the grid; see the
provided lambdas.

## Running Journey

To run Journey, install Python 3 then Flask with ``python3 -m pip install flask``.
Then, run Journey with ``python3 journey.py`` to serve from the Flask dev server.

Instructions for deploying with Apache/nginx follow standard Flask procedures.


## Dragons

Journey is mostly created for my use, and I make no guarantees that the code is pretty;
feel free to run and modify if the spirit compels you.

If you do manage to get this running, help with a better README is always appreciated.

