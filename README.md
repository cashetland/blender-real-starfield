# blender-real-starfield
Make a starfield in Blender 3D using the real positions of stars in our cosmic neighborhood
Let's say you're writing a sci-fi story and you want it to be as realistic as possible, so you want to consider the positions of real stars near Earth when talking about how long it takes to get from one place to another, and to help your characters make decisions about where to go and where to avoid. There are plenty of amazing star maps available, but they all show how the night sky looks from Earth. Astronomers can deduce the distance of each star from Earth using parallax for near stars and spectral analysis for distant stars, and the position in the night sky gives us a direction (right ascension and declination). With a direction vector and a distance, we should be able to asign 3D coordinates to every star (within a certain error range).

There are fewer star maps that show what we want, and most aren't highly configurable. It would be much better if we could import a list of authentic star coordinates into Blender and create a marker at each place. Then we can create any star map we want; and more importantly, we can rotate, zoom, and pan, to get the "lay of the land" (or galaxy, in this case). We also need some basic stats like the brightness and mass of each star.

But most star lists are formatted for use by professional astronomers, researchers, and academics. There are many subtle problems around measuring star data, and since the techniques for removing different sources of distortion are active research fields, usually you'll find the "original measured" value rather than the "corrected" value for things like position and brightness. The main issue here is that the majority of lists published by academia don't give us the ready-baked 3D coordinates and brightness values we need. Fortunately, a community of brave volunteers have compiled some useful databases, and those in turn have been gathered and formatted by David Nash (astronexus.com):
https://github.com/astronexus/HYG-Database

# To make a real 3D starfield in Blender:

# Get the latest version of the HYG star list:
~$ git clone https://github.com/astronexus/HYG-Database.git

# Extract the "Augumented HYG" list:
~$ gzip -d HYG-Database/athyg/v1/athyg_v10-1.csv.gz
~$ gzip -d HYG-Database/athyg/v1/athyg_v10-2.csv.gz

# Assemble the files:
This command will give you a 343 MB file with over 2M lines and 23 columns; but only a few of the columns are useful to us.
cat HYG-Database/athyg/v1/athyg_v10-1.csv HYG-Database/athyg/v1/athyg_v10-2.csv > athyg_v1_0.csv
