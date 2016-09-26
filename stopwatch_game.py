# template for "Stopwatch: The Game"

# define global variables
import simplegui
import time

canvas_width = 300
canvas_height = 300
time = 0
no_of_stops = 0
successful_stops = 0


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global millisec
    mins = time // 600
    seconds  = (time - 600*mins) // 10
    millisec = (time - 600*mins) % 10
    if seconds // 10 == 0:
        seconds = "0"+str(seconds)
    return str(mins) + ":" + str(seconds) + ":" + str(millisec)
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"


    
def start_handler():
    timer.start()
    
def stop_handler():
    global no_of_stops
    global successful_stops
    if timer.is_running():
        timer.stop()
        no_of_stops += 1
        if millisec == 0:
            successful_stops += 1
        

def reset_handler():
    global time
    global no_of_stops
    global successful_stops
    timer.stop()
    time = 0
    no_of_stops = 0
    successful_stops = 0
    
    
# define event handler for timer with 0.1 sec interval

def timer_handler():
    global time
    time = (time + 1)
    
    
# define draw handler
def draw(canvas):
    message = format(time) 
    result = str(no_of_stops) + " / " + str(successful_stops)
    canvas.draw_text(message, (100, 150), 36, "White")
    canvas.draw_text(result, (200, 40), 36, "Red")
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", canvas_width, canvas_height) 
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, timer_handler)
# register event handlers

frame.add_button("Start", start_handler, 100)
frame.add_button("Stop", stop_handler, 100)
frame.add_button("Reset", reset_handler, 100)

frame.start()
# start frame
timer.start()

# Please remember to review the grading rubric
