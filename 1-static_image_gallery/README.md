
# static_image_gallery project

For information about installing django and setting up the required virtual environments, etc. see ../README.md .

For information about how to use startproject, startapp, etc. see the ../0-hello_world/startproject subdirectory.

## static_image_gallery - goals

Keep in mind that the main goal is get a django site running on my server, no matter how simplistic, asap.

1. Learn how to get views.py and urls.py to work together
2. Have something minimal to host at groja.com
3. Lay the mental groundwork for building something that uses models or PIP or both

#### For future reference

Googling for python image gallery tutorials I found some links which may be useful for the next project.

Having vetted some of the search results and identified these as interesting, just thought that I'd save them here.

* http://eflorenzano.com/blog/2006/12/20/writing-gallery-app-part-one/  ## lots of information about models, that looks good
* http://grasshopperpebbles.com/django-python/creating-a-photo-gallery-with-django-and-jquery/  ## mobile-friendly, using jQueryMoble(!?)

Not tutorials but look to be useful:

* http://stackoverflow.com/questions/11166156/how-to-create-a-django-image-gallery
* https://github.com/samuelmh/django-smh_gallery

But seriously, first things first, and that is hosting a minimal django site.

## Requirements

### Pages

The Static Image Gallery shall contain the following pages, with content as described.

* Home Page: static; briefly describe what the site is about and include a self-portrait
* List of Galleries: driven by JSON data
* Set of GRoJA Images: driven by JSON data
* Single Image Page: contains the image, its title and description (and navigation) only
* About: static; more information, and links to other sites and a Contact Me page

This is the bulk of the project: routes (urls) and views.

### Navigation and urls

KISS is how we want to play it, through and through.

* Home page: `**home**
* Generics: `**generics**
* Celebrities: `**celebrities**
  * Politicians: `**celebrities/politicians**
  * TV Shows: `**celebrities/tv_shows**
  * Historical: `**celebrities/historical**
* About: `**about**

### Page Layouts

KISS is the key here.  All pages shall contain:

* navigation and
* content

ONLY.

### Data

Lists of images shall be stored in JSON format.

### Devices

* Keep layouts as simple as possible.
* Use minimal media queries.
* Probably want to use bootstrap to build columns of images
* No need for device detection at this time.

#### Bonus Extra Credit!

Have navigation shrink into a hambuger menu icon on small screen sizes.

### Design

Most of the site's design is determined by django.

* Single project: `**static_image_gallery**
* Single app: `**groja_gallery**

Views: TBD.

### Masterplan

Be mindful that the masterplan is to do something very similar using Node.js and React.

E.g., be on the lookout for opportunities to share non-react-dependent JavaScript, HTML, or CSS between the two!


