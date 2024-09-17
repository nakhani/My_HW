import math
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

global flg 
flg = 0

def sub():
    global num1, a
    if(main_window.screen.text()==""): main_window.screen.settext("0")
    num1 = float(main_window.screen.text())
    main_window.txt_1.setText("")
    a = "-"

def div():
    global num1, a
    if(main_window.screen.text()==""): main_window.screen.setText("0")
    num1 = float(main_window.screen.text())
    main_window.txt_1.setText("")
    a= "/"

def sum():
    global num1, a
    if(main_window.screen.text()==""): main_window.screen.setText("0")
    num1 = float(main_window.screen.text())
    main_window.txt_1.setText("")
    a= "+"

def sin():
    global flg 
    main_window.screen.setText(str(math.sin(float(main_window.screen.text()))))
    flg = 1
    
def cos():
    global flg 
    main_window.screen.setText(str(math.cos(float(main_window.screen.text()))))
    flg = 1
def tan():
    global flg 
    main_window.screen.setText(str(math.tan(float(main_window.screen.text()))))
    flg = 1
def cot():
    global flg 
    main_window.screen.setText(str(math.cot(float(main_window.screen.text()))))
    flg = 1
def mul():
    global num1, a
    if(main_window.screen.text()==""): main_window.screen.setText("0")
    num1 = float(main_window.screen.text())
    main_window.txt_1.setText("")
    a="*"

def result():
    global flg
    num2=float(main_window.screen.text())
    if a =="-":
      result = num1-num2

    elif a =="+":
      result = num1+num2

    elif a =="/":
      while(num2==0):
        B=float(main_window.screen.text())

      result = num1/num2

    elif a =="+":
      result = num1*num2

    main_window.screen.setText(str(result))
    flg = 1

def AC():
    main_window.screen.setText("")

def negative():
    ...

def perc():
    ...

def zero():
    if(flg):
        main_window.screen.setText('0')
        flg =0
    else:
        main_window.screen.setText(main_window.screen.text()+'0')

def one():
    if(flg):
        main_window.screen.setText('1')
        flg=0
    else:
        main_window.screen.setText(main_window.screen.text()+'1')

def two():
    if(flg):
        main_window.screen.setText('2')
        flg=0
    else:
        main_window.screen.setText(main_window.screen.text()+'2')

def three():
    if(flg):
        main_window.screen.setText('3')
        flg=0
    else:
        main_window.screen.setText(main_window.screen.text()+'3')

def four():
    if(flg):
        main_window.screen.setText('4')
        flg=0
    else:
       main_window.screen.setText(main_window.screen.text()+'4')

def five():
    if(flg):
        main_window.screen.setText('5')
        flg=0
    else:
        main_window.screen.setText(main_window.screen.text()+'5')

def six():
    if(flg):
        main_window.screen.setText('6')
        flg=0
    else:
        main_window.screen.setText(main_window.screen.text()+'6')

def seven():
    if(flg):
        main_window.screen.setText('7')
        flg=0
    else:
        main_window.screen.setText(main_window.screen.text()+'7')

def eight():
    if(flg):
        main_window.screen.setText('8')
        flg=0
    else:
        main_window.screen.setText(main_window.screen.text()+'8')

def nine():
    if(flg):
        main_window.screen.setText('9')
        flg=0
    else:
        main_window.screen.setText(main_window.screen.text()+'9')
    
def decimal_point():
    main_window.screen.setText(main_window.screen.text()+'.')

app = QApplication([])
loader = QUiLoader()
main_window = loader.load("main.ui")
main_window.show()
main_window.sub.clicked.connect(sub)
main_window.sum.clicked.connect(sum)
main_window.mul.clicked.connect(mul)
main_window.div.clicked.connect(div)
main_window.sin.clicked.connect(sin)
main_window.cos.clicked.connect(cos)
main_window.tan.clicked.connect(tan)
main_window.cos.clicked.connect(cos)
main_window.AC.clicked.connect(AC)
main_window.equal.clicked.connect(result)
main_window.zero.clicked.connect(zero)
main_window.one.clicked.connect(one)
main_window.two.clicked.connect(two)
main_window.three.clicked.connect(three)
main_window.four.clicked.connect(four)
main_window.five.clicked.connect(five)
main_window.six.clicked.connect(six)
main_window.seven.clicked.connect(seven)
main_window.eight.clicked.connect(eight)
main_window.nine.clicked.connect(nine)
main_window.point.clicked.connect(decimal_point)
main_window.negative.clicked.connect(negative)
main_window.perc.clicked.connect(perc)



app.exec_()