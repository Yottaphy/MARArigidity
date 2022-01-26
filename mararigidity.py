# MARA Rigidity parameters calculator
#
# Developped by Jorge Romero at JYU
# based on an excel sheet by Jan Sarén
# joromero@jyu.fi
# 2021

from tkinter.constants import N, S
import numpy as np
import math
import tkinter as tk

from numpy.lib.function_base import insert

#CONSTANTS
u           = 1.6605402E-27         #kg
epsilon0    = 8.85419E-12           #F/m
e_charge    = 1.6021773E-19         #C
c           = 2.99792458E8          #m/s
pi          = 3.14159265359

superscript = "⁰¹²³⁴⁵⁶⁷⁸⁹"

def getElement(a,z):
    a = int(a)
    z = int(z)
    n = a-z
    symbol = listName[z] if z < 119 else 'X'
    return n, symbol

listName = open("elements.txt","r").read().splitlines()
window = tk.Tk()
window.configure(bg='#ededed')
window.title('MARA Rigidity Calculator')
frm_disclaimer = tk.Frame(master = window, relief=tk.FLAT, borderwidth=0)
frm_disclaimer.grid(row=0,column=3, columnspan= 1, padx=5, pady=5, sticky = 'e')
lbl_disclaimer = tk.Label(master=frm_disclaimer, text="© 2021 Jorge Romero, joromero@jyu.fi", bg='#ededed', font='Calibri 10 italic')
lbl_disclaimer.pack(side=tk.LEFT)


frm_namer = tk.Frame(master = window, relief=tk.RAISED, borderwidth=1)
frm_namer.grid(row=0,column=0, columnspan= 1, padx=5, pady=5, sticky = 'nsew')
lbl_namer_name = tk.Label(master=frm_namer, text="Z lookup", width=10, font='Helvetica 12 bold')
lbl_namer_name.pack(side=tk.LEFT)
lbl_symb_name = tk.Label(master=frm_namer, text="Symbol", width=6)
lbl_symb_name.pack(side=tk.LEFT)
ent_symb = tk.Entry(master=frm_namer, width=6)
ent_symb.pack(side=tk.LEFT)
lbl_Z_name = tk.Label(master=frm_namer, text="→ Z", width=3)
lbl_Z_name.pack(side=tk.LEFT)
lbl_Z = tk.Label(master=frm_namer, text='', width=6)
lbl_Z.pack(side=tk.LEFT)

def namer(event):
    symb = ent_symb.get() 
    if  symb == '': return 0
    if not symb == 'n': 
        symb = symb.title()
    if symb == 'Nice':
        lbl_Z['text'] = 69
        return 0
    if symb == 'Fy':
        lbl_Z['text'] = 137
        return 0
    lbl_Z['text'] = listName.index(symb) if symb in listName else 'Error'

frm_radius0 = tk.Frame(master = window, relief=tk.RAISED, borderwidth=1)
frm_radius0.grid(row=0,column=1, columnspan= 1, padx=5, pady=5, sticky = 'nsew')
lbl_radius0_name = tk.Label(master=frm_radius0, text="r₀", width=10, font='Helvetica 12 bold')
lbl_radius0_name.pack(side=tk.LEFT)
ent_radius0 = tk.Entry(master=frm_radius0, width=6)
ent_radius0.pack(side=tk.LEFT)
ent_radius0.insert(0, '1.4')
lbl_radius0_unit = tk.Label(master=frm_radius0, text="fm", width=3)
lbl_radius0_unit.pack(side=tk.LEFT)
lbl_radius0_formula = tk.Label(master=frm_radius0, text="r = r₀ A"+superscript[1]+superscript[3], width=3)
lbl_radius0_formula.pack(side=tk.LEFT)

frm_proj = tk.Frame(master = window, relief=tk.RAISED, borderwidth=1)
frm_proj.grid(row=1,column=0, padx=5, pady=5, sticky = 'nsew')
frm_projtitle = tk.Frame(master = frm_proj, relief=tk.FLAT)
frm_projtitle.pack()
lbl_proj = tk.Label(master=frm_projtitle, text="Projectile", width=20, font='Helvetica 12 bold')
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
lbl_Nproj_res.grid(row=2,column=1, sticky = 'e')
frm_projsymb = tk.Frame(master = frm_proj, relief=tk.FLAT)
frm_projsymb.pack()
lbl_nameproj = tk.Label(master=frm_projsymb, width=5, text="")
lbl_nameproj.pack()
frm_radproj = tk.Frame(master = frm_proj, relief=tk.FLAT)
frm_radproj.pack()
lbl_radproj = tk.Label(master=frm_radproj, text="Radius = ")
lbl_radproj.grid(row=0,column=0,sticky='e')
lbl_radproj_res = tk.Label(master=frm_radproj,text="")
lbl_radproj_res.grid(row=0,column=1, sticky = 'e')
lbl_radproj_unit = tk.Label(master=frm_radproj,text="fm")
lbl_radproj_unit.grid(row=0,column=2,sticky='w')

def updateProj(event):
    r0 = float(ent_radius0.get())
    n, symbol = getElement(ent_Aproj.get(),ent_Zproj.get())
    lbl_Nproj_res["text"] = str(n)
    a = int(ent_Aproj.get())
    lbl_radproj_res["text"] = round(r0*(a**(1/3)),2)
    show = ''
    if int(ent_Zproj.get()) > 118:
        lbl_nameproj["text"] = 'Error'
        lbl_nameproj["fg"] = 'red'
    else:
        lbl_nameproj["fg"] = 'black'
        if a >= 100:
            hunds = int(a/100)
            a -= 100*hunds
            show += superscript[hunds]
            if a == 0: show += superscript[0]
        if a >= 10:
            tens = int(a/10)
            a -= 10*tens
            show += superscript[tens]
        elif a>=1:
            show += superscript[0]
        show += superscript[int(a)]
        lbl_nameproj["text"] = show + symbol

