# blender-real-starfield
Make a starfield in Blender 3D using the real positions of stars in our cosmic neighborhood

Let's say you're writing a sci-fi story and you want it to be as realistic as possible, so you want to consider the positions of real stars near Earth when talking about how long it takes to get from one place to another, and to help your characters make decisions about where to go and where to avoid. There are plenty of amazing star maps available, but they all show how the night sky looks from Earth. Astronomers can deduce the distance of each star from Earth using parallax for near stars and spectral analysis for distant stars, and the position in the night sky gives us a direction (right ascension and declination). With a direction vector and a distance, we should be able to assign 3D coordinates to every star (within a certain error range).

There are fewer star maps that show what we want, and most aren't highly configurable. It would be much better if we could import a list of authentic star coordinates into Blender and create a marker at each place. Then we can create any star map we want; and more importantly, we can rotate, zoom, and pan, to get the "lay of the land" (or galaxy, in this case). We also need some basic stats like the brightness and mass of each star.

But most star lists are formatted for use by professional astronomers, researchers, and academics. There are many subtle problems around measuring star data, and since the techniques for removing different sources of distortion are active research fields, usually you'll find the "original measured" value rather than the "corrected" value for things like position and brightness. The main issue here is that the majority of lists published by academia don't give us the ready-baked 3D coordinates and brightness values we need. Fortunately, a community of hard-working volunteers have compiled some databases for us non-specialists, and those in turn have been gathered and formatted by David Nash (astronexus.com):
https://github.com/astronexus/HYG-Database

These lists have XYZ coordinates and brightness for each star! All we need to do is figure out the format, read it into Blender, and render our stars!

# To make a real 3D starfield in Blender:

# Get the latest version of the HYG star list:
~$ git clone https://github.com/astronexus/HYG-Database.git

We will use the smaller HYG list at:

HYG-Database/hyg/v3/hyg_v35.csv 

This is still quite a big list, with 119614 entries and 37 columns. There is an even larger list available in the "Augmented HYG" folder: 

HYG-Database/athyg/v1

You can extract and combine the Augmented HYG files to get a 343 MB file with 2552167 lines and 23 columns. You will probably need to trim the list. 2.5 million stars sounds cool, but many of them are extremely distant stars that will not be shown in our Blender render. It's a problem of geometry -- aside from the issue of clipping distance, an extremely distant object will only show up if the viewport is very carefully aligned, so most of the rendering resources will be wasted. Although Blender can definitely render 2.5 M objects, on most consumer HW we can't do anything too fancy with that many objects in the scene. And the whole point is to get a 3D scene we can work with. So if you want to use the augmented list, you might want to trim the list of stars to be (1) closer and (2) fewer. For now, let's proceed with the HYG list.

# Edit the script:
Open Blender and select the "Scripting" layout. Load create-stars.py and take a look at it: you'll probably need to make a couple of edits to the script before you run it. You need to point the file path to your file location, and also take a look at the comments to see if there is anything else you want to adjust.
Then click the "Run" button in the text editing window. Depending on your HW and how many stars you are creating, it could take a minute. Then zoom out and marvel at your stars!

