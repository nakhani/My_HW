import math
from functools import partial
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader


global flg 
flg = 0

def sub():
    global num1, a
    if(main_window.screentext.toPlainText()==""): main_window.screentext.setText("0")
    num1 = float(main_window.screentext.toPlainText())
    main_window.screentext.setText("")
    a = "-"

def div():
    global num1, a
    if(main_window.screentext.toPlainText()==""): main_window.screentext.setText("0")
    num1 = float(main_window.screentext.toPlainText())
    main_window.screentext.setText("")
    a= "/"

def sum():
    global num1, a
    if(main_window.screentext.toPlainText()==""): main_window.screentext.setText("0")
    num1 = float(main_window.screentext.toPlainText())
    main_window.screentext.setText("")
    a= "+"

def sin():
    global flg 
    main_window.screentext.setText(str(math.sin(float(main_window.screentext.toPlainText()))))
    flg = 1
    
def cos():
    global flg 
    main_window.screentext.setText(str(math.cos(float(main_window.screentext.toPlainText()))))
    flg = 1
def tan():
    global flg 
    main_window.screentext.setText(str(math.tan(float(main_window.screentext.toPlainText()))))
    flg = 1
def cot():
    global flg 
    main_window.screentext.setText(str(math.cot(float(main_window.screentext.toPlainText()))))
    flg = 1
def mul():
    global num1, a
    if(main_window.screentext.toPlainText()==""): main_window.screentext.setText("0")
    num1 = float(main_window.screentext.toPlainText())
    main_window.screentext.setText("")
    a="*"

def result():
    global flg
    num2=float(main_window.screentext.toPlainText())
    if a =="-":
      result = num1-num2

    elif a =="+":
      result = num1+num2

    elif a =="/":
      while(num2==0):
        B=float(main_window.screentext.toPlainText())

      result = num1/num2

    elif a =="+":
      result = num1*num2

    main_window.screentext.setText(str(result))
    flg = 1

def AC():
    main_window.screentext.setText("")

def negative():
    global flg
    main_window.screentext.setText(str(float(main_window.screentext.toPlainText())*-1))
    flg=1

def perc():
    global flg
    main_window.screentext.setText(str(float(main_window.screentext.toPlainText())/100))
    flg=1

def num(a):
    global flg
    if(flg):
        main_window.screentext.setText(a)
        flg =0
    else:
        main_window.screentext.setText(main_window.screentext.toPlainText() + a)
    
def decimal_point():
    main_window.screentext.setText(main_window.screentext.toPlainText()+'.')

loader = QUiLoader()
app = QApplication([])

main_window = loader.load("new_calculator\main.ui")

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
main_window.ziro.clicked.connect(partial(num, "0"))
main_window.one.clicked.connect(partial(num, "1"))
main_window.two.clicked.connect(partial(num, "2"))
main_window.three.clicked.connect(partial(num, "3"))
main_window.four.clicked.connect(partial(num, "4"))
main_window.five.clicked.connect(partial(num, "5"))
main_window.six.clicked.connect(partial(num, "6"))
main_window.seven.clicked.connect(partial(num, "7"))
main_window.eight.clicked.connect(partial(num, "8"))
main_window.nine.clicked.connect(partial(num, "9"))
main_window.point.clicked.connect(decimal_point)
main_window.negative.clicked.connect(negative)
main_window.perc.clicked.connect(perc)


main_window.show()
app.exec()