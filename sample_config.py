import random

""" List of collections to display; each collection ID maps to a list of directories or other collections containing pictures for that collection
 (eg, below, the collection w id 'minneawaska' contains folder 'minneawaska19';
    the collection 'hiking' also contains the collection 'minneawaska' and therefore recursively all photos in the folder 'minneawaska19')

 NOTE: collection names must therefore have names distinct from folder names.
"""
collections = {'minneawaska': ['minneawaska19'], 'devilspath': ['devil_take1'], 'hiking': ['devilspath, minneawaska']}

""" Title of HTML page to display """
page_title = "Phil's Journey"


""" Style function for scrapbook mode; determines image styles on page.

We show how to build a style function out of a function that computes a random image width and two that compute random paddings.
Our function style_function is a lambda that encases both and runs them to resolve random values as the page is built.
"""
# (these are optional utility methods)
width_function = lambda : str(int(40 + random.random() * 20 + random.choice([0,1]) * (random.random() * 60 - 5))) + "em"
padding_left_function = lambda : str(10 * random.random() + random.choice([0,0,1]) * 20 * random.random())  + "%"
padding_top_function = lambda : str(10 * random.random()) + "%"
# (this is the relevant config item)
random_style_function = lambda: "width: " + width_function() + "; padding-left: " + padding_left_function() + "; padding-top: " + padding_top_function() + "; max-width: 100%;"

""" Style function for boring mode (whenever ?boring=1 is added to URLs) """
boring_style_function = lambda : "max-width: 90%; max-height: 100%;"

""" Extensions that will be displayed on the site """
allowed_extensions = ["jpg", "png", "JPG"]

sort_by_filename = lambda y : y.split('/')[-1]
custom_sorts = {'hiking': sort_by_filename}





