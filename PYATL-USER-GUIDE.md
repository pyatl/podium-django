This user guide is meant for the functionality of the pyatl website (in the `pyatl` directory).

All content is meant to be created through the django admin.
The page design is mobile first.

## Events

An `Event` represents a date and time when the group has scheduled to meet.
Events can be online and offline.

**Important**

When creating events through the django admin:

- Know that the backend is setup to be timezone aware.
- Note that the datetimes in the admin are in `UTC`.
- The datetime widget will tell you how many hours from `UTC` you are. The info is displayed under the widget.
- Make sure to enter all event datetimes in UTC

Examples:

You are creating an event for the 14th of November at 7:00 PM.
Count how many hours from UTC that would be. 
Atlanta falls under the `America/New_York` timezone which is -4:00 (-5:00 during Daylight Savings Time) from UTC.
That means that you should create the event in the future: 7:00 PM plus whatever hours the UTC offset will be.
When this guide was created, Daylight Savings Time was happening. So it would be 7:00 PM plus 5 hours difference. Meaning that you would
create the event for the 15th of November at 00:00:00 hours.

The templates are timezone aware and will display the datetimes as the `America/New_York` timezone.


The event admin allows you to provide two types of event descriptions:

- Short description
- Description

#### Short description

The short description is the event's description, but in tweetable form.
It is limited to 280 characters and must be plain text (no HTML).
It is also used for the twitter cards and event invites
This is an important field. 

#### Description

The event description is simply what the event is about and what will happen.
Please include the talks schedule or any detail deemed important.
The description uses a TinyMCE WYSIWYG as the widget.


## Invites

Event calendar invites (in .ics format) can be downloaded from the event page.
The invite will include:

- The event start time (with date)
- The event end time (with date)
- Whatever was written in the `short_description` field
- A link to the event page on the pyatl website
- A link to the event's location page on the pyatl website


## Locations

A `location` represents a place where an event takes place. It can be online or offline.
An example of an offline location is Manuel's Tavern.
The locations description provides WISIWYG funcitonality.

The Location has a field called `map_embed_code` for offline locations. Online locations can simply have their URL posted in the description.
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

## Pages

A page is a simple WISIWYG enabled content type meant to share general information
with members without the need to create new HTML template. Pages need to be published in order to be accessible.

There is no way to see all the published pages at once. This was done on purpose to avoid turning this feature
into a defacto blogging engine.

Links to published pages can be made to show in the footer by checking the `footer link` option.

A example of a page that would show in the footer would be a code of conduct page.
