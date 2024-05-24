def turn_right():
    turn_left()
    turn_left()
    turn_left()


#for step in range(6):
while not at_goal():

    if front_is_clear():
        move()
    elif wall_in_front() and right_is_clear():
        turn_right()
    elif front_is_clear() and right_is_clear():
        turn_right()

    else :
        turn_left()
