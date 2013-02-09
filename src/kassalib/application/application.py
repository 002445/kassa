from Tkinter import *

class Application:
        
    def __init__(self):
        self.root = Tk()
        self.gui()
        
    def gui(self):
        frame = Frame(self.root)
        frame.pack()

        button = Button(frame, text="QUIT", command=frame.quit)
        button.pack(side=LEFT)
        
        button = Button(frame, text="FOO", command=self.sayHi)
        button.pack(side=RIGHT)
        
    def sayHi(self):
        print 'hello world!'
    
    def start(self):
        self.root.mainloop()