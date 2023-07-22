import bpy, csv

in_filename = "/home/shetland91/Documents/Blender Projects/starlist.csv" # Change path or filename if needed

# Check whether the column selections here are what you want
# Column headings as of v3.5:
#
# 0     1   2   3   4   5   6       7   8   9       10      11      12  13  14      15      16  17  18  19  20  21  22
# id	hip	hd	hr	gl	bf	proper	ra	dec	dist	pmra	pmdec	rv	mag	absmag	spect	ci	x	y	z	vx	vy	vz
#
# 23    24      25      26          27      28      29          30              31      32  33  34      35	
# rarad	decrad	pmrarad	pmdecrad	bayer	flam	con	comp	comp_primary	base	lum	var	var_min	var_max

proper_name_column = 6 # The preferred name to use first
alt_name_column1 = 5 # The backup name to use if the preferred name is blank
alt_name_column2 = 0 # The catchall name; choose a column that is never blank, like "id"

absmag_column = 14 # The 'absolute magnitude', or brightness as perceived from 10 parsecs away. See comment below about format
x_column = 17 
y_column = 18
z_column = 19

star_rad_max = 0.1 # The rendered radius of star markers, in parsecs. Far larger than a real star's radius so the marker is large enough to see
star_rad_min = 0.02 # The star markers will be rendered at different sizes depending on the star's brightness
absmagmax = -2.705 # absolute magnitude of brightness is logarithmic with the sign inverted; lesser is brighter
absmagmin = 19.629

with open(in_filename) as csvfile:
    csvReader = csv.reader(csvfile)
    for i, row in enumerate(csvReader):
        if i == 0: continue # Skip column titles
        if i % 100 == 0: print("Created ", i, " stars so far")
        star_name = row[proper_name_column]
        if star_name == "":
            star_name = row[alt_name_column1]
        if star_name == "":
            star_name = row[alt_name_column2]
        x, y, z = row[x_column:(z_column+1)] # The coordinates are already in parsecs
        absmag = row[absmag_column]
        star_render_radius = ( ( ( float(absmag) - absmagmin ) / (absmagmax - absmagmin) ) * (star_rad_max - star_rad_min) ) + star_rad_min
        bpy.ops.mesh.primitive_uv_sphere_add(segments=8, ring_count=4, location = ( float(x), float(y), float(z) ), radius = float(star_render_radius) )
        bpy.context.object.name = star_name
        if row[proper_name_column] != "":
            bpy.context.object.show_name = True

