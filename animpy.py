from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import turtle1 as turtle
import time
from PIL import Image
s=""
k=""
sav=1
bh=""
file=""
angle=0
i=0
window = Tk()
tabcon=ttk.Notebook(window)
pw=Frame(tabcon)
tabcon.add(pw,text="Movements")
pl=Frame(tabcon)
tabcon.add(pl,text="Time")
nb=Frame(tabcon)
tabcon.add(nb,text="Loop")
ia=Frame(tabcon)
tabcon.add(ia,text="Objects")
tabcon.grid(row=0,column=0,sticky="n")
canvas = turtle.ScrolledCanvas(master = window, width = 500, height = 800)
canvas.grid(row=0,column=1)
screen=turtle.TurtleScreen(canvas)
draw = turtle.RawTurtle(screen)
draw.pu()
index=1
print(dir(draw.getscreen()))

def dragging(x, y):
    global s
    draw.ondrag(None)
    s+=f"draw.goto({x},{y})\n"
    draw.goto(x, y)
    draw.ondrag(dragging)
def fwd():
	global s
	global k
	global sav
	global bh
	if(k!=""):
		bh+=k+"draw.fd(15)\n"
	else:
		draw.fd(15)
	s+=k+"draw.fd(15)\n"
	sav=0
def bwd():
	global s
	global k
	global sav
	global bh
	if(k!=""):
		bh+=k+"draw.bk(15)\n"
	else:
		draw.bk(15)
	s+=k+"draw.bk(15)\n"
	sav=0
def rot():
	global s
	global k
	global sav
	global bh
	global i
	global file
	global angle
	try:
		int(deg.get())
		if(i==0):
			s+=k+"draw.lt(int("+deg.get()+"))\n"
			if(k!=""):
				bh+=k+"draw.lt(int("+deg.get()+"))\n"
			else:
				draw.lt(int(deg.get()))
			sav=0
		else:
			im=Image.open(file)
			im=im.convert('RGBA')
			angle+=int(deg.get())
			im=im.rotate(angle,expand=1)
			dst_im = Image.new("RGBA",im.size,screen.bgcolor())
			dst_im.paste( im, (0,0),im)
			dst_im.save("a.gif")
			screen.addshape("a.gif")
			draw.shape("a.gif")
			s+="""im=Image.open('"""+file+"""')
im=im.convert('RGBA')
angle+=int("""+deg.get()+""")
im=im.rotate("""+str(angle)+""",expand=1)
dst_im = Image.new("RGBA",im.size,screen.bgcolor())
dst_im.paste( im, (0,0),im)
dst_im.save("a.gif")
screen.addshape("a.gif")
draw.shape("a.gif")
"""
			s+=k+"draw.lt(int("+deg.get()+"))\n"
			if(k!=""):
				bh+="""im=Image.open('"""+file+"""')
im=im.convert('RGBA')
angle+=int("""+deg.get()+""")
im=im.rotate("""+str(angle)+""",expand=1)
dst_im = Image.new("RGBA",im.size,screen.bgcolor())
dst_im.paste( im, (0,0),im)
dst_im.save("a.gif")
screen.addshape("a.gif")
draw.shape("a.gif")
"""
				bh+=k+"draw.lt(int("+deg.get()+"))\n"
			else:
				draw.lt(int(deg.get()))
	except:
		raise
def show():
	global s
	draw.st()
	s+="draw.st()\n"
def hide():
	global s
	draw.ht()
	s+="draw.ht()\n"
def ru():
	global s
	draw.reset()
	draw.pu()
	exec(s)
	time.sleep(2)
	draw.pu()
def wa():
	global s
	global k
	global sav
	global bh
	try:
		int(wo.get())
		s+=k+"time.sleep(int("+wo.get()+"))\n"
		if(k!=""):
			bh+=k+"time.sleep(int("+wo.get()+"))\n"
		else:
			time.sleep(int(wo.get()))
		sav=0
	except:
		pass
def lop():
	global s
	global k
	global sav
	global bh
	s+=k+"for i in range(0,int("+lo.get()+")):\n"
	bh+=k+"for i in range(0,int("+lo.get()+")):\n"
	k+="    "
	sav=0
def loz():
	global k
	global bh
	k=""
	exec(bh)
	bh=""
