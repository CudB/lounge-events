# Author: Andy Au
# Date Modified: Mar 15, 2015

import Tkinter
from PIL import Image, ImageTk

class boardapp_tk(Tkinter.Tk):
  def __init__(self,parent):
    Tkinter.Tk.__init__(self,parent)
    self.parent = parent
    self.initialize()

  def initialize(self):
    self.grid()

    image_file = Image.open("images/pool.jpg")
    image = ImageTk.PhotoImage(image_file)

    main = Tkinter.Label(self,image=image)
    main.image = image
    main.grid(column=0,row=0,rowspan=10,sticky='EW')

    b1 = Tkinter.Button(self,text=u"Pool")
    b1.grid(column=1,row=0,sticky='EWN')

    b2 = Tkinter.Button(self,text=u"Foosball")
    b2.grid(column=1,row=1,sticky='EWN')

    b3 = Tkinter.Button(self,text=u"Super Smash Brothers")
    b3.grid(column=1,row=2,sticky='EWN')

    self.grid_columnconfigure(0,weight=1)
    self.resizable(True,False)
    self.update()
    self.geometry(self.geometry())

if __name__ == "__main__":
  app = boardapp_tk(None)
  app.title('Digital Board')
  app.mainloop()