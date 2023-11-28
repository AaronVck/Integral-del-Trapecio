from tkinter import *

from sympy import sympify, SympifyError, sqrt, symbols

root = Tk()
root.title("Integral del Trapecio")
root.geometry("500x400")

font_size = 16

menu = Menu(root)
root.config(menu=menu)




Options = Menu(menu, tearoff=0)
Options.add_command(label = "Fix...", command=lambda:selectFix())


Integrals = Menu(menu, tearoff=0)
Integrals.add_command(label = "Establecer función", command=lambda:function())
Integrals.add_command(label = "Limite superior de la integral", command=lambda:upintegralLimit())
Integrals.add_command(label = "Limite inferior de la integral",command=lambda:downintegralLimit())
Integrals.add_command(label = "Valor de n", command=lambda:nNumber())
Integrals.add_command(label = "Calcular integral", command=lambda:calculateTrapeze())


menu.add_cascade(label="Opciones", menu=Options)
menu.add_cascade(label="Trapecio", menu=Integrals)

display = Entry(root, font=("Helvetica", font_size))


display.grid(row=1, columnspan=6, sticky=N+S+W+E)

x = symbols('x')

i = 0
downLimit = ""
upLimit = ""
n = ""
mathFunction = ""
fix = 3



def getNumbers(n):
  global i
  display.insert(i,n)
  i+=1

def getOperators(operator):
  global i 
  operatorLength = len(operator)
  display.insert(i,operator)
  i+=operatorLength

def clearDisplay():
  display.delete(0, END)

def undo():
  displayState = display.get()
  if len(displayState):
    displayNewState = displayState[:-1]
    clearDisplay()
    display.insert(0,displayNewState)
  elif len(displayState) == 0:
    clearDisplay()
  
  else:
    clearDisplay()
    display.insert(0,'Error')

def calculate():
  displayState = display.get()
  try:
    mathExpression = sympify(displayState)
    result = mathExpression.evalf()
   
    clearDisplay()
    display.insert(0,str(result))
  except SympifyError:
    clearDisplay()
    display.insert(0,'Error')
    return

def selectFix():
  global fix
  displayState = display.get()
  try:
    fix = sympify(displayState)
  except SympifyError:
    clearDisplay()
    display.insert(0, "Error")


def function():
  global mathFunction
  displayState = display.get()
  try:
    mathFunction = sympify(displayState)
    clearDisplay()
    display.insert(0, mathFunction)
  except SympifyError:
    clearDisplay()
    display.insert(0,'Error')
    return

def upintegralLimit():
  global upLimit 
  
  displayState = display.get()
  try:
    upLimit = sympify(displayState)
    display.insert(0, "Limite superior:")
    
  except SympifyError:
    clearDisplay()
    display.insert(0,'Error')
    return

def downintegralLimit():
  global downLimit
  displayState = display.get()
  try:
    downLimit = sympify(displayState)
    display.insert(0, "Limite inferior:")
  except SympifyError:
    clearDisplay()
    display.insert(0,'Error')
    return

def nNumber():
  global n
  displayState = display.get()
  try:
    n = sympify(displayState)
    display.insert(0, "n:")
  except SympifyError:
    clearDisplay()
    display.insert(0,'Error')
    return

def calculateTrapeze():
  global downLimit, upLimit, n, mathFunction
  upLimit = upLimit.evalf()
  iter = 0
  finalFunction = []
  mid = 0
  clearDisplay()
  
  if downLimit == "" or upLimit == "" or n == "" or mathFunction == "":
    
    display.insert(0,'Error ingrese los valores necesarios')
  else:
    
    if downLimit>upLimit:
      
      clearDisplay()
      display.insert(0,"Error, revise los limites")
    else:
      
      mathFunction = sympify(mathFunction)
      triangle = ((upLimit - downLimit) / n).evalf()
      clearDisplay()
      display.insert(0, triangle)
      
      
      while True:
        
        finalFunction.append(mathFunction.evalf(subs={x:downLimit}))
        downLimit += triangle
        iter +=1
        print('limit sup '+str(upLimit)+', limit inf '+str(downLimit))
        if downLimit == upLimit or iter == n:
          
          iter +=1
          finalFunction.append(mathFunction.evalf(subs={x:downLimit}))
          downLimit += triangle
          
          break
      position = 0
      print('X'+str(position)+'='+str(finalFunction[0]))
      for elemento in finalFunction[1:-1]:
        position += 1
        print('X'+str(position)+'='+str(mid))
        mid = mid + (elemento * 2)
      position += 1
      print('X'+str(position)+'='+str(finalFunction[-1]))
      mid = mid + (finalFunction[0])
      mid = mid + (finalFunction[-1])
      
      triangle = triangle * 0.5
      finalResult = mid * triangle
      clearDisplay()
      display.insert(0, finalResult)



