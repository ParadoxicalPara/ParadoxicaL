from graphics import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
def main():
    win=GraphWin("Black and White", 500,500)
    pics=Image(Point(250,250), askopenfilename())
    pics.draw(win)
    width, height=pics.getWidth(), pics.getHeight()
    for x in range(width):
        for y in range(height):
            [r,g,b]=pics.getPixel(x,y)
            if (int(r)+int(g)+int(b))/3<=127:
                pics.setPixel(x,y, "black")
            else:
                pics.setPixel(x,y, "white")
    pics.save(asksaveasfilename())
    win.getMouse()
    win.close()
main()
