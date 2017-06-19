from graphics import *
from random import randint
import time

def roll():
    return randint(1,6)

def interface():
    win = GraphWin("Dice", 500,500)
    win.setBackground('white')
    rollbox = Rectangle(Point(125,475),Point(225,450))
    rollbox.setFill('black')
    rollText = Text(Point(175,463),'Roll')
    rollText.setFill('white')
    rollText.setStyle('bold')
    quitText = Text(Point(325,463),'Quit')
    quitText.setStyle('bold')
    quitText.setFill('white')
    quitBox = Rectangle(Point(275,475),Point(375,450))
    quitBox.setFill('black')
    rollbox.draw(win)
    rollText.draw(win)
    quitBox.draw(win)
    quitText.draw(win)
    
    run = True
    count = 0
    while run == True:
        clickcoords = win.getMouse()
        click = [clickcoords.getX(),clickcoords.getY()]

        if count>0:
            for i in circles:
                i.undraw()
        else:
            pass
        
        if (click[0]>=125 and click[0]<=225) and (click[1]>=450 and click[1]<=475):
            rollnum = roll()
            rollAni = [roll(),roll(),roll()]
            for i in rollAni:
                die = Circs(i)
                for j in die:
                    j.draw(win)
                time.sleep(0.2)
                for k in die:
                    k.undraw()
                
            if rollnum == 1:
                circles = Circs(1)
                circles[0].draw(win)
                
            elif rollnum == 2:
                circles = Circs(2)
                circles[0].draw(win)
                circles[1].draw(win)
                
            elif rollnum == 3:
                circles = Circs(3)
                for i in circles:
                    i.draw(win)
                
            elif rollnum == 4:
                circles = Circs(4)
                for i in circles:
                    i.draw(win)
                    
            elif rollnum == 5:
                circles = Circs(5)
                for i in circles:
                    i.draw(win)
                
            elif rollnum == 6:
                circles = Circs(6)
                for i in circles:
                    i.draw(win)
                
            count = count+1
            run = True
            
        elif (click[0]>=275 and click[0]<=325) and (click[1]>=450 and click[1]<=475):
            win.close()
            run = False
        else:
            count = 0
            run = True

def Circs(n):
    if n == 1:
        circ1 = Circle(Point(250,250),50)
        circ1.setFill('black')
        circles = [circ1]
        return circles
    elif n == 2:
        circ1 = Circle(Point(166,250),50)
        circ2 = Circle(Point(332,250),50)
        circles = [circ1,circ2]
        for i in circles:
            i.setFill('black')
        return circles
        
    elif n == 3:
        circ1 = Circle(Point(125,125),50)
        circ2 = Circle(Point(250,250),50)
        circ3 = Circle(Point(375,375),50)
        circles = [circ1,circ2,circ3]
        for i in circles:
            i.setFill('black')
        return circles
        
    elif n == 4:
        circ1 = Circle(Point(166,166),50)
        circ2 = Circle(Point(166,332),50)
        circ3 = Circle(Point(332,166),50)
        circ4 = Circle(Point(332,332),50)
        circles = [circ1,circ2,circ3,circ4]
        for i in circles:
            i.setFill('black')
        return circles
    
    elif n == 5:
        circ1 = Circle(Point(166,125),50)
        circ2 = Circle(Point(332,125),50)
        circ3 = Circle(Point(250,250),50)
        circ4 = Circle(Point(166,375),50)
        circ5 = Circle(Point(332,375),50)
        circles = [circ1,circ2,circ3,circ4,circ5]
        for i in circles:
            i.setFill('black')
        return circles
        
    elif n == 6:
        circ1 = Circle(Point(166,125),50)
        circ2 = Circle(Point(332,125),50)
        circ3 = Circle(Point(166,250),50)
        circ4 = Circle(Point(166,375),50)
        circ5 = Circle(Point(332,375),50)
        circ6 = Circle(Point(332,250),50)
        circles = [circ1,circ2,circ3,circ4,circ5,circ6]
        for i in circles:
            i.setFill('black')
        return circles

interface()
