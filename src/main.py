import curses
from product import Product
from inventary import Inventary


def main(stdscr):
    # Curses Initial configuration
    curses.curs_set(0)  # Hide the cursor
    stdscr.clear()  # Clean the screen

    while True:
        stdscr.addstr("Management Inventary\n")
        stdscr.addstr("1. Add product\n")
        stdscr.addstr("2. Remove product\n")
        stdscr.addstr("3. Update product\n")
        stdscr.addstr("4. Show inventary\n")
        stdscr.addstr("5. Exit\n")
        stdscr.addstr("Please, choose an option: ")

        # Get the user's choice
        choice = stdscr.getch()

        if choice == ord('1'):
            pass
        elif choice == ord('2'):
            pass

        if choice == ord('5'):
            break

        stdscr.clear()


if __name__ == "__main__":
    curses.wrapper(main)

