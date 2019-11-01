### Location Maps

The Location model has a field called `map_embed_code`.
The purpose of this field is to store the embed code of open street maps.
These embed codes are generated from the open street maps page. [Example](https://www.openstreetmap.org/export#map=19/33.77077/-84.35373)

Important!

The open street maps embed code is provided as an iframe.
Example:

```
<iframe width="425" height="350" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://www.openstreetmap.org/export/embed.html?bbox=-84.35519188642503%2C33.76984792852217%2C-84.35227632522583%2C33.771691836631966&amp;layer=mapnik&amp;marker=33.77076988753727%2C-84.35373410582542" style="border: 1px solid black"></iframe><br/><small><a href="https://www.openstreetmap.org/?mlat=33.77077&amp;mlon=-84.35373#map=19/33.77077/-84.35373">View Larger Map</a></small>
```

You need to change the iframe width and height values to `auto` like so: 

```
<iframe width="auto" height="auto" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://www.openstreetmap.org/export/embed.html?bbox=-84.35519188642503%2C33.76984792852217%2C-84.35227632522583%2C33.771691836631966&amp;layer=mapnik&amp;marker=33.77076988753727%2C-84.35373410582542" style="border: 1px solid black"></iframe><br/><small><a href="https://www.openstreetmap.org/?mlat=33.77077&amp;mlon=-84.35373#map=19/33.77077/-84.35373">View Larger Map</a></small>
```

Otherwise it breaks the responsive layout.


### WYSIWYG

The app now has the `django-tinymce` installed. It allows to convert textareas into WYSIWYG editors.
This also includes those im the admin site. Read the docs!
[django-tinymce documentation](https://django-tinymce.readthedocs.io/en/latest/usage.html)