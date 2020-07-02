

"""

FOR 1V1

if ball not in captured range
    if ball in vision
        rotate till ball in center of vision
        move towards ball till in captured range
    else
        rotate till ball in vision


if ball in captured range
    if goal in vision
        rotate till goal in center of vision
        move towards goal till in captured range
    else
        rotate till goal in vision

"""


from moveBot import rotate_left, rotate_right, moveForward, moveStop
from findPosition import getAngle, getBallPosition, getDistance, getGoalPosition
from capture import init, getFrame, showFrame, end

# initialize limits
init()
init_frame = getFrame()
h, w, d = init_frame.shape

capturedHigh = int(h)
capturedLow = int(h-h*.1)
print("captured Range on y axis", capturedLow, capturedHigh)
end()


init()

# further improve implementation with fixed movement instead of continuous movement


while(True):
    # captured = False
    # capturedDistance = 50
    # goalDistance = 20
    showFrame()
    ball = getBallPosition()
    goal = getGoalPosition()
    ballDist = getDistance(ball)
    goalDist = getDistance(goal)
    print("ball dist ", h-ballDist)
    print("goal dist ", h-goalDist)
    if(ballDist < capturedLow or ballDist > capturedHigh):
        captured = False
    if(captured and goalDist > capturedLow and goalDist <= capturedHigh):
        print("Ball in Goal")
        break
    if(not captured):
        print("Towards ball ", ball[0], ball[1])
        angle = getAngle(ball)
        if(angle != None):
            if(angle < -10):
                rotate_left()
            elif(angle > +10):
                rotate_right()
            else:

                if(ballDist <= capturedHigh and ballDist > capturedLow):
                    captured = True
                    moveStop()
                else:
                    moveForward()
                # dist = getDistance(ball)
                # while(dist > capturedDistance):
                #     moveForward()
        else:
            rotate_left()

    else:
        print("Towards goal ", goal[0], goal[1])
        angle = getAngle(goal)
        if(angle != None):
            if(angle < -10):
                rotate_left()
            elif(angle > +10):
                rotate_right()
            else:
                moveForward()
        else:
            rotate_left()


showFrame()
end()
