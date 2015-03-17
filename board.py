# Author: Andy Au
# Date Modified: Mar 16, 2015

import Tkinter, threading
from PIL import Image, ImageTk

class boardapp_tk(Tkinter.Tk, threading.Thread):
  def __init__(self,parent):
    Tkinter.Tk.__init__(self,parent)
    self.parent = parent
    self.initialize()
    # self.thread()

  def initialize(self):
    self.grid()

    self.last = 1

    #image sizes
    self.imagesize = 640,400
    self.arrowsize = 30,20

    # images and resizing
    self.pool_image = Image.open("images/pool.jpg")
    self.pool_image.thumbnail(self.imagesize, Image.ANTIALIAS)
    self.tournament_bracket_image = Image.open("images/tournament-bracket.jpg")
    self.tournament_bracket_image.thumbnail(self.imagesize, Image.ANTIALIAS)
    self.smash_image = Image.open("images/smash.jpg")
    self.smash_image.thumbnail(self.imagesize, Image.ANTIALIAS)
    self.games_night_image = Image.open("images/games_night.jpg")
    self.games_night_image.thumbnail(self.imagesize, Image.ANTIALIAS)
    self.arrow = Image.open("images/arrow.jpg")
    self.arrow.thumbnail(self.arrowsize, Image.ANTIALIAS)
    
    # conversion to Tkinter object
    self.image = ImageTk.PhotoImage(self.pool_image)
    self.arrow_image = ImageTk.PhotoImage(self.arrow)

    # main
    self.main = Tkinter.Label(self,image=self.image)
    self.main.image = self.image
    self.main.grid(column=0,row=0,rowspan=6,sticky='EW')

    # arrow
    self.button_label = Tkinter.Label(self,image=self.arrow_image)
    self.main.arrowimage = self.arrow_image
    self.button_label.grid(column=1,row=0,sticky='EWNS')

    # buttons
    b1 = Tkinter.Button(self,text=u"Pool League",command=self.OnButton1Click)
    b1.grid(column=2,row=0,sticky='EWNS')
    b2 = Tkinter.Button(self,text=u"Tournament", command=self.OnButton2Click)
    b2.grid(column=2,row=1,sticky='EWNS')
    b3 = Tkinter.Button(self,text=u"Super Smash Brothers", command=self.OnButton3Click)
    b3.grid(column=2,row=2,sticky='EWNS')
    b4 = Tkinter.Button(self,text=u"Games Night", command=self.OnButton4Click)
    b4.grid(column=2,row=3,sticky='EWNS')

    self.grid_columnconfigure(0,weight=1)
    self.resizable(True,False)
    self.update()
    self.geometry(self.geometry())

  def OnButton1Click(self):
    self.image = ImageTk.PhotoImage(self.pool_image)
    self.main.configure(image = self.image)
    self.main.image = self.image
    self.button_label.grid(column=1,row=0,sticky='EWNS')
    self.last = 1

  def OnButton2Click(self):
    self.image = ImageTk.PhotoImage(self.tournament_bracket_image)
    self.main.configure(image = self.image)
    self.main.image = self.image
    self.button_label.grid(column=1,row=1,sticky='EWNS')
    self.last = 2

  def OnButton3Click(self):
    self.image = ImageTk.PhotoImage(self.smash_image)
    self.main.configure(image = self.image)
    self.main.image = self.image
    self.button_label.grid(column=1,row=2,sticky='EWNS')
    self.last = 3

  def OnButton4Click(self):
    self.image = ImageTk.PhotoImage(self.games_night_image)
    self.main.configure(image = self.image)
    self.main.image = self.image
    self.button_label.grid(column=1,row=3,sticky='EWNS')
    self.last = 3

  def thread(self):
    threading.Timer(10.0, self.thread).start()
    if self.last == 1:
      self.OnButton2Click()
      self.last = 2
    elif self.last == 2:
      self.last = 3
      self.OnButton3Click()
    elif self.last == 3:
      self.last = 1
      self.OnButton3Click()

if __name__ == "__main__":
  app = boardapp_tk(None)
  app.title('ECE Live Events')
  app.mainloop()