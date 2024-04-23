from pygame_functions import *
from words import items1
import random

screenSize(1500,1000)
setBackgroundColour("pink")

setAutoUpdate(False)
targetLabel = makeLabel("", 50, 750,950,"black","Consolas")
labels = []
for i in range(100):
        labels.append(makeLabel("",45,(i%10)*150+75,(i//10)*90+45,"red","Consolas"))

def reveal(num, labels, wordlist, colour):
    drawRect(num%10*150+2,num//10*90+2,146,86,colour)
    changeLabel(labels[num], wordlist[num], "white")
    moveLabel(labels[num],(num%10)*150+75,(num//10)*90+45)
    
def runDemo():
    wordlist = []
    tries = 0
    clearShapes()
    for i in range(100):
        temp = None
        while temp is None or temp in wordlist:
            temp = random.choice(items1)
        wordlist.append(temp)
    target = random.choice(wordlist)
    changeLabel(targetLabel, "Look for the word: " + target)
    moveLabel(targetLabel, 750, 950)
    showLabel(targetLabel)
    for row in range(10):
        drawLine(0,row*90,1500,row*90, "black",3)
        drawLine(row*150,0,row*150,900, "black",3)
    for i in range(100):
        changeLabel(labels[i], str(i),"red")
        moveLabel(labels[i], (i%10)*150+75,(i//10)*90+45)
        showLabel(labels[i])
    updateDisplay()
    revealed = [False for i in range(100)]
    while True:
        if mousePressed():
            num = mouseX()//150 + (mouseY()//90)*10
            if not revealed[num]:
                tries += 1
                revealed[num] = True
                print(num)
                if wordlist[num]== target:
                    changeLabel(targetLabel, "You found " + target + " in " + str(tries) + " tries. (Press Space)")
                    reveal(num,labels, wordlist, "red")
                    moveLabel(targetLabel, 750, 950)
                    return
                else:
                    reveal(num,labels, wordlist, "grey")
                    changeLabel(targetLabel, wordlist[num] + " is not " + target + ".")
                    moveLabel(targetLabel, 750, 950)
        updateDisplay()
        tick(100)
        
while True:
    runDemo()
    while not keyPressed("space"):
        updateDisplay()
        tick(100)
endWait()