# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 11:41:26 2017

@author: Faria
"""

import json
import glob

json_file=glob.glob(r'D:\WAZE\WAZE\*.*.201*.*.*.*.json')

Myfile=r'D:\WAZE\Docs\Norfolk_Irregularities_Data.txt'
f=open(Myfile,'w')

#myRoads = {1:'Streets',2:'Primary Street',3:'Freeways',4:'Ramps',5:'Trails',6:'Primary',7:'Secondary',8:'4X4 Trails',14:'4X4 Trails',9:'Walkway',10:'Pedestrian',11:'Exit',15:'Ferry crossing',16:'Stairway',17:'Private road',18:'Railroads',19:'Runway/Taxiway',20:'Parking lot road',21:'Service road'}
f.write('file_name\tcity\tspeed\tregularSpeed\tlength\tdelaySec\ttrend\tseverity\tjamLevel\tdriversCount\talertsCount\tline(x)\tline(y)\n')

for file in range(len(json_file)):
    json_data=open(json_file[file],'r')
    
    try:
        data = json.load(json_data)
    except UnicodeDecodeError:
        continue
    except json.JSONDecodeError:
        continue
    
    
    if "irregularities" in data:
            irg = data["irregularities"]
            
            count = 0
            while count<len(irg):
                j = data['irregularities'][count]
                if "city" in j:
                    if j["city"]=="Naval Station Norfolk, VA" or j["city"]=="Norfolk, VA":
                        for i in range(len(j["line"])):
                            message = json_file[file]+'\t'+str(j['city'])+'\t'+str(j["speed"])+'\t'+str(j["regularSpeed"])+'\t'+str(j['length'])+'\t'+str(j["delaySeconds"])+'\t'+str(j["trend"])+'\t'+str(j["severity"])+'\t'+str(j["jamLevel"])+'\t'+str(j["driversCount"])+'\t'+str(j["alertsCount"])+'\t'+str(j["line"][i]["x"])+'\t'+str(j["line"][i]["y"])+'\n'
                            f.write(message)
                            print(json_file[file],'\n',data["jams"][count])
                count+=1   
            else:
                print(json_file[file]+' No irregularties alert in Norfolk')

        
json_data.close()
f.close()
