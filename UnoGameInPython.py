'''
Created on Sep 1, 2021
@author: Nasir Khurshid
All rights reserved.
'''

def canPlay (hand, face):
    faceNum = face[-1:]
    faceColor = face[:-2]
    for x in range(len(hand)):
        if faceNum in hand[x]:
            return True
        if faceColor in hand[x]:
            return True
    return False
    
hand = ["blue 3", "red 7", "black 5"]
face1 = "blue 5"
face2 = "red 7"
face3 = "green 3"
face4 = "orange 8"

print("Can play? : ", canPlay(hand, face1))
print("Can play? : ", canPlay(hand, face2))
print("Can play? : ", canPlay(hand, face3))
print("Can play? : ", canPlay(hand, face4))