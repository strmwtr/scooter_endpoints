import arcpy

#Databases
gdb = r'\path\to\Scooter.gdb'
sde = r'Database Connections\Connection to GISPRDDB.sde'

#Source data
rcl = f'{sde}\cvgis.CITY.Transportation_Road\cvGIS.CITY.road_centerline'


#Derived Data
rcl_buff = f'{gdb}/road_centerline_buffer'
rcl_dis = f'{gdb}/road_centerline_dis'
rcl_int = f'{gdb}/road_centerline_int'
rcl_int_buff = f'{gdb}/road_centerline_int_buff'
block_endpoints = f'{gdb}/block_endpoints'
block_midpoints = f'{gdb}/block_midpoints'


arcpy.Buffer_analysis(
  in_features= rcl,
  out_feature_class= rcl_buff
  buffer_distance_or_field="75 Feet", 
  line_side="FULL", 
  line_end_type="ROUND", 
  dissolve_option="NONE", 
  dissolve_field="", 
  method="PLANAR")

arcpy.Dissolve_management(
  in_features= rcl_buff, 
  out_feature_class= rcl_dis, 
  dissolve_field="", 
  statistics_fields="", 
  multi_part="MULTI_PART", 
  unsplit_lines="DISSOLVE_LINES")

arcpy.Intersect_analysis(
  in_features= rcl, 
  out_feature_class= rcl_int, 
  join_attributes="ALL", 
  cluster_tolerance="-1 Unknown", 
  output_type="POINT")

arcpy.Buffer_analysis(
  in_features= rcl_int,
  out_feature_class= rcl_int_buff
  buffer_distance_or_field="75 Feet", 
  line_side="FULL", 
  line_end_type="ROUND", 
  dissolve_option="NONE", 
  dissolve_field="", 
  method="PLANAR")

arcpy.Dissolve_management(
  in_features= rcl_int_buff, 
  out_feature_class= rcl_int_buff_dis, 
  dissolve_field="", 
  statistics_fields="", 
  multi_part="MULTI_PART", 
  unsplit_lines="DISSOLVE_LINES")

arcpy.Erase_analysis(
  in_features= rcl_dis, 
  erase_features= block_endpoints, 
  out_feature_class= block_midpoints, 
  cluster_tolerance="")

