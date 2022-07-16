def draw_line(tick_length, tick_label=""):
    line = "-"*tick_length
    if tick_label:
        line += " "+tick_label
    print(line)


def draw_interval(central_length):
    if central_length > 0:
        draw_interval(central_length-1)
        draw_line(central_length)
        draw_interval(central_length-1)
# def draw_interval(central_length):
#     for i in range(central_length,0,-1):
#         draw_line(i-1)
#     draw_line(central_length)
#     for i  in range(1,central_length+1):
#         draw_line(i-1)


def draw_ruler(num_inches, major_length):
    draw_line(major_length, '0')
    for i in range(1, 1+major_length):
        draw_interval(major_length-1)
        draw_line(major_length, str(i))


draw_ruler(2, 3)

# draw line
# draw interval
# draw ruler


def draw_line1(length, label=""):
    line = "-" * length
    if label:
        line += " " + label
    print(line)


def draw_interval1(length):
    if length > 0:
        draw_interval1(length-1)
        draw_line1(length)
        draw_interval1(length-1)
