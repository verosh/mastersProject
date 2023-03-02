#we want list of dicts with same headers
import json, os
import re
import csv 
import sys
import glob

def jsonToDict(file):
    with open(file) as json_file:
        data = json.load(json_file)
        f = {}

        if( len(data['people'])>0 ):
 
            d = data['people'][0]

            #print(type(d['hand_left_keypoints_2d']), type(d['hand_right_keypoints_2d']),type(d['pose_keypoints_2d']))
   
            f = { 'participant':  re.findall("(p_[0-9]+)",file)[0],'frame': int(re.findall("_([0-9]+)_", file)[0]) , 'pose' : d['pose_keypoints_2d'], 'hand_left': d['hand_left_keypoints_2d'], 'hand_right':d['hand_right_keypoints_2d']}
    return f

#path_to_json = '/home/vero/coding/masters/mastersProject/src/output/p_13'
path_to_json = sys.argv[1]
# import all files from folder which ends with .json 
json_files = glob.glob(os.path.join(path_to_json, '*.json'))
all_frames = []

for i in json_files:
    temp = jsonToDict(i)
    if(len(temp)>0):
        all_frames.append( temp )

field_names = [ "participant", "frame", "pose", "hand_left", "hand_right" ]

#need output path as 2nd arg

output_path = sys.argv[2]
with open( output_path + '/keypoints.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(all_frames)