import processing
from qgis.core import *
from qgis.utils import iface
from osgeo import gdal

# Set Data Directories
data_dir = "C:\\Users\\Cate\\Dropbox\\PC\\Documents\\4 Data GIS\\heritage"
#iiep_worldpop_dir = "...\\MST Python Inputs\\IIEP_WorldPop\\school_age_population"
# Set Output Locations
output_dir = "..."
slash ="\\"


## In QGIS, set extent to UKR
extent = iface.mapCanvas().extent()

## Take historic places from OSM. Repeated for Values of: building, castle, church, tomb ##
results = processing.run("quickosm:buildqueryextent", 
                        {"KEY":"historic", 
                         "VALUE":"tomb",
                         "EXTENT":extent})
## Download the .osm file ##                     
osm = processing.run("native:filedownloader", 
                        {'URL':results['OUTPUT_URL'], 
                         'OUTPUT':data_dir+slash+'tomb'})
## extract multipolygons from the .osm file ##                     
shp = processing.run('quickosm:openosmfile', 
                        {"FILE":osm["OUTPUT"]})
## save the multipolygons vector file in a variable ##                
OSMLayer = shp['OUTPUT_MULTIPOLYGONS']
OSMLayer.setName('OSM buildings')
## add the layer to the project instance ##
QgsProject().instance().addMapLayer(OSMLayer)

#After this step is complete, the following steps were done in QGIS:
    #Fix geometries
    #Centroids: convert polygons to points
    #Add geometries: create an x and y coordinates column 
    #Merge building, castle, church and tomb datasets
    #Export to shp 