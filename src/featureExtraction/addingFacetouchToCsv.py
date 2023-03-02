import pandas as pd
import os, sys

#USAGE: input path to csv file as param


csvFile = sys.argv[1]

df = pd.read_csv(csvFile)
df = df.sort_values('frame')

def checkForFacetouch(pose, hand):
    head_coords =  pose[0:2] 
    hand_coords = hand[0:2]

    #print(head_coords, hand_coords)

    diff = 15

    if( hand_coords[0] <= (head_coords[0] + diff) and hand_coords[0] >= (head_coords[0] - diff) and hand_coords[1] <= (head_coords[1] + diff) and hand_coords[1] >= (head_coords[1] - diff) ):
        #print("hand touching face")
        return True
    else:
        return False


df['leftHandTouching'] = df.apply(lambda x: checkForFacetouch([ float(i) for i in (x['pose'][1:-1]).split(', ') ], [ float(i) for i in (x['hand_left'][1:-1]).split(', ') ]),axis=1)
df['rightHandTouching'] = df.apply(lambda x: checkForFacetouch([ float(i) for i in (x['pose'][1:-1]).split(', ') ], [ float(i) for i in (x['hand_right'][1:-1]).split(', ') ]), axis=1)

#now need to save to file
df.to_csv(csvFile)