# Botones


Button(root,text="1", command=lambda:getNumbers(1), font=("Helvetica", font_size)).grid(row=2 , column=0, sticky=N+S+W+E)
Button(root,text="2", command=lambda:getNumbers(2), font=("Helvetica", font_size)).grid(row=2 , column=1, sticky=N+S+W+E)
Button(root,text="3", command=lambda:getNumbers(3), font=("Helvetica", font_size)).grid(row=2 , column=2, sticky=N+S+W+E)
Button(root,text="⇐", command=lambda:undo(), font=("Helvetica", font_size)).grid(row=2 , column=3, sticky=N+S+W+E)
Button(root,text="AC",command=lambda:clearDisplay(), font=("Helvetica", font_size)).grid(row=2 , column=4, sticky=N+S+W+E)

Button(root,text="4", command=lambda:getNumbers(4), font=("Helvetica", font_size)).grid(row=3 , column=0, sticky=N+S+W+E)
Button(root,text="5", command=lambda:getNumbers(5), font=("Helvetica", font_size)).grid(row=3 , column=1, sticky=N+S+W+E)
Button(root,text="6", command=lambda:getNumbers(6), font=("Helvetica", font_size)).grid(row=3 , column=2, sticky=N+S+W+E)
Button(root,text="+", command=lambda:getOperators("+"), font=("Helvetica", font_size)).grid(row=3 , column=3, sticky=N+S+W+E)
Button(root,text="-", command=lambda:getOperators("-"), font=("Helvetica", font_size)).grid(row=3 , column=4, sticky=N+S+W+E)

Button(root,text="7", command=lambda:getNumbers(7), font=("Helvetica", font_size)).grid(row=4 , column=0, sticky=N+S+W+E)
Button(root,text="8", command=lambda:getNumbers(8), font=("Helvetica", font_size)).grid(row=4 , column=1, sticky=N+S+W+E)
Button(root,text="9", command=lambda:getNumbers(9), font=("Helvetica", font_size)).grid(row=4 , column=2, sticky=N+S+W+E)
Button(root,text="*", command=lambda:getOperators("*"), font=("Helvetica", font_size)).grid(row=4 , column=3, sticky=N+S+W+E)
Button(root,text="/", command=lambda:getOperators("/"), font=("Helvetica", font_size)).grid(row=4 , column=4, sticky=N+S+W+E)

Button(root,text="0", command=lambda:getNumbers(0), font=("Helvetica", font_size)).grid(row=5 , column=0, sticky=N+S+W+E)
Button(root,text=".", command=lambda:getOperators("."), font=("Helvetica", font_size)).grid(row=5 , column=1, sticky=N+S+W+E)
Button(root,text="x", command=lambda:getOperators("x"), font=("Helvetica", font_size)).grid(row=5 , column=2, sticky=N+S+W+E)
Button(root,text="(", command=lambda:getOperators("("), font=("Helvetica", font_size)).grid(row=5 , column=3, sticky=N+S+W+E)
Button(root,text=")", command=lambda:getOperators(")"), font=("Helvetica", font_size)).grid(row=5 , column=4, sticky=N+S+W+E)

Button(root,text="^2", command=lambda:getOperators("**2"), font=("Helvetica", font_size)).grid(row=6 , column=0, sticky=N+S+W+E)
Button(root,text="^", command=lambda:getOperators("**"), font=("Helvetica", font_size)).grid(row=6 , column=1, sticky=N+S+W+E)
Button(root,text="√", command=lambda:getOperators("sqrt"), font=("Helvetica", font_size)).grid(row=6 , column=2, sticky=N+S+W+E)
Button(root,text="π", command=lambda:getOperators("pi"), font=("Helvetica", font_size)).grid(row=6 , column=3, sticky=N+S+W+E)
Button(root,text="=", command=lambda:calculate(), font=("Helvetica", font_size)).grid(row=6 , column=4, sticky=N+S+W+E)

Button(root,text="sin", command=lambda:getOperators("sin"), font=("Helvetica", font_size)).grid(row=7 , column=0, sticky=N+S+W+E)
Button(root,text="cos", command=lambda:getOperators("cos"), font=("Helvetica", font_size)).grid(row=7 , column=1, sticky=N+S+W+E)
Button(root,text="tan", command=lambda:getOperators("tan"), font=("Helvetica", font_size)).grid(row=7 , column=2, sticky=N+S+W+E)
Button(root,text="e", command=lambda:getOperators("e"), font=("Helvetica", font_size)).grid(row=7 , column=3, sticky=N+S+W+E)


for i in range(8):
    root.grid_columnconfigure(i, weight=1)
    root.grid_rowconfigure(i, weight=1)

root.mainloop()