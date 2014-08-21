import pygame, ImageOps, shutil, ImageEnhance, Image, sys, os
from pygame.locals import *
from gi.repository import Gtk

class Photo(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title= "Python Hunter")
        self.a = 1
        self.b = 1
        self.c = 1
        self.d = 1
        self.e = 0
        self.border = 0          
        self.A = 1
        self.B = 1
        self.C = 1
        self.D = 1
        self.W = 1
        self.X = 1
        self.Y = 1
        self.Z = 1
        

        self.box = Gtk.Box(spacing = 10)
        self.right = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 6)
        self.left = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 18)
        self.box.pack_start(self.left, True, True, 0)        
        self.box.pack_start(self.right, True, True, 0)
        self.box1 = Gtk.Box(spacing = 6)
        self.box2 = Gtk.Box(spacing = 6)
        self.box3 = Gtk.Box(spacing = 6)
        self.box4 = Gtk.Box(spacing = 6)
        self.box9 = Gtk.Box(spacing = 6)
        self.box5 = Gtk.Box(spacing = 6)       
        self.box6 = Gtk.Box(spacing = 1)
        self.box7 = Gtk.Box(spacing = 1)
        self.box8 = Gtk.Box(spacing = 1) 
        self.box10 = Gtk.Box(spacing = 1)
        self.box11 = Gtk.Box(spacing = 1)
        self.box12 = Gtk.Box(spacing = 1)        


        self.right.pack_start(self.box8, True, True, 0)
        self.right.pack_start(self.box1, True, True, 0)
        self.right.pack_start(self.box2, True, True, 0)
        self.right.pack_start(self.box3, True, True, 0)
        self.right.pack_start(self.box4, True, True, 0)
        self.right.pack_start(self.box9, True, True, 0)      
         
        self.add(self.box)
 
        self.Button13 = Gtk.Button(label = "Upload")
        self.Button13.connect("clicked", self.Upload)
        self.box8.pack_start(self.Button13, True, True, 0)
        self.Button14 = Gtk.Button(label = "Save")
        self.Button14.connect("clicked", self.Save)
        self.box8.pack_start(self.Button14, True, True, 0)
     
        self.BA1 = Gtk.Button(label = "+")
        self.BA1.connect("clicked", self.BriA1)
        self.box1.pack_start(self.BA1, True, True, 0)
        self.BS1 = Gtk.Button(label = "-")
        self.BS1.connect("clicked", self.BriS1)
        self.box1.pack_start(self.BS1, True, True, 0)

 
        self.BA2 = Gtk.Button(label = "+")
        self.BA2.connect("clicked", self.ShaA2)
        self.box2.pack_start(self.BA2, True, True, 0)
        self.BS2 = Gtk.Button(label = "-")
        self.BS2.connect("clicked", self.ShaS2)
        self.box2.pack_start(self.BS2, True, True, 0)

       

        self.BA3 = Gtk.Button(label = "+")
        self.BA3.connect("clicked", self.ColA3)
        self.box3.pack_start(self.BA3, True, True, 0)
        self.BS3 = Gtk.Button(label = "-")
        self.BS3.connect("clicked", self.ColS3)
        self.box3.pack_start(self.BS3, True, True, 0)



        self.BA4 = Gtk.Button(label = "+")
        self.BA4.connect("clicked", self.ConA4)
        self.box4.pack_start(self.BA4, True, True, 0)
        self.BS4 = Gtk.Button(label = "-")
        self.BS4.connect("clicked", self.ConS4)
        self.box4.pack_start(self.BS4, True, True, 0)
        self.Button10 = Gtk.Button(label = "Classic")
        self.Button10.connect("clicked", self.Classic)
        self.right.pack_start(self.Button10, True, True, 0)
       
        self.right.pack_start(self.box5, True, True, 0)

        self.Button11 = Gtk.Button(label = "Paint")
        self.Button11.connect("clicked", self.Paint)
        self.right.pack_start(self.Button11, True, True, 0)

        

        self.right.pack_start(self.box6, True, True, 0)
        self.right.pack_start(self.box7, True, True, 0)
 
        self.E1 = Gtk.Entry()
        self.E1.set_text("100")
        self.E1.set_max_length(3)
        self.E2 = Gtk.Entry()
        self.E2.set_text("100")
        self.E2.set_max_length(3)
        self.E3 = Gtk.Entry()
        self.E3.set_text("600")
        self.E3.set_max_length(3)
        self.E4 = Gtk.Entry()
        self.E4.set_text("500")
        self.E4.set_max_length(3)
        self.L1 = Gtk.Label("LFT")
        self.L2 = Gtk.Label("TOP")
        self.L3 = Gtk.Label("RGT")
        self.L4 = Gtk.Label("BTM")
        
       

        self.box6.pack_start(self.L1, True, True, 0)
        self.box6.pack_start(self.E1, True, True, 0)
        self.box6.pack_start(self.L2, True, True, 0)
        self.box6.pack_start(self.E2, True, True, 0)
        self.box7.pack_start(self.L3, True, True, 0)
        self.box7.pack_start(self.E3, True, True, 0)
        self.box7.pack_start(self.L4, True, True, 0)
        self.box7.pack_start(self.E4, True, True, 0)

        self.Button5 = Gtk.Button(label = "Crop")
        self.Button5.connect("clicked", self.Crop)
        self.right.pack_start(self.Button5, True, True, 0)
        
        self.right.pack_start(self.box10, True, True, 0)
        self.right.pack_start(self.box11, True, True, 0) 
        self.right.pack_start(self.box12, True, True, 0)                

        self.Button6 = Gtk.Button(label = "Cropborder")
        self.Button6.connect("clicked", self.Cropborder)
        self.box10.pack_start(self.Button6, True, True, 0)
        self.Button7 = Gtk.Button(label = "Invert")
        self.Button7.connect("clicked", self.Invert)
        self.box10.pack_start(self.Button7, True, True, 0)
        self.Button8 = Gtk.Button(label = "Rgba")
        self.Button8.connect("clicked", self.Rgba)
        self.box10.pack_start(self.Button8, True, True, 0)
        self.Button9 = Gtk.Button(label = "Cmyk")
        self.Button9.connect("clicked", self.Cmyk)
        self.box11.pack_start(self.Button9, True, True, 0)
        self.Button12 = Gtk.Button(label = "Sepia" ) 
        self.Button12.connect("clicked", self.Sepia)
        self.box11.pack_start(self.Button12, True, True, 0)
        self.Button15 = Gtk.Button(label = "Rotate")
        self.Button15.connect("clicked", self.Rotate)
        self.box11.pack_start(self.Button15, True, True, 0)        
        self.Button16 = Gtk.Button(label = "Resize")
        self.Button16.connect("clicked", self.Resize)
        self.box12.pack_start(self.Button16, True, True, 0)
        self.Button17 = Gtk.Button(label = "FBcover")
        self.Button17.connect("clicked", self.FBcover)
        self.box12.pack_start(self.Button17, True, True, 0)

        self.Entry = Gtk.Entry()
        self.Entry.set_text("#000000")
        self.Entry.set_max_length(7)
        self.Lab = Gtk.Label("Color")
        self.box9.pack_start(self.Lab, True, True, 0)
        self.box9.pack_start(self.Entry, True, True, 0)
        

        self.Entr = Gtk.Entry()
        self.Entr.set_text("#000033")
        self.Entr.set_max_length(7)
        self.Entr1 = Gtk.Entry()
        self.Entr1.set_text("1")
        self.Entr1.set_max_length(2)
        self.La = Gtk.Label("Color")
        self.La1 = Gtk.Label("Contrast")
        self.box5.pack_start(self.La1, True, True, 0)
        self.box5.pack_start(self.Entr1, True, True, 0)
        self.box5.pack_start(self.La, True, True, 0)
        self.box5.pack_start(self.Entr, True, True, 0)

        self.Label1 = Gtk.Label("")
        self.left.pack_start(self.Label1, False, False, 0) 
        self.Label1 = Gtk.Label("Bright")
        self.left.pack_start(self.Label1, False, False, 0)
        self.Label2 = Gtk.Label("Sharpness")
        self.left.pack_start(self.Label2, False, False, 0)
        self.Label3 = Gtk.Label("Color")
        self.left.pack_start(self.Label3, False, False, 0)
        self.Label4 = Gtk.Label("Contrast")
        self.left.pack_start(self.Label4, False, False, 0)
    



    def BriA1(self, Button):
        self.p = Image.open(self.Newpath)
        if self.a < 1:
            self.a = 1
        self.a = self.a + 0.1
        self.s = ImageEnhance.Brightness(self.p).enhance(self.a)
        self.s.show()
        self.s.save(self.Newpath)

    def BriS1(self, Button):
        self.p = Image.open(self.Newpath)
        if self.a > 1:
            self.a = 1
        self.a = self.a - 0.1
        self.s = ImageEnhance.Brightness(self.p).enhance(self.a)
        self.s.show()
        self.s.save(self.Newpath)

    def ShaA2(self, Button): 
        self.p = Image.open(self.Newpath)
        if self.b < 1:
            self.b = 1
        self.b = self.b + 0.1
        self.s = ImageEnhance.Sharpness(self.p).enhance(self.b)
        self.s.show()
        self.s.save(self.Newpath)

    def ShaS2(self, Button):    
        self.p = Image.open(self.Newpath)
        if self.b > 1:
            self.b = 1
        self.b = self.b - 0.1
        self.s = ImageEnhance.Sharpness(self.p).enhance(self.b)
        self.s.show()
        self.s.save(self.Newpath)


    def ColA3(self, Button):
        self.p = Image.open(self.Newpath)
        if self.c < 1:
            self.c = 1
        self.c = self.c + 0.1
        self.s = ImageEnhance.Color(self.p).enhance(self.c)
        self.s.show()
        self.s.save(self.Newpath)

    def ColS3(self, Button):
        self.p = Image.open(self.Newpath)
        if self.c > 1:
            self.c = 1
        self.c = self.c - 0.1
        self.s = ImageEnhance.Color(self.p).enhance(self.c)
        self.s.show()
        self.s.save(self.Newpath)

    def ConA4(self, Button):
        self.p = Image.open(self.Newpath)
        if self.d < 1:
            self.d = 1
        self.d = self.d + 0.05
        self.s = ImageEnhance.Contrast(self.p).enhance(self.d)
        self.s.show()
        self.s.save(self.Newpath)

    def ConS4(self, Button):
        self.p = Image.open(self.Newpath)
        if self.d > 1:
            self.d = 1
        self.d = self.d - 0.05
        self.s = ImageEnhance.Contrast(self.p).enhance(self.d)
        self.s.show()
        self.s.save(self.Newpath)


    def Resize(self, Button):  
       
        self.p = Image.open(self.Newpath)
        self.width = self.p.size[0] /2
        self.height = self.p.size[1] /2
        self.s = self.p.resize((self.width, self.height)) 
        self.s.show()
        self.s.save(self.Newpath)
 
    def Rotate(self, Button):
        self.p = Image.open(self.Newpath)
        self.e = self.e + 90
        self.s = self.p.rotate(self.e)
        self.s.show()
        self.s.save(self.Newpath)
 
    def FBcover(self, Button):
        width = 858
        height = 315 
        self.p = Image.open(self.Newpath)
        self.s = self.p.resize((width, height), Image.ANTIALIAS)
        self.s.show()
        self.s.save(self.Newpath)

          
    def Invert(self, Button): 
        self.p = Image.open(self.Newpath)
        self.s = ImageOps.invert(self.p)
        self.s.show()
        self.s.save(self.Newpath)

   

    def Rgba(self, Button):      
        self.p = Image.open(self.Newpath)  
        self.p = self.p.convert("RGBA")
        r, g, b, a = self.p.split()
        self.s = Image.merge("RGBA", (b, r, g, a))
        self.s.show()
        self.s.save(self.Newpath)

    def Cmyk(self, Button):       
        self.p = Image.open(self.Newpath)
        self.p = self.p.convert("CMYK")
        c, m, y, k = self.p.split()
        self.s = Image.merge("CMYK", (m, y, c, k))
        self.s.show()
        self.s.save(self.Newpath)

    def Classic(self, Button, alpha = 0.3):        
        self.p = Image.open(self.Newpath)
        color = self.Entry.get_text()
        self.p1 = ImageEnhance.Color(self.p).enhance(0)
        self.p2 = Image.new(self.p.mode, (self.p.size[0], self.p.size[1]), color)
        self.s = Image.blend(self.p1, self.p2, alpha)
        self.s.show()
        self.s.save(self.Newpath)
           
    def Paint(self, Button, alpha = 0.3):
        self.p = Image.open(self.Newpath)
        color = self.Entr.get_text()
        con = int(self.Entr1.get_text())
        self.p1 = ImageEnhance.Contrast(self.p).enhance(con)
        self.p2 = Image.new(self.p.mode, (self.p.size[0], self.p.size[1]), color)
        self.s = Image.blend(self.p1, self.p2, alpha)
        self.s.show()
        self.s.save(self.Newpath)
   
 

    def Cropborder(self, Button):      
        self.p = Image.open(self.Newpath)
        self.border = self.border + 10
        self.s = ImageOps.crop(self.p, self.border)
        self.s.show()
        self.s.save(self.Newpath)

    def Crop(self, Button):
        self.p = Image.open(self.Newpath)
        self.A = int(self.E1.get_text())
        self.B = int(self.E2.get_text())
        self.C = int(self.E3.get_text())
        self.D = int(self.E4.get_text())
        print self.E1.get_text(), self.E2.get_text(), self.E3.get_text(), self.E4.get_text()
        print self.p.size, self.A, self.B, self.C, self.D
        print self.p.size[0]/4
        print self.p.size[0]/4
        print self.p.size[1]*3/4 
        print self.p.size[1]*3/4
        self.p1 = (self.A, self.B, self.C, self.D)
        #self.p1 = (self.p.size[0]/4, self.p.size[0]/4, self.p.size[1]*3/4, self.p.size[1]*3/4)
        self.s = self.p.crop(self.p1)
        self.s.show()
        self.s.save(self.Newpath)
 
    def Sepia(self, Button):
        self.p = Image.open(self.Newpath)
        self.s= self.p.convert("L")
        self.s.show()
        self.s.save(self.Newpath)
 
    def Upload(self, Button):
        dialog = Gtk.FileChooserDialog("Please choose a file", self, Gtk.FileChooserAction.OPEN, (Gtk.STOCK_OPEN, Gtk.ResponseType.OK, Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL))
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print "Clicked Open"
            self.Path = dialog.get_filename()
            direct = os.path.dirname(self.Path)
            self.Newpath = direct + "/editor.jpg" 
            shutil.copy(self.Path, self.Newpath)
            Pic = Image.open(self.Path)
            Pic.show()
            print "File Selected:" + self.Path
        elif response == Gtk.ResponseType.CANCEL:
            print "Clicked Cancel"    
        dialog.destroy()

    def Save(self, Button):
        dialog = Gtk.FileChooserDialog("Select the location", self, Gtk.FileChooserAction.SAVE, (Gtk.STOCK_SAVE, Gtk.ResponseType.OK, Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL))
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print "Clicked save"
            self.Save = dialog.get_filename()
            self.s.save(self.Save) 
        elif response == Gtk.ResponseType.CANCEL:
            print "Clicked cancel"
        dialog.destroy()

           
win = Photo()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
