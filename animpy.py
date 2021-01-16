from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import turtle
import time
from PIL import Image
from tkinter import tix

class App:
    s="""self.screen.clearscreen()
self.screen.listen()
self.draw = turtle.RawTurtle(self.screen)
self.draw.pu()
self.screen.onclick(self.listen)
self.draw.ondrag(self.dragging)
self.k=""
self.sav=0
self.bh=""
self.file=""
self.i=0
self.jj=1
self.jj1=0
self.fgh=0
self.func=""
self.func_name=""
self.functions=[]
self.keylinks={}
self.headings={"Object1":0}
self.objects={"Object1":self.draw}
self.index=1
self.stam=0
self.redos=[]#
"""
    s1=s
    k=""
    sav=1
    bh=""
    file=""
    i=0
    jj=1
    jj1=0
    fgh=0
    func=""
    func_name=""
    functions=[]
    keylinks={}
    headings={"Object1":0}
    index=1
    stam=0
    redos=[]
    COLOURS  =['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
    'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
    'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
    'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
    'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
    'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
    'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
    'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
    'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
    'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
    'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
    'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
    'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
    'indian red', 'saddle brown', 'sandy brown',
    'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
    'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
    'pale violet red', 'maroon', 'medium violet red', 'violet red',
    'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
    'thistle', 'snow2', 'snow3',
    'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
    'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
    'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
    'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
    'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
    'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
    'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
    'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
    'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
    'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
    'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
    'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
    'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
    'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
    'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
    'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
    'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
    'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
    'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
    'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
    'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
    'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
    'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
    'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
    'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
    'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
    'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
    'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
    'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
    'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
    'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
    'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
    'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
    'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
    'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
    'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
    'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
    'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
    'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
    'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
    'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
    'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
    'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
    'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
    'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
    'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',
    'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10',
    'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19',
    'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28',
    'gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37',
    'gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47',
    'gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56',
    'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65',
    'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74',
    'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83',
    'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92',
    'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']
    def __init__(self,master):
        self.master=master
        b=tix.Balloon(self.master)
        self.tabcon=ttk.Notebook(self.master)
        self.pw=Frame(self.tabcon)
        self.tabcon.add(self.pw,text="Actions")
        self.pl=Frame(self.tabcon)
        self.tabcon.add(self.pl,text="Time")
        self.nb=Frame(self.tabcon)
        self.tabcon.add(self.nb,text="Loop")
        self.ia=Frame(self.tabcon)
        self.tabcon.add(self.ia,text="Objects")
        self.fg=Frame(self.tabcon)
        self.tabcon.add(self.fg,text="functions")
        self.df=Frame(self.tabcon)
        self.tabcon.add(self.df,text="key links")
        self.yu=Frame(self.tabcon)
        self.tabcon.add(self.yu,text="Screen")
        self.tabcon.grid(row=0,column=0,sticky="n")
        self.canvas = turtle.ScrolledCanvas(master = self.master)
        self.canvas.grid(row=0,column=1)
        self.screen=turtle.TurtleScreen(self.canvas)
        self.draw = turtle.RawTurtle(self.screen)
        self.screen.listen()
        self.draw.pu()
        self.objects={"Object1":self.draw}
        self.screen.onclick(self.listen)
        self.draw.ondrag(self.dragging)
        
        Button(self.pw,text="move upwards",command=self.up).grid()
        Button(self.pw,text="move downwards",command=self.down).grid()
        Button(self.pw,text="move right",command=self.right).grid()
        Button(self.pw,text="move left",command=self.left).grid()
        Button(self.pw,text="move forward",command=self.fwd).grid(row=4,column=0)
        Button(self.pw,text="move backward",command=self.bwd).grid(row=5,column=0)
        self.deg=Entry(self.pw)
        self.deg.grid(row=6,column=1)
        Button(self.pw,text="Rotate left",command=self.rotlt).grid(row=6,column=0)
        self.deg1=Entry(self.pw)
        self.deg1.grid(row=7,column=1)
        Button(self.pw,text="Rotate right",command=self.rotrt).grid(row=7,column=0)
        Button(self.pw,text="Show object",command=self.show).grid(row=8,column=0)
        Button(self.pw,text="Hide object",command=self.hide).grid(row=9,column=0)
        Button(self.pw,text="stamp",command=self.stamp).grid(row=10,column=0)
        Button(self.pw,text="clear previous stamp",command=self.clprestmp).grid(row=11)
        Button(self.pw,text="clear all stamps",command=self.clallstmp).grid(row=12)
        self.gotopos=Entry(self.pw)
        self.gotopos.grid(row=13,column=1)
        Button(self.pw,text="goto position",command=self.goto).grid(row=13,column=0)
        self.circpar=Entry(self.pw)
        self.circpar.grid(row=14,column=1)
        Button(self.pw,text="circle",command=self.circ).grid(row=14,column=0)
        b.bind_widget(self.circpar, msg="""Draw a circle with given radius. The center is radius units left of the turtle; extent – an angle – determines which
part of the circle is drawn. If extent is not given, draw the entire circle. If extent is not a full circle, one endpoint
of the arc is the current pen position. Draw the arc in counterclockwise direction if radius is positive, otherwise in
clockwise direction. Finally the direction of the turtle is changed by the amount of extent. As the circle is approximated
by an inscribed regular polygon, steps determines the number of steps to use. If not given, it will be calculated automatically.
May be used to draw regular polygons. Enter the three parameters one after the other separated by commas. radius is compulsory.""")
        Button(self.pw,text="pen down",command=self.pendown).grid()
        Button(self.pw,text="pen up",command=self.penup).grid()
        Button(self.pw,text="Choose pen colour",command=lambda:self.colourchoose("pencolour")).grid()

        self.wo=Entry(self.pl)
        self.wo.grid(row=0,column=1)
        Button(self.pl,text="Wait for",command=self.wa).grid(row=0,column=0)
        self.delay=Entry(self.pl)
        self.delay.grid(row=1,column=1)
        Button(self.pl,text="set animation delay",command=self.dela).grid(row=1,column=0)
        self.speed=Entry(self.pl)
        self.speed.grid(row=2,column=1)
        Button(self.pl,text="set object speed",command=self.spee).grid(row=2,column=0) 
        b.bind_widget(self.speed,msg="enter integer from 0 to 10. 0 means no animation.")

        self.lo=Entry(self.nb)
        self.lo.grid(row=0,column=1)
        Label(self.nb,text="Loop length").grid(row=0,column=0)
        Button(self.nb,text="Start loop",command=self.lop).grid(row=1,column=0)
        Button(self.nb,text="End loop",command=self.loz).grid(row=2,column=0)

        Button(self.ia,text="Object"+str(self.index),command=lambda:self.chobj("Object1")).grid(row=0,column=0)
        self.chs=Button(self.ia,text="Change shape of current object",command=lambda:self.chsh())
        self.chs.grid(row=1,column=0)

        self.addt=Button(self.ia,text="Add object",command=lambda:self.addobj())
        self.addt.grid(row=self.jj+1,column=0)
        self.curob=Label(self.ia,text="current object is Object1")
        self.curob.grid(row=self.jj+2)


        self.stf=Button(self.fg,text="Start Creating Function",command=lambda:self.stafunc())
        self.stf.grid(row=self.jj1)
        self.stf1=Button(self.fg,text="Stop Creating Function",command=lambda:self.stofunc())
        self.stf1.grid(row=self.jj1+1)
        func_name=""
        func=""

        self.keymenu=Menubutton(self.df,text="keys",relief=RAISED)
        self.keymenu.grid(row=self.fgh)
        self.keymenu.menu = Menu(self.keymenu,tearoff=0)   
        self.keymenu["menu"]= self.keymenu.menu
        keys=['space','enter','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','Up','Down','Left','Right','1','2','3','4','5','6','7','8','9','0','Shift']
        for j in keys:
            self.keymenu.menu.add_command(label=j,command=lambda j=j:self.key(j))
        self.fulk=Entry(self.df)
        self.fulk.grid(row=self.fgh,column=1)
        self.keylink=Button(self.df,text="add keylink",command=lambda:self.addkeylink())
        self.keylink.grid(row=self.fgh,column=2)

        Button(self.yu,text="Stop animating",command=self.stoani).grid()
        Button(self.yu,text="Start animating",command=self.staani).grid()
        Button(self.yu,text="choose bgpic",command=self.bgpic).grid()
        Button(self.yu,text="choose bgcolour",command=lambda:self.colourchoose("bgcolour")).grid()

        self.menubar=Menu(self.master)
        self.file = Menu(self.menubar, tearoff=0)  
        self.file.add_command(label="New",command=lambda:self.new()) 
        self.file.add_command(label="Open",command=lambda:self.ope())  
        self.file.add_command(label="Save",command=lambda:self.save())
        self.file.add_command(label="Exit", command=self.master.quit)  
        self.menubar.add_cascade(label="File", menu=self.file)  
        self.edit = Menu(self.menubar, tearoff=0)  
        self.edit.add_command(label="Undo",command=lambda:self.undo())
        self.menubar.add_cascade(label="Edit", menu=self.edit)  
        self.helpa = Menu(self.menubar, tearoff=0)  
        self.helpa.add_command(label="About")  
        self.menubar.add_cascade(label="Help", menu=self.helpa)  
        self.run=Menu(self.menubar,tearoff=0)
        self.run.add_command(label="Run",command=lambda:self.starun())
        self.menubar.add_cascade(label="Run",menu=self.run)
        self.master.config(menu=self.menubar)

    def listen(self,x,y):
        self.screen.listen()
        print(x,y)
    def dragging(self,x, y):
        if(self.k!=""):
            self.bh+=self.k+f"self.draw.ondrag(None)\n{self.k}self.draw.goto({x},{y})\n{self.k}self.draw.ondrag(self.dragging)\n"
        elif(self.func!=""):
            self.func+=f"    self.draw.goto({x},{y})\n"
        else:
            self.draw.ondrag(None)
            self.s+=f"self.draw.goto({x},{y})#\n"
            self.draw.goto(x, y)
            self.draw.ondrag(self.dragging)
        self.sav=0
    def up(self):
        if(self.k!=""):
            self.bh+=self.k+"self.draw.sety(self.draw.ycor()+15)\n"
        elif(self.func!=""):
            self.func+="    self.draw.sety(self.draw.ycor()+15)\n"
        else:
            self.draw.sety(self.draw.ycor()+15)
            self.s+="self.draw.sety(self.draw.ycor()+15)#\n"
        self.sav=0
    def down(self):
        if(self.k!=""):
            self.bh+=self.k+"self.draw.sety(self.draw.ycor()-15)\n"
        elif(self.func!=""):
            self.func+="    self.draw.sety(self.draw.ycor()-15)\n"
        else:
            self.draw.sety(self.draw.ycor()-15)
            self.s+="self.draw.sety(self.draw.ycor()-15)#\n"
        self.sav=0
    def right(self):
        if(self.k!=""):
            self.bh+=self.k+"self.draw.setx(self.draw.xcor()+15)\n"
        elif(self.func!=""):
            self.func+="    self.draw.setx(self.draw.xcor()+15)\n"
        else:
            self.draw.setx(self.draw.xcor()+15)
            self.s+="self.draw.setx(self.draw.xcor()+15)#\n"
        self.sav=0
    def left(self):
        if(self.k!=""):
            self.bh+=self.k+"self.draw.setx(self.draw.xcor()-15)\n"
        elif(self.func!=""):
            self.func+="    self.draw.setx(self.draw.xcor()-15)\n"
        else:
            self.draw.setx(self.draw.xcor()-15)
            self.s+="self.draw.setx(self.draw.xcor()-15)#\n"
        self.sav=0
    def fwd(self):
        if(self.k!=""):
            self.bh+=self.k+"self.draw.fd(15)\n"
        elif(self.func!=""):
            self.func+="    self.draw.fd(15)\n"
        else:
            self.draw.fd(15)
            self.s+="self.draw.fd(15)#\n"
        self.sav=0
    def bwd(self):
        if(self.k!=""):
            self.bh+=self.k+"self.draw.bk(15)\n"
        elif(self.func!=""):
            self.func+="    self.draw.bk(15)\n"
        else:
            self.draw.bk(15)
            self.s+="self.draw.bk(15)#\n"
        self.sav=0
    def rotlt(self):
        try:
            int(self.deg.get())
            if(self.i==0):
                if(self.k!=""):
                    self.bh+=self.k+"self.draw.lt(int("+self.deg.get()+"))\n"+self.k+"self.angle+=int("+self.deg.get()+")\n"
                elif(self.func!=""):
                    self.func+="    self.draw.lt(int("+self.deg.get()+"))\n"+"    self.angle+=int("+self.deg.get()+")\n"
                else:
                    self.s+="self.draw.lt(int("+self.deg.get()+"))#\n"
                    self.draw.lt(int(self.deg.get()))
                    self.headings[self.curob["text"][18:]]+=int(self.deg.get())
            else:
                if(self.k!=""):
                    self.bh+=f"""{self.k}im=Image.open('"""+self.file+f"""')
{self.k}im=im.convert('RGBA')
{self.k}self.headings[self.curob["text"][18:]]+=int("""+self.deg.get()+f""")
{self.k}im=im.rotate(self.headings[self.curob["text"][18:]],expand=1)
{self.k}dst_im = Image.new("RGBA",im.size,"white")
{self.k}dst_im.paste( im, (0,0),im)
{self.k}dst_im.save("a.gif",transparency=0)
{self.k}self.screen.addshape("a.gif")
{self.k}self.draw.shape("a.gif")
"""
                    self.bh+=self.k+"self.draw.lt(int("+self.deg.get()+"))\n"
                elif(self.func_name!=""):
                    self.func+="""    im=Image.open('"""+self.file+"""')
    im=im.convert('RGBA')
    self.headings[self.curob["text"][18:]]+=int("""+self.deg.get()+""")
    im=im.rotate("""+str(self.headings[self.curob["text"][18:]])+""",expand=1)
    dst_im = Image.new("RGBA",im.size,"white")
    dst_im.paste( im, (0,0),im)
    dst_im.save("a.gif",transparency=0)
    self.screen.addshape("a.gif")
    self.draw.shape("a.gif")
    """
                    self.func+="    self.draw.lt(int("+self.deg.get()+"))\n"                  
                else:
                    im=Image.open(self.file)
                    im=im.convert('RGBA')
                    self.headings[self.curob["text"][18:]]+=int(self.deg.get())
                    im=im.rotate(self.headings[self.curob["text"][18:]],expand=1)
                    dst_im = Image.new("RGBA",im.size,"white")
                    dst_im.paste( im, (0,0),im)
                    dst_im.save("a.gif",transparency=0)
                    self.screen.addshape("a.gif")
                    self.draw.shape("a.gif")
                    self.s+="""im=Image.open('"""+self.file+"""')
im=im.convert('RGBA')
self.headings[self.curob["text"][18:]]+=int("""+self.deg.get()+""")
im=im.rotate("""+str(self.headings[self.curob["text"][18:]])+""",expand=1)
dst_im = Image.new("RGBA",im.size,"white")
dst_im.paste( im, (0,0),im)
dst_im.save("a.gif",transparency=0)
self.screen.addshape("a.gif")
self.draw.shape("a.gif")
"""
                    self.s+="self.draw.lt(int("+self.deg.get()+"))#\n"  
                    self.draw.lt(int(self.deg.get()))
            self.sav=0
        except:
            pass
    def rotrt(self):
        try:
            int(self.deg1.get())
            if(self.i==0):
                if(self.k!=""):
                    self.bh+=self.k+"self.draw.rt(int("+self.deg1.get()+"))\n"+self.k+"self.angle+=int("+self.deg.get()+")\n"
                elif(self.func!=""):
                    self.func+="    self.draw.rt(int("+self.deg1.get()+"))\n"+"    self.angle+=int("+self.deg.get()+")\n"
                else:
                    self.s+="self.draw.rt(int("+self.deg1.get()+"))\n"
                    self.draw.rt(int(self.deg1.get()))
                    self.headings[self.curob["text"][18:]]+=360-int(self.deg.get())
            else:
                if(self.k!=""):
                    self.bh+=f"""{self.k}im=Image.open('"""+self.file+f"""')
{self.k}im=im.convert('RGBA')
{self.k}self.headings[self.curob["text"][18:]]+=360-int("""+self.deg1.get()+f""")
{self.k}im=im.rotate(self.headings[self.curob["text"][18:]],expand=1)
{self.k}dst_im = Image.new("RGBA",im.size,"white")
{self.k}dst_im.paste( im, (0,0),im)
{self.k}dst_im.save("a.gif",transparency=0)
{self.k}self.screen.addshape("a.gif")
{self.k}self.draw.shape("a.gif")
"""
                    self.bh+=self.k+"self.draw.rt(int("+self.deg1.get()+"))\n"
                elif(self.func_name!=""):
                    self.func+="""    im=Image.open('"""+self.file+"""')
    im=im.convert('RGBA')
    self.headings[self.curob["text"][18:]]+=360-int("""+self.deg1.get()+""")
    im=im.rotate("""+str(self.headings[self.curob["text"][18:]])+""",expand=1)
    dst_im = Image.new("RGBA",im.size,"white")
    dst_im.paste( im, (0,0),im)
    dst_im.save("a.gif",transparency=0)
    self.screen.addshape("a.gif")
    self.draw.shape("a.gif")
    """
                    self.func+="    self.draw.rt(int("+self.deg1.get()+"))\n"                  
                else:
                    im=Image.open(self.file)
                    im=im.convert('RGBA')
                    self.headings[self.curob["text"][18:]]+=360-int(self.deg1.get())
                    im=im.rotate(self.headings[self.curob["text"][18:]],expand=1)
                    dst_im = Image.new("RGBA",im.size,"white")
                    dst_im.paste( im, (0,0),im)
                    dst_im.save("a.gif",transparency=0)
                    self.screen.addshape("a.gif")
                    self.draw.shape("a.gif")
                    self.s+="""im=Image.open('"""+self.file+"""')
im=im.convert('RGBA')
self.headings[self.curob["text"][18:]]+=360-int("""+self.deg1.get()+""")
im=im.rotate("""+str(self.headings[self.curob["text"][18:]])+""",expand=1)
dst_im = Image.new("RGBA",im.size,"white")
dst_im.paste( im, (0,0),im)
dst_im.save("a.gif",transparency=0)
self.screen.addshape("a.gif")
self.draw.shape("a.gif")
"""
                    self.s+="self.draw.rt(int("+self.deg1.get()+"))#\n"  
                    self.draw.rt(int(self.deg1.get()))
            self.sav=0
        except:
            raise
    def show(self):
        if(self.k!=""):
            self.bh+=self.k+"self.draw.st()\n"
        elif(self.func!=""):
            self.func+="    self.draw.st()\n"        
        else:
            self.draw.st()
            self.s+="self.draw.st()#\n"
        self.sav=0
    def hide(self):
        if(self.k!=""):
            self.bh+=self.k+"self.draw.ht()\n"
        elif(self.func!=""):
            self.func+="    self.draw.st()\n"   
        else:
            self.draw.ht()
            self.s+="self.draw.ht()#\n"
        self.sav=0
    def stamp(self):
        if(self.k!=""):
            self.bh+=self.k+"self.stam=self.draw.stamp()\n"
        elif(self.func!=""):
            self.func+="    self.stam=self.draw.stamp()\n"
        else:
            self.stam=self.draw.stamp()
            self.s+="self.stam=self.draw.stamp()#\n"
        self.sav=0
    def clprestmp(self):
        if(self.k!=""):
            self.bh+=self.k+"self.draw.clearstamp(self.stam)\n"
        elif(self.func!=""):
            self.func+="    self.draw.clearstamp(self.stam)\n"
        else:
            self.draw.clearstamp(self.stam)
            self.s+="self.draw.clearstamp(self.stam)#\n"
        self.sav=0
    def clallstmp(self):
        if(self.k!=""):
            self.bh+=self.k+"self.draw.clearstamps()\n"
        elif(self.func!=""):
            self.func+="    self.draw.clearstamps()\n"
        else:
            self.draw.clearstamps()
            self.s+="self.draw.clearstamps()#\n"
        self.sav=0
    def goto(self):
        import random
        try:
            float(self.gotopos.get().split(',')[0])
            if(self.k!=""):
                if(self.gotopos.get()=="random"):
                    x=random.randint(0,list(self.screen.screensize())[0])
                    y=random.randint(0,list(self.screen.screensize())[1])
                    self.bh+=self.k+f"self.draw.goto({x},{y})\n"
                else:
                    self.bh+=self.k+f"self.draw.goto(float({self.gotopos.get().split(',')[0]}),float({self.gotopos.get().split(',')[1]}))\n"
            elif(self.func!=""):
                if(self.gotopos.get()=="random"):
                    x=random.randint(0,list(self.screen.screensize())[0])
                    y=random.randint(0,list(self.screen.screensize())[1])
                    self.func+=f"    self.draw.goto({x},{y})\n"
                else:
                    self.func+=f"    self.draw.goto(float({self.gotopos.get().split(',')[0]}),float({self.gotopos.get().split(',')[1]}))\n"
            else:
                if(self.gotopos.get()=="random"):
                    x=random.randint(0,list(self.screen.screensize())[0])
                    y=random.randint(0,list(self.screen.screensize())[1])
                    self.draw.goto(x,y)
                    self.s+=f"self.draw.goto({x},{y})#\n"
                else:
                    self.draw.goto(float(self.gotopos.get().split(",")[0]),float(self.gotopos.get().split(",")[1]))
                    self.s+=f"self.draw.goto(float({self.gotopos.get().split(',')[0]}),float({self.gotopos.get().split(',')[1]}))#\n"
            self.sav=0
        except:
            pass
    def circ(self):
        try:
            int(self.circpar.get().split(',')[0])
            if(self.k!=""):
                if(len(self.circpar.get().split(','))==3):
                    self.bh+=self.k+f"self.draw.circle(int({self.circpar.get().split(',')[0]}),int({self.circpar.get().split(',')[1]}),int({self.circpar.get().split(',')[2]}))\n"
                elif(len(self.circpar.get().split(','))==2):
                    self.bh+=self.k+f"self.draw.circle(int({self.circpar.get().split(',')[0]}),int({self.circpar.get().split(',')[1]}))\n"
                elif(len(self.circpar.get().split(','))==1):
                    self.bh+=self.k+f"self.draw.circle(int({self.circpar.get().split(',')[0]}))\n"
            elif(self.func!=""):
                if(len(self.circpar.get().split(','))==3):
                    self.func+=f"    self.draw.circle(int({self.circpar.get().split(',')[0]}),int({self.circpar.get().split(',')[1]}),int({self.circpar.get().split(',')[2]}))\n"
                elif(len(self.circpar.get().split(','))==2):
                    self.func+=f"    self.draw.circle(int({self.circpar.get().split(',')[0]}),int({self.circpar.get().split(',')[1]}))\n"
                elif(len(self.circpar.get().split(','))==1):
                    self.func+=f"    self.draw.circle(int({self.circpar.get().split(',')[0]}))\n"
            else:
                if(len(self.circpar.get().split(','))==3):
                    self.draw.circle(int(self.circpar.get().split(",")[0]),int(self.circpar.get().split(",")[1]),int(self.circpar.get().split(",")[2]))
                    self.s+=f"self.draw.circle(int({self.circpar.get().split(',')[0]}),int({self.circpar.get().split(',')[1]}),int({self.circpar.get().split(',')[2]}))#\n"
                elif(len(self.circpar.get().split(','))==2):
                    self.draw.circle(int(self.circpar.get().split(',')[0]),int(self.circpar.get().split(',')[1]))
                    self.s+=f"self.draw.circle(int({self.circpar.get().split(',')[0]}),int({self.circpar.get().split(',')[1]}))#\n"
                elif(len(self.circpar.get().split(','))==1):
                    self.draw.circle(int(self.circpar.get().split(",")[0]))
                    self.s+=f"self.draw.circle(int({self.circpar.get().split(',')[0]}))#\n"
            self.sav=0
        except:
            pass
    def pendown(self):
        if(self.k!=""):
            self.bh+=self.k+"self.draw.pd()\n"
        elif(self.func!=""):
            self.func+="    self.draw.pd()\n"
        else:
            self.draw.pd()
            self.s+="self.draw.pd()#\n"
        self.sav=0
    def penup(self):
        if(self.k!=""):
            self.bh+=self.k+"self.draw.pu()\n"
        elif(self.func!=""):
            self.func+="    self.draw.pu()\n"
        else:
            self.draw.pu()
            self.s+="self.draw.pu()#\n"
        self.sav=0
    def wa(self):
        try:
            float(self.wo.get())
            if(self.k!=""):
                self.bh+=self.k+"time.sleep(float("+self.wo.get()+"))\n"
            elif(self.func!=""):
                self.func+="    time.sleep(float("+self.wo.get()+"))\n"
            else:
                self.s+="time.sleep(float("+self.wo.get()+"))#\n"
            self.sav=0
        except:
            pass
    def dela(self):
        try:
            float(self.delay.get())
            if(self.k!=""):
                self.bh+=self.k+f"self.screen.delay({self.delay.get()})\n"
            elif(self.func!=""):
                self.func+=f"    self.screen.delay({self.delay.get()})\n"
            else:
                self.screen.delay(float(self.delay.get()))
                self.s+=f"self.screen.delay({self.delay.get()})\n"
            self.sav=0
        except:
            pass
    def spee(self):
        try:
            float(self.speed.get())
            if(self.k!=""):
                self.bh+=self.k+f"self.draw.speed({self.speed.get()})\n"
            elif(self.func!=""):
                self.func+=f"    self.draw.speed({self.speed.get()})\n"
            else:
                self.draw.speed(float(self.speed.get()))
                self.s+=f"self.draw.speed({self.speed.get()})\n"
            self.sav=0
        except:
            pass
    def lop(self):
        self.bh+=self.k+"for i in range(0,int('"+self.lo.get()+"')):\n"
        self.k+="    "
        self.sav=0
    def loz(self):
        if(len(self.k)>4):
            self.k=self.k[-4:0:-1]
        else:
            if(self.func==""):
                if(len(self.bh.split("\n"))==2):
                    self.bh+=self.k+"pass\n"
                self.s+=self.bh+"#\n"
                exec(self.bh,dict(globals(),**locals()))
            else:
                for i in self.bh.split("\n"):
                    self.func+="    "+i+"\n"
            self.k=""
            self.bh=""
    def chsh(self):
        def sho(x):
            self.i=0
            self.draw.shape(x)
            self.s+="self.draw.shape('"+x+"')#\n"
        def shf():
            Tk().withdraw()
            self.file=filedialog.askopenfilename(filetypes=[("png",".png"),("jpg",".jpg")])
            self.i=1
            if(self.k!=""):
                self.bh+=f"""{self.k}im=Image.open('"""+self.file+f"""')
{self.k}im=im.convert('RGBA')
{self.k}im=im.rotate("""+str(self.headings[self.curob["text"][18:]])+f""",expand=1)
{self.k}dst_im = Image.new("RGBA",im.size,"white")
{self.k}dst_im.paste( im, (0,0),im)
{self.k}dst_im.save("a.gif",transparency=0)
{self.k}self.screen.addshape("a.gif")
{self.k}self.draw.shape('a.gif')
{self.k}self.draw.ondrag(self.dragging)
"""
            elif(self.func!=""):
                self.func+="""    im=Image.open('"""+self.file+"""')
    im=im.convert('RGBA')
    im=im.rotate("""+str(self.headings[self.curob["text"][18:]])+""",expand=1)
    dst_im = Image.new("RGBA",im.size,"white")
    dst_im.paste( im, (0,0),im)
    dst_im.save("a.gif",transparency=0)
    self.screen.addshape("a.gif")
    self.draw.shape('a.gif')
    self.draw.ondrag(self.dragging)
"""
            else:
                im=Image.open(self.file)
                im=im.convert('RGBA')
                im=im.rotate(self.headings[self.curob["text"][18:]],expand=1)
                dst_im = Image.new("RGBA",im.size,"white")
                dst_im.paste(im, (0,0),im)
                dst_im.save("a.gif",'GIF',transparency=0)
                self.screen.addshape("a.gif")
                self.draw.shape('a.gif')
                self.draw.ondrag(self.dragging)
                self.s+="""im=Image.open('"""+self.file+"""')
im=im.convert('RGBA')
im=im.rotate("""+str(self.headings[self.curob["text"][18:]])+""",expand=1)
dst_im = Image.new("RGBA",im.size,"white")
dst_im.paste( im, (0,0),im)
dst_im.save("a.gif",transparency=0)
self.screen.addshape("a.gif")
self.draw.shape('a.gif')#
"""
        q=Toplevel()
        q.wm_geometry("350x200")
        q.attributes('-topmost', 'true')
        q.title("Choose shape of the object")
        li=['arrow', 'circle', 'classic', 'square', 'triangle', 'turtle']
        for j in li:
            Button(q,text=j,command=lambda j=j:sho(j)).pack()
        Button(q,text="Choose image from system",command=lambda:shf()).pack()
        self.sav=0
    def chobj(self,x):
        self.objects[self.curob["text"][18:]]=self.draw
        self.objects[self.curob["text"][18:]].ondrag(None)
        self.draw=self.objects[x]
        self.draw.ondrag(self.dragging)
        self.draw.pu()
        self.curob["text"]="current object is "+x
        self.s+=f"""self.objects[self.curob["text"][18:]]=self.draw
self.objects[self.curob["text"][18:]].ondrag(None)
self.draw=self.objects['{x}']
self.draw.ondrag(self.dragging)
self.draw.pu()
self.curob["text"]="current object is "+'{x}'#
"""
        self.sav=0
    def addobj(self):
        name=self.screen.textinput(title="new object's name",prompt="enter name of new object")
        if(name!=None and name not in self.objects.keys()):
            self.objects[name]=turtle.RawTurtle(self.screen)
            self.objects[name].pu()
            self.headings[name]=0
            ljo=len(self.objects)
            print(ljo)
            Button(self.ia,text=name,command=lambda:self.chobj(name)).grid(row=self.jj)
            self.chs.grid(row=self.jj+1,column=0)
            self.jj+=1
            self.addt.grid(row=self.jj+1)
            self.curob.grid(row=self.jj+2)
            self.s+=f"""self.objects['{name}']=turtle.RawTurtle(self.screen)
self.objects['{name}'].pu()
ljo=len(self.objects)
print(ljo)
Button(self.ia,text='{name}',command=lambda:self.chobj('{name}')).grid(row=self.jj)
self.chs.grid(row=self.jj+1,column=0)
self.jj+=1
self.addt.grid(row=self.jj+1)
self.curob.grid(row=self.jj+2)#
"""
    def stafunc(self):
        if(self.func_name==""):
            self.func_name=self.screen.textinput(title="new function's name",prompt="enter name of new function")
            if(self.func_name not in self.functions):
                self.func="def " +self.func_name + "(self):\n"
            else:
                self.func_name=""
    def stofunc(self):
        if(self.func_name!=""):
            func_nam=self.func_name
            if(len(self.func.split("\n"))==2):
                self.func+="    pass"
            exec(self.func)
            self.s+=self.func
            exec("setattr(self,'"+func_nam+"',"+func_nam+")",dict(globals(),**locals()))
            self.s+="setattr(self,'"+func_nam+"',"+func_nam+")\n"
            self.functions.append(func_nam)
            Button(self.fg,text=self.func_name,command=lambda:self.callfunc(func_nam)).grid(row=self.jj1)
            self.jj1+=1
            self.stf.grid(row=self.jj1)
            self.stf1.grid(row=self.jj1+1)
            self.s+=f"""self.functions.append('{func_nam}')
Button(self.fg,text='{self.func_name}',command=lambda:self.callfunc('{func_nam}')).grid(row=self.jj1)
self.jj1+=1
self.stf.grid(row=self.jj1)
self.stf1.grid(row=self.jj1+1)
self.func_name=""
self.func=""#
"""
            self.func_name=""
            self.func=""
    def callfunc(self,x):
        if(self.k!=""):
            self.bh+=self.k+x+"()\n"
        elif(self.func!=""):
            self.func+="    "+x+"()\n"
        else:
            self.s+=x+"(self)#\n"
            exec(f"self."+x+"(self)",dict(globals(),**locals()))
    def callfunc1(self,sz):
        if(self.k!=""):
            self.bh+="self."+self.keylinks[sz]+"(self)\n"
        elif(self.func!=""):
            self.func+="self."+self.keylinks[sz]+"(self)\n"
        else:
            self.s+="self."+self.keylinks[sz]+"(self)#\n"
            exec("self."+self.keylinks[sz]+"(self)",dict(globals(),**locals()))
    def key(self,x):
        self.keymenu['text']=x
        self.s+=f"self.keymenu['text']='{x}'#\n"
    def addkeylink(self):
        self.keylinks[self.keymenu['text']]=self.fulk.get()
        self.s+=f"self.keylinks['{self.keymenu['text']}']='{self.fulk.get()}'\n"
        sz=self.keymenu['text']
        self.s+=f"sz='{self.keymenu['text']}'\n"
        self.screen.onkey(lambda: self.callfunc1(sz),sz)
        self.s+=f"self.screen.onkey(lambda: self.callfunc1('{sz}'),'{sz}')\n"
        self.canvas.focus()
        Label(self.df,text=sz+" : "+self.keylinks[sz]).grid(row=self.fgh)
        self.fgh+=1
        self.keymenu.grid(row=self.fgh,column=0)
        self.fulk.grid(row=self.fgh,column=1)
        self.keylink.grid(row=self.fgh,column=2)   
        self.screen.listen()
        self.s+=f"""Label(self.df,text='{sz}'+" : "+self.keylinks['{sz}']).grid(row=self.fgh)
self.fgh+=1
self.keymenu.grid(row=self.fgh,column=0)
self.fulk.grid(row=self.fgh,column=1)
self.keylink.grid(row=self.fgh,column=2)   
self.screen.listen()#
"""
    def stoani(self):
        if(self.k!=""):
            self.bh+=self.k+"self.screen.tracer(0)\n"
        elif(self.func!=""):
            self.func+="    self.screen.tracer(0)\n"
        else:
            self.s+="self.screen.tracer(0)#\n"
            self.screen.tracer(0)
    def staani(self):
        if(self.k!=""):
            self.bh+=self.k+"self.screen.tracer(1)\n"
        elif(self.func!=""):
            self.func+="    self.screen.tracer(1)\n"
        else:
            self.s+="self.screen.tracer(1)#\n"
            self.screen.tracer(1)
    def bgpic(self):
        file1=filedialog.askopenfilename(filetypes=[("png",".png"),("jpg",".jpg")])
        if(self.k!=""):
            self.bh+=f"""{self.k}im=Image.open('{file1}')
{self.k}im.save('b.gif')
{self.k}self.screen.bgpic('b.gif')
"""
        elif(self.func!=""):
            self.func+=f"""    im=Image.open('{file1}')
    im.save('b.gif')
    self.screen.bgpic('b.gif')
"""
        else:
            im=Image.open(file1)
            im.save('b.gif')
            self.screen.bgpic('b.gif')
            self.s+=f"""im=Image.open('{file1}')
im.save('b.gif')
self.screen.bgpic('b.gif')#
"""
    def colourchoose(self,z):
        def penco(colour):
            if(self.k!=""):
                self.bh+=self.k+f"self.draw.pencolor('{colour}')\n"
            elif(self.func!=""):
                self.func+=f"    self.draw.pencolor('{colour}')\n"
            else:
                self.s+=f"self.draw.pencolor('{colour}')#\n"
                self.draw.pencolor(colour)
        def bgco(colour):
            if(self.k!=""):
                self.bh+=self.k+f"self.screen.bgcolor('{colour}')\n"
            elif(self.func!=""):
                self.func+=f"    self.screen.bgcolor('{colour}')\n"
            else:
                self.s+=f"self.screen.bgcolor('{colour}')#\n"
                self.screen.bgcolor(colour)
        qi=Toplevel()
        x = root.winfo_x()
        y = root.winfo_y()
        qi.geometry("+%d+%d" % (x+10, y+10))
        container = Frame(qi)
        canvas = Canvas(container)
        scrollbar = Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollable_frame = Frame(canvas)
        scrollable_frame.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        container.pack()
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        if(z=="bgcolour"):
            for colour in self.COLOURS:
                Button(scrollable_frame,text=colour,bg=colour,width=55,command=lambda colour=colour:bgco(colour)).pack()
        elif(z=="pencolour"):
            for colour in self.COLOURS:
                Button(scrollable_frame,text=colour,bg=colour,width=55,command=lambda colour=colour:penco(colour)).pack()
    def new(self):
        if(self.sav==1):
            self.s=self.s1
            self.screen.clearscreen()
            exec(self.s)
            self.draw.pu()
        else:
            close=messagebox.askyesno(title="save file prompt",message="do you want to save file, yes or no")
            if(close==1):
                self.save()
            self.s=self.s1
            self.screen.clearscreen()
            exec(self.s)
            self.draw.pu()
    def ope(self):
        if(self.sav==1):
            self.file=filedialog.askopenfilename(filetypes=[("animpy files",".ampy")])
            fil=open(self.file,"r")
            self.s=fil.read()
            self.starun()
        else:
            close=messagebox.askyesno(title=" do you want to save the file")
            if(close==1):
                self.save()
            self.file=filedialog.askopenfilename(filetypes=[("animpy files",".ampy")])
            fil=open(self.file,"r")
            self.s=fil.read()
            self.starun()
    def save(self):
        self.sav=1
        self.file=filedialog.asksaveasfilename(defaultextension="*.*",filetypes=[("animpy files",".ampy")])
        try:
            fil=open(self.file,"w")
            fil.write(self.s)
        except:
            pass
    def undo(self):
        li=self.s.split("#\n")
        if(len(li)>2):
            xz=li.pop(-2)
            self.redos.append(xz)
            self.s="#\n".join(li)
            za=self.s
            self.s="self.screen.tracer(0)\n"+self.s+"self.screen.tracer(1)\n"
            self.screen.clearscreen()
            exec(self.s,dict(globals(),**locals()))
            self.s=za
    def starun(self):
        self.screen.clearscreen()
        self.screen.listen()
        exec(self.s,dict(globals(),**locals()))
        
if __name__ == "__main__":
    root=tix.Tk()
    app=App(root)
    root.mainloop()
