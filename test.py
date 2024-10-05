import time


SET_COLOR = "\x1b[48;5;"
END = "\x1b[0m"
CLEAR = "\033[H"


def draw_line(offset=0, length=1, color=222):
    line = " " * length
    print(f"{' ' * offset}\x1b[48;5;{color}m{line}\x1b[0m")


def draw_romb ():
    size = 15 
    center = size // 2
    offset = size // 2

    step = 1
    lenght = 1

    #print(size, center, offset)

    colors = [222,157]

    while True:
        for color in colors:
            for line in range(size):
                draw_line(offset, lenght, color)

                if line < center:
                    offset -=step
                    lenght += step*2
                else:
                    offset +=step
                    lenght -= step*2
            print(f"\x1b[{size+2}A")
            print(f"\x1b[{offset}D")

            length = 1
            offset = size // 2

            time.sleep(2)

# print("jhgjhj")    

# if __name__ ==  "__main__ ":
    # print("jhgjhj")
draw_romb()
# for i in range(20):
#     draw_line(length=20, color=7, offset=20)
#     print(f"{CLEAR}")
#     time_sleep(0.5)