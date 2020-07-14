from tkinter import Tk, Label, Button, LEFT,RIGHT

class MyFirstGUI:
  def __init__(self, master):
    self.master = master
    master.title('A Simple Gui')

    self.label = Label(master, text="This is our first GUI")
    self.label.pack()

    self.greet_button = Button(master, text='Greetint', command=self.greet)
    self.greet_button.pack(side=LEFT)

    self.close_button = Button(master, text="Close", command=master.quit)
    self.close_button.pack(side=RIGHT)

  def greet(self):
    print('Greetings!')

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()