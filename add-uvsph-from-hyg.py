import bpy, csv

fp = "/Users/calebshetland/Documents/Blender Projects/testcsv001.csv"

with open( fp ) as csvfile:
    rdr = csv.reader( csvfile )
    for i, row in enumerate( rdr ):
        if i == 0: continue # Skip column titles
        x, y, z, r = row[0:4]

        # Generate UV sphere at these coordinates
        bpy.ops.mesh.primitive_uv_sphere_add( location = ( float(x), float(y), float(z) ), radius = float(r) )
