import bpy, csv

fp = "~/Documents/Blender Projects/hygdata_v3_within_50_parsec.csv"

with open( fp ) as csvfile:
    rdr = csv.reader( csvfile )
    for i, row in enumerate( rdr ):
        if i == 0: continue # Skip column titles
        proper_name = row[6]
        x, y, z = row[18:21] # The coordinates are already in parsecs
        absmag = row[15]
        rmax = 0.1
        rmin = 0.02
        absmagmax = -2.705 # absolute magnitude of brightness is logarithmic with the sign inverted; lesser is brighter
        absmagmin = 19.629
        rrender = ( ( ( float(absmag) - absmagmin ) / (absmagmax - absmagmin) ) * (rmax - rmin) ) + rmin
        name = proper_name
        if name == "":
            name = str(i)
        bpy.ops.mesh.primitive_uv_sphere_add( location = ( float(x), float(y), float(z) ), radius = float(rrender) )
        bpy.context.object.name = name
