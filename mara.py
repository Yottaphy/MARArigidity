from tkinter.constants import N, S
import numpy as np
import tkinter as tk

from numpy.lib.function_base import insert

#CONSTANTS
u           = 1.6605402E-27         #kg
epsilon0    = 8.85419E-12           #F/m
e_charge    = 1.6021773E-19         #C
c           = 2.99792458E8          #m/s
r0          = 1.4                   #fm

superscript = "⁰¹²³⁴⁵⁶⁷⁸⁹"

def getElement(a,z):
    a = int(a)
    z = int(z)
    n = a-z
    symbol = listName[z] if z < 119 else 'X'
    return n, symbol

listName = open("elements.txt","r").readlines()

window = tk.Tk()

frm_proj = tk.Frame(master = window, relief=tk.RAISED, borderwidth=1)
frm_proj.grid(row=0,column=0, padx=5, pady=5)
frm_projtitle = tk.Frame(master = frm_proj, relief=tk.FLAT)
frm_projtitle.pack()
lbl_proj = tk.Label(master=frm_projtitle, text="Projectile", width=20)
lbl_proj.pack()

frm_projboxes = tk.Frame(master = frm_proj, relief=tk.FLAT)
frm_projboxes.pack()
lbl_Aproj = tk.Label(master=frm_projboxes, text="A", width=2)
lbl_Aproj.grid(row=0, column=0)
ent_Aproj = tk.Entry(master=frm_projboxes, width=5)
ent_Aproj.grid(row=0,column=1)
ent_Aproj.insert(0,"0")
lbl_Zproj = tk.Label(master=frm_projboxes, text="Z", width=2)
lbl_Zproj.grid(row=1, column=0)
ent_Zproj = tk.Entry(master=frm_projboxes, width=5)
ent_Zproj.grid(row=1,column=1)
ent_Zproj.insert(0,"0")
lbl_Nproj = tk.Label(master=frm_projboxes, text="N", width=2)
lbl_Nproj.grid(row=2, column=0)
lbl_Nproj_res = tk.Label(master=frm_projboxes, width=5, text="")
lbl_Nproj_res.grid(row=2,column=1)
frm_projsymb = tk.Frame(master = frm_proj, relief=tk.FLAT)
frm_projsymb.pack()
lbl_nameproj = tk.Label(master=frm_projsymb, width=5, text="")
lbl_nameproj.pack()
frm_radproj = tk.Frame(master = frm_proj, relief=tk.FLAT)
frm_radproj.pack()
lbl_radproj = tk.Label(master=frm_radproj, text="Radius ")
lbl_radproj.grid(row=0,column=0,sticky='e')
lbl_radproj_res = tk.Label(master=frm_radproj,text="")
lbl_radproj_res.grid(row=0,column=1)
lbl_radproj_unit = tk.Label(master=frm_radproj,text=" fm")
lbl_radproj_unit.grid(row=0,column=2,sticky='w')

def updateProj(event):
    n, symbol = getElement(ent_Aproj.get(),ent_Zproj.get())
    lbl_Nproj_res["text"] = str(n)
    a = int(ent_Aproj.get())
    lbl_radproj["text"] = round(r0*(a**(1/3)),2)
    show = ''
    if int(ent_Zproj.get()) > 118:
        lbl_nameproj["text"] = 'Error'
    else:
        if a >= 100:
            hunds = int(a/100)
            a -= 100*hunds
            show += superscript[hunds]
            if a == 0: show += superscript[0]
        if a >= 10:
            tens = int(a/10)
            a -= 10*tens
            show += superscript[tens]
        show += superscript[int(a)]
        lbl_nameproj["text"] = show + symbol

frm_targ = tk.Frame(master = window, relief=tk.RAISED, borderwidth=1)
frm_targ.grid(row=0,column=1, padx=5, pady=5)
frm_targtitle = tk.Frame(master = frm_targ, relief=tk.FLAT)
frm_targtitle.pack()
lbl_targ = tk.Label(master=frm_targtitle, text="Target", width=20)
lbl_targ.pack()

