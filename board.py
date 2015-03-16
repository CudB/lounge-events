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

    self.pool_image = Image.open("images/pool.jpg")
    self.foosball_image = Image.open("images/foosball.jpg")
    self.smash_image = Image.open("images/smash.jpg")

    self.image = ImageTk.PhotoImage(self.smash_image)

    self.main = Tkinter.Label(self,image=self.image)
    self.main.image = self.image
    self.main.grid(column=0,row=0,rowspan=10,sticky='EW')

    b1 = Tkinter.Button(self,text=u"Pool", command=self.OnButton1Click)
    b1.grid(column=1,row=0,sticky='EWN')

    b2 = Tkinter.Button(self,text=u"Foosball", command=self.OnButton2Click)
    b2.grid(column=1,row=1,sticky='EWN')

    b3 = Tkinter.Button(self,text=u"Super Smash Brothers", command=self.OnButton3Click)
    b3.grid(column=1,row=2,sticky='EWN')

    self.grid_columnconfigure(0,weight=1)
    self.resizable(True,False)
    self.update()
    self.geometry(self.geometry())

  def OnButton1Click(self):
    self.image = ImageTk.PhotoImage(self.pool_image)
    self.main.configure(image = self.image)
    self.main.image = self.image

  def OnButton2Click(self):
    self.image = ImageTk.PhotoImage(self.foosball_image)
    self.main.configure(image = self.image)
    self.main.image = self.image

  def OnButton3Click(self):
    self.image = ImageTk.PhotoImage(self.smash_image)
    self.main.configure(image = self.image)
    self.main.image = self.image

if __name__ == "__main__":
  app = boardapp_tk(None)
  app.title('Digital Board')
  app.mainloop()