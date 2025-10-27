import curses

# idea for the program: draw grid, use list to keep track of which way the snake is turning
# and iterate down that, pushing turns further each time.

# set speed (1-5)
SPEED = 1

# main loop
def main(stdscr):
    # make cursor invisible
    curses.curs_set(0)

    while True:
        # create and update grid - can't find good characters and structure; later this will include
        # the actual snake code
        stdscr.clear()
        stdscr.addstr(0, 0, "▁" * 50) 
        for i in range(48):
            stdscr.addstr(1, 0, "| " * 25 + "|")
        stdscr.refresh()

        c = stdscr.getch()
        if c == ord('e'):
            break

# initialize window with wrapper
stdscr = curses.initscr()
curses.wrapper(lambda stdscr: main(stdscr))