frm_targboxes = tk.Frame(master = frm_targ, relief=tk.FLAT)
frm_targboxes.pack()
lbl_Atarg = tk.Label(master=frm_targboxes, text="A", width=2)
lbl_Atarg.grid(row=0, column=0)
ent_Atarg = tk.Entry(master=frm_targboxes, width=5)
ent_Atarg.grid(row=0,column=1)
ent_Atarg.insert(0,"0")
lbl_Ztarg = tk.Label(master=frm_targboxes, text="Z", width=2)
lbl_Ztarg.grid(row=1, column=0)
ent_Ztarg = tk.Entry(master=frm_targboxes, width=5)
ent_Ztarg.grid(row=1,column=1)
ent_Ztarg.insert(0,"0")
lbl_Ntarg = tk.Label(master=frm_targboxes, text="N", width=2)
lbl_Ntarg.grid(row=2, column=0)
lbl_Ntarg_res = tk.Label(master=frm_targboxes, width=5, text="")
lbl_Ntarg_res.grid(row=2,column=1)
frm_targsymb = tk.Frame(master = frm_targ, relief=tk.FLAT)
frm_targsymb.pack()
lbl_nametarg = tk.Label(master=frm_targsymb, width=5, text="")
lbl_nametarg.pack()
frm_radtarg = tk.Frame(master = frm_targ, relief=tk.FLAT)
frm_radtarg.pack()
lbl_radtarg = tk.Label(master=frm_radtarg, text="Radius ")
lbl_radtarg.grid(row=0,column=0,sticky='e')
lbl_radtarg_res = tk.Label(master=frm_radtarg,text="")
lbl_radtarg_res.grid(row=0,column=1)
lbl_radtarg_unit = tk.Label(master=frm_radtarg,text=" fm")
lbl_radtarg_unit.grid(row=0,column=2,sticky='w')

def updateTarg(event):
    n, symbol = getElement(ent_Atarg.get(),ent_Ztarg.get())
    lbl_Ntarg_res["text"] = str(n)
    a = int(ent_Atarg.get())
    lbl_radtarg["text"] = round(r0*(a**(1/3)),2)
    show = ''
    if int(ent_Ztarg.get()) > 118:
        lbl_nametarg["text"] = 'Error'
    else:
        if a >= 100:
            hunds = int(a/100)
            a -= 100*hunds
            show += superscript[hunds]
            if a == 0: show += superscript[0]
        if a >= 10:
            tens = int(a/10)
            a -= 10*tens
            show += superscript[tens]
        show += superscript[int(a)]
        lbl_nametarg["text"] = show + symbol

frm_comp = tk.Frame(master = window, relief=tk.RAISED, borderwidth=1)
frm_comp.grid(row=1,column=0, padx=5, pady=5)
frm_comptitle = tk.Frame(master = frm_comp, relief=tk.FLAT)
frm_comptitle.pack()
lbl_comp = tk.Label(master=frm_comptitle, text="Compound", width=20)
lbl_comp.pack()

frm_compboxes = tk.Frame(master = frm_comp, relief=tk.FLAT)
frm_compboxes.pack()
lbl_Acomp = tk.Label(master=frm_compboxes, text="A", width=2)
lbl_Acomp.grid(row=0, column=0)
lbl_Acomp_res = tk.Label(master=frm_compboxes, width=5, text="")
lbl_Acomp_res.grid(row=0,column=1)
lbl_Zcomp = tk.Label(master=frm_compboxes, text="Z", width=2)
lbl_Zcomp.grid(row=1, column=0)
lbl_Zcomp_res = tk.Label(master=frm_compboxes, text="", width=5)
lbl_Zcomp_res.grid(row=1,column=1)
lbl_Ncomp = tk.Label(master=frm_compboxes, text="N", width=2)
lbl_Ncomp.grid(row=2, column=0)
lbl_Ncomp_res = tk.Label(master=frm_compboxes, text="", width=5)
lbl_Ncomp_res.grid(row=2,column=1)
frm_compsymb = tk.Frame(master = frm_comp, relief=tk.FLAT)
frm_compsymb.pack()
lbl_namecomp = tk.Label(master=frm_compsymb, width=5, text="")
lbl_namecomp.pack()

def updateComp(event):
    lbl_Zcomp_res["text"] = int(ent_Zproj.get()) + int(ent_Ztarg.get())
    lbl_Acomp_res["text"] = int(ent_Aproj.get()) + int(ent_Atarg.get())

    n, symbol = getElement(lbl_Acomp_res["text"],lbl_Zcomp_res["text"])
    lbl_Ncomp_res["text"] = str(n)
    a = lbl_Acomp_res["text"]
    show = ''
    if a >= 100:
        hunds = int(a/100)
        a -= 100*hunds
        show += superscript[hunds]
        if a == 0: show += superscript[0]
    if a >= 10:
        tens = int(a/10)
        a -= 10*tens
        show += superscript[tens]
    show += superscript[int(a)]
    lbl_namecomp["text"] = show + symbol

def update(event):
    updateProj(event)
    updateTarg(event)
    updateComp(event)

window.bind('<Return>', update)
window.bind('<KP_Enter>', update)





frm_proj.mainloop()