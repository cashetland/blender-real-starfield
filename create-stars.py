import bpy, csv

fp = "/home/shetland91/Documents/Blender Projects/hyg_v35_sorted_by_dist.csv" # Change path or filename if needed

# Check whether the column selections are what you want
proper_name_column = 6 # The preferred name to use first
alt_name_column1 = 5 # The backup name to use if the preferred name is blank
alt_name_column2 = 0 # The catchall name; choose a column that is never blank, like "id"

absmag_column = 14 # The 'absolute magnitude', or brightness as perceived from 10 parsecs away. See comment below about format
x_column = 17 
y_column = 18
z_column = 19

# We'll filter the stars by distance. If you want to limit the number of entries due to render resource constraints, try setting
# the distance_filter value to 100 parsecs or even 50
dist_column = 9
distance_filter = 10000 # A distance value over about 1000 parsecs indicates no valid distance information available

star_rad_max = 0.1 # The rendered radius of star markers, in parsecs. Musn't be the true radius or they'll be too small to see...
star_rad_min = 0.02 # The star markers will be rendered at different sizes depending on the star's brightness
absmagmax = -2.705 # absolute magnitude of brightness is logarithmic with the sign inverted; lesser is brighter
absmagmin = 19.629

with open( fp ) as csvfile:
    rdr = csv.reader( csvfile )
    for i, row in enumerate( rdr ):
        if i == 0: continue # Skip column titles
        if float(row[dist_column]) > distance_filter: continue # filter entries with invalid distance (flagged by large value)
        star_name = row[proper_name_column]
        if star_name == "":
            star_name = row[alt_name_column1]
        if star_name == "":
            star_name = row[alt_name_column2]
        x, y, z = row[x_column:(z_column+1)] # The coordinates are already in parsecs
        absmag = row[absmag_column]
        star_render_radius = ( ( ( float(absmag) - absmagmin ) / (absmagmax - absmagmin) ) * (star_rad_max - star_rad_min) ) + star_rad_min
        bpy.ops.mesh.primitive_uv_sphere_add( location = ( float(x), float(y), float(z) ), radius = float(star_render_radius) )
        bpy.context.object.name = star_name


