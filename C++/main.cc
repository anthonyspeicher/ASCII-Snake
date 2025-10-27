/**
 * Author: Anthony Speicher
 * Date: 10/27/2025
 * Description: Snake game in C++ using ncurses
**/

#include <ncurses.h>

int main()
{
	initscr();
	printw("Hello World!");
	refresh();
	endwin();

	return 0;
}
