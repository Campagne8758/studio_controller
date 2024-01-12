#handling the different color combinations for each page
import picokeypad as keypad


def draw_page_0():
    #Row 2
    keypad.illuminate(4, 180, 70, 0)
    keypad.illuminate(5, 110, 110, 0)
    keypad.illuminate(6, 0, 20, 110)
    keypad.illuminate(7, 110, 0, 0)
    #Row 3
    keypad.illuminate(8, 180, 0, 0)
    keypad.illuminate(9, 180, 70, 0)
    keypad.illuminate(10, 150, 110, 20)
    keypad.illuminate(11, 110, 0, 0)
    #Row 4
    keypad.illuminate(12, 180, 70, 0)
    keypad.illuminate(13, 180, 70, 0)
    keypad.illuminate(14, 200, 0, 0)
    keypad.illuminate(15, 0, 200, 0)
    keypad.update()
    
    return

def draw_page_1():
    #Row 2
    keypad.illuminate(4, 180, 70, 10)
    keypad.illuminate(5, 120, 0, 0)
    keypad.illuminate(6, 0, 20, 110)
    keypad.illuminate(7, 10, 10, 10)
    #Row 3
    keypad.illuminate(8, 180, 70, 10)
    keypad.illuminate(9, 60, 10, 0)
    keypad.illuminate(10, 0, 20, 190)
    keypad.illuminate(11, 10, 10, 10)
    #Row 4
    keypad.illuminate(12, 200, 0, 0)
    keypad.illuminate(13, 255, 0, 0)
    keypad.illuminate(14, 200, 0, 0)
    keypad.illuminate(15, 0, 200, 0)
    keypad.update()
    
    return

def draw_page_2():
    #Row 2
    keypad.illuminate(4, 0, 128, 128)
    keypad.illuminate(5, 0, 220, 20)
    keypad.illuminate(6, 120, 20, 110)
    keypad.illuminate(7, 110, 110, 110)
    #Row 3
    keypad.illuminate(8, 80, 80, 80)
    keypad.illuminate(9, 200, 40, 0)
    keypad.illuminate(10, 0, 0, 190)
    keypad.illuminate(11, 255, 80, 51)
    #Row 4
    keypad.illuminate(12, 200, 25, 25)
    keypad.illuminate(13, 255, 0, 0)
    keypad.illuminate(14, 200, 0, 0)
    keypad.illuminate(15, 0, 200, 0)
    keypad.update()
    
    return

def draw_page_3():
    #Row 2
    keypad.illuminate(4, 0, 28, 200)
    keypad.illuminate(5, 100, 100, 100)
    keypad.illuminate(6, 120, 0, 120)
    keypad.illuminate(7, 100, 100, 100)
    #Row 3
    keypad.illuminate(8, 0, 0, 0)
    keypad.illuminate(9, 0, 0, 0)
    keypad.illuminate(10, 200, 50, 0)
    keypad.illuminate(11, 0, 50, 200)
    #Row 4
    keypad.illuminate(12, 200, 25, 25)
    keypad.illuminate(13, 255, 0, 0)
    keypad.illuminate(14, 200, 0, 0)
    keypad.illuminate(15, 0, 200, 0)
    keypad.update()
    
    return