def chsh():
	def sho(x):
		q.destroy()
		global i
		i=0
		draw.shape(x)
		s+="draw.shape("+x+")\n"
	def shf():
		q.destroy()
		global file
		global i
		global s
		Tk().withdraw()
		filename=filedialog.askopenfilename(filetypes=[("png",".png")])
		file=filename
		i=1
		im=Image.open(filename)
		im=Image.open(file)
		im=im.convert('RGBA')
		im=im.rotate(angle,expand=1)
		dst_im = Image.new("RGBA",im.size,screen.bgcolor())
		dst_im.paste( im, (0,0),im)
		dst_im.save("a.gif")
		screen.addshape("a.gif")
		draw.shape('a.gif')
		draw.ondrag(dragging)
		s+="""im=Image.open('"""+filename+"""')
im=Image.open('"""+file+"""')
im=im.convert('RGBA')
im=im.rotate("""+str(angle)+""",expand=1)
dst_im = Image.new("RGBA",im.size,screen.bgcolor())
dst_im.paste( im, (0,0),im)
dst_im.save("a.gif")
screen.addshape("a.gif")
draw.shape('a.gif')
draw.ondrag(dragging)
"""
	q=Toplevel()
	q.title("Choose shape of the object")
	li=['arrow', 'circle', 'classic', 'square', 'triangle', 'turtle']
	Button(q,text=li[0],command=lambda:sho(li[0])).pack()
	Button(q,text=li[1],command=lambda:sho(li[1])).pack()
	Button(q,text=li[2],command=lambda:sho(li[2])).pack()
	Button(q,text=li[3],command=lambda:sho(li[3])).pack()
	Button(q,text=li[4],command=lambda:sho(li[4])).pack()
	Button(q,text=li[5],command=lambda:sho(li[5])).pack()
	Button(q,text="Choose image from system",command=lambda:shf()).pack()
def chobj(x):
	global objects
	global index
	global draw
	objects["Object"+str(index)]=draw
	objects['Object'+str(index)].ondrag(None)
	draw=objects[x]
	index=int(x.split("Object")[-1])
	draw.ondrag(dragging)
def add():
	global objects
	global draw
	global jj
	objects["Object"+str(len(objects)+1)]=turtle.RawTurtle(screen)
	objects["Object"+str(len(objects))].pu()
	Button(ia,text="Object"+str(len(objects)),command=lambda:chobj("Object"+str(len(objects)))).grid(row=jj)
	jj+=1
	addt.grid(row=jj)
def new():
	global s
	global sav
	if(sav==1):
	    s=""
	    draw.reset()
	    draw.pu()
	else:
		close=messagebox.askyesno()
def ope():
	global s
	global sav
	if(sav==1):
		file=filedialog.askopenfilename(filetypes=[("animpy files",".ampy")])
		fil=open(file,"r")
		s=fil.read()
		draw.reset()
		draw.pu()
		exec(s)
def save():
	global s
	global sav
	sav=1
	file=filedialog.asksaveasfilename(filetypes=[("animpy files",".ampy")])
	print(file)
	fil=open(file,"w")
	fil.write(s)
def undo():
	global s
	draw.undo()
	li=s.split("\n")
	li.pop(-2)
	s="\n".join(li)
	
objects={"Object1":draw}
draw.ondrag(dragging)
Button(pw,text="move forward",command=lambda:fwd()).grid(row=0,column=0)
Button(pw,text="move backwards",command=lambda:bwd()).grid(row=1,column=0)
deg=Entry(pw)
deg.grid(row=4,column=1)
Button(pw,text="Rotate",command=lambda:rot()).grid(row=4,column=0)
Button(pw,text="Show object",command=lambda:show()).grid(row=5,column=0)
Button(pw,text="Hide object",command=lambda:hide()).grid(row=6,column=0)

wo=Entry(pl)
wo.grid(row=0,column=1)
Button(pl,text="Wait for",command=lambda:wa()).grid(row=0,column=0)

lo=Entry(nb)
lo.grid(row=0,column=1)
Label(nb,text="Loop length").grid(row=0,column=0)
Button(nb,text="Start loop",command=lambda:lop()).grid(row=1,column=0)
Button(nb,text="End loop",command=lambda:loz()).grid(row=2,column=0)

Button(ia,text="Object"+str(index)).grid(row=0,column=0)

Button(ia,text="Change shape",command=lambda:chsh()).grid(row=0,column=1)
jj=1
addt=Button(ia,text="Add object",command=lambda:add())
addt.grid(row=jj,column=0)

menubar=Menu(window)
file = Menu(menubar, tearoff=0)  
file.add_command(label="New",command=lambda:new()) 
file.add_command(label="Open",command=lambda:ope())  
file.add_command(label="Save",command=lambda:save())
file.add_command(label="Exit", command=window.quit)  
menubar.add_cascade(label="File", menu=file)  
edit = Menu(menubar, tearoff=0)  
edit.add_command(label="Undo",command=lambda:undo()) 
menubar.add_cascade(label="Edit", menu=edit)  
help = Menu(menubar, tearoff=0)  
help.add_command(label="About")  
menubar.add_cascade(label="Help", menu=help)  
run=Menu(menubar,tearoff=0)
run.add_command(label="Run",command=lambda:ru())
menubar.add_cascade(label="Run",menu=run)
window.config(menu=menubar)  
window.mainloop()