frm_targ = tk.Frame(master = window, relief=tk.RAISED, borderwidth=1)
frm_targ.grid(row=1,column=1, padx=5, pady=5, sticky = 'nsew')
frm_targtitle = tk.Frame(master = frm_targ, relief=tk.FLAT)
frm_targtitle.pack()
lbl_targ = tk.Label(master=frm_targtitle, text="Target", width=20, font='Helvetica 12 bold')
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
lbl_Ntarg_res.grid(row=2,column=1, sticky = 'e')
frm_targsymb = tk.Frame(master = frm_targ, relief=tk.FLAT)
frm_targsymb.pack()
lbl_nametarg = tk.Label(master=frm_targsymb, width=5, text="")
lbl_nametarg.pack()
frm_radtarg = tk.Frame(master = frm_targ, relief=tk.FLAT)
frm_radtarg.pack()
lbl_radtarg = tk.Label(master=frm_radtarg, text="Radius = ")
lbl_radtarg.grid(row=0,column=0,sticky='e')
lbl_radtarg_res = tk.Label(master=frm_radtarg,text="")
lbl_radtarg_res.grid(row=0,column=1, sticky = 'e')
lbl_radtarg_unit = tk.Label(master=frm_radtarg,text="fm")
lbl_radtarg_unit.grid(row=0,column=2,sticky='w')

def updateTarg(event):
    r0 = float(ent_radius0.get())
    n, symbol = getElement(ent_Atarg.get(),ent_Ztarg.get())
    lbl_Ntarg_res["text"] = str(n)
    a = int(ent_Atarg.get())
    lbl_radtarg_res["text"] = round(r0*(a**(1/3)),2)
    show = ''
    if int(ent_Ztarg.get()) > 118:
        lbl_nametarg["text"] = 'Error'
        lbl_nametarg["fg"] = 'red'
    else:
        lbl_nametarg["fg"] = 'black'
        if a >= 100:
            hunds = int(a/100)
            a -= 100*hunds
            show += superscript[hunds]
            if a == 0: show += superscript[0]
        if a >= 10:
            tens = int(a/10)
            a -= 10*tens
            show += superscript[tens]
        elif a>=1:
            show += superscript[0]
        show += superscript[int(a)]
        lbl_nametarg["text"] = show + symbol

frm_comp = tk.Frame(master = window, relief=tk.RAISED, borderwidth=1)
frm_comp.grid(row=2,column=0, padx=5, pady=5, sticky = 'nsew')
frm_comptitle = tk.Frame(master = frm_comp, relief=tk.FLAT)
frm_comptitle.pack()
lbl_comp = tk.Label(master=frm_comptitle, text="Compound", width=20, font='Helvetica 12 bold')
lbl_comp.pack()

frm_compboxes = tk.Frame(master = frm_comp, relief=tk.FLAT)
frm_compboxes.pack()
lbl_Acomp = tk.Label(master=frm_compboxes, text="A", width=2)
lbl_Acomp.grid(row=0, column=0)
lbl_Acomp_res = tk.Label(master=frm_compboxes, width=5, text="")
lbl_Acomp_res.grid(row=0,column=1, sticky = 'e')
lbl_Zcomp = tk.Label(master=frm_compboxes, text="Z", width=2)
lbl_Zcomp.grid(row=1, column=0)
lbl_Zcomp_res = tk.Label(master=frm_compboxes, text="", width=5)
lbl_Zcomp_res.grid(row=1,column=1, sticky = 'e')
lbl_Ncomp = tk.Label(master=frm_compboxes, text="N", width=2)
lbl_Ncomp.grid(row=2, column=0)
lbl_Ncomp_res = tk.Label(master=frm_compboxes, text="", width=5)
lbl_Ncomp_res.grid(row=2,column=1, sticky = 'e')
frm_compsymb = tk.Frame(master = frm_comp, relief=tk.FLAT)
frm_compsymb.pack()
lbl_namecomp = tk.Label(master=frm_compsymb, width=5, text="")
lbl_namecomp.pack()
frm_compK = tk.Frame(master = frm_comp, relief=tk.FLAT)
frm_compK.pack()
lbl_compK = tk.Label(master=frm_compK, text="Compound K ")
lbl_compK.grid(row=0,column=0,sticky='w')
lbl_compK_res = tk.Label(master=frm_compK, text="")
lbl_compK_res.grid(row=0,column=1, sticky = 'e')
lbl_compK_unit = tk.Label(master=frm_compK, text="MeV")
lbl_compK_unit.grid(row=0,column=2)
lbl_compV = tk.Label(master=frm_compK, text="Compound v ")
lbl_compV.grid(row=1,column=0,sticky='w')
lbl_compV_res = tk.Label(master=frm_compK, text="")
lbl_compV_res.grid(row=1,column=1, sticky = 'e')
lbl_compV_unit = tk.Label(master=frm_compK, text="m/s")
lbl_compV_unit.grid(row=1,column=2)
lbl_compC = tk.Label(master=frm_compK, text="Compound v ")
lbl_compC.grid(row=2,column=0,sticky='w')
lbl_compC_res = tk.Label(master=frm_compK, text="")
lbl_compC_res.grid(row=2,column=1, sticky = 'e')
lbl_compC_unit = tk.Label(master=frm_compK, text="c")
lbl_compC_unit.grid(row=2,column=2)
lbl_compBohr = tk.Label(master=frm_compK, text="Compound Bohr v ")
lbl_compBohr.grid(row=3,column=0,sticky='w')
lbl_compBohr_res = tk.Label(master=frm_compK, text="")
lbl_compBohr_res.grid(row=3,column=1, sticky = 'e')
lbl_compBohr_unit = tk.Label(master=frm_compK, text="v₀")
lbl_compBohr_unit.grid(row=3,column=2)

def updateComp(event):
    r0 = float(ent_radius0.get())
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
    elif a>=1:
        show += superscript[0]
    show += superscript[int(a)]
    lbl_namecomp["text"] = show + symbol

frm_refr = tk.Frame(master = window, relief=tk.RAISED, borderwidth=1)
frm_refr.grid(row=2,column=1, padx=5, pady=5, sticky = 'nsew')
frm_refrtitle = tk.Frame(master = frm_refr, relief=tk.FLAT)
frm_refrtitle.pack()
lbl_refr = tk.Label(master=frm_refrtitle, text="Reference", width=20, font='Helvetica 12 bold')
lbl_refr.pack()

frm_refrboxes = tk.Frame(master = frm_refr, relief=tk.FLAT)
frm_refrboxes.pack()
lbl_Arefr = tk.Label(master=frm_refrboxes, text="A", width=2)
lbl_Arefr.grid(row=0, column=0)
ent_Arefr = tk.Entry(master=frm_refrboxes, width=5)
ent_Arefr.grid(row=0,column=1)
ent_Arefr.insert(0,"0")
lbl_Zrefr = tk.Label(master=frm_refrboxes, text="Z", width=2)
lbl_Zrefr.grid(row=1, column=0)
ent_Zrefr = tk.Entry(master=frm_refrboxes, width=5)
ent_Zrefr.grid(row=1,column=1)
ent_Zrefr.insert(0,"0")
lbl_Nrefr = tk.Label(master=frm_refrboxes, text="N", width=2)
lbl_Nrefr.grid(row=2, column=0)
lbl_Nrefr_res = tk.Label(master=frm_refrboxes, width=5, text="")
lbl_Nrefr_res.grid(row=2,column=1, sticky = 'e')
frm_refrsymb = tk.Frame(master = frm_refr, relief=tk.FLAT)
frm_refrsymb.pack()
lbl_namerefr = tk.Label(master=frm_refrsymb, width=5, text="")
lbl_namerefr.pack()
frm_Krefr = tk.Frame(master = frm_refr, relief=tk.FLAT)
frm_Krefr.pack()
lbl_Krefr = tk.Label(master=frm_Krefr, text="Energy ")
lbl_Krefr.grid(row=0,column=0, sticky='w')
ent_Krefr = tk.Entry(master=frm_Krefr, width=5)
ent_Krefr.grid(row=0,column=1, sticky='e')
ent_Krefr.insert(0,"0")
lbl_Krefr_unit = tk.Label(master=frm_Krefr, text=' MeV')
lbl_Krefr_unit.grid(row=0,column=2, sticky='w')
lbl_RefrV = tk.Label(master=frm_Krefr, text="Velocity ")
lbl_RefrV.grid(row=1,column=0, sticky='w')
lbl_RefrV_res = tk.Label(master=frm_Krefr, text= '')
lbl_RefrV_res.grid(row=1,column=1, sticky='e')
lbl_RefrV_unit = tk.Label(master=frm_Krefr, text=' m/s')
lbl_RefrV_unit.grid(row=1,column=2, sticky='w')
lbl_RefrC = tk.Label(master=frm_Krefr, text="Velocity ")
lbl_RefrC.grid(row=2,column=0, sticky='w')
lbl_RefrC_res = tk.Label(master=frm_Krefr, text= '')
lbl_RefrC_res.grid(row=2,column=1, sticky='e')
lbl_RefrC_unit = tk.Label(master=frm_Krefr, text=' c')
lbl_RefrC_unit.grid(row=2,column=2, sticky='w')
lbl_chstRefr = tk.Label(master=frm_Krefr, text="Charge State ", font = 'Calibri 12 bold')
lbl_chstRefr.grid(row=3,column=0, sticky='w')
lbl_chstRefr_res = tk.Label(master=frm_Krefr, text= '', font = 'Calibri 12 bold')
lbl_chstRefr_res.grid(row=3,column=1, sticky='e')
lbl_chstRefr_unit = tk.Label(master=frm_Krefr, text=' e', font = 'Calibri 12 bold')
lbl_chstRefr_unit.grid(row=3,column=2, sticky='w')

def updateRefr(event):
    r0 = float(ent_radius0.get())
    n, symbol = getElement(ent_Arefr.get(),ent_Zrefr.get())
    lbl_Nrefr_res["text"] = str(n)
    a = int(ent_Arefr.get())
    show = ''
    if int(ent_Zrefr.get()) > 118:
        lbl_namerefr["text"] = 'Error'
        lbl_namerefr["fg"] = 'red'
    else:
        lbl_namerefr["fg"] = 'black'
        if a >= 100:
            hunds = int(a/100)
            a -= 100*hunds
            show += superscript[hunds]
            if a == 0: show += superscript[0]
        if a >= 10:
            tens = int(a/10)
            a -= 10*tens
            show += superscript[tens]
        elif a>=1:
            show += superscript[0]
        show += superscript[int(a)]
        lbl_namerefr["text"] = show + symbol


frm_energies = tk.Frame(master = window, relief=tk.RAISED, borderwidth=1)
frm_energies.grid(row=1,column=2, padx=5, pady=5, sticky = 'nsew')
frm_energiestitle = tk.Frame(master = frm_energies, relief=tk.FLAT)
frm_energiestitle.pack()
lbl_energies = tk.Label(master=frm_energiestitle, text="Energies and Velocities", width=20, font='Helvetica 12 bold')
lbl_energies.pack()
frm_energiesboxes = tk.Frame(master = frm_energies, relief=tk.FLAT)
frm_energiesboxes.pack()
lbl_Coulomb = tk.Label(master=frm_energiesboxes, text="Coulomb Barrier")
lbl_Coulomb.grid(row=0, column=0, sticky='w')
lbl_Coulomb_res = tk.Label(master=frm_energiesboxes, text="")
lbl_Coulomb_res.grid(row=0, column=1, sticky='e')
lbl_Coulomb_unit = tk.Label(master=frm_energiesboxes, text="MeV")
lbl_Coulomb_unit.grid(row=0, column=2)
lbl_CoulombK = tk.Label(master=frm_energiesboxes, text="Projectile K for Coulomb Barrier")
lbl_CoulombK.grid(row=1, column=0, sticky='w')
lbl_CoulombK_res = tk.Label(master=frm_energiesboxes, text="")
lbl_CoulombK_res.grid(row=1, column=1, sticky = 'e')
lbl_CoulombK_unit = tk.Label(master=frm_energiesboxes, text="MeV")
lbl_CoulombK_unit.grid(row=1, column=2)
lbl_ProjK = tk.Label(master=frm_energiesboxes, text="Selected Projectile K")
lbl_ProjK.grid(row=2, column=0, sticky='w')
ent_ProjK = tk.Entry(master=frm_energiesboxes, width=10)
ent_ProjK.grid(row=2, column=1)
ent_ProjK.insert(0,"0")
lbl_ProjK_unit = tk.Label(master=frm_energiesboxes, text="MeV")
lbl_ProjK_unit.grid(row=2, column=2)
lbl_ProjV = tk.Label(master=frm_energiesboxes, text="Projectile v")
lbl_ProjV.grid(row=3, column=0, sticky='w')
lbl_ProjV_res = tk.Label(master=frm_energiesboxes, text="")
lbl_ProjV_res.grid(row=3, column=1, sticky = 'e')
lbl_ProjV_unit = tk.Label(master=frm_energiesboxes, text="m/s")
lbl_ProjV_unit.grid(row=3, column=2)
lbl_ProjC = tk.Label(master=frm_energiesboxes, text="Projectile v")
lbl_ProjC.grid(row=4, column=0, sticky='w')
lbl_ProjC_res = tk.Label(master=frm_energiesboxes, text="")
lbl_ProjC_res.grid(row=4, column=1, sticky = 'e')
lbl_ProjC_unit = tk.Label(master=frm_energiesboxes, text="c")
lbl_ProjC_unit.grid(row=4, column=2)

def updateCoulomb(event):
    r0 = float(ent_radius0.get())
    Zt = float(ent_Ztarg.get())
    Zp = float(ent_Zproj.get())
    rt = float(lbl_radtarg_res["text"])
    rp = float(lbl_radproj_res["text"])
    Coul = ((1E9*e_charge)/(4*pi*epsilon0))*(Zt*Zp)/(rp+rt)
    lbl_Coulomb_res["text"]=round(Coul,2)
    lbl_CoulombK_res["text"]=round(Coul*float(lbl_Acomp_res["text"])/float(ent_Atarg.get()),2)

def updateKV(event):
    r0 = float(ent_radius0.get())
    v_proj                   = math.sqrt(2E6*e_charge*float(ent_ProjK.get())/(float(ent_Aproj.get())*u))
    lbl_ProjV_res['text']    = f'{v_proj:.3e}'
    lbl_ProjC_res['text']    = round(v_proj/c, 4)
    lbl_compK_res['text']    = round(float(ent_ProjK.get())*float(ent_Aproj.get())/float(lbl_Acomp_res["text"]),2)
    v_comp                   = v_proj*float(ent_Aproj.get())/float(lbl_Acomp_res["text"])
    lbl_compV_res['text']    = f'{v_comp:.3e}'
    lbl_compC_res['text']    = round(v_comp/c, 4)
    lbl_compBohr_res['text'] = round(v_comp/2190000, 4)
    v_refr                   = math.sqrt(2E6*e_charge*float(ent_Krefr.get())/(float(ent_Arefr.get())*u))
    lbl_RefrV_res['text']    = f'{v_refr:.3e}'
    lbl_RefrC_res['text']    = round(v_refr/c, 4)
    
    
frm_scatter = tk.Frame(master = window, relief=tk.RAISED, borderwidth=1)
frm_scatter.grid(row=2,column=2, padx=5, pady=5, sticky = 'nsew')
frm_scattertitle = tk.Frame(master = frm_scatter, relief=tk.FLAT)
frm_scattertitle.pack()
lbl_scatter = tk.Label(master=frm_scattertitle, text="Scattered Data", width=20, font='Helvetica 12 bold')
lbl_scatter.pack()
frm_scatterboxes = tk.Frame(master = frm_scatter, relief=tk.FLAT)
frm_scatterboxes.pack()
lbl_scatTargK = tk.Label(master=frm_scatterboxes, text="Scattered Target K ")
lbl_scatTargK.grid(row=0, column=0, sticky='w')
lbl_scatTargK_res = tk.Label(master=frm_scatterboxes, text="")
lbl_scatTargK_res.grid(row=0, column=1, sticky = 'e')
lbl_scatTargK_unit = tk.Label(master=frm_scatterboxes, text="MeV")
lbl_scatTargK_unit.grid(row=0, column=2)
lbl_scatTargV = tk.Label(master=frm_scatterboxes, text="Scattered Target v ")
lbl_scatTargV.grid(row=1, column=0, sticky='w')
lbl_scatTargV_res = tk.Label(master=frm_scatterboxes, text="")
lbl_scatTargV_res.grid(row=1, column=1, sticky = 'e')
lbl_scatTargV_unit = tk.Label(master=frm_scatterboxes, text="m/s")
lbl_scatTargV_unit.grid(row=1, column=2)
lbl_scatCarbK = tk.Label(master=frm_scatterboxes, text="Scattered Carbon K ")
lbl_scatCarbK.grid(row=2, column=0, sticky='w')
lbl_scatCarbK_res = tk.Label(master=frm_scatterboxes, text="")
lbl_scatCarbK_res.grid(row=2, column=1, sticky = 'e')
lbl_scatCarbK_unit = tk.Label(master=frm_scatterboxes, text="MeV")
lbl_scatCarbK_unit.grid(row=2, column=2)
lbl_scatCarbV = tk.Label(master=frm_scatterboxes, text="Scattered Carbon v ")
lbl_scatCarbV.grid(row=3, column=0, sticky='w')
lbl_scatCarbV_res = tk.Label(master=frm_scatterboxes, text="")
lbl_scatCarbV_res.grid(row=3, column=1, sticky = 'e')
lbl_scatCarbV_unit = tk.Label(master=frm_scatterboxes, text="m/s")
lbl_scatCarbV_unit.grid(row=3, column=2)
lbl_scatAlK = tk.Label(master=frm_scatterboxes, text="Scattered Aluminium K ")
lbl_scatAlK.grid(row=4, column=0, sticky='w')
lbl_scatAlK_res = tk.Label(master=frm_scatterboxes, text="")
lbl_scatAlK_res.grid(row=4, column=1, sticky = 'e')
lbl_scatAlK_unit = tk.Label(master=frm_scatterboxes, text="MeV")
lbl_scatAlK_unit.grid(row=4, column=2)
lbl_scatAlV = tk.Label(master=frm_scatterboxes, text="Scattered Aluminium v ")
lbl_scatAlV.grid(row=5, column=0, sticky='w')
lbl_scatAlV_res = tk.Label(master=frm_scatterboxes, text="")
lbl_scatAlV_res.grid(row=5, column=1, sticky = 'e')
lbl_scatAlV_unit = tk.Label(master=frm_scatterboxes, text="m/s")
lbl_scatAlV_unit.grid(row=5, column=2)
lbl_backscK = tk.Label(master=frm_scatterboxes, text="Backscattered K from Al ")
lbl_backscK.grid(row=6, column=0, sticky='w')
lbl_backscK_res = tk.Label(master=frm_scatterboxes, text="")
lbl_backscK_res.grid(row=6, column=1, sticky = 'e')
lbl_backscK_unit = tk.Label(master=frm_scatterboxes, text="MeV")
lbl_backscK_unit.grid(row=6, column=2)
lbl_backscV = tk.Label(master=frm_scatterboxes, text="Backscattered v from Al ")
lbl_backscV.grid(row=7, column=0, sticky='w')
lbl_backscV_res = tk.Label(master=frm_scatterboxes, text="")
lbl_backscV_res.grid(row=7, column=1, sticky = 'e')
lbl_backscV_unit = tk.Label(master=frm_scatterboxes, text="m/s")
lbl_backscV_unit.grid(row=7, column=2)

def updateScat(event):
    Atarg = float(ent_Atarg.get())
    Aproj = float(ent_Aproj.get())
    Kproj = float(ent_ProjK.get())

    Kscat  = 4*Kproj*Atarg*Aproj/(Atarg+Aproj)**2
    Kcarb  = 4*Kproj*12*Aproj/(12+Aproj)**2
    Kalum  = 4*Kproj*27*Aproj/(27+Aproj)**2
    Kbscat = Kproj - Kalum

    Vscat  = math.sqrt(2E6*e_charge*Kscat/(Atarg*u))
    Vcarb  = math.sqrt(2E6*e_charge*Kcarb/(12*u))
    Valum  = math.sqrt(2E6*e_charge*Kalum/(27*u))
    Vbscat = math.sqrt(2E6*e_charge*Kbscat/(Aproj*u))
    
    lbl_scatTargK_res['text'] = round(Kscat, 3)
    lbl_scatCarbK_res['text'] = round(Kcarb, 3)
    lbl_scatAlK_res['text']   = round(Kalum, 3)
    lbl_backscK_res['text']   = round(Kbscat, 3)
    lbl_scatTargV_res['text'] = f'{Vscat:.3e}'
    lbl_scatCarbV_res['text'] = f'{Vcarb:.3e}'
    lbl_scatAlV_res['text']   = f'{Valum:.3e}'
    lbl_backscV_res['text']   = f'{Vbscat:.3e}'

frm_chstates = tk.Frame(master = window, relief=tk.RAISED, borderwidth=1)
frm_chstates.grid(row=3,column=0, padx=5, pady=5, sticky = 'nsew')
frm_chstatestitle = tk.Frame(master = frm_chstates, relief=tk.FLAT)
frm_chstatestitle.pack()
lbl_chstates = tk.Label(master=frm_chstatestitle, text="Charge States after\n Solid Target (C-foil)", width=20, font='Helvetica 12 bold')
lbl_chstates.pack()
lbl_chstates = tk.Label(master=frm_chstatestitle, text="According to Nikolaev", width=20, font='Helvetica 8 italic')
lbl_chstates.pack()
frm_chstatesboxes = tk.Frame(master = frm_chstates, relief=tk.FLAT)
frm_chstatesboxes.pack()
lbl_chstComp = tk.Label(master=frm_chstatesboxes, text="Compound ")
lbl_chstComp.grid(row=0, column=0, sticky='w')
lbl_chstComp_res = tk.Label(master=frm_chstatesboxes, text="")
lbl_chstComp_res.grid(row=0, column=1, sticky = 'e')
lbl_chstComp_unit = tk.Label(master=frm_chstatesboxes, text="e")
lbl_chstComp_unit.grid(row=0, column=2)
lbl_chstProj = tk.Label(master=frm_chstatesboxes, text="Projectile ")
lbl_chstProj.grid(row=1, column=0, sticky='w')
lbl_chstProj_res = tk.Label(master=frm_chstatesboxes, text="")
lbl_chstProj_res.grid(row=1, column=1, sticky = 'e')
lbl_chstProj_unit = tk.Label(master=frm_chstatesboxes, text="e")
lbl_chstProj_unit.grid(row=1, column=2)
lbl_chstTarg = tk.Label(master=frm_chstatesboxes, text="Scattered Target ")
lbl_chstTarg.grid(row=2, column=0, sticky='w')
lbl_chstTarg_res = tk.Label(master=frm_chstatesboxes, text="")
lbl_chstTarg_res.grid(row=2, column=1, sticky = 'e')
lbl_chstTarg_unit = tk.Label(master=frm_chstatesboxes, text="e")
lbl_chstTarg_unit.grid(row=2, column=2)
lbl_chstCarb = tk.Label(master=frm_chstatesboxes, text="Scattered C ")
lbl_chstCarb.grid(row=3, column=0, sticky='w')
lbl_chstCarb_res = tk.Label(master=frm_chstatesboxes, text="")
lbl_chstCarb_res.grid(row=3, column=1, sticky = 'e')
lbl_chstCarb_unit = tk.Label(master=frm_chstatesboxes, text="e")
lbl_chstCarb_unit.grid(row=3, column=2)
lbl_chstAlum = tk.Label(master=frm_chstatesboxes, text="Scattered Al ")
lbl_chstAlum.grid(row=4, column=0, sticky='w')
lbl_chstAlum_res = tk.Label(master=frm_chstatesboxes, text="")
lbl_chstAlum_res.grid(row=4, column=1, sticky = 'e')
lbl_chstAlum_unit = tk.Label(master=frm_chstatesboxes, text="e")
lbl_chstAlum_unit.grid(row=4, column=2)
lbl_chstBack = tk.Label(master=frm_chstatesboxes, text="Backscat. from Al ")
lbl_chstBack.grid(row=5, column=0, sticky='w')
lbl_chstBack_res = tk.Label(master=frm_chstatesboxes, text="")
lbl_chstBack_res.grid(row=5, column=1, sticky = 'e')
lbl_chstBack_unit = tk.Label(master=frm_chstatesboxes, text="e")
lbl_chstBack_unit.grid(row=5, column=2)

def updateChst(event):
    r0 = float(ent_radius0.get())
    Zcomp = float(lbl_Zcomp_res['text'])
    Zproj = float(ent_Zproj.get())
    Ztarg = float(ent_Ztarg.get())
    Zrefr = float(ent_Zrefr.get())

    vcomp = float(lbl_compV_res['text'])
    vproj = float(lbl_ProjV_res['text'])
    vtarg = float(lbl_scatTargV_res['text'])
    vcarb = float(lbl_scatCarbV_res['text'])
    valum = float(lbl_scatAlV_res['text'])
    vback = float(lbl_backscV_res['text'])
    vrefr = float(lbl_RefrV_res['text'])

    lbl_chstComp_res['text'] = round(Zcomp*(1+(vcomp/((Zcomp**0.45)*3.6E6))**(-1/0.6))**(-0.6), 3)
    lbl_chstProj_res['text'] = round(Zproj*(1+(vproj/((Zproj**0.45)*3.6E6))**(-1/0.6))**(-0.6), 3)
    lbl_chstTarg_res['text'] = round(Ztarg*(1+(vtarg/((Ztarg**0.45)*3.6E6))**(-1/0.6))**(-0.6), 3)
    lbl_chstCarb_res['text'] = round(6*(1+(vcarb/((6**0.45)*3.6E6))**(-1/0.6))**(-0.6), 3)
    lbl_chstAlum_res['text'] = round(13*(1+(valum/((13**0.45)*3.6E6))**(-1/0.6))**(-0.6), 3)
    lbl_chstBack_res['text'] = round(Zproj*(1+(vback/((Zproj**0.45)*3.6E6))**(-1/0.6))**(-0.6), 3)
    lbl_chstRefr_res['text'] = round(Zrefr*(1+(vrefr/((Zrefr**0.45)*3.6E6))**(-1/0.6))**(-0.6), 3)

frm_rigid = tk.Frame(master = window, relief=tk.RAISED, borderwidth=1)
frm_rigid.grid(row=3,column=1, columnspan=2, padx=5, pady=5, sticky = 'nsew')
frm_rigidtitle = tk.Frame(master = frm_rigid, relief=tk.FLAT)
frm_rigidtitle.grid(row=0, sticky='nwe')
lbl_rigid = tk.Label(master=frm_rigidtitle, text="MARA Deflector and Magnet Settings", width=40, font='Helvetica 12 bold')
lbl_rigid.pack()
frm_rigidboxes0 = tk.Frame(master = frm_rigid, relief=tk.FLAT)
frm_rigidboxes0.grid(row=1, sticky='we')
lbl_reminderchst = tk.Label(master=frm_rigidboxes0, text='Recoil Charge State ')
lbl_reminderchst.grid(row=0,column=0, sticky='w')
lbl_reminderchst_res = tk.Label(master=frm_rigidboxes0, text= '')
lbl_reminderchst_res.grid(row=0,column=1, sticky='e')
lbl_reminderchst_unit = tk.Label(master=frm_rigidboxes0, text=' e')
lbl_reminderchst_unit.grid(row=0,column=2, sticky='w')
lbl_spacer = tk.Label(master=frm_rigidboxes0, text='\t')
lbl_spacer.grid(row=1,column=3)
lbl_chstSelectorMin = tk.Label(master=frm_rigidboxes0, text='Min Charge State ')
lbl_chstSelectorMin.grid(row=0,column=4, sticky='e')
ent_chstSelectorMin_res = tk.Entry(master=frm_rigidboxes0, width=10)
ent_chstSelectorMin_res.grid(row=0,column=5, sticky='e')
ent_chstSelectorMin_res.insert(0, '0')
lbl_chstSelector_unit = tk.Label(master=frm_rigidboxes0, text=' e')
lbl_chstSelector_unit.grid(row=0,column=6, sticky='w')
lbl_spacer2 = tk.Label(master=frm_rigidboxes0, text='  ')
lbl_spacer2.grid(row=0,column=7, sticky='e')
lbl_chstSelectorMax = tk.Label(master=frm_rigidboxes0, text='Max Charge State ')
lbl_chstSelectorMax.grid(row=0,column=8, sticky='e')
ent_chstSelectorMax_res = tk.Entry(master=frm_rigidboxes0, width=10)
ent_chstSelectorMax_res.grid(row=0,column=9, sticky='e')
ent_chstSelectorMax_res.insert(0, '0')
lbl_chstSelector_unit = tk.Label(master=frm_rigidboxes0, text=' e')
lbl_chstSelector_unit.grid(row=0,column=10, sticky='w')

frm_rigidboxes = tk.Frame(master = frm_rigid, relief=tk.FLAT)
frm_rigidboxes.grid(row=2, sticky='we')

def updateRigid(event):
    r0 = float(ent_radius0.get())
    for widget in frm_rigidboxes.winfo_children():
        widget.destroy()

    lbl_chstTable = tk.Label(master=frm_rigidboxes, text='Charge State', font='Calibri 12 bold')
    lbl_chstTable.grid(row=2,column=0, sticky='w')
    lbl_spacer = tk.Label(master=frm_rigidboxes, text='', font='Calibri 12 bold')
    lbl_spacer.grid(row=2,column=1)
    lbl_DeflU = tk.Label(master=frm_rigidboxes, text='Deflector U [V]', font='Calibri 12 bold')
    lbl_DeflU.grid(row=2,column=2)
    lbl_DipField = tk.Label(master=frm_rigidboxes, text='Dipole Field [T]', font='Calibri 12 bold')
    lbl_DipField.grid(row=2,column=3)
    lbl_spacer = tk.Label(master=frm_rigidboxes, text='', font='Calibri 12 bold')
    lbl_spacer.grid(row=2,column=4)
    lbl_SepCh = tk.Label(master=frm_rigidboxes, text='Charge Sep. [mm/e]')
    lbl_SepCh.grid(row=2,column=5)
    lbl_SepM = tk.Label(master=frm_rigidboxes, text='Mass Sep. [mm/u]')
    lbl_SepM.grid(row=2,column=6)
    lbl_Sep = tk.Label(master=frm_rigidboxes, text='Masses per Charge')
    lbl_Sep.grid(row=2,column=7)

    lbl_reminderchst_res['text'] = lbl_chstRefr_res['text']
    chstmin = float(ent_chstSelectorMin_res.get())
    chstmax = float(ent_chstSelectorMax_res.get())
    if chstmax > float(lbl_Zcomp_res['text']): 
        chstmax = float(lbl_Zcomp_res['text'])
        ent_chstSelectorMax_res.delete(0,'end')
        ent_chstSelectorMax_res.insert(0, lbl_Zcomp_res['text'])

    if chstmin < 0: 
        chstmin = 0
        ent_chstSelectorMin_res.delete(0,'end')
        ent_chstSelectorMin_res.insert(0,'0')
    if chstmax == 0 or chstmax < chstmin: 
        chstmax = chstmin
        ent_chstSelectorMax_res.delete(0,'end')
        ent_chstSelectorMax_res.insert(0, chstmin)
    
    diff = chstmax - chstmin

    for i in range(int(2*chstmin),int(2*chstmax)+1):
        chst_current = float(i/2)

        lbl_Chst_res = tk.Label(master=frm_rigidboxes, text='', font='Calibri 12 bold')
        lbl_Chst_res.grid(row=2+i,column=0, sticky='w')
        lbl_DeflU_res = tk.Label(master=frm_rigidboxes, text='', font='Calibri 12 bold')
        lbl_DeflU_res.grid(row=2+i,column=2)
        lbl_DipField_res = tk.Label(master=frm_rigidboxes, text='', font='Calibri 12 bold')
        lbl_DipField_res.grid(row=2+i,column=3)
        lbl_SepCh_res = tk.Label(master=frm_rigidboxes, text='')
        lbl_SepCh_res.grid(row=2+i,column=5)
        lbl_SepM_res = tk.Label(master=frm_rigidboxes, text='')
        lbl_SepM_res.grid(row=2+i,column=6)
        lbl_Sep_res = tk.Label(master=frm_rigidboxes, text='')
        lbl_Sep_res.grid(row=2+i,column=7)

        lbl_Chst_res['text']         = chst_current
        lbl_DeflU_res['text']        = round(1.015E6*math.log(4.07/3.93)*float(ent_Krefr.get())/(chst_current), 0)
        lbl_DipField_res['text']     = round(math.sqrt(2E6*u*e_charge*float(ent_Krefr.get())*float(ent_Arefr.get()))/((chst_current)*e_charge), 4)
        lbl_SepCh_res['text']        = round(800/(chst_current), 2)
        lbl_SepM_res['text']         = round(800/float(ent_Arefr.get()), 2)
        lbl_Sep_res['text']          = round(float(ent_Arefr.get())/(chst_current), 2)
    
frm_reac = tk.Frame(master = window, relief=tk.RAISED, borderwidth=1)
frm_reac.grid(row=1,column=3, rowspan=3, padx=5, pady=5, sticky = 'nsew')
frm_reactitle = tk.Frame(master = frm_reac, relief=tk.FLAT)
frm_reactitle.grid(row=0, sticky='n')
lbl_reac = tk.Label(master=frm_reactitle, text="Reaction Channels", width=80, font='Helvetica 12 bold')
lbl_reac.pack()
frm_dqenter = tk.Frame(master = frm_reac, relief=tk.FLAT)
frm_dqenter.grid(row=1, sticky='n')
lbl_dqenter = tk.Label(master=frm_dqenter, text="Selected δq")
lbl_dqenter.grid(row=0,column=0, sticky='w')
ent_dqenter = tk.Entry(master=frm_dqenter, width = 10)
ent_dqenter.grid(row=0,column=1, sticky='e')
lbl_dqenter_unit = tk.Label(master=frm_dqenter, text=" e")
lbl_dqenter_unit.grid(row=0,column=2, sticky='w')
lbl_dqenter_unit = tk.Label(master=frm_dqenter, text="\tEdit this field to set the charge state of the possible reaction channels.", font='Calibri 10 italic')
lbl_dqenter_unit.grid(row=0,column=3, sticky='e')
frm_reacboxes_spacer = tk.Frame(master = frm_reac, relief=tk.FLAT)
frm_reacboxes_spacer.grid(row=2, sticky='we')
lbl_reacboxes_spacer = tk.Label(master=frm_reacboxes_spacer, text="\t")
lbl_reacboxes_spacer.pack()
frm_reacboxes = tk.Frame(master = frm_reac, relief=tk.FLAT)
frm_reacboxes.grid(row=3, sticky='we')

