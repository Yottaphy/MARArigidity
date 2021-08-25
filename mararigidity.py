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
r0          = 1.4                   #fm
pi          = 3.14159265359

superscript = "⁰¹²³⁴⁵⁶⁷⁸⁹"

def getElement(a,z):
    a = int(a)
    z = int(z)
    n = a-z
    symbol = listName[z] if z < 119 else 'X'
    return n, symbol

listName = open("elements.txt","r").readlines()

window = tk.Tk()
window.configure(bg='#ededed')
window.title('MARA Rigidity Calculator')

frm_proj = tk.Frame(master = window, relief=tk.RAISED, borderwidth=1)
frm_proj.grid(row=0,column=0, padx=5, pady=5, sticky = 'nsew')
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
        show += superscript[int(a)]
        lbl_nameproj["text"] = show + symbol

frm_targ = tk.Frame(master = window, relief=tk.RAISED, borderwidth=1)
frm_targ.grid(row=0,column=1, padx=5, pady=5, sticky = 'nsew')
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
        show += superscript[int(a)]
        lbl_nametarg["text"] = show + symbol

frm_comp = tk.Frame(master = window, relief=tk.RAISED, borderwidth=1)
frm_comp.grid(row=1,column=1, padx=5, pady=5, sticky = 'nsew')
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

frm_refr = tk.Frame(master = window, relief=tk.RAISED, borderwidth=1)
frm_refr.grid(row=1,column=0, padx=5, pady=5, sticky = 'nsew')
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
lbl_Krefr.grid(row=0,column=0)
ent_Krefr = tk.Entry(master=frm_Krefr, width=5)
ent_Krefr.grid(row=0,column=1)
ent_Krefr.insert(0,"0")
lbl_Krefr_unit = tk.Label(master=frm_Krefr, text=' MeV')
lbl_Krefr_unit.grid(row=0,column=2)


def updateRefr(event):
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
        show += superscript[int(a)]
        lbl_namerefr["text"] = show + symbol


frm_energies = tk.Frame(master = window, relief=tk.RAISED, borderwidth=1)
frm_energies.grid(row=0,column=2, padx=5, pady=5, sticky = 'nsew')
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
    Zt = float(ent_Ztarg.get())
    Zp = float(ent_Zproj.get())
    rt = float(lbl_radtarg_res["text"])
    rp = float(lbl_radproj_res["text"])
    Coul = ((1E9*e_charge)/(4*pi*epsilon0))*(Zt*Zp)/(rp+rt)
    lbl_Coulomb_res["text"]=round(Coul,2)
    lbl_CoulombK_res["text"]=round(Coul*float(lbl_Acomp_res["text"])/float(ent_Atarg.get()),2)

def updateKV(event):
    v_proj                   = math.sqrt(2E6*e_charge*float(ent_ProjK.get())/(float(ent_Aproj.get())*u))
    lbl_ProjV_res['text']    = f'{v_proj:.3e}'
    lbl_ProjC_res['text']    = round(v_proj/c, 4)
    lbl_compK_res['text']    = (float(ent_ProjK.get())*float(ent_Aproj.get())/float(lbl_Acomp_res["text"]),2)
    v_comp                   = v_proj*float(ent_Aproj.get())/float(lbl_Acomp_res["text"])
    lbl_compV_res['text']    = f'{v_comp:.3e}'
    lbl_compC_res['text']    = round(v_comp/c, 4)
    lbl_compBohr_res['text'] = round(v_comp/2190000, 4)
    
frm_scatter = tk.Frame(master = window, relief=tk.RAISED, borderwidth=1)
frm_scatter.grid(row=1,column=2, padx=5, pady=5, sticky = 'nsew')
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
frm_chstates.grid(row=2,column=0, padx=5, pady=5, sticky = 'nsew')
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
    Zcomp = float(lbl_Zcomp_res['text'])
    Zproj = float(ent_Zproj.get())
    Ztarg = float(ent_Ztarg.get())

    vcomp = float(lbl_compV_res['text'])
    vproj = float(lbl_ProjV_res['text'])
    vtarg = float(lbl_scatTargV_res['text'])
    vcarb = float(lbl_scatCarbV_res['text'])
    valum = float(lbl_scatAlV_res['text'])
    vback = float(lbl_backscV_res['text'])


    lbl_chstComp_res['text'] = round(Zcomp*(1+(vcomp/((Zcomp**0.45)*3.6E6))**(-1/0.6))**(-0.6), 3)
    lbl_chstProj_res['text'] = round(Zproj*(1+(vproj/((Zproj**0.45)*3.6E6))**(-1/0.6))**(-0.6), 3)
    lbl_chstTarg_res['text'] = round(Ztarg*(1+(vtarg/((Ztarg**0.45)*3.6E6))**(-1/0.6))**(-0.6), 3)
    lbl_chstCarb_res['text'] = round(6*(1+(vcarb/((6**0.45)*3.6E6))**(-1/0.6))**(-0.6), 3)
    lbl_chstAlum_res['text'] = round(13*(1+(valum/((13**0.45)*3.6E6))**(-1/0.6))**(-0.6), 3)
    lbl_chstBack_res['text'] = round(Zproj*(1+(vback/((Zproj**0.45)*3.6E6))**(-1/0.6))**(-0.6), 3)

def update(event):
    updateProj(event)
    updateTarg(event)
    updateComp(event)
    updateRefr(event)
    updateCoulomb(event)
    updateKV(event)
    updateScat(event)
    updateChst(event)

window.bind('<Return>', update)
window.bind('<KP_Enter>', update)





frm_proj.mainloop()