def updateChans(event):
    r0 = float(ent_radius0.get())
    for widget in frm_reacboxes.winfo_children():
        widget.destroy()

    if ent_dqenter.get() == '': return 0
    compA = float(lbl_Acomp_res['text'])
    refrA = float(ent_Arefr.get())
    diffA = compA - refrA

    compZ = float(lbl_Zcomp_res['text'])
    refrZ = float(ent_Zrefr.get())
    diffZ = compZ - refrZ
    
    row_n = 0
    lbl_reacchan = tk.Label(master=frm_reacboxes, text='Channel', font='Calibri 12 bold')
    lbl_reacchan.grid(row=row_n,column=0, sticky='w')
    lbl_reacchan_p = tk.Label(master=frm_reacboxes, text= 'p', font='Calibri 12 bold')
    lbl_reacchan_p.grid(row=row_n,column=1, sticky='')
    lbl_reacchan_n = tk.Label(master=frm_reacboxes, text= 'n', font='Calibri 12 bold')
    lbl_reacchan_n.grid(row=row_n,column=2, sticky='')
    lbl_reacchan_a = tk.Label(master=frm_reacboxes, text= 'α', font='Calibri 12 bold')
    lbl_reacchan_a.grid(row=row_n,column=3, sticky='')
    lbl_reacchan_spacer = tk.Label(master=frm_reacboxes, text='\t', font='Calibri 12 bold')
    lbl_reacchan_spacer.grid(row=row_n,column=4, sticky='')
    lbl_reacchan_A = tk.Label(master=frm_reacboxes, text='A', font='Calibri 12 bold')
    lbl_reacchan_A.grid(row=row_n,column=5, sticky='')
    lbl_reacchan_Z = tk.Label(master=frm_reacboxes, text='Z', font='Calibri 12 bold')
    lbl_reacchan_Z.grid(row=row_n,column=6, sticky='')
    lbl_reacchan_name = tk.Label(master=frm_reacboxes, text='Recoil', font='Calibri 12 bold')
    lbl_reacchan_name.grid(row=row_n,column=7, sticky='')
    lbl_reacchan_spacer = tk.Label(master=frm_reacboxes, text='\t', font='Calibri 12 bold')
    lbl_reacchan_spacer.grid(row=row_n,column=8, sticky='')
    lbl_reacchan_q = tk.Label(master=frm_reacboxes, text='q\t', font='Calibri 12 bold')
    lbl_reacchan_q.grid(row=row_n,column=9, sticky='')
    lbl_reacchan_mq = tk.Label(master=frm_reacboxes, text=' m/q\t', font='Calibri 12 bold')
    lbl_reacchan_mq.grid(row=row_n,column=10, sticky='')
    lbl_reacchan_dmq = tk.Label(master=frm_reacboxes, text=' δ(m/q)\t', font='Calibri 12 bold')
    lbl_reacchan_dmq.grid(row=row_n,column=11, sticky='')
    lbl_reacchan_pos = tk.Label(master=frm_reacboxes, text=' pos [mm]', font='Calibri 12 bold')
    lbl_reacchan_pos.grid(row=row_n,column=12, sticky='')
    lbl_reacchan_pos = tk.Label(master=frm_reacboxes, text='pos from ref', font='Calibri 12 bold')
    lbl_reacchan_pos.grid(row=row_n,column=13, sticky='w')


    for i in range(3):
        for j in range(10):
            for k in range(10):
                if i+j+k < 5:
                    row_n +=1

                    lbl_reacchan = tk.Label(master=frm_reacboxes, text='')
                    lbl_reacchan.grid(row=row_n,column=0, sticky='w')
                    lbl_reacchan_p = tk.Label(master=frm_reacboxes, text= '')
                    lbl_reacchan_p.grid(row=row_n,column=1, sticky='')
                    lbl_reacchan_n = tk.Label(master=frm_reacboxes, text= '')
                    lbl_reacchan_n.grid(row=row_n,column=2, sticky='')
                    lbl_reacchan_a = tk.Label(master=frm_reacboxes, text= '')
                    lbl_reacchan_a.grid(row=row_n,column=3, sticky='')

                    lbl_reacchan_A = tk.Label(master=frm_reacboxes, text='')
                    lbl_reacchan_A.grid(row=row_n,column=5, sticky='')
                    lbl_reacchan_Z = tk.Label(master=frm_reacboxes, text='')
                    lbl_reacchan_Z.grid(row=row_n,column=6, sticky='')
                    lbl_reacchan_name = tk.Label(master=frm_reacboxes, text='')
                    lbl_reacchan_name.grid(row=row_n,column=7, sticky='')

                    lbl_reacchan_q = tk.Label(master=frm_reacboxes, text='')
                    lbl_reacchan_q.grid(row=row_n,column=9, sticky='')
                    lbl_reacchan_mq = tk.Label(master=frm_reacboxes, text='')
                    lbl_reacchan_mq.grid(row=row_n,column=10, sticky='')
                    lbl_reacchan_dmq = tk.Label(master=frm_reacboxes, text='')
                    lbl_reacchan_dmq.grid(row=row_n,column=11, sticky='')
                    lbl_reacchan_pos = tk.Label(master=frm_reacboxes, text='')
                    lbl_reacchan_pos.grid(row=row_n,column=12, sticky='')
                    lbl_reacchan_posref = tk.Label(master=frm_reacboxes, text='')
                    lbl_reacchan_posref.grid(row=row_n,column=13, sticky='')
                    lbl_reacchan_overlap = tk.Label(master=frm_reacboxes, text='')
                    lbl_reacchan_overlap.grid(row=row_n,column=14, sticky='')

                    if i+j+k == 0:
                        lbl_reacchan['text']='No evap.'
                    else:
                        if i == 0: 
                            if j == 0:
                                lbl_reacchan['text']= str(k) +'p'
                            else: 
                                if k == 0:
                                    lbl_reacchan['text']= str(j) + 'n'
                                else:
                                    lbl_reacchan['text']= str(k) +'p' + str(j) + 'n'
                        else:
                            if k == 0:
                                if j == 0: 
                                    lbl_reacchan['text']= str(i) +'α'
                                else:
                                    lbl_reacchan['text']= str(i) +'α' + str(j) + 'n'
                            else:
                                if j == 0: 
                                    lbl_reacchan['text']= str(i) +'α' + str(k) +'p'
                                else:
                                    lbl_reacchan['text']= str(i) +'α' + str(k) +'p' + str(j) + 'n'

                    lbl_reacchan_p['text'] = k
                    lbl_reacchan_n['text'] = j
                    lbl_reacchan_a['text'] = i

                    reacA = compA - (k+j+4*i)
                    reacZ = compZ - (k+2*i)

                    n, symbol = getElement(reacA,reacZ)
                    a = reacA
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
                    elif a>=1:
                        show += superscript[0]
                    show += superscript[int(a)]

                    lbl_reacchan_A['text']    = int(reacA)
                    lbl_reacchan_Z['text']    = int(reacZ)
                    lbl_reacchan_name['text'] = show + symbol

                    q = float(ent_chstSelectorMin_res.get())+float(ent_dqenter.get())
                    lbl_reacchan_q['text']      = round(q,1)

                    mq = reacA / q
                    lbl_reacchan_mq['text']     = round(mq,3)

                    dmq = (mq / (float(ent_Arefr.get())/float(ent_chstSelectorMin_res.get()))) -1                    
                    lbl_reacchan_dmq['text']    = round(dmq,3)

                    posref = 800*dmq
                    lbl_reacchan_pos['text']    = round(posref +64, 1)
                    lbl_reacchan_posref['text'] = round(posref, 1)
                    if abs(posref) < 0.9*float(800/float(ent_Arefr.get())):
                        lbl_reacchan_overlap['text'] = 'Overlap'
                        
                    if reacA == refrA and reacZ == refrZ:
                        lbl_reacchan['font'] = 'Calibri 12 bold'
                        lbl_reacchan_p['font'] = 'Calibri 12 bold'
                        lbl_reacchan_n['font'] = 'Calibri 12 bold'
                        lbl_reacchan_a['font'] = 'Calibri 12 bold'
                        lbl_reacchan_A['font'] = 'Calibri 12 bold'
                        lbl_reacchan_Z['font'] = 'Calibri 12 bold'
                        lbl_reacchan_name['font'] = 'Calibri 12 bold'
                        lbl_reacchan_q['font'] = 'Calibri 12 bold'
                        lbl_reacchan_mq['font'] = 'Calibri 12 bold'
                        lbl_reacchan_dmq['font'] = 'Calibri 12 bold'
                        lbl_reacchan_pos['font'] = 'Calibri 12 bold'
                        lbl_reacchan_posref['font'] = 'Calibri 12 bold'
                        lbl_reacchan_overlap['font'] = 'Calibri 12 bold'

for i in range(0,5):
    window.grid_columnconfigure(i, weight=1)
    window.grid_rowconfigure(i, weight=1)


def update(event):
    namer(event)
    updateProj(event)
    updateTarg(event)
    updateComp(event)
    updateRefr(event)
    updateCoulomb(event)
    updateKV(event)
    updateScat(event)
    updateChst(event)
    updateRigid(event)
    updateChans(event)

window.bind('<Return>', update)
window.bind('<KP_Enter>', update)

frm_proj.mainloop()
