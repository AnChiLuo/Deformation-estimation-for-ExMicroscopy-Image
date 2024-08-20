# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 14:49:18 2024
Version 26_replace Show_State() with Insertion a Label 
Next goal: Check if thread release after step4, change sheet2 to sheet1 model, Step5 no reponse, DFmap title, sheet2 DFmap dpi 
Final goal to soulve runtime ERROR(observing.....)
@author: Owner
"""

import tkinter as tk
from tkinter.font import Font
import matplotlib
from tkinter import filedialog, ttk
from tkinter.ttk import Separator
import os
from skimage import io, exposure
from skimage.filters import threshold_otsu, gaussian
from matplotlib import pyplot as plt
#import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import pyelastix
import numpy as np
import pandas as pd
from skimage.morphology import skeletonize
from math import ceil
from matplotlib.pyplot import MultipleLocator
import threading, queue
import cv2
import subprocess
from PIL import Image, ImageTk
# matplotlib.use('Agg')

##Open File(Pre, Post, Skeleton)
def TextWidth(style, s, text):
    # create a font object with Arial font, size 16, and bold style
    font = Font(family=style, size=s)
    # measure the height of the string
    width = font.measure(text)
    return width+200


def browseFiles_Pre():
    # global Fullwidth
    try :
        Path_Post_ExM
        FileName = filedialog.askopenfilename(initialdir = os.path.dirname(Path_Post_ExM), title = "Select a File", filetypes =[("All files", "*"),("tif files","*.tif"),("jpeg files","*.jpg"),("png files", "*.png"),("tiff files","*.tiff"),("gif files","*.gif"), ("raw files", "*.raw")])
    except NameError:
        FileName = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes =[("All files", "*"),("tiff files","*.tiff"),("jpeg files","*.jpg"),("png files", "*.png"),("tif files","*.tif"),("gif files","*.gif"), ("raw files", "*.raw")])
   
    global Path_Pre_ExM
    Path_Pre_ExM = FileName
    tv_file.item(0, values=(f"{Path_Pre_ExM}",))
    tv_file.tag_configure("realPath", foreground= "#ee4863")
    Cur_width = tv_file.column('Path', 'width')
    Fullwidth = TextWidth(Font_W, Size-2, Path_Pre_ExM)
    if Fullwidth > Cur_width:
        tv_file.column("Path", width= Fullwidth, stretch=0)
    if 'Path_Post_ExM' in globals():
        btn3.configure(state = "normal", bg = bg, fg = Color_ButNor)
        btn4.configure(state = "normal", bg = bg, fg = Color_ButNor)
  
def browseFiles_Post():
    try :
        Path_Pre_ExM 
        FileName = filedialog.askopenfilename(initialdir = os.path.dirname(Path_Pre_ExM), title = "Select a File", filetypes =[("All files", "*"),("tif files","*.tif"),("jpeg files","*.jpg"),("png files", "*.png"),("tiff files","*.tiff"),("gif files","*.gif"), ("raw files", "*.raw")]) 
    except NameError:    
        FileName = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes =[("All files", "*"),("jpeg files","*.jpg"),("png files", "*.png"),("tiff files","*.tiff"),("tif files","*.tif"),("gif files","*.gif"), ("raw files", "*.raw")])
    global Path_Post_ExM
    Path_Post_ExM = FileName
    tv_file.item(1, values=(Path_Post_ExM,)) 
    Cur_width = tv_file.column('Path', 'width')
    Fullwidth = TextWidth(Font_W, Size-2, Path_Post_ExM)
    if Fullwidth > Cur_width:
        tv_file.column("Path", width= Fullwidth, stretch=0)      
    if 'Path_Pre_ExM' in globals():
        btn3.configure(state = "normal", bg = bg, fg = Color_ButNor)
        btn4.configure(state = "normal", bg = bg, fg = Color_ButNor)
        
def browseFiles_Skele():
    FileName = filedialog.askopenfilename(initialdir = "/", title = "Select the Skeleton Image", filetypes =[("jpeg files","*.jpg"),("png files", "*.png"),("tiff files","*.tiff"),("tif files","*.tif"),("gif files","*.gif"),("All files", "*")])
    global Path_Skeleton
    Path_Skeleton = FileName 

def browseFiles_Tranformix():
    FileName = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes =[("txt files","*.txt"),("All files", "*")])
    global Transformix_out
    Transformix_out = FileName
    tv_fileT.item(0, values = (Transformix_out,))
    tv_fileT.tag_configure("realPath", foreground= "#ee4863")
    Cur_width = tv_fileT.column("Path", 'width')
    Fullwidth = TextWidth(Font_W, Size-2, Transformix_out)
    if Fullwidth > Cur_width:
        tv_fileT.column("Path", width = Fullwidth, stretch=0)
    if "Transformix_out" in globals():
        CheckScale2.configure(state = "normal")
        Sampling_InII.configure(Act_Entry)
        btnII_2.configure(Act_but)

def browseFiles_Tranformix_DF():
    FileName = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes =[("txt files","*.txt"),("All files", "*")])
    global Transformix_out_DF
    Transformix_out_DF = FileName
    tv_fileS2.item(1, value =(Transformix_out_DF,))
    tv_fileS2.tag_configure("realPath", foreground= "#ee4863")
    Cur_width = tv_fileS2.column("Path", "width")
    Fullwidth = TextWidth(Font_W, Size-2, Transformix_out_DF)
    if Fullwidth > Cur_width:
        tv_fileS2.column("Path", width = Fullwidth, stretch = 0)
    try:
        Transformix_out_DF
        Transformix_out_DF_fig
        btnII_7.configure(Act_but)
    except:
        pass
        
def browseFiles_Tranformix_DF_fig():
    FileName = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes =[("jpeg files","*.jpg"),("png files", "*.png"),("tiff files","*.tiff"),("tif files","*.tif"),("gif files","*.gif"),("All files", "*")])
    global Transformix_out_DF_fig
    Transformix_out_DF_fig = FileName
    tv_fileS2.item(0, value =(Transformix_out_DF_fig,))
    tv_fileS2.tag_configure("realPath", foreground= "#ee4863")
    Cur_width = tv_fileS2.column("Path", "width")
    Fullwidth = TextWidth(Font_W, Size-2, Transformix_out_DF_fig)
    if Fullwidth > Cur_width:
        tv_fileS2.column("Path", width = Fullwidth, stretch = 0)
    try:
        Transformix_out_DF
        Transformix_out_DF_fig
        btnII_7.configure(Act_but)
    except:
        pass
                
def checkDimension():
    Fix = io.imread(Path_Pre_ExM)
    Moving = io.imread(Path_Post_ExM)
    if Fix.shape == Moving.shape:
        return True
    else:
        tv_file.item(0, values=("The dimensions of Images are different! please select again!! "))
        tv_file.item(1, values=("The dimensions of Images are different! please select again!! ")) 

def StartRun():
    if checkDimension() == True:
        def show_result(imgs,Method):
            def GetName(Obj, nameLst):
                N = "Composited"
                for i in nameLst:
                   if nameLst[i] is Obj:
                       N = i
                return N
                #return [i for i in nameLst if nameLst[i] is Obj][0]           
            f ,ax = plt.subplots(1,len(imgs), figsize=(20,6))
            for i in range(len(imgs)):       
                ax[i].imshow(imgs[i], cmap = "gray")
                ax[i].set_title(GetName(imgs[i], globals()))
                ax[i].axis("off")
            f.suptitle(Method, fontsize = 32, va = "bottom", ha = "center")
        
def Validate2(Num, Type):
    if Num == "":
        return True
    else:
        try :
            eval(Num)
            if type(eval(Num)) in Type:
                return True
            else:
                return False
        except :
            return False
          
def ImageinPreview(Img1, Img2, Name1, Name2):
    fig, ax = plt.subplots(1,2,facecolor =bg,edgecolor = "white")
    ax[0].imshow(Img1, cmap = "gray")
    ax[0].set_title(Name1,fontsize=18, color = "white" )
    ax[0].axis("off")
    ax[1].imshow(Img2, cmap = "gray")
    ax[1].set_title(Name2,fontsize=18, color = "white")
    ax[1].axis("off")
    fig.tight_layout()
    canvas_prew = FigureCanvasTkAgg(fig, master = Prev_frame1)
    canvas_prew.draw()
    canvas_prew.get_tk_widget().pack(side= "top", fill="both",expand=True)
        
def Preview():
    for widgets in Prev_frame1.winfo_children():
        widgets.destroy()
    Post_Img = io.imread(Path_Post_ExM, as_gray = True)
    Pre_Img = io.imread(Path_Pre_ExM, as_gray = True)    
    if VarGau.get() == 1:        
        Pre_GF.set(Pre_GF_In.get())
        Post_GF.set(Post_GF_In.get())
        Pre_Img = gaussian(Pre_Img, sigma = Pre_GF.get())
        Post_Img = gaussian(Post_Img, sigma = Post_GF.get())
    
    ImageinPreview(Pre_Img, Post_Img, "Pre ExM", "Post ExM")
 
def Preview_Mask(Img1):
    global M_Pre_Img
    for widgets in Prev_frame1.winfo_children():
        widgets.destroy()
    if VarClear.get() == 1:
        M_Pre_Img = Pre_Img * Mask
    
    ImageinPreview(Img1, M_Pre_Img, "Pre ExM", "Mask Image")
   
def SkeletonMaker(Img):
    Thresh_Pre = threshold_otsu(Img)
    Pre_binary = Img > Thresh_Pre
    Pre_Skele = skeletonize(Pre_binary, method = "zhang") ##Zhang for 2d； Lee for 3D
    if VarClear == 1:
        Pre_Skele = Pre_Skele * Mask
    return Pre_Skele

def Preview_skeleton(Img1):
    global Skeleton_Img
    for widgets in Prev_frame1.winfo_children():
        widgets.destroy()
    if VarSkele.get() == 0:
        if VarClear.get() == 1:
           Img1 = Img1 * Mask 
        Skeleton_Img = SkeletonMaker(Img1)
    elif VarSkele.get() == 1:
        if "Path_Skeleton" not in globals():
            browseFiles_Skele()
        Skeleton_Img = io.imread(Path_Skeleton)
        if VarClear.get() == 1:
            Skeleton_Img = Skeleton_Img*Mask            
    ImageinPreview(Img1, Skeleton_Img, "Pre ExM", "Skeleton")
            
def checkDimension2():
    global C_Post_Img
    global C_Pre_Img
    C_Post_Img = io.imread(Path_Post_ExM, as_gray = True)
    C_Pre_Img = io.imread(Path_Pre_ExM, as_gray = True)
    if C_Post_Img.shape == C_Pre_Img.shape:
        global Post_Img
        Post_Img = C_Post_Img                   
        global Pre_Img
        Pre_Img = C_Pre_Img
        global Active_step
        Active_step[0] = 2
        Pre_Img = Pre_Img.astype("float32")
        Post_Img= Post_Img.astype("float32")
        # Step2 region activation
        for widgets in frame2.winfo_children():
            if widgets.winfo_class() == "Button":
                if widgets.cget("text") == "Save result":
                    continue
                widgets.configure(Act_but)
            elif widgets.winfo_class() == "Frame":
                for C_widgets in widgets.winfo_children():
                    if C_widgets.winfo_class() == "Entry":
                        C_widgets.configure(Act_Entry)
            else:
                widgets.config(state = "normal")
        Pre_GF_In["state"] = "disable"
        Post_GF_In["state"] = "disable"
        CheckGau["state"] = "normal"           
                                
        for widgets in frame1.winfo_children():
            if widgets.winfo_class() == "Button":
                widgets.configure(Dis_but)
        btn1.config(state = "disable")
        btn2.config(state = "disable")
    else:
        for widgets in Prev_frame1.winfo_children():
            widgets.destroy()
            Error1 = tk.Label(Prev_frame1, text = "The dimensions of Images are different!\n please select again!! ", fg = "#e6d2d5",font = ("Dubai", 20), bg = bg ,relief='groove',bd = 1, padx = 100, pady = 100)
            Error1.pack( anchor= "center", padx = 30, pady = 30)
       
def enable(Var, frame):
    if Var.get() == 1:
        for widgets in frame.winfo_children():
            if widgets.winfo_class() == "Entry":
                widgets.configure(Act_Entry)
            elif widgets.winfo_class() == "Label":
                    widgets.configure(fg = "#2983bb", bg = bg)
            elif widgets.winfo_class() == "Button":
                widgets.configure(Act_but)
            elif widgets.winfo_class() == "TCombobox":
                widgets.config(state = "normal")              
    elif Var.get() == 0:   
        for widgets in frame.winfo_children():
            if widgets.winfo_class() == "Entry":
                widgets.configure(Dis_Entry)
            elif widgets.winfo_class() == "Label":
                    widgets.configure(fg = "#2b333e", bg = bg )
            elif widgets.winfo_class() == "Button":
                widgets.configure(Dis_but)
            elif widgets.winfo_class() == "TCombobox":
                widgets.config(state = "disable")

def Composite_Img(Imgs, equalize = False):
    if equalize:
        Imgs = [exposure.equalize_hist(Img) for Img in Imgs]    
    Imgs = [Img/Img.max() for Img in Imgs]
    Imgs += [np.zeros(shape = Imgs[0].shape)]
    return np.dstack(Imgs)

def show_result(imgs,Method):
    def GetName(Obj, nameLst):
        N = "Overlay_Img"
        for i in nameLst:
           if nameLst[i] is Obj:
               N = i
        return N
    fig, ax = plt.subplots(1, len(imgs), facecolor = bg, edgecolor = "white")
    Color_type = ["gray", "Reds", "gray"]
    for i in range(len(imgs)):
        if i < 2:
            Holder_img = np.zeros(imgs[i].shape + (3,))
            Holder_img[:,:,i] = imgs[i]/imgs[i].max()
            ax[i].imshow(Holder_img, cmap = Color_type[i])
        else:
            ax[i].imshow(imgs[i], cmap = Color_type[i])
        ax[i].set_title(GetName(imgs[i], globals()), fontsize=18, color = "white")
        ax[i].axis("off")
    fig.subplots_adjust(bottom =0.05, wspace = 0.05, left = 0.02, right = 0.98, top = 0.9, hspace = 0.15)
    #fig.suptitle(Method, fontsize = 18, va = "top", ha = "center", color='white')   
    return fig

def show_state():   
     # matplotlib.use('TkAgg')
     bg = "#1c2938"
     fig2, ax = plt.subplots(1, 1, facecolor = bg, edgecolor = "red", dpi = 100, figsize = (5,3))
     fig2.text(0.51, 0.5, "Deflection Calculation is done!!", style = 'normal', fontsize = 20, color = "#d0dfe6", horizontalalignment = "center", fontweight = "normal", fontfamily = "Dubai")
     #fig.text(0.3, 0.5, "Calculation of Deflection is done!!", style = 'normal', fontsize = 30, fontfamily = "Dubai", color = "#b598a1", bbox = {"facecolor": bg, "alpha": 0.6, "pad": 10})
     #ax.axis("off")
     ax.set_facecolor(bg)
     ax.set_xticks([])
     ax.set_yticks([])
     ax.set(ylim = (0,2))
     ax.set(xlim = (0,10))
     ax.spines['bottom'].set_color('gray')
     ax.spines['top'].set_color('gray')
     ax.spines['left'].set_color('gray')
     ax.spines['right'].set_color('gray')
     return fig2

def R_threading(func, *args):
    Thred = threading.Thread(target = func, args = args)
    Thred.setDaemon(True)
    Thred.start()


def NR(Img1, Img2, NR_para, AS):
    global Reg1st
    global Info
    global Active_step
    Para1 = pyelastix.get_default_params(type = "SIMILARITY")
    Para1.AutomaticScalesEstimation = True
    Para1.NumberOfResolutions = NR_para[0]
    Para1.MaximumStepLength = NR_para[1]# Stepsize too big may cause Elastix unstable and to send the images too far appart.Increasing the step length makes your program faster
    Para1.MaximumNumberOfIterations = NR_para[2]
    # Rigid transformation_Regist
    Reg1st, field_NR, Info = pyelastix.register(Post_Img, Pre_Img, Para1, Path_Post_ExM)
    q.put(1)
    

def NRR(Img1, Img2, R_para, AS):
    global Reg2nd
    global field
    Para_Def = pyelastix.get_default_params(type = "BSPLINE")
    Para_Def.NumberOfResolutions = R_para[0]
    Para_Def.MaximumStepLength =  R_para[1]
    Para_Def.MaximumNumberOfIterations =  R_para[2]
    Para_Adv = pyelastix.get_advanced_params()
    Para = Para_Def + Para_Adv        
    # Non_Rigid transformation__Regist & show result       
    Reg2nd, field = pyelastix.register(Img2, Img1, Para, Path_Post_ExM )
    #print("pyramidsamples :", Para.ImagePyramidSchedule)
    q.put(1)

                    
def GoNext(AS):   
    global Pre_Img
    global Post_Img
    global Active_step
    #多線程控制
    global lock
    global q
    try:
        lock
    except NameError:       
        lock = threading.Lock()
    try:
        q
    except NameError:
        q = queue.Queue()
    lock.acquire()       
    Temp = Active_step
    if VarGau.get() == 1:
        Pre_GF.set(Pre_GF_In.get())
        Post_GF.set(Post_GF_In.get())
        Pre_Img = gaussian(Pre_Img, sigma = Pre_GF.get())
        Post_Img = gaussian(Post_Img, sigma = Post_GF.get())
    elif VarGau.get() == 0:
        Post_Img = C_Post_Img.astype("float32")
        Pre_Img = C_Pre_Img.astype("float32")
    try:
       Prev_Win.after_cancel(Refresh)
    except:
        pass
         
    if AS == 2:
        global NR_para
        ## Disable Region2
        for i in [Pre_GF_In, Post_GF_In, NR_Res_In, NR_Length_In, NR_Iterations_In]:
            i.config(Dis_Entry)
        for j in[btn5, btn6, btn9]:
            j.config(Dis_but)
        CheckGau.config(state = "disable")
        btn7.config(Dis_but)
        btn6.config(Busy_btn)
        #Start NRR
        Res, Leng, Iter = NR_Res.get(), NR_Length.get(), NR_Iterations.get()
        NR_para = [Res, Leng, Iter]
        R_threading(NR, Pre_Img, Post_Img, NR_para, AS)
        Prev_Win.after(100, Refresh)
        #                    
    elif AS == 3:
        global MaPre
        global R_para
        ##Disable Region3:
        for i in ["btn9", "btn10", "btn12"]:
            eval(i).config(Dis_but)
        for j in [R_Res_In, R_Length_In, R_Iterations_In]:
            j.config(Dis_Entry)
        CheckClear.config(stat = "disable")
        btn10.config(Dis_but)
        btn9.config(Busy_btn)
        btn12.config(Dis_but)
        #Check if we need the Mask Image
        if VarClear.get() == 1:
            MaPre = Pre_Img * Mask
            Pre_Img = Pre_Img * Mask          
        elif VarClear.get() == 0:
            Pre_Img = C_Pre_Img.astype("float32")           
        #Start RR
        Res, Leng, Iter = R_Res_In.get(), R_Length_In.get(), R_Iterations_In.get()
        R_para = [Res, Leng, Iter]
        R_threading(NRR, Pre_Img, Reg1st, R_para, AS )
        Prev_Win.after(100, Refresh)
        
    elif AS == 4:
        global Skeleton_Img
        global Unit
        global xy_offset
        global ShowState
        ##Disable Region4
        for i in [AutoChek, RefChek, CheckScale, Unit_In]:
            i.config(state = "disable")
        for j in [btn15, btn16, btn14]:
            j.config(Dis_but)
        for k in [X_scale_In, Y_scale_In, Sampling_In]:
            k.config(Dis_Entry)
        btn15.config(Busy_btn)
        btn16.config(Dis_but)
        Sampling_size = int(Sampling_In.get())

        if "Skeleton_Img" not in globals():
            Preview_skeleton(Pre_Img)
        if Skeleton_Img.dtype != "bool":
            Skeleton_Img = Skeleton_Img > 0        
        if VarScale.get() == 1:
            Unit = Unit_In.get()
            Bin_unit.set(Unit)
        elif VarScale.get() == 0:
            Unit = "Pixel"
            Bin_unit.set(Unit)
        R_threading(CDef, Sampling_size)
        Prev_Win.after(100, Refresh)
        
    elif AS == 5:
        global BL
        global BW
        global Deformation_Lst
        BW = float(Bin_width.get())
        BL = float(Total_binL.get())
        Bin_width_In.config(Dis_Entry)
        Total_binL_In.config(Dis_Entry)
        RMS_limit_In.config(Dis_Entry)
        btn18.config(Busy_btn)
        btn19.config(Dis_but)
        
        Deformation_Lst = np.array(Deformation_Lst)
        Deformation_Lst = np.round(Deformation_Lst, 4 )
        if VarScale.get() == 1:
            Deformation_Lst_R = Deformation_Lst * float(X_scale.get())
        elif VarScale.get() == 0:
            Deformation_Lst_R = Deformation_Lst
        R_threading(CRMS, Deformation_Lst_R)
        Prev_Win.after(100, Refresh)

        
def GoNextII(AS):
    global UnitII
    global Active_step 
    global q
    #多線程控制
    global lock
    global SowState
    ShowState = show_state()
    try:
        lock
    except NameError:       
        lock = threading.Lock()
    try:
        q
    except NameError:
        q = queue.Queue()
    def Test():
        global Active_step 
        lock.acquire()
        Active_step[1] = 7 
               
        Sampling_size = int(Sampling_InII.get())
        CDef(Sampling_size)
    Sampling_size = int(Sampling_InII.get())
    if VarScale2.get() == 1:
        UnitII.set(Unit_InII.get())
    elif VarScale2.get() == 0:
        UnitII.set("Pixel")
     # ##Disable sheetII,region1
    for i in [Unit_InII, CheckScale2]:
        i.config(state = "disable")
    for j in [btnII_1]:
        j.configure(Dis_but)
    for k in [X_scale_In, Y_scale_In, Sampling_InII]:
        k.config(Dis_Entry)
    btnII_2.config(Busy_btn)
    R_threading(Test)
    # R_threading(CDef, Sampling_size, Active_step)
    Prev_Win.after(500, RefreshII)
    #root.after(100, Refresh, AS)
  
def GoNextII_RMS(AS):
    global Active_step
    global q

    #多線程控制
    global lock
    try:
        lock
    except NameError:
        lock = threading.Lock()
    try:
        q
    except NameError:
        q = queue.Queue()
    def Get_Var():
        global Active_step
        global BWII
        global BLII
        global Deformation_LstII
        lock.acquire()
        Active_step[1] = 8 
        BWII = float(Bin_widthII.get())
        BLII = float(Total_binLII.get())
        Deformation_LstII = np.array(Deformation_LstII)
        Deformation_LstII = np.round(Deformation_LstII, 4 )
        if VarScale2.get() == 1:
            Deformation_Lst_R = Deformation_LstII * float(X_scale2.get())
        elif VarScale2.get() == 0:
            Deformation_Lst_R = Deformation_LstII
        CRMS(Deformation_Lst_R )
    # ##Disable sheetII,region2
    Bin_width_InII.config(Dis_Entry)
    Total_binL_InII.config(Dis_Entry)
    RMS_limit_InII.config(Dis_Entry)
    btnII_3.config(Busy_btn)
    btnII_4.config(Dis_but)
    #線程開始 Get_Var() 取得線程鎖   
    R_threading(Get_Var)
    Prev_Win.after(100, RefreshII)

def CoordinateVH(Array):
    Points = len(Array)
    Array_YH = np.empty((Points, Points))
    for j in range(0, Points):
        Array_YH[j,:] = Array
    Array_YV = np.einsum("ji", Array_YH)
    return Array_YH, Array_YV
        
def CDef(Sampling_size):
    global Deformation_Lst
    global Distance
    global xy_offset
    global Deformation_LstII 
    global DistanceII        
    Temp_Deformation_Lst =[]

    if Active_step[0] == 4 and Active_step != 7:
        Temp_Distance = pd.DataFrame({})
        # Return the displacement
        xy_offset = np.array(field)
        Skele_point = np.where(Skeleton_Img == True)
        Temp_Distance["Ori_X"] = Skele_point[1]
        Temp_Distance["Ori_Y"] = Skele_point[0]
        Temp_Distance["Offset_X"] = xy_offset[0][Skeleton_Img]
        Temp_Distance["Offset_Y"] = xy_offset[1][Skeleton_Img]
        Temp_Distance["Deform_X"] = Temp_Distance["Ori_X"] + Temp_Distance["Offset_X"] 
        Temp_Distance["Deform_Y"] = Temp_Distance["Ori_Y"] + Temp_Distance["Offset_Y"]
    elif Active_step[1] == 7:
        outputpoints = pd.read_table(Transformix_out, header = None,  delimiter = " ")
        Temp_Distance = pd.DataFrame(outputpoints)
        Temp_Distance = Temp_Distance[outputpoints.columns[[10,11,22,23]]]
        Temp_Distance = Temp_Distance.rename(columns =  {10: "Ori_X", 11: "Ori_Y", 22: "Deform_X", 23: "Deform_Y"})
    
    ##Generate deltaX and delta Y for Ori and Deform
    Ori_X = np.array(Temp_Distance["Ori_X"])
    Ori_XH, Ori_XV = CoordinateVH(Ori_X)
    Ori_Y = np.array(Temp_Distance["Ori_Y"])
    Ori_YH, Ori_YV = CoordinateVH(Ori_Y)
    Deform_X = np.array(Temp_Distance["Deform_X"])
    Deform_XH, Deform_XV = CoordinateVH(Deform_X)
    Deform_Y = np.array(Temp_Distance["Deform_Y"])
    Deform_YH, Deform_YV = CoordinateVH(Deform_Y)

    #Distance calculation
    deltaOri_X = Ori_XH - Ori_XV
    deltaOri_Y = Ori_YH - Ori_YV
    deltaDef_X = Deform_XH- Deform_XV
    deltaDef_Y = Deform_YH - Deform_YV
    m_Ori = np.sqrt(np.einsum("ij,ij->ij", deltaOri_X, deltaOri_X) + np.einsum("ij,ij->ij", deltaOri_Y, deltaOri_Y))
    m_Def = np.sqrt(np.einsum("ij,ij->ij", deltaDef_X, deltaDef_X) + np.einsum("ij,ij->ij", deltaDef_Y, deltaDef_Y))
    m_offset = m_Def - m_Ori
    ##Group the Deformed_distance(m) and Difference (m'-m). The sampling size is adjustable to speed up the calculation.
    m_offset_F = []
    m_OriN_F = []
    for i in range(1, len(m_offset)):
        m_offset_F += list(np.diagonal(m_offset, offset = i))
        m_OriN_F += list(np.diagonal(m_Ori, offset = i))
    Temp_Deformation_Lst = [[m_OriN_F[i], m_offset_F[i]] for i in range(0, len(m_offset_F), Sampling_size)]
    if Active_step[0] == 4 and Active_step[1] != 7:
        Deformation_Lst = Temp_Deformation_Lst
        Distance = Temp_Distance
    elif Active_step[1] == 7:
        Deformation_LstII = Temp_Deformation_Lst
        DistanceII = Temp_Distance
    q.put(1)

def CRMS(Lst):
    global RMS_value
    global RMS_valueII
    global Bin_Lst
    global Bin_LstII
    Temp_Lst = []    
    # Bin data for calculating RMS_get the Ceiling of Distance and group it.
    #Deformation_Lst = np.array(Deformation_Lst)
    Lst = np.array(Lst)
    # Deformation_Lst = np.round(Deformation_Lst, 4 )
    # if VarScale.get() == 1:
    #     Deformation_Lst = Deformation_Lst * float(X_scale.get())
    
    #Bin_Lst = [i*BW for i in range(0,ceil(max(Lst[:,0])/BW))]
    if Active_step[0] == 5 and Active_step[1] !=8:
        Temp_Lst = [i*BW for i in range(0,ceil(max(Lst[:,0])/BW))]
    elif Active_step[1] == 8:
        Temp_Lst = [i*BWII for i in range(0,ceil(max(Lst[:,0])/BWII))]
        
    #Bin_Lst = np.linspace(0, max(Deformation_Lst[:,0]), ceil(max(Deformation_Lst[:,0])/BW))# We currently break the Difference (m'-m) into BL/BW group.
    label =  np.digitize(Lst[:,0], Temp_Lst)# Merge the Difference (m'-m) with Bin
    Deformation_DF = np.column_stack((Lst, label))
    Deformation_DF = pd.DataFrame(Deformation_DF, columns = ["m","RMS","Bin_Type"])        
    # Calculate the RMS of each Bin
    TempRMS_value = Deformation_DF.groupby("Bin_Type").agg(list)
    TempRMS_value["m"]= TempRMS_value["m"].apply(lambda x: np.array(x).mean())
    #RMS_value["i"] = RMS_value["RMS"].apply(lambda i: len(i))
    TempRMS_value["RMS"] = TempRMS_value["RMS"].apply(lambda i: np.linalg.norm(np.array(i))/len(i)**0.5)
    if  Active_step[0] == 5 and Active_step[1] !=8:
        RMS_value = TempRMS_value
        Bin_Lst = Temp_Lst
    elif Active_step[1] == 8:
        RMS_valueII = TempRMS_value
        Bin_LstII = Temp_Lst
    q.put(1)

def Transformix(Path):
    global Raw_trans
    global cmd
    def Bit_convert(Path, Old_N, New_N):
        Open = os.path.join(Path, Old_N)
        Save = os.path.join(Path, New_N)
        Img = io.imread(Open)
        Img = cv2.normalize(Img, None, 0,255, cv2.NORM_MINMAX)
        Img = Img.astype(np.uint8)
        io.imsave(Save, Img)
        
    def Edit_TransPara(Path):
        NewLine = []
        with open(Path, "r") as file:
            for Item in file:
                Temp = Item.replace("mhd", "tiff")
                NewLine.append(Temp)
        with open(Path, "w") as file:
            for line in NewLine:
                file.writelines(line)
            file.close()
        
    Parent = os.path.dirname(Path)
    Path_Tp_NR = os.path.join(Parent, "NRTransformParameters.0.txt")
    Path_Tp_NRR = os.path.join(Parent, "NRRTransformParameters.0.txt")
    Path_Img = os.path.join(Parent, "Raw.tif")
    Path_Img_NR = os.path.join(Parent, "NRresult.tiff")
    #Save Img for Transformix
    Raw = io.imread(Path)
    Raw = cv2.normalize(Raw, None, 0,255, cv2.NORM_MINMAX)
    Raw = Raw.astype(np.uint8)
    io.imsave(Path_Img, Raw) 
    #Edit Trasformparameter for Transformix
    Edit_TransPara(Path_Tp_NR)
    Edit_TransPara(Path_Tp_NRR)
    #Calling Transformix        
    cmd = ["transformix", "-in", Path_Img, "-out", Parent, "-tp", Path_Tp_NR]
    Sup_NR = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    Sup_NR.communicate()
    Bit_convert(Parent, "result.tiff", "NRresult.tiff")
    cmd = ["transformix", "-in", Path_Img_NR, "-out", Parent, "-tp", Path_Tp_NRR]
    Sup_NRR = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr = subprocess.STDOUT)
    Sup_NRR.communicate()
    Bit_convert(Parent, "result.tiff", "NRRresult.tiff")
    Raw_trans = io.imread(Path_Img_NR)

        
def DFmapGenerate(AS, Img1, Img2):
    global DFmap
    global Temp_Path
    Temp_Path = os.path.join(os.path.dirname(Path_Post_ExM), "DFmap.tiff")
    if VarRaw.get()==1:
        Transformix(Path_Post_ExM)
        Img2 = Raw_trans  
    Gap = Gap_DM.get()
    height, weight = Img1.shape
    ##Use meshgrid to return coordinate matrices from coordinate vectors.
    ##Extract row and cloumn coordinates  to which flow vector values will be add
    row_coords, col_coords = np.meshgrid(np.arange(height), np.arange(weight), indexing= "ij")
    DFmap = plt.figure(facecolor = bg, dpi= 600)
    plt.imshow(Composite_Img([Img1, Img2]))
    #plt.quiver(col_coords[::Gap,::Gap],row_coords[::Gap,::Gap], xy_offset[0][::Gap,::Gap], -xy_offset[1][::Gap,::Gap] ,color='w', units='xy', scale=1,alpha=0.5 )
    plt.quiver(col_coords[::Gap,::Gap],row_coords[::Gap,::Gap], -xy_offset[0][::Gap,::Gap], xy_offset[1][::Gap,::Gap] ,color= "w", units='xy', scale=1, alpha=0.9, headwidth = 4 )
    # plt.title('Deformation Vector')
    # plt.ylim(max(row_coords[::Gap,::Gap][:,0]), min(row_coords[::Gap,::Gap][:,0]))
    # plt.tick_params(axis='both', bottom=False, left = False, labelbottom = False, labelleft = False)
    # plt.gcf().set_dpi(1200)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.savefig(Temp_Path, pad_inches=0, bbox_inches='tight', transparent=True)

    for widgets in Prev_frame1.winfo_children():
        # widgets.update()
        widgets.destroy()
    DF_title = tk.Label(Prev_frame1, text = "Deformation Vector", fg = "#d0dfe6", font = (Font_W, Size), bg = bg )
    DF_title.pack(anchor= "center", expand = True, fill = "x")
    # canvas = tk.Canvas(Prev_frame1)
    # canvas.create_image(0, 0, anchor='nw', image=tk_DFmap)   # 在 Canvas 中放入圖片
    # canvas.pack(anchor = "nw",expand=False, padx = 10, pady = 20)   
    canvas_prew = FigureCanvasTkAgg(DFmap, master = Prev_frame1)
    canvas_prew.draw()
    canvas_prew.get_tk_widget().pack(anchor = "nw",expand=False, padx = 10, pady = 20)   
    btn23.config(Act_but)
    
def DFmapGenerateII(AS):
    global q
    global lock
    try:
        lock
    except NameError:
        lock = threading.Lock()
    try:
        q
    except NameError:
        q = queue.Queue()
    def Get_varII():
        global Active_step
        global DF_info
        global DFmapII
        lock.acquire()
        Active_step[1] = 9
        #load Grid offset
        Temp= pd.read_table( Transformix_out_DF, header = None,  delimiter = " ")
        Temp = pd.DataFrame(Temp)
        Temp = Temp[Temp.columns[[10,11,28,29]]]     
        Temp= Temp.rename(columns =  {10: "Ori_X", 11: "Ori_Y", 28: "offset_X", 29: "offset_Y"})
        ####Draw vector on Image(Do not disrupt codes  on this region!!We will get shit!!)
        DFmapII = plt.figure(facecolor =  "white")
        Img1 = io.imread(Transformix_out_DF_fig)
        plt.imshow(Img1)
        plt.quiver(np.array(Temp["Ori_Y"]), np.array(Temp["Ori_X"]), np.array(Temp["offset_Y"]), np.array(Temp["offset_X"]), color='w', units='xy', scale=1, alpha=0.5)
        plt.title('Deformation Vector')
        plt.ylim(max(Temp["Ori_Y"]), min(Temp["Ori_Y"]))
        plt.xlim(max(Temp["Ori_X"]), min(Temp["Ori_X"])) 
        plt.tick_params(axis='both', bottom=False, left = False, labelbottom = False, labelleft = False)
        plt.gcf().set_dpi(300)
        ###End of draw figure
        q.put(1)
    # ##Disable sheetII,region3
    btnII_10.config(Dis_but)
    btnII_7.config(Busy_btn)
    btnII_6.config(Dis_but)
    btnII_4.config(Dis_but)
     #線程開始 Get_VarII() 取得線程鎖     
    R_threading(Get_varII) 
    Prev_Win.after(100, RefreshII)
                
def Refresh():
    global Active_step
    global End
    global Timer1
    global MaxM
    End = "No"
    while not q.empty():
        try:
            Finish = q.get()
            #print("Finish: ", Finish, Active_step, AS )
            for widgets in Prev_frame1.winfo_children():
                widgets.destroy()   
            if Finish == 1 and Active_step[0] == 2:
                ##Disable Region2
                btn6.config(Dis_but)
                ##Active Region3
                for k in [ btn9, btn10, btn8]:
                    k.config(Act_but)
                for L in [R_Res_In, R_Length_In, R_Iterations_In]:
                    L.config(Act_Entry)
                CheckClear.config(state = "normal")
                ##Show Info in PreviewWindow
                tv1.item(0, values= [round(float(i),4) for i in Info[1:]])
                ##Generate plot
                Massage1.destroy()
                Composited_Img = Composite_Img([Pre_Img, Reg1st])
                fig = show_result([Pre_Img, Reg1st, Composited_Img], "Similarity Registration")
                
            elif Finish == 1 and Active_step[0] == 3:
                ##Disable Region3:
                btn9.config(Dis_but)
                ##Active Region4:
                for i in [AutoChek, RefChek, CheckScale ]:
                    i.config(state = "normal")
                for j in [btn14, btn15, btn16, btn11]:
                    j.config(Act_but)
                Sampling_In.config(Act_Entry)
                ## Generate plot
                Composited_Img = Composite_Img([Pre_Img, Reg2nd])
                fig = show_result([Pre_Img, Reg2nd, Composited_Img], "Beta-spline Registration")
                        
            elif Finish == 1 and Active_step[0] == 4:
                ##Calculate the Max for measurement M
                Max = np.array(Deformation_Lst)
                MaxM = ceil(max(Max[:,0])/10)*10
                Total_binL.set(MaxM)
                ##Disable Region4:              
                btn15.config(Dis_but)
                ##Active Region5
                for i in [btn18, btn19, btn17]:
                    i.config(Act_but)
                for j in [Bin_width_In, Total_binL_In, RMS_limit_In]:
                    j.config(Act_Entry)
                State_Info = tk.Label(Prev_frame1, text = "Deflection Calculation is done!!", bg = bg, fg = "#b598a1",font = ("Dubai", Size+12), padx = 100, pady = 100, relief= relief, bd = 1 )
                State_Info.pack(anchor = "nw", expand = True, fill = "both", padx = 20, pady = (10,0) )
                Active_step[0] = Active_step[0]+1
                End = "Yes"           
                lock.release()
                break
                           
            elif Finish == 1 and Active_step[0] == 5:
                global RMS_plot
                #print("yes in 5")
                ##Disable Region5
                btn18.config(Dis_but)
                ##Active Region6
                for i in [btn21, btn22,btn20]:
                    i.config(Act_but)
                Gap_In.config(Act_Entry)
                if VarGau.get() == 1:
                    Raw_use["state"] = "normal"
                    Raw_use.select()
    
                #ShowImage od Preview window
                X_Label = [Bin_Lst[i] if i%4 == 0 else 0 for i in range(0, len(Bin_Lst))]
                #RMS_plot = plt.figure(figsize=(5,4))
                #matplotlib.use('TkAgg')
                fig = plt.figure(figsize=(5,4))
                plt.title("RMS plot")
                #plt.plot(RMS_value["m"], RMS_value["RMS"], color = "dodgerblue", marker = "o", label = "RMS" )
                plt.plot(RMS_value["m"], RMS_value["RMS"], color = "dodgerblue", marker = "o", label = "RMS" )
                ax = plt.gca()
                #x_major_locator = MultipleLocator(100)
                ax.xaxis.set_major_locator(MultipleLocator(100))
                plt.xlabel(f"Measurement Length ({Unit})")
                plt.ylabel(f"RMS Error({Unit})")
                plt.xticks( X_Label , fontsize = 10)
                plt.xlim(0, BL)
                plt.ylim(0, float(RMS_limit.get()))
                plt.legend()
                RMS_plot = fig

                ##Prepare Main window for Treeview for RMS
                MainW_tv2 = tk.LabelFrame(Prev_frame1, text = "Root Mean Square(RMS) value", fg = "#d0dfe6", font = (Font_W, Size), bg = bg )
                MainW_tv2.pack(anchor = "nw", expand = True, fill = "both",pady = 10, padx = 10, side = "right")
                # Treeview start
                tv2 = ttk.Treeview(MainW_tv2, style="mystyle1.Treeview", height= 10)
                tv2.pack(anchor = "nw", side= "left", expand = True, fill = "both", padx=5)
                #Add scrolly of y direction
                tv2scrolly = tk.Scrollbar(MainW_tv2, orient= "vertical", command= tv2.yview)
                tv2.configure(yscrollcommand= tv2scrolly.set)
                tv2scrolly.pack(side= "right", fill = "y", padx = (2,5))
                # Format of column
                tv2["columns"] = ["m", "RMS"]
                tv2.column("#0", stretch = False, width = 35, minwidth = 30)
                tv2.column("m", width = 35, minwidth = 20, anchor = "center")
                tv2.column("RMS", width = 35, minwidth = 20, anchor = "center")
                # Heading of column
                tv2.heading("#0", text = "Bin", anchor = "center")
                tv2.heading("m", text = "length(m)", anchor = "center")
                tv2.heading("RMS", text = "RMS", anchor = "center")            
                for index, row in RMS_value.iterrows():
                    tv2.insert(parent="", index = "end", iid = index, text= int(index),  values = [round(i, 3) for i in list(row)])                                                  
            # for widgets in Prev_frame1.winfo_children():
            #     widgets.destroy()    
            canvas_prew = FigureCanvasTkAgg(fig, master = Prev_frame1)
            canvas_prew.draw()
            canvas.update()
            canvas_prew.get_tk_widget().pack(side= "left", fill="x",expand = True, padx = 20, pady = (5,0))
            End = "Yes"           
            lock.release()
            Active_step[0] = Active_step[0]+1            
            # root.after_cancel(S)            
        except:
            break
        break            
            #Show the Result
    if End == "No":
        Timer1 = Prev_Win.after(500, Refresh)
    elif End == "Yes":
        Prev_Win.after_cancel(Timer1)#取消循環事件
    #root.after(500, Refresh ,AS)
    
def RefreshII():
    global Active_step
    global End
    global Timer
    global BackF
    End = "No"
    while not q.empty():
        try: 
            Finish = q.get()
            for widgets in Prev_frame1.winfo_children():
                widgets.destroy() 
            if Finish == 1 and Active_step[1] ==7 :
                ##Calculate the Max for measurement M
                MaxII = np.array(Deformation_LstII)
                MaxMII = ceil(max(MaxII[:,0])/10)*10
                Total_binLII.set(MaxMII)
                btnII_2.config(Dis_but)
                for i in [btnII_3, btnII_4]:
                    i.config(Act_but)
                for j in [Bin_width_InII, Total_binL_InII, RMS_limit_InII]:
                    j.config(Act_Entry)
                BackF =  Active_step[1]
                State_Info = tk.Label(Prev_frame1, text = "Deflection Calculation is done!!", bg = bg, fg = "#b598a1",font = ("Dubai", Size+12), padx = 100, pady = 100, relief= relief, bd = 1 )
                State_Info.pack(anchor = "nw", expand = True, fill = "both", padx = 20, pady = (10,0) )
                Active_step[1] = 0
                End = "Yes"           
                lock.release()
                break
                
            elif Finish == 1 and Active_step[1] ==8 :
                global RMS_plotII
                btnII_3.config(Dis_but)
                ##Active Region6
                for i in [btnII_7, btnII_8, btnII_5]:
                    i.config(Act_but)
                BackF =  Active_step[1]
                #ShowImage od Preview window
                X_Label = [Bin_LstII[i] if i%4 == 0 else 0 for i in range(0, len(Bin_LstII))]
                fig = plt.figure(figsize=(5,4))
                plt.title("RMS plot of Outpupoints")
                #plt.plot(RMS_value["m"], RMS_value["RMS"], color = "dodgerblue", marker = "o", label = "RMS" )
                plt.plot(RMS_valueII["m"], RMS_valueII["RMS"], color = "dodgerblue", marker = "o", label = "RMS" )
                ax = plt.gca()
                #x_major_locator = MultipleLocator(100)
                ax.xaxis.set_major_locator(MultipleLocator(100))
                plt.xlabel("Measurement Length ("+UnitII.get()+")")
                plt.ylabel("RMS Error("+UnitII.get()+")")
                plt.xticks( X_Label , fontsize = 10)
                plt.xlim(0, BLII)
                plt.ylim(0, float(RMS_limitII.get()))
                plt.legend()
                RMS_plotII = fig                
                ##Prepare Main window for Treeview for RMS
                MainW_tv2 = tk.LabelFrame(Prev_frame1, text = "Root Mean Square(RMS) value", fg = "#d0dfe6", font = (Font_W, Size), bg = bg )
                MainW_tv2.pack(anchor = "nw", expand = True, fill = "both",pady = 10, padx = 10, side = "right")
                # Treeview start
                tv2 = ttk.Treeview(MainW_tv2, style="mystyle1.Treeview", height= 10)
                tv2.pack(anchor = "nw", side= "left", expand = True, fill = "both", padx=5)
                #Add scrolly of y direction
                tv2scrolly = tk.Scrollbar(MainW_tv2, orient= "vertical", command= tv2.yview)
                tv2.configure(yscrollcommand= tv2scrolly.set)
                tv2scrolly.pack(side= "right", fill = "y", padx = (2,5))
                # Format of column
                tv2["columns"] = ["m", "RMS"]
                tv2.column("#0", stretch = False, width = 35, minwidth = 30)
                tv2.column("m", width = 35, minwidth = 20, anchor = "center")
                tv2.column("RMS", width = 35, minwidth = 20, anchor = "center")
                # Heading of column
                tv2.heading("#0", text = "Bin", anchor = "center")
                tv2.heading("m", text = "length(m)", anchor = "center")
                tv2.heading("RMS", text = "RMS", anchor = "center")            
                for index, row in RMS_valueII.iterrows():
                    tv2.insert(parent="", index = "end", iid = index, text= int(index),  values = [round(i, 3) for i in list(row)])
                    
            elif Finish == 1 and Active_step[1] == 9:
                for i in [btnII_6,btnII_7, btnII_8, btnII_9, btnII_10]:
                    i.config(Act_but)
                btnII_4.config(Dis_but)
                BackF =  Active_step[1]
                fig = DFmapII                          
            canvas_prew = FigureCanvasTkAgg(fig, master = Prev_frame1)
            canvas_prew.draw()
            canvas_prew.get_tk_widget().pack(side = "top", fill = "x", expand = True, padx = 20)
            #Control panel
            lock.release()
            Active_step[1] = 0
            End = "Yes"           
           # Prev_Win.after_cancel(RefreshII)#取消循環事件
        except:
            break
    if End == "No":
        Timer = Prev_Win.after(500, RefreshII)
    elif End == "Yes":
        Prev_Win.after_cancel(Timer)
                   
def saveResullt(Items):
    for Item in Items:
        if type(eval(Item)) == pyelastix.Image:
            FileName = filedialog.asksaveasfilename(initialdir = Item, title = f"Save the {Item}", filetypes =[("tiff files","*.tiff"), ("All Files", " *")], defaultextension = ".tiff")
            io.imsave(FileName, eval(Item))
        elif str(type(eval(Item))) == "<class 'pandas.core.frame.DataFrame'>":
            FileName = filedialog.asksaveasfilename(initialdir = Item, title = f"Save the {Item}", filetypes =[("csv file(*.csv)","*.csv"),("All Files", " *")], defaultextension = ".csv")
            eval(Item).to_csv(FileName, sep = "," ,index = True, header = True, encoding = "utf-8_sig")
        
        elif str(type(eval(Item))) == "<class 'matplotlib.figure.Figure'>":
            FileName = filedialog.asksaveasfilename(initialdir = Item, title = f"Save the {Item}", filetypes =[("tiff files","*.tiff"), ("All Files", " *")], defaultextension = ".tiff")
            eval(Item).savefig(FileName, dpi=300)
        elif str(type(eval(Item))) =="<class 'numpy.ndarray'>" and Item != "Skeleton_Img":
            FileName = filedialog.asksaveasfilename(initialdir = Item, title = f"Save the {Item}", filetypes =[("csv file(*.csv)","*.csv"),("All Files", " *")], defaultextension = ".csv")
            eval(Item).tofile('FileName', sep = ',')
        else:
            FileName = filedialog.asksaveasfilename(initialdir = Item, title = f"Save the {Item}", filetypes =[("tiff files","*.tiff"), ("All Files", " *")], defaultextension = ".tiff")
            io.imsave(FileName, eval(Item))

def Summary(As):   
    if As == 4 :        
# Show the results of Registation
        global Sum
        Sum = plt.figure(1);
        plt.clf()
        plt.subplot(241); plt.imshow(Pre_Img); plt.title("Pre",{"fontsize":8}); plt.tick_params( axis = "both", bottom = False, top = False, labelbottom = False, left = False, labelleft = False )
        plt.subplot(242); plt.imshow(Post_Img); plt.title("Post",{"fontsize":8}); plt.tick_params( axis = "both", bottom = False, top = False, labelbottom = False, left = False, labelleft = False )
        plt.subplot(243); plt.imshow(Reg1st); plt.title("Reg1st",{"fontsize":8}); plt.tick_params( axis = "both", bottom = False, top = False, labelbottom = False, left = False, labelleft = False )
        plt.subplot(244); plt.imshow(Reg2nd); plt.title("Reg2nd",{"fontsize":8}); plt.tick_params( axis = "both", bottom = False, top = False, labelbottom = False, left = False, labelleft = False )
        plt.subplot(245); plt.imshow(field[0]); plt.title("X_offset",{"fontsize":8})
        plt.subplot(246); plt.imshow(field[1]);plt.title("Y_offset",{"fontsize":8});
        plt.colorbar()
         
def GoBack2(AS, AcItem, ExceItem):
    global Active_step
    Current_F = "".join(["frame", str(AS)])
    Prev_F = "".join(["frame", str(AS-1)])
    for widgets in eval(Prev_F).winfo_children():
        Temp_class = widgets.winfo_class()
        if Temp_class == "Botton":
            widgets.config(state = "normal", fg = Color_ButNor, bg = bg)
            continue
        elif Temp_class == "Checkbotton":
            widgets.config(state = "normal")
        elif Temp_class == "Frame":
            for C_widgets in widgets.winfo_children():
                if C_widgets.winfo_class() == "Button":
                    if C_widgets.cget("text") not in AcItem :
                        C_widgets.config(Act_but)
                elif C_widgets.winfo_class() == "Entry":
                    C_widgets.configure(Act_Entry)
                elif C_widgets.winfo_class() in ["Radiobutton", "TCombobox","Checkbutton"]:
                    C_widgets.config(state = "normal")
        else :
            widgets.config(state = "normal", bg = bg)
    for widgets in eval(Current_F).winfo_children():
        Temp_class = widgets.winfo_class()
        if Temp_class == "Button" and widgets.cget("text") not in ExceItem:
            widgets.config(state = "disable", bg = Color_ButDis)
        elif Temp_class == "Frame":
            for C_widgets in widgets.winfo_children():
                if C_widgets.winfo_class() == "Button":
                    if C_widgets.cget("text") not in ExceItem:
                        C_widgets.config(Dis_but)
                elif C_widgets.winfo_class() == "Entry":
                    C_widgets.configure(Dis_Entry)
                elif C_widgets.winfo_class() in ["Radiobutton", "TCombobox","Checkbutton"]:
                   C_widgets.configure(state = "disable")           
        elif Temp_class == "Checkbotton":
            widgets.configure(state = "disable")
            widgets.deselect()
            
    if AS ==3:
        btn1.config(bg = "white", fg = "black")
        btn2.config(bg = "white", fg = "black")
        CheckGau.deselect()
        VarGau.set(0)
        enable(VarGau, frame2_1)

    if AS == 4:
        CheckClear.deselect()
        Pre_GF_In.config(Dis_Entry)
        Post_GF_In.config(Dis_Entry)
    if AS == 5:       
        btn13.config(bg = "white", fg = "gray")
        CheckScale.deselect()
        
    Active_step[0] = AS-1
   
def GobackII():
    global BackF
    if BackF == 7:
        for i in [btnII_3, btnII_4]:
            i.config(Dis_but)
        for j in [Bin_width_InII, Total_binL_InII, RMS_limit_InII]:
            j.config(Dis_Entry)
        #Widget in Step1
        for k in [btnII_1, btnII_2]:
            k.config(Act_but)    
        CheckScale2.config(state = "normal")
        Sampling_InII.config(Act_Entry)
    elif BackF == 8:
        for i in [btnII_6, btnII_7, btnII_8, btnII_10]:
            i.config(Dis_but)
        for j in [Bin_width_InII, Total_binL_InII, RMS_limit_InII]:
            j.config(Act_Entry)
        btnII_4.config(Act_but)
        btnII_5.config(Act_but)
        btnII_3.config(Act_but)
    BackF = BackF-1
          
                    
def MaskCreate(Var):
    if Var.get() == 1:
        global Mask
        global A
        global Paper_Mask
        Mask = np.zeros(Post_Img.shape)
        Mask[:,:] = 1
    #Extract Similarity Regestration factor(Scale, Rotation(radian), X_offset, Y_offset)
        Scale, Rotate, X, Y = Info[1:]
        A = [Scale, Rotate, X, Y]
        Y = Y.replace(")","")
        
        SFT = np.float32([[1,0,-float(X)],[0,1,-float(Y)],[0,0,1]])
        ROT = cv2.getRotationMatrix2D(center = (Mask.shape[0]/2, Mask.shape[1]/2), angle = np.rad2deg(float(Rotate)), scale =1/float(Scale))
        ROT = np.vstack([ROT,[0,0,1]])
        TransformMatrix = np.matmul(SFT, ROT)
        Mask = cv2.warpPerspective(Mask, TransformMatrix, (Mask.shape[1], Mask.shape[0]),flags=cv2.INTER_LANCZOS4)
        btn12.config(state = "normal", fg = Color_ButNor, bg = bg)   
    elif Var.get() == 0:
        btn12.config(state = "disable", bg = Color_ButDis, fg = "#cdd1d3")

def Seperator(Location, i):
     s = ttk.Style()
     s.configure('1.TSeparator', background = "#495c69" )
     Sep1 = Separator(Location, orient = "horizontal", style = '1.TSeparator' )
     #Sep1.pack(fill = "x", padx = 5)   
     Sep1.grid(row = i, column = 0, sticky = "EW", padx = (4,2))

def Seperator2(Location):
     s = ttk.Style()
     s.configure('1.TSeparator', background = "#495c69" )
     Sep1 = Separator(Location, orient = "horizontal", style = '1.TSeparator' )
     #Sep1.pack(fill = "x", padx = 5)   
     Sep1.pack(anchor = "nw", padx = (4,2), fill = "x", expand = False)
            
def enable_skele():    
    if VarSkele.get() == 1:
        btn13["state"] = "normal"
        
    elif VarSkele.get() == 0:
        btn13["state"] = "disable"

def on_configure(event):
    # update scrollregion after starting 'mainloop'
    # when all widgets are in canvas
    canvas.configure(scrollregion=canvas.bbox('all'))

def on_configure2(event):
    # update scrollregion after starting 'mainloop'
    # when all widgets are in canvas
    canvas2.configure(scrollregion=canvas2.bbox('all'))

def size(event):
    canvas2 =event.widget
    canvas2.itemconfigure("Full_view2", width = frame1.winfo_width())
    #canvas2.itemconfigure("Full_view2", width = event.width-5)
    canvas2.configure(scrollregion=canvas2.bbox("all"))

def catch_maximize(event):
    global i
    i=0
    def dragging(event):
        global i
        ww = root.winfo_width()
        wh = root.winfo_height()
        left = root.winfo_x()
        top = root.winfo_y()
        root.geometry(f'{ww}x{wh}')
        root.unbind('<Configure>')
      
    root.bind('<Configure>', dragging)
    # root.maxsize(frame6.winfo_width()+20, 5*wh)
    # print(f'{ww}x{wh}+{left}+{top}')
    
    
def exit():
    def AutoSave():
        for i, element in enumerate([var1, Save1, Save2, Save3, Save4, Save5, Save6, Save7, Save8]):
            if  element.get() == 1 and i in [0,1,2]:
                #print(SavePath[i], DataLst[i])
                io.imsave(SavePath[i], eval(DataLst[i]))
            elif element.get() == 1 and i in [3,4,7,8] :
                eval(DataLst[i]).savefig(SavePath[i], dpi=300)
            elif element.get() == 1 and i in [5,6]:
                eval(DataLst[i]).to_csv(SavePath[i], sep = "," ,index = True, header = True, encoding = "utf-8_sig")
                
        Exit_Win.destroy()
        #Prev_Win.destroy()
        root.destroy()
    def Cancel():
        Exit_Win.destroy()
    ###Prepare Paths for saving Data
    #Parent = os.path.dirname(Path_Pre_ExM)
    DataLst = ["Reg1st", "Reg2nd", "Skeleton_Img", "DFmap", "RMS_plot", "RMS_value", "RMS_valueII", "RMS_plotII", "DFmapII"]
    SaveLst = [ i for i in DataLst if i in globals()]
    SaveExten = [".tiff", ".tiff", ".tiff", ".tiff",".tiff", ".csv", ".csv", ".tiff", ".tiff"]
    Parent = ["",""]
    try:
        Parent[0] = os.path.dirname(Path_Pre_ExM)
    except:
        Parent[0] = ""
    try:
        Parent[1] = os.path.dirname(Transformix_out)
    except:
        Parent[1] = ""

    #SavePath = [os.path.join(Parent, DataLst[i]+SaveExten[i] ) if DataLst[i] in SaveLst else "" for i in range(0,9)]
    SavePath = []
    for i in range(0,9):
        if DataLst[i] in SaveLst:
            if i < 6:
                Temp_path = os.path.join(Parent[0], DataLst[i]+SaveExten[i])
                SavePath += [os.path.normpath(Temp_path)]
            elif i > 5:
                Temp_path = os.path.join(Parent[1], DataLst[i]+SaveExten[i])
                SavePath += [os.path.normpath(Temp_path)]
        else:
          SavePath +=[""]  
                

    Exit_Win = tk.Toplevel()
    var1 = tk.IntVar(master = Exit_Win)
    Save1, Save2, Save3, Save4, Save5, Save6, Save7, Save8 = tk.IntVar(master = Exit_Win), tk.IntVar(master = Exit_Win), tk.IntVar(master = Exit_Win), tk.IntVar(master = Exit_Win), tk.IntVar(master = Exit_Win), tk.IntVar(master = Exit_Win), tk.IntVar(master = Exit_Win), tk.IntVar(master = Exit_Win)
    Exit_Win.title("Save Documents before leaving")
    Exit_Win.config(bg = bg)
    frame_Exit1 = tk.Frame(Exit_Win, bg = bg, relief = relief)
    frame_Exit2 = tk.Frame(Exit_Win, bg = bg, relief = relief)
    
    Seperator = ttk.Style()
    Seperator.configure('1.TSeparator', background = "#495c69" )
    Sep1 = Separator(frame_Exit1, orient = "horizontal", style = '1.TSeparator' )
    Sep2 = Separator(frame_Exit2, orient = "horizontal", style = '1.TSeparator' )
    
    Name = tk.Label(frame_Exit1, text = "Name", bg = bg, font = (Font_W, Size), fg = "#51c4d3")
    SaveReg1st = tk.Checkbutton(frame_Exit1, text = "Reg1st", justify = "left", bg = bg, font = (Font_W, Size-1), fg = "#cdd1d3", state = "disable", variable= var1, onvalue="1", offvalue="0")
    SaveReg2nd = tk.Checkbutton(frame_Exit1, text = "Reg2nd", variable = Save1, onvalue = 1, offvalue = 0, justify = "left", bg = bg, font = (Font_W, Size-1), fg = "#cdd1d3", state = "disable" )
    SaveSkeleton_Img = tk.Checkbutton(frame_Exit1, text = "Skeleton_Img", variable = Save2, onvalue = 1, offvalue = 0, justify = "left", bg = bg, font = (Font_W, Size-1), fg = "#cdd1d3", state = "disable" )
    SaveDFmap = tk.Checkbutton(frame_Exit1, text = "Deformation Map", variable = Save3, onvalue = 1, offvalue = 0, justify = "left", bg = bg, font = (Font_W, Size-1), fg = "#cdd1d3", state = "disable" )
    SaveRMS_plot = tk.Checkbutton(frame_Exit1, text = "RMS_plot", variable = Save4, onvalue = 1, offvalue = 0, justify = "left", bg = bg, font = (Font_W, Size-1), fg = "#cdd1d3", state = "disable" )
    SaveRMS_value = tk.Checkbutton(frame_Exit1, text = "RMS_value", variable = Save5, onvalue = 1, offvalue = 0, justify = "left", bg = bg, font = (Font_W, Size-1), fg = "#cdd1d3", state = "disable" )
    SaveRMS_valueII = tk.Checkbutton(frame_Exit1, text = "RMS_value from Transformix output", variable = Save6, onvalue = 1, offvalue = 0, justify = "left", bg = bg, font = (Font_W, Size-1), fg = "#cdd1d3", state = "disable" )
    SaveRMS_plotII = tk.Checkbutton(frame_Exit1, text = "RMS_plot from Transformix output", variable = Save7, onvalue = 1, offvalue = 0, justify = "left", bg = bg, font = (Font_W, Size-1), fg = "#cdd1d3", state = "disable" )
    SaveDFmapII = tk.Checkbutton(frame_Exit1, text = "Deformation Map from Transformix output", variable = Save8, onvalue = 1, offvalue = 0, justify = "left", bg = bg, font = (Font_W, Size-1), fg = "#cdd1d3", state = "disable" )
    DType = tk.Label(frame_Exit2, text = "Type                 Path", bg = bg, font = (Font_W, Size), fg = "#51c4d3")
    TReg1st = tk.Label(frame_Exit2, text = f"Image               {SavePath[0]}", bg = bg, font = (Font_W, Size-1), fg = "gray")
    TReg2nd = tk.Label(frame_Exit2, text = f"Image               {SavePath[1]}", bg = bg, font = (Font_W, Size-1), fg = "gray")
    TSkeleton_Img = tk.Label(frame_Exit2, text = f"Image               {SavePath[2]}", bg = bg, font = (Font_W, Size-1), fg = "gray")
    TDFmap = tk.Label(frame_Exit2, text = f"Image               {SavePath[3]}", bg = bg, font = (Font_W, Size-1), fg = "gray")
    TRMS_plot = tk.Label(frame_Exit2, text = f"Image               {SavePath[4]}", bg = bg, font = (Font_W, Size-1), fg = "gray")
    TRMS_value = tk.Label(frame_Exit2, text = f"Table               {SavePath[5]}", bg = bg, font = (Font_W, Size-1), fg = "gray")
    TRMS_valueII = tk.Label(frame_Exit2, text = f"Table        {SavePath[6]}", bg = bg, font = (Font_W, Size-1), fg = "gray")
    TRMS_plotII = tk.Label(frame_Exit2, text = f"Table        {SavePath[7]}", bg = bg, font = (Font_W, Size-1), fg = "gray")
    TDFmapII = tk.Label(frame_Exit2, text = f"Image          {SavePath[8]}", bg = bg, font = (Font_W, Size-1), fg = "gray")
    for i in SaveLst:
        eval(f"Save{i}").config(state = "normal")
        eval(f"T{i}").config(fg = "#cdd1d3")
               
    Final_Exit = tk.Button(Exit_Win, Act_but, text = "     OK     ", command = AutoSave)
    Final_Cancel = tk.Button(Exit_Win, Act_but, text = "  Cancel  ", command = Cancel)    
    Name.pack(anchor = "nw", padx = (10,0), pady = (5,1))
    Sep1.pack(anchor = "nw", padx = (10,0), expand = 1, fill = "x")      
    SaveReg1st.pack(anchor = "nw", padx = (10,0), pady = (5,1))
    SaveReg2nd.pack(anchor = "nw", padx = (10,0), pady = 1)
    SaveSkeleton_Img.pack(anchor = "nw", padx = (10,0), pady = 1)
    SaveDFmap.pack(anchor = "nw", padx = (10,0), pady = 1)
    SaveRMS_plot.pack(anchor = "nw", padx = (10,0), pady = 1)
    SaveRMS_value.pack(anchor = "nw", padx = (10,0), pady = 1)
    SaveRMS_valueII.pack(anchor = "nw", padx = (10,0), pady = 1)
    SaveRMS_plotII.pack(anchor = "nw", padx = (10,0), pady = 1)
    SaveDFmapII.pack(anchor = "nw", padx = (10,0), pady = 1)
    DType.pack(anchor = "sw", padx = 10, pady = (5,1))
    Sep2.pack(anchor = "nw", padx = (0,0), expand = 1, fill = "x")  
    TReg1st.pack(anchor = "sw", padx = 10, pady = (7,3))
    TReg2nd.pack(anchor = "sw", padx = 10, pady = 3)
    TSkeleton_Img.pack(anchor = "sw", padx = 10, pady = 3)
    TDFmap.pack(anchor = "sw", padx = 10, pady = 3)
    TRMS_plot.pack(anchor = "sw", padx = 10, pady = 3)
    TRMS_value.pack(anchor = "sw", padx = 10, pady = 3)
    TRMS_valueII.pack(anchor = "sw", padx = 10, pady = 3)
    TRMS_plotII.pack(anchor = "sw", padx = 10, pady = 3)
    TDFmapII.pack(anchor = "sw", padx = 10, pady = 3)
    
    frame_Exit1.pack(anchor = "nw", padx = (20,0), side = "left")
    frame_Exit2.pack(anchor = "nw", padx = (0,20))
    Final_Cancel.pack(anchor = "nw", side = "right", padx = (5,15), pady = 10)
    Final_Exit.pack(anchor = "nw", side = "right", padx = (15,5), pady = 10)
    
    
             
#Style of whole window
bg = "#1c2938"
Color_ButNor = "#cdd1d3"
Color_ButDis = "#2b333e"
Font_W, Size = "Arial", 12 
Act_but = {'bg': bg, 'fg': Color_ButNor, 'state': "normal", "relief": "raised"}
Dis_but = {'bg':Color_ButDis, 'fg':"#cdd1d3", 'state':"disabled", 'disabledforeground': "gray", "relief": "raised"}
Act_Entry = {'fg':"#a7a8bd", 'bg':"#142334", 'relief':"groove", 'state':"normal", "font":(Font_W, Size-1), "width": 5}
Dis_Entry ={'font': (Font_W, Size-1), 'bg': bg, "width":5, 'fg':"#5e616d", 'state':"disable", 'disabledbackground': bg, 'relief':"groove"}
#Busy_btn = {'bg':"#a5a7a8", 'disabledforeground': "#2d2e36", 'state':"disabled", "relief": "sunken"}
Busy_btn = {'bg':"#a5a7a8", 'disabledforeground': bg, 'state':"disabled", "relief": "sunken"}
Info = ["NA", "N/A","N/A","N/A","N/A"]
#matplotlib.use('Agg')
Active_step = [1,0]

#Prepare the elastix(Add the new Path to environment variable )
Elastix_Env = os.path.dirname(__file__)
Elastix_Env = os.path.join(Elastix_Env, "Elastix")
Current_Env = os.environ.get("Path").split(";")
if Elastix_Env not in Current_Env:
    Current_Env.append(Elastix_Env)
    Current_Env= ";".join(Current_Env)
    os.environ["Path"] = Current_Env

#Start Main window
root = tk.Tk()
root.title("RMS analysis")

W = root.winfo_screenwidth()
H = root.winfo_screenheight()
ww = int(0.1*W)
wh = int(0.1*H)
left = int((W-int(0.1*W))/2)
top = int((H-int(0.1*H))/2)
normalW = 2560
normalH = 1440
scaleW  = W/normalW
scaleH = H/normalH
SF = (scaleW + scaleH)/2
if SF < 0.916:
    SF = 0.916
#root.geometry(f'{ww}x{wh}+{left}+{top}')
root.config(bg = bg)
notebook = ttk.Notebook(root)

#scrollbar = tk.Scrollbar(canvas, orient="vertical", command=canvas.yview, bg = bg)
#scrollbar.pack(side = "left", fill = "y", anchor = "nw")

vcmd_Int = (root.register(lambda Num: Validate2(Num, [int])), "%P")
vcmd_float_Int = (root.register(lambda Num: Validate2(Num, [int, float])), '%P')



#Preview window
Font_W, Size, relief = "Arial", int(12*SF), "groove"
Prev_Win = tk.Toplevel(root)
Prev_Win.title("Show Image")
Prev_Win.config(bg = bg)
Prev_frame1 = tk.Frame(Prev_Win, bg = bg, relief = relief)
Prev_Lframe1_1 = tk.LabelFrame(Prev_Win, text=" Analysis result ", font = (Font_W, Size), fg = "#d0dfe6", bg = bg)
Prev_Lframe2 = tk.LabelFrame(Prev_Win, text=" About the writer ", font = (Font_W, Size), fg = "#d0dfe6", bg = bg)

Massage1= tk.Label(Prev_frame1, text = "Show Image here! ", fg = "#b598a1",font = ("Dubai", Size+8), bg = bg, padx = 100, pady = 100, relief= relief, bd = 1)
Massage1.pack(anchor= "center", padx =30, pady = 25, expand = True, fill = "x")
tv_type = tk.Label(Prev_Lframe1_1, text = "Similarity Transform Parameter", fg = "#b598a1", font = (Font_W, Size), bg = bg )
tv_type.pack(anchor = "nw")
Massage2 = tk.Label(Prev_Lframe2, text = "An-Chi Luo \n-- Imaging Core, College of Medicine, National Taiwan University, Taipei, Taiwan", fg = "#b598a1", font = (Font_W, Size), bg = bg, justify="left")
Massage2.pack(anchor = "nw", expand = True)

#For treeview in "Analysis result"
MainW_tv = tk.Frame(Prev_Lframe1_1, bg = bg)
MainW_tv.pack(anchor = "nw", padx = 10, pady = (1,5), expand = True, fill = "x",side = "top")
Style_tv = ttk.Style()
Style_tv.theme_use('clam')
Style_tv.configure("mystyle1.Treeview", background= bg, foreground = "white", relief = "groove", fieldbackground = bg)
Style_tv.configure("mystyle1.Treeview.Heading", font=(Font_W, Size), foreground="white", background="#4C5461", relief = "flat", width = -1) #
Style_tvF = ttk.Style()
Style_tvF.theme_use('clam')
Style_tvF.configure("mystyle2.Treeview", background= bg, foreground = "#51c4d3", relief = "flat", fieldbackground = bg, Font = (Font_W, Size-2), lightcolor= bg, bordercolor= bg, borderwidth = 0)
Style_tvF.configure("mystyle2.Treeview.Heading", foreground="white", background="#4C5461", relief = "flat", Font = (Font_W, Size-2), padding = [0,2,0,2])
Style_bar = ttk.Style()
Style_bar.theme_use('clam')
Style_bar.configure("mystytle3.Horizontal.TScrollbar", gripcount=0, background="#2C4158", darkcolor=bg, lightcolor="#2C4158", troughcolor= bg, bordercolor= bg , arrowcolor="#c4cbcf", relief = 'flat')
Style_bar.map("mystytle3.Horizontal.TScrollbar", background= [("pressed", "#1B5798")] )

tv1 = ttk.Treeview(MainW_tv, style="mystyle1.Treeview",height=1)
tv1.pack(anchor = "nw", side= "top", expand = True, fill = "x")
#tv1.place(relheight=1, relwidth=1)
# #tvscrolly = tk.Scrollbar(MainW_tv, orient= "vertical", command= tv1.yview)
# tvscrollx = tk.Scrollbar(MainW_tv, orient= "horizontal", command= tv1.xview)
# tv1.configure(xscrollcommand= tvscrollx.set)#,yscrollcommand= tvscrolly.set)
# tvscrollx.pack(anchor = "nw", side= "bottom", fill = "x")
# # tvscrolly.pack(side= "right", fill = "y")


# Format of column
tv1["columns"] = ["Scaling", "Rotation", "deltaX", "deltaY"]
tv1['show']='headings'
tv1.column("Scaling", width = 80, minwidth = 70, anchor = "center")
tv1.column("Rotation", width = 80, minwidth = 70, anchor = "center")
tv1.column("deltaX", width = 80, minwidth = 70, anchor = "center")
tv1.column("deltaY", width = 80, minwidth = 70, anchor = "center")
#Creat Heading
tv1.heading("Scaling", text = "Scaling factor", anchor = "center")
tv1.heading("Rotation", text = "Rotation angle", anchor = "center")
tv1.heading("deltaX", text = "Tranlation in X", anchor = "center")
tv1.heading("deltaY", text = "Tranlation in Y", anchor = "center")
#Add Data
tv1.insert(parent="", index = "end", iid = 0, values=Info[1:])

Prev_frame1.pack(anchor = "nw", expand = True, fill = "both")
Prev_Lframe1_1.pack(anchor = "nw", padx = 20, pady = 10, expand = True, fill = "x",side = "top")
Prev_Lframe2.pack(anchor = "nw", padx = 20, pady = 10, expand = True, fill = "x",side = "top")

#Step1 region
canvas = tk.Canvas(root, bg = bg)
canvas.pack(anchor = "nw", side = "left", fill="both",expand=True)
canvas.bind('<Configure>', on_configure)
Full_view = tk.Frame(canvas, bg= bg )
canvas.create_window((0,0), window = Full_view, anchor='nw')
##卷軸區

scrollbar = tk.Scrollbar(canvas, orient="vertical", command=canvas.yview, bg = bg)
scrollbar.pack(anchor = "ne", side="right", fill = "y", expand = True )
canvas.configure(yscrollcommand = scrollbar.set)

notebook.add(canvas, text = "Start with Image model")



#Full_view.pack(anchor = "nw",expand = True, fill = "both",side = "left")
frame1 = tk.Frame(Full_view, bg = bg)
frame1.grid(row = 0, column = 0, sticky= tk.W)
frame1_1 =  tk.Frame(frame1, bg = bg)
#Step_Label1 = tk.Label(frame1, text = "Step1. Loading Images", font = (Font, Size), fg = "#66c18c", bg = bg)
Step_Label1 = tk.Label(frame1,font = (Font_W, Size), fg = "#66c18c", bg = bg, text = "Step1. Import Data")


Pre_label = tk.Label(frame1_1, text= "Select Pre-ExM image", font = (Font_W, Size), fg = "#3EEDE7", bg = bg)
btn1 = tk.Button(frame1_1, text = "Browse", command = browseFiles_Pre)
Post_label = tk.Label(frame1_1, text = "Select Post_ExM_img", font = (Font_W, Size), fg="#51c4d3" ,bg = bg)
btn2 = tk.Button(frame1_1, text = "Browse", command = browseFiles_Post )
#Perpare table for showing Data loading
MainW_tvF = tk.Frame(frame1, bg = bg)
tvFScroll = ttk.Scrollbar(MainW_tvF, orient= "horizontal")
#Title for Image type & path
tv_heading = ttk.Treeview(MainW_tvF, style= "mystyle2.Treeview",height=0, column = ["Image type"], show = "headings")
tv_heading.column("Image type", width = 80, minwidth= 80, stretch = False, anchor = "e")
tv_heading.heading("Image type", text =  "Image type", anchor = "center")
tv_heading.grid(row =0, column = 0, sticky = "NWS")

tv_heading1 = ttk.Treeview(MainW_tvF, style= "mystyle2.Treeview",height=2, column = ["Type"], show = "")
tv_heading1.column("Type", width = 80, minwidth= 80, stretch = False, anchor = "e")
tv_heading1.heading("Type", text =  "Image type", anchor = "center")
tv_heading1.insert(parent="", index = "end", iid = 0, values = ("Pre_ExM : ",))
tv_heading1.insert(parent="", index = "end", iid = 1, values = ("Post_ExM : ",))
tv_heading1.grid(row =1, column = 0, sticky = "NWS")

tv_heading2 = ttk.Treeview(MainW_tvF, style= "mystyle2.Treeview",height=0, column = ["Path"], show = "headings")
tv_heading2.column("Path", width = 80, minwidth= 80, stretch = True, anchor = "e")
tv_heading2.heading("Path", text =  "Path", anchor = "center")
tv_heading2.grid(row =0, column = 1, sticky = "EW")

tv_file = ttk.Treeview(MainW_tvF, style="mystyle2.Treeview",height=2, column = ["Path"], xscrollcommand= tvFScroll.set, show = "")
#Set column&heading
tv_file.column("#0", width = 80, minwidth = 80,stretch = False, anchor = "e")
tv_file.column("Path", width = 40, anchor = "w")
tv_file.heading("#0", text =  "Image type", anchor = "center")
tv_file.heading("Path", text =  "File Path", anchor = "center")
tv_file.update()
#Insert row
tv_file.insert(parent="", index = "end", iid = 0, text = "Pre_ExM  : ", values = "", tags = ("realPath",))
tv_file.insert(parent="", index = "end", iid = 1, text = "Post_ExM : ", values = "", tags = ("realPath",))

# tvFscrollx = tk.Scrollbar(MainW_tvF, orient= "horizontal", command= tv_file.xview)
tvFScroll.configure(command= tv_file.xview, style = "mystytle3.Horizontal.TScrollbar")

# tv_file.configure(xscrollcommand= tvFscrollx.set)


# Open_Label1 = tk.Label(frame1, text ="#File Opened", font = (Font, Size-2), fg = "#2983bb", bg = bg)
# Open_Label2 = tk.Label(frame1, text = "#File Opened", font = (Font, Size-2), fg ="#2983bb",bg = bg)
btn3 = tk.Button(frame1, Dis_but, text = "Preview", command = Preview)
btn4 = tk.Button(frame1, Dis_but, text = "Go next", command = checkDimension2)

Step_Label1.pack(anchor = "nw")
frame1_1.pack(anchor = "nw", padx = (0,2.5))


Pre_label.pack(anchor = "nw", side = "left", padx = (50, 5), pady = 2.5)
btn1.pack(anchor = "w", side = "left", padx = (0, 40), pady = 2.5)
Post_label.pack(anchor = "nw", side = "left", padx = (15, 5), pady =2.5)
btn2.pack(anchor = "w", padx = (0, 13), pady = 2.5)
MainW_tvF.pack(anchor = "nw", padx = (20,15), expand= True, fill = "both")
MainW_tvF.columnconfigure(1,weight = 1)

tv_file.grid(row =1, column = 1, sticky = "EW")
tvFScroll.grid(row = 2, column = 0, columnspan = 2,  sticky = "EW", pady=(0,0))
# tv_file.pack(anchor = "nw", side= "top", expand = True, fill = "x", padx= 20 )
# tvFScroll.pack(expand= True, fill = "x", padx = 20, side = "bottom")
# tvFscrollx.pack(anchor = "nw", side= "bottom", fill = "x")
# Open_Label1.pack(anchor= "nw", padx = 75,pady =(2.5, 0))
# Open_Label2.pack(anchor = "nw", padx = 75)
btn4.pack(anchor = "nw", side = "right", padx = (5, 10), pady = 5)
btn3.pack(anchor = "nw", side = "right", padx = (0, 0), pady = 5)

Seperator(Full_view, 1)

#Step2 region
NR_para = [4, 5, 800]
frame2 = tk.Frame(Full_view, bg = bg)
frame2.grid(row = 2, column = 0, sticky = "NSEW")

frame2_1 = tk.Frame(frame2, bg = bg)
frame2_2 = tk.Frame(frame2, bg = bg)
frame2_3 = tk.Frame(frame2, bg =bg)
frame2_4 = tk.Frame(frame2, bg = bg)
#frame2_5 = tk.LabelFrame(frame2, text = " Current status ", font = ("Arial",11), fg = "gray", bd = 1)
#rame2_5.config(bg = bg)

Pre_GF, Post_GF = tk.IntVar(root), tk.IntVar(root)
Pre_GF.set(0)
Post_GF.set(0)

NR_Res, NR_Length, NR_Iterations = tk.IntVar(root), tk.IntVar(root), tk.IntVar(root)
NR_Res.set(NR_para[0])
NR_Length.set(NR_para[1])
NR_Iterations.set(NR_para[2])

Step_Label2 = tk.Label(frame2, text = "Step2. Similarity Registration", font = (Font_W, Size), fg = "#66c18c", bg = bg)
VarGau = tk.IntVar(root)
CheckGau = tk.Checkbutton(frame2, text = "Smooth", justify = "left", bg = bg, font = ("Arial",Size-1), fg = "#51c4d3", command = lambda: enable(VarGau, frame2_1), state = "disable" )
CheckGau.configure(variable = VarGau, onvalue = 1, offvalue = 0)
CheckGau.deselect()
Step_Label2_1 = tk.Label(frame2_1, text = "Input the radius(pix)", font=("Arial", Size-1),fg = "#2b333e", bg = bg)
Step_Label2_2 = tk.Label(frame2_1, text = "Pre_ExM Image: ", font = ("Arial", Size-1), fg = "#2b333e", bg = bg)

#vcmd = (frame2_1.register(Validate, '%P'))
Pre_GF_In = tk.Entry(frame2_1, Dis_Entry, validate = "key", validatecommand = vcmd_Int, textvariable = Pre_GF)
Step_Label2_3 = tk.Label(frame2_1, text = "Post_ExM Image: ", font = ("Arial", Size-1), fg = "#2b333e", bg = bg)
Post_GF_In = tk.Entry(frame2_1, Dis_Entry, validate = "key", validatecommand = vcmd_Int, textvariable = Post_GF)
btn5 = tk.Button(frame2_1, Dis_but, text = "Preview", command = Preview)

Step_Label2.pack(anchor="nw")
CheckGau.pack( padx =50, anchor = "nw")
Step_Label2_1.pack(padx = 75, anchor = "nw" )
Step_Label2_2.pack(padx = (75,3), side= "left", pady = 2.5)
Pre_GF_In.pack(side = "left", anchor = "w", pady = 2.5)
Step_Label2_3.pack(padx = (30,3), pady = 5, side = "left")
Post_GF_In.pack(pady = 2.5, side= "left", anchor = "w" )
btn5.pack(pady = 2.5,padx = (25,10), side="right", anchor = "w")
frame2_1.pack(anchor = "nw")

Step_Label2_4 = tk.Label(frame2, text = "Parameter setting", bg = bg, font = ("Arial",Size), fg = "#51c4d3")
Step_Label2_5 = tk.Label(frame2_2, text = "Number Of Resolutions: ", bg = bg, font = ("Arial", Size-1), fg = "#2983bb")
Step_Label2_6 = tk.Label(frame2_3, text = "Maximum Step Length: ", bg = bg, font = ("Arial", Size-1), fg = "#2983bb")
Step_Label2_7 = tk.Label(frame2_4, text = "Maximum Number Of Iterations: ", font = ("Arial", Size-1), bg  = bg, fg = "#2983bb")

NR_Res_In = tk.Entry(frame2_2, Dis_Entry, validate = "key", validatecommand = vcmd_Int, textvariable = NR_Res)
NR_Length_In = tk.Entry(frame2_3, Dis_Entry, validate = "key", validatecommand = vcmd_float_Int, textvariable = NR_Length, state = "disable", disabledbackground = bg, )
NR_Iterations_In = tk.Entry(frame2_4, Dis_Entry, validate = "key", validatecommand =vcmd_Int,textvariable = NR_Iterations)

Step_Label2_4.pack(padx = 50, pady = 2.5, anchor = "nw")
Step_Label2_5.pack(padx = (75,13), pady = 5, anchor = "nw", side = "left")
Step_Label2_6.pack(padx = (75,21), pady =5, anchor = "nw", side = "left")
Step_Label2_7.pack(padx = (75,13), pady =5, anchor = "nw", side = "left")

NR_Res_In.pack(pady = 5, anchor = "w")
NR_Length_In.pack(pady = 5, anchor = "w")
NR_Iterations_In.pack(pady = 5, anchor = "w")

#Progross = tk.Label(frame2_5, text = "Wait for setting ", font = ("Arial", 10), width = 500, bg = bg, fg = "gray" )
#Progross.pack(anchor = "w", expand= 1, fill = "x")
btn6 = tk.Button(frame2, Dis_but, text = "Go Next", command = lambda: GoNext(Active_step[0]))
btn7 = tk.Button(frame2, Dis_but, text = "Go back", command = lambda: GoBack2(Active_step[0],[""], ["Save result"]))
btn8 = tk.Button(frame2, Dis_but, text = "Save result", command = lambda: saveResullt(["Reg1st"]))

frame2_2.pack(anchor = "nw")
frame2_3.pack(anchor = "nw")
frame2_4.pack(anchor = "nw")
#frame2_5.pack(anchor = "nw", padx = 50)

btn6.pack(anchor= "nw", side = "right", pady = 5, padx = (5,10))
btn7.pack(anchor= "nw", side = "right", pady = 5)
btn8.pack(anchor= "nw", side = "right", pady = 5, padx = (0,5))
Seperator(Full_view, 3)

#Step3 region
R_para = [4, 1.0, 800]
frame3 = tk.Frame(Full_view, bg = bg)
frame3.grid(row = 4, column = 0, sticky = "NSEW")

frame3_1 = tk.Frame(frame3, bg = bg)
frame3_2 = tk.Frame(frame3, bg = bg)
frame3_3 = tk.Frame(frame3, bg = bg)
frame3_4 = tk.Frame(frame3, bg = bg)

R_Res, R_Length, R_Iterations, VarClear = tk.IntVar(root), tk.IntVar(root), tk.IntVar(root), tk.IntVar(root)
R_Res.set(R_para[0])
R_Length.set(R_para[1])
R_Iterations.set(R_para[2])

Step_Label3 = tk.Label(frame3, text = "Step3. beta-spline Registration", font = (Font_W, Size), fg = "#66c18c", bg = bg)
CheckClear = tk.Checkbutton(frame3_4, text = "Apply the Mask to Pre_Img", variable = VarClear, onvalue = 1, offvalue = 0, justify = "left", bg = bg, font = ("Arial",Size-1), fg = "#51c4d3", command = lambda: MaskCreate(VarClear), state = "disable")
CheckClear.deselect()
btn12 = tk.Button(frame3_4, Dis_but, text ="Preview", command = lambda: Preview_Mask(Pre_Img))
Step_Label3_1 = tk.Label(frame3, text = "Parameter setting", bg = bg, font = ("Arial",Size), fg = "#51c4d3")
Step_Label3_2 = tk.Label(frame3_1, text = "Number Of Resolutions: ", bg =bg , font = (Font_W, Size-1), fg = "#2983bb")
Step_Label3_3 = tk.Label(frame3_2, text = "Maximum Step Length: ", bg = bg, font = (Font_W, Size-1), fg = "#2983bb")
Step_Label3_4 = tk.Label(frame3_3, text = "Maximum Number Of Iterations: ", font = (Font_W, Size-1), bg  = bg, fg = "#2983bb")

R_Res_In = tk.Entry(frame3_1, Dis_Entry, validate = "key", validatecommand = vcmd_Int, textvariable = R_Res)
R_Length_In = tk.Entry(frame3_2, Dis_Entry, validate = "key", validatecommand = vcmd_Int, textvariable = R_Length)
R_Iterations_In = tk.Entry(frame3_3, Dis_Entry, validate = "key", validatecommand = vcmd_Int, textvariable = R_Iterations)

btn9 = tk.Button(frame3, Dis_but, text = "Go Next", command = lambda: GoNext(Active_step[0]))
btn10 = tk.Button(frame3, Dis_but, text = "Go back", command = lambda: GoBack2(Active_step[0], ["Preview"], ["Save result"]))
btn11 = tk.Button(frame3, Dis_but, text = "Save result", command = lambda: saveResullt(["Reg2nd"]))

##Pack widgets in frame3
Step_Label3.pack(anchor = "nw", padx = (0, 5))
frame3_4.pack(anchor = "nw")
Step_Label3_1.pack(padx = 50, pady = 2.5, anchor = "nw")

CheckClear.pack(padx = (50, 5), pady = 2.5, anchor = "nw", side = "left")
btn12.pack(pady = 2.5, anchor = "nw", side = "left")

Step_Label3_2.pack(padx = (75, 13), pady = 5, anchor = "nw", side = "left")
Step_Label3_3.pack(padx = (75, 21), pady = 5, anchor = "nw", side = "left" )
Step_Label3_4.pack(padx = (75, 13), pady = 5, anchor = "nw", side = "left")

R_Res_In.pack(pady = 5, anchor = "w")
R_Length_In.pack(pady = 5, anchor = "w")
R_Iterations_In.pack(pady = 5, anchor = "w")

frame3_1.pack(anchor = "nw")
frame3_2.pack(anchor = "nw")
frame3_3.pack(anchor = "nw")

btn9.pack(anchor= "nw", side = "right", pady = 5, padx = (5,10))
btn10.pack(anchor= "nw", side = "right", pady = 5)
btn11.pack(anchor= "nw", side = "right", pady = 5, padx = (0,5))
Seperator(Full_view, 5)

#Step4 Region
frame4 = tk.Frame(Full_view, bg = bg)
frame4.grid(row = 6, column = 0, sticky = "NSEW") 

frame4_1 = tk.Frame(frame4, bg = bg)
frame4_2 = tk.Frame(frame4, bg = bg)
frame4_3 = tk.Frame(frame4, bg = bg)
frame4_4 = tk.Frame(frame4, bg = bg)

VarSkele, VarScale, VarUnit, Sampling_In, X_scale, Y_scale = tk.IntVar(root), tk.IntVar(root), tk.StringVar(root), tk.IntVar(root), tk.StringVar(root), tk.StringVar(root)
Unit_Lst = ["","um", "mm", "cm"] 
VarUnit.set("")
Sampling_In.set(1)
X_scale.set(1)
Y_scale.set(1)

Step_Label4 = tk.Label(frame4, text = "Step4. Calculate Structure Deflection", font = (Font_W, Size), fg = "#66c18c", bg = bg)
Step_Label4_1 = tk.Label(frame4, text = "Select the Skeleton Image", font = (Font_W, Size-1), fg = "#51c4d3", bg = bg)

AutoChek = tk.Radiobutton(frame4_1, text = "Automatic", font = (Font_W, Size-1), fg = "#2983bb", bg = bg, variable = VarSkele, value = 0, command = enable_skele, state = "disable")
RefChek = tk.Radiobutton(frame4_1, text = "Reference", font = (Font_W, Size-1), fg = "#2983bb", bg = bg, variable = VarSkele, value = 1, command = enable_skele, state = "disable")
btn13 = tk.Button(frame4_1, text = "Browse", command = browseFiles_Skele, state = "disable")
btn14 = tk.Button(frame4_1, text = "Preview", bg = Color_ButDis, width = 12, command = lambda: Preview_skeleton(Pre_Img),fg = "#cdd1d3", state = "disable")
CheckScale = tk.Checkbutton(frame4_2, text = "Set scaling( pre Pixel )", font = (Font_W, Size-1), bg = bg, fg = "#51c4d3", variable = VarScale, onvalue = 1, offvalue = 0, command = lambda: enable(VarScale, frame4_3),state ="disable")
Step_Labe4_2 = tk.Label(frame4_3, text = "X:", font = (Font_W, Size-1), bg = bg, fg = "#2b333e" )
X_scale_In = tk.Entry(frame4_3, Dis_Entry, validate = "key", validatecommand = vcmd_float_Int, borderwidth = 1.5, textvariable = X_scale)
Step_Labe4_3 = tk.Label(frame4_3, text = "Y:", font = (Font_W, Size-1), bg = bg, fg = "#2b333e" )
Y_scale_In = tk.Entry(frame4_3, Dis_Entry , validate = "key", validatecommand = vcmd_float_Int, borderwidth = 1.5, textvariable = Y_scale)
Step_Labe4_4 = tk.Label(frame4_3, text = "Unit:", font = (Font_W, Size-1), bg = bg, fg = "#2b333e" )
style = ttk.Style()
style.theme_use('clam')
style.configure('TCombobox',fieldbackground= bg, background= "#ccccd6", foreground = Color_ButNor, borderwidth =1, relief = "groove")
Unit_In = ttk.Combobox(frame4_3, width = 5 , values = ["um", "mm", "cm"], style = "TCombobox", font = (Font_W, 11), state = "disable")
Unit_In.current(0)

Step_Label4_5 = tk.Label(frame4_4, text = "Sampling size of Skeleton:", font = (Font_W, Size-1), bg = bg , fg = "#51c4d3")
Sampling_In = tk.Entry(frame4_4, Dis_Entry, validate = "key", validatecommand = vcmd_Int, textvariable = Sampling_In)

btn15 = tk.Button(frame4,Dis_but, text = "Go Next", command = lambda: GoNext(Active_step[0]))
btn16 = tk.Button(frame4,Dis_but, text = "Go Back", command = lambda: GoBack2(Active_step[0],["Preview"], ["Save result"]))
btn17 = tk.Button(frame4, Dis_but, text = "Save result", command = lambda: saveResullt(["Skeleton_Img"]))
##Pack widgets in frame4
AutoChek.pack(padx = (75,3), side= "left", pady = 2.5)
RefChek.pack(padx = (50,3), side= "left", pady = 2.5)
btn13.pack(padx = (0, 20), side = "left", pady = 2.5)
btn14.pack(padx = (40, 5), side = "left", pady = 2.5)
AutoChek.select()

CheckScale.pack(anchor = "nw", padx = 50, pady = 2.5)
Step_Labe4_2.pack(anchor = "nw", padx = (75,4), pady = 3, side = "left")
X_scale_In.pack(anchor = "nw", padx = (0, 15), pady = 3, side = "left")
Step_Labe4_3.pack(anchor = "nw", padx = (15, 4), pady = 3, side = "left")
Y_scale_In.pack(anchor = "nw", padx = (0, 22), pady = 3, side = "left")
Step_Labe4_4.pack(anchor = "nw", padx = (10, 4), pady = 3, side = "left")
Unit_In.pack(anchor = "nw", padx = (0,5), pady = 3) 
Step_Label4_5.pack(anchor = "nw", padx = (50, 10), pady = 15, side = "left")
Sampling_In.pack(anchor = "w", side = "left", pady = 15)

Step_Label4.pack(anchor = "nw", padx = (0, 5))
Step_Label4_1.pack(padx = 50, pady = 2.5, anchor = "nw")
frame4_1.pack(anchor = "nw")
frame4_2.pack(anchor = "nw")
frame4_3.pack(anchor = "nw")
frame4_4.pack(anchor = "nw")
btn15.pack(anchor= "nw", side = "right", pady = 5, padx = (5,10))
btn16.pack(anchor= "nw", side = "right", pady = 5)
btn17.pack(anchor= "nw", side = "right", pady = 5, padx = (0,5))
Seperator(Full_view, 7)

#Step5 region
frame5 = tk.Frame(Full_view, bg = bg)
frame5.grid(row = 8, column = 0, sticky = "NSEW")

Bin_width, Total_binL, Bin_unit, RMS_limit  = tk.StringVar(root), tk.StringVar(root), tk.StringVar(root), tk.StringVar(root)

Bin_width.set("1")
Total_binL.set("300")
Bin_unit.set("pixel")
RMS_limit.set(10.0)

frame5_1 = tk.Frame(frame5, bg = bg)
frame5_2 = tk.Frame(frame5, bg = bg)
frame5_3 = tk.Frame(frame5, bg = bg)

Step_Label5 = tk.Label(frame5, text = "Step5. Calculate Root mean square(RMS) and plot", font = (Font_W, Size), fg = "#66c18c", bg = bg)
Step_Label5_1 = tk.Label(frame5_1, text = "Length interval: " , font = (Font_W, Size-1), bg = bg , fg = "#51c4d3")
Bin_width_In = tk.Entry(frame5_1, Dis_Entry, textvariable= Bin_width, validate = "key", validatecommand = vcmd_float_Int, borderwidth = 1.5)
Step_Label5_2 = tk.Label(frame5_1, textvariable = Bin_unit, font = (Font_W, Size-1), bg = bg , fg = "#51c4d3" )
Step_Label5_3 = tk.Label(frame5_2, text = "Maximum Bound(X-axis): " , font = (Font_W, Size-1), bg = bg , fg = "#51c4d3")
Total_binL_In = tk.Entry(frame5_2, Dis_Entry, textvariable= Total_binL, validate = "key", validatecommand = vcmd_float_Int, borderwidth = 1.5)
Step_Label5_4 = tk.Label(frame5_2, textvariable = Bin_unit, font = (Font_W, Size-1), bg = bg , fg = "#51c4d3" )
Step_Label5_5 = tk.Label(frame5_3, text = "Maximum Bound(Y-axis):", font = (Font_W, Size-1), bg = bg , fg = "#51c4d3")
RMS_limit_In = tk.Entry(frame5_3, Dis_Entry, textvariable= RMS_limit, validate = "key", validatecommand = vcmd_float_Int, borderwidth = 1.5)
Step_Label5_6 = tk.Label(frame5_3, textvariable = Bin_unit, font = (Font_W, Size-1), bg = bg , fg = "#51c4d3" )

btn18 = tk.Button(frame5, Dis_but, text = "Go Next", command =  lambda: GoNext(Active_step[0]))
btn19 = tk.Button(frame5, Dis_but, text = "Go Back", command = lambda: GoBack2(Active_step[0], ["Browse"], ["Save result"]))
btn20 = tk.Button(frame5, Dis_but, text = "Save result", command = lambda: saveResullt(["RMS_value", "RMS_plot"]))

#Pack the widgets in Resion5
Step_Label5.pack(anchor = "nw", padx = (0, 5) )
frame5_1.pack(anchor = "nw")
Step_Label5_1.pack(anchor = "nw", padx = (50, 5), pady = 10, side = "left")
Bin_width_In.pack(anchor = "nw", padx = (0,5), pady = 10, side = "left")
Step_Label5_2.pack(anchor = "nw", padx = (5,25), pady = 10, side = "left")
frame5_2.pack(anchor = "nw")
Step_Label5_3.pack(anchor = "nw", padx = (50, 5), pady = 5, side = "left")
Total_binL_In.pack(anchor = "nw", padx = (0,5), pady = 5, side = "left")
Step_Label5_4.pack(anchor = "nw", padx = (5,25), pady = 5, side = "left")
frame5_3.pack(anchor = "nw")
Step_Label5_5.pack(anchor = "nw", padx = (50,5), pady = 10, side = "left")
RMS_limit_In.pack(anchor = "nw", padx = (0,5), pady = 10, side = "left")
Step_Label5_6.pack(anchor = "nw", padx = (5,25), pady = 5, side = "left")

btn18.pack(anchor= "nw", side = "right", pady = 10, padx = (5,10))
btn19.pack(anchor= "nw", side = "right", pady = 10)
btn20.pack(anchor= "nw", side = "right", pady = 10, padx = (0,5))

Seperator(Full_view, 9)

#Step6 Region6
frame6 = tk.Frame(Full_view, bg = bg)
frame6.grid(row = 10, column = 0, sticky = "NSEW")

Gap_DM, VarRaw = tk.IntVar(root), tk.IntVar(root)
Gap_DM.set(20)

frame6_1 = tk.Frame(frame6, bg = bg)
Step_Label6 = tk.Label(frame6, text = "Step6. Plot the Deformation map", font = (Font_W, Size), fg = "#66c18c", bg = bg)
Raw_use = tk.Checkbutton(frame6, text = "Use the raw image to generate Deformation map", justify = "left", bg = bg, font = (Font_W, Size-1), fg = "#51c4d3", state = "disable"
                         ,variable= VarRaw, onvalue = 1, offvalue = 0)
Raw_use.deselect()
Step_Label6_1 = tk.Label(frame6_1, text = "Sampling size of Deformation map:",font = (Font_W, Size-1), bg = bg , fg = "#51c4d3")
Gap_In = tk.Entry(frame6_1, Dis_Entry, textvariable = Gap_DM, validate = "key", validatecommand = vcmd_Int, borderwidth = 1.5 )

btn21 = tk.Button(frame6, Dis_but, text = "Start Run", command = lambda: DFmapGenerate(Active_step[0], Pre_Img, Reg1st))
btn22 = tk.Button(frame6, Dis_but, text = "Go Back", command = lambda: GoBack2(Active_step[0], [""], ["Save result"]))
btn23 = tk.Button(frame6, Dis_but, text = "Save result", command = lambda: saveResullt(["DFmap"]))


Step_Label6.pack(anchor = "nw", padx = (0,5))
Raw_use.pack(anchor= "nw", padx = (45, 5), pady = (10,5))
frame6_1.pack(anchor = "nw")
Step_Label6_1.pack(anchor = "nw", padx = (50, 5), pady = 10, side = "left" )
Gap_In.pack(anchor = "nw",padx = (0,5), pady = 10, side = "left")
btn21.pack(anchor= "nw", side = "right", pady = 10, padx = (5,10))
btn22.pack(anchor= "nw", side = "right", pady = 10)
btn23.pack(anchor= "nw", side = "right", pady = 10, padx = (0,5))

##########################################Spradsheet2#########################################################
#-----創建主畫布與眷軸給Model2
canvas2 = tk.Canvas(root, bg = bg)
canvas2.bind('<Configure>', on_configure2)
canvas2.pack(anchor = "nw", side = "left", expand = True, fill="both")

Full_view2 =tk.Frame(canvas2, bg = bg)
canvas2.create_window(0,0,window = Full_view2, anchor='nw', tags=("Full_view2",))#只有使用create_window才能滾動卷軸

S = tk.Scrollbar(canvas2, orient="vertical",command=canvas2.yview, bg = bg)
S.pack( side="right" , fill = "y", anchor = "ne" )

canvas2.configure(yscrollcommand = S.set)
canvas2.bind("<Configure>", size)#重設Full_view2 填滿畫面

#-----變數存取
VarScale2, X_scale2, Y_scale2, VarUnitII, Sampling_InII = tk.IntVar(root), tk.IntVar(root), tk.IntVar(root), tk.StringVar(root), tk.IntVar(root)
#VarUnitII.set("")
Sampling_InII.set(1)
X_scale2.set(1)
Y_scale2.set(1)

#-----元件與框架創建(Step1)
frameII_1 = tk.Frame(Full_view2, bg = bg)#區域主框架
frameII_1.grid(column =0, row = 0, sticky="NSEW")
Full_view2.columnconfigure(0, weight = 1)

frameII_1_1 = tk.Frame(frameII_1, bg = bg)
frameII_1_2 = tk.Frame(frameII_1, bg = bg)
frameII_1_3 = tk.Frame(frameII_1, bg = bg)
frameII_1_4 = tk.Frame(frameII_1, bg = bg)

Title_Label1 = tk.Label(frameII_1, text = "Step1. Import Outputpoint_data", font = (Font_W, Size), fg = "#66c18c", bg = bg)
Data_Label1 = tk.Label(frameII_1_1, text = "Select the data of skeleton ", font = (Font_W, Size), fg = "#3EEDE7", bg = bg)
btnII_1 = tk.Button(frameII_1_1, text = "Browse", command = browseFiles_Tranformix)
#Treeview for Data Loading
MainW_tv3 = tk.Frame(frameII_1, bg = bg)
tvFScroll2 = ttk.Scrollbar(MainW_tv3, orient= "horizontal")
# Open_LabelII_1 = tk.Label(frameII_1, text ="#File Opened", font = (Font_W, Size-2), fg = "#2983bb", bg = bg)
tv_heading2 = ttk.Treeview(MainW_tv3, style= "mystyle2.Treeview",height=0, column = ["Image type"], show = "headings")
tv_heading2.column("Image type", width = 120, minwidth= 80, stretch = False, anchor = "e")
tv_heading2.heading("Image type", text =  "Data type", anchor = "center")
tv_heading2.grid(row =0, column = 0, sticky = "NWS")

tv_heading3 = ttk.Treeview(MainW_tv3, style= "mystyle2.Treeview",height=1, column = ["Type"], show = "")
tv_heading3.column("Type", width = 120, minwidth= 80, stretch = False, anchor = "e")
tv_heading3.heading("Type", text =  "Image type", anchor = "center")
tv_heading3.insert(parent="", index = "end", iid = 0, values = ("Transformix Data : ",))
tv_heading3.grid(row =1, column = 0, sticky = "NWS")

tv_heading4 = ttk.Treeview(MainW_tv3, style= "mystyle2.Treeview",height=0, column = ["Path"], show = "headings")
tv_heading4.column("Path", width = 80, minwidth= 80, stretch = True, anchor = "e")
tv_heading4.heading("Path", text =  "Path", anchor = "center")
tv_heading4.grid(row =0, column = 1, sticky = "EW")

tv_fileT = ttk.Treeview(MainW_tv3, style="mystyle2.Treeview",height=1, column = ["Path"], xscrollcommand= tvFScroll2.set, show = "")
#Set column&heading
tv_fileT.column("#0", width = 80, minwidth = 80,stretch = False, anchor = "e")
tv_fileT.column("Path", width = 40, anchor = "w")
tv_fileT.heading("#0", text =  "Type", anchor = "center")
tv_fileT.heading("Path", text =  "File Path", anchor = "center")
tv_fileT.update()
#Insert row
tv_fileT.insert(parent="", index = "end", iid = 0, text = "ASD : ", values = "", tags = ("realPath",))
tv_fileT.grid(row =1, column = 1, sticky = "EW")
tvFScroll2.configure(command= tv_fileT.xview, style = "mystytle3.Horizontal.TScrollbar")

tvFScroll2.configure(command= tv_fileT.xview, style = "mystytle3.Horizontal.TScrollbar")
tvFScroll2.grid(row = 2, column = 0, columnspan = 2,  sticky = "EW", pady=(5,10))
MainW_tv3.columnconfigure(1, weight = 1)
CheckScale2 = tk.Checkbutton(frameII_1_2 , text = "Set scaling( pre Pixel )", font = (Font_W, Size), bg = bg, fg = "#51c4d3", variable = VarScale2, onvalue = 1, offvalue = 0, command = lambda: enable(VarScale2,frameII_1_3),state ="disable")
X_scaleII = tk.Label(frameII_1_3, text = "X:", font = (Font_W, Size-1), bg = bg, fg = "#2b333e" )
X_scale_InII = tk.Entry(frameII_1_3, Dis_Entry, validate = "key", validatecommand = vcmd_float_Int, borderwidth = 1.5, textvariable = X_scale2)
Y_scaleII = tk.Label(frameII_1_3, text = "Y:", font = (Font_W, Size-1), bg = bg, fg = "#2b333e" )
Y_scale_InII = tk.Entry(frameII_1_3, Dis_Entry , validate = "key", validatecommand = vcmd_float_Int, borderwidth = 1.5, textvariable = Y_scale2)
UnitII = tk.Label(frameII_1_3, text = "Unit:", font = (Font_W, Size-1), bg = bg, fg = "#2b333e" )
#-----下拉式選單控鍵(Step1)
style = ttk.Style()
style.theme_use('clam')
style.configure('TCombobox',fieldbackground= bg, background= "#ccccd6", foreground = Color_ButNor, borderwidth =1, relief = "groove")
Unit_InII = ttk.Combobox(frameII_1_3, width = 5 , values = ["um", "mm", "cm"], style = "TCombobox", font = (Font_W, 11), state = "disable", textvariable = VarUnitII)
Unit_InII.current(0)
#下拉式選單控鍵#
SamplingII = tk.Label(frameII_1_4, text = "Sampling size of Skeleton:", font = (Font_W, Size-1), bg = bg , fg = "#51c4d3")
Sampling_InII = tk.Entry(frameII_1_4, Dis_Entry, validate = "key", validatecommand = vcmd_Int, textvariable = Sampling_InII)

btnII_2 = tk.Button(frameII_1, Dis_but, text = "Go Next", command = lambda: GoNextII(Active_step[1]))

#-----元件與框架添加(Step1)
Data_Label1.pack(anchor = "nw", side = "left", padx = (50, 5), pady = 2.5) 
btnII_1.pack(anchor = "w", side = "left", padx = (0, 40), pady = 2.5)
CheckScale2.pack(anchor = "nw", padx = 50, pady = 2.5)
X_scaleII.pack(anchor = "nw", padx = (75,4), pady = 3, side = "left")
X_scale_InII.pack(anchor = "nw", padx = (0, 15), pady = 3, side = "left")
Y_scaleII.pack(anchor = "nw", padx = (50,4), pady = 3, side = "left")
Y_scale_InII.pack(anchor = "nw", padx = (0, 15), pady = 3, side = "left")
UnitII.pack(anchor = "nw", padx = (10, 4), pady = 3, side = "left")
Unit_InII.pack(anchor = "nw", padx = (0,5), pady = 3)
SamplingII.pack(anchor = "nw", padx = (50, 10), pady = 15, side = "left")
Sampling_InII.pack(anchor = "w", side = "left", pady = 15)

Title_Label1.pack(anchor = "nw", padx = (0,5))
frameII_1_1.pack(anchor = "nw")
MainW_tv3 .pack(anchor = "nw", padx = (20,15), expand= True, fill = "both")
# Open_LabelII_1.pack(anchor= "nw", padx = (75,0) ,pady =(2.5, 0))
frameII_1_2.pack(anchor = "nw")
frameII_1_3.pack(anchor = "nw")
frameII_1_4.pack(anchor = "nw")
btnII_2 .pack(anchor = "nw", padx = (5, 10), pady = 5, side = "right" )
# Seperator2(Full_view2)
Seperator(Full_view2,1)

#-----框架創建(Step2)
frameII_2 = tk.Frame(Full_view2, bg = bg)
frameII_2.grid(column = 0, row = 2, sticky = tk.NSEW )
# frameII_2.pack(anchor = "nw", fill = "x", expand = False)

frameII_2_1 = tk.Frame(frameII_2, bg = bg )
frameII_2_2 = tk.Frame(frameII_2, bg = bg )
frameII_2_3 = tk.Frame(frameII_2, bg = bg )
frameII_2_4 = tk.Frame(frameII_2, bg = bg )

#-----變數存取(Step2)
Bin_widthII, UnitII, Total_binLII, RMS_limitII = tk.IntVar(root), tk.StringVar(root), tk.IntVar(root), tk.IntVar(root)
UnitII.set("Pixel")
Bin_widthII.set(20)
RMS_limitII.set(10)

#-----元件創建(Step2)
Title_Label2 = tk.Label(frameII_2_1, text = "Step2. Calculate Root mean square(RMS) and plot", font = (Font_W, Size), fg = "#66c18c", bg = bg)
Leng_LabelII = tk.Label(frameII_2_2, text = "Length interval: " , font = (Font_W, Size-1), bg = bg , fg = "#51c4d3")
Bin_width_InII = tk.Entry(frameII_2_2, Dis_Entry, textvariable= Bin_widthII, validate = "key", validatecommand = vcmd_float_Int, borderwidth = 1.5)
Unit_LabelII = tk.Label(frameII_2_2, textvariable = UnitII, font = (Font_W, Size-1), bg = bg , fg = "#51c4d3" )
X_max_LabelII = tk.Label(frameII_2_3, text = "Maximum Bound(X-axis): " , font = (Font_W, Size-1), bg = bg , fg = "#51c4d3")
Total_binL_InII = tk.Entry(frameII_2_3, Dis_Entry, textvariable= Total_binLII, validate = "key", validatecommand = vcmd_float_Int, borderwidth = 1.5)
Unit_LabelIII = tk.Label(frameII_2_3, textvariable = UnitII, font = (Font_W, Size-1), bg = bg , fg = "#51c4d3" )
Y_max_LabelII = tk.Label(frameII_2_4, text = "Maximum Bound(Y-axis):", font = (Font_W, Size-1), bg = bg , fg = "#51c4d3")
RMS_limit_InII = tk.Entry(frameII_2_4, Dis_Entry, textvariable= RMS_limitII, validate = "key", validatecommand = vcmd_float_Int, borderwidth = 1.5)
Unit_LabelIV = tk.Label(frameII_2_4, textvariable = UnitII, font = (Font_W, Size-1), bg = bg , fg = "#51c4d3" )

btnII_3 = tk.Button(frameII_2, Dis_but, text = "Go Next", command =  lambda: GoNextII_RMS(Active_step[1]))
btnII_4 = tk.Button(frameII_2, Dis_but, text = "Go Back", command = GobackII)
btnII_5 = tk.Button(frameII_2, Dis_but, text = "Save result", command = lambda: saveResullt(["RMS_valueII", "RMS_plotII"]))

#-----元件與框架添加(Step2)
Title_Label2.pack(anchor = "nw", padx = (0,5))
Leng_LabelII.pack(anchor= "nw", side = "left", padx = (50, 5), pady = 5)
Bin_width_InII.pack(anchor= "nw", side = "left", padx = (25, 5), pady = 10)
Unit_LabelII.pack(anchor= "nw", side = "left", padx = (25, 5), pady = 10)
X_max_LabelII.pack(anchor = "nw", side = "left", padx = (50, 5), pady = 10)
Total_binL_InII.pack(anchor = "nw", side = "left", padx = (25, 5), pady = 10 )
Unit_LabelIII.pack(anchor = "nw", side = "left", padx = (25, 5), pady = 10 )
Y_max_LabelII.pack(anchor = "nw", side = "left", padx = (50, 5), pady = 10 )
RMS_limit_InII.pack(anchor = "nw", side = "left", padx = (25, 5), pady = 10 )
Unit_LabelIV.pack(anchor = "nw", side = "left", padx = (25, 5), pady = 10 )

frameII_2_1.pack(anchor = "nw")
frameII_2_2.pack(anchor = "nw")
frameII_2_3.pack(anchor = "nw")
frameII_2_4.pack(anchor = "nw")
btnII_3.pack(anchor = "nw", side = "right", pady = 5, padx = (5,10))
btnII_4.pack(anchor = "nw", side = "right", pady = 5)
btnII_5.pack(anchor = "nw", side = "right", pady = 5, padx = (0,5))
# Seperator2(Full_view2)
Seperator(Full_view2,3)

#-----框架創建(Step3)
frameII_3 = tk.Frame(Full_view2, bg = bg)
frameII_3 .grid(row = 4, column = 0, sticky = "NSEW")
frameII_3_1 = tk.Frame(frameII_3, bg= bg)
frameII_3_2 = tk.Frame(frameII_3, bg =bg)
MainW_tv4 = tk.Frame(frameII_3, bg = bg)
tvFScroll3 = ttk.Scrollbar(MainW_tv4, orient= "horizontal")#FrameforTreeview


#-----變數存取(Step3)
Gap_DMII = tk.IntVar(root)
Gap_DMII.set(20)

#-----元件創建(Step3)
Title_Label3 = tk.Label(frameII_3, text = "Step6. Plot the Deformation map", font = (Font_W, Size), fg = "#66c18c", bg = bg)
DM_LabelII = tk.Label(frameII_3_1, text = "Select Image to Overlay",font = (Font_W, Size-1), bg = bg , fg = "#51c4d3")
btnII_10 = tk.Button(frameII_3_1, text = "Browse", command = browseFiles_Tranformix_DF_fig)
# Open_LabelII_3 = tk.Label(frameII_3, text ="#File Opened", font = (Font_W, Size-2), fg = "#2983bb", bg = bg)
Data_Label2 = tk.Label(frameII_3_2, text = "Select the Outpupoints to draw map ", font = (Font_W, Size-1), bg = bg , fg = "#51c4d3")
btnII_6 = tk.Button(frameII_3_2, text = "Browse", command = browseFiles_Tranformix_DF, state = "normal")
# Open_LabelII_2 = tk.Label(frameII_3, text ="#File Opened", font = (Font_W, Size-2), fg = "#2983bb", bg = bg)
#Table1 to add title
tv_heading5 = ttk.Treeview(MainW_tv4, style= "mystyle2.Treeview",height=0, column = ["Data type"], show = "headings")
tv_heading5.column("Data type", width = 100, minwidth= 80, stretch = False, anchor = "e")
tv_heading5.heading("Data type", text =  "Data type", anchor = "center")
tv_heading5.grid(row =0, column = 0, sticky = "NWS")
#Table2 to add value for DataType
tv_heading6 = ttk.Treeview(MainW_tv4, style= "mystyle2.Treeview",height=2, column = ["Type"], show = "")
tv_heading6.column("Type", width = 100, minwidth= 80, stretch = False, anchor = "e")
tv_heading6.heading("Type", text =  "Data type", anchor = "center")
tv_heading6.insert(parent="", index = "end", iid = 0, values = ("Ovelay Image : ",))
tv_heading6.insert(parent="", index = "end", iid = 1, values = ("Outputpoints : ",))
tv_heading6.grid(row =1, column = 0, sticky = "NWS")
#Table3 to add heading for path
tv_heading7 = ttk.Treeview(MainW_tv4, style= "mystyle2.Treeview",height=0, column = ["Path"], show = "headings")
tv_heading7.column("Path", width = 80, minwidth= 80, stretch = True, anchor = "e")
tv_heading7.heading("Path", text =  "Path", anchor = "center")
tv_heading7.grid(row =0, column = 1, sticky = "EW")
#Table4 to Show Paths
tv_fileS2 = ttk.Treeview(MainW_tv4, style = "mystyle2.Treeview", height =2, column = ["Path"], show = "" , xscrollcommand= tvFScroll3.set)
tv_fileS2.column("#0", width = 80, minwidth = 80,stretch = False, anchor = "e")
tv_fileS2.column("Path", width = 40, anchor = "w")
tv_fileS2.heading("#0", text =  "Image type", anchor = "center")
tv_fileS2.heading("Path", text =  "File Path", anchor = "center")
tv_fileS2.update()

#Insert row
tv_fileS2.insert(parent="", index = "end", iid = 0, text = "Ovelay Image : ", values = "", tags = ("realPath",))
tv_fileS2.insert(parent="", index = "end", iid = 1, text = "Outputpoints : ", values = "", tags = ("realPath",))

# tvFscrollx = tk.Scrollbar(MainW_tvF, orient= "horizontal", command= tv_file.xview)
tvFScroll3.configure(command= tv_fileS2.xview, style = "mystytle3.Horizontal.TScrollbar")
tv_fileS2.grid(row =1, column = 1, sticky = "EW")
tvFScroll3.grid(row = 2, column = 0, columnspan = 2,  sticky = "EW", pady=(0,0))



btnII_7 = tk.Button(frameII_3, Dis_but, text = "Start Run", command = lambda:  DFmapGenerateII(Active_step[1]))
btnII_8 = tk.Button(frameII_3, Dis_but, text = "Go Back", command = GobackII)
btnII_9 = tk.Button(frameII_3, Dis_but, text = "Save result", command = lambda: saveResullt(["DFmapII"]))

#-----框架與元件添加(Step3)
Title_Label3.pack(anchor = "nw", padx = (0,5))
frameII_3_1.pack(anchor = "nw")
# Open_LabelII_3.pack(anchor= "nw", padx = (75,0), pady =(2.5, 0))
frameII_3_2.pack(anchor = "nw")
MainW_tv4.pack(anchor = "nw", padx = (20,15), expand= True, fill = "both")
MainW_tv4.columnconfigure(1, weight =1)

DM_LabelII.pack(anchor = "nw", padx = (50, 5), pady = 10, side = "left")
btnII_10.pack(anchor = "w", side = "left", padx = (0, 40), pady = 2.5)

Data_Label2.pack(anchor = "nw", padx = (50, 5), pady = 10, side = "left")
btnII_6.pack(anchor = "w", side = "left", padx = (0, 40), pady = 2.5)

btnII_7.pack(anchor= "nw", side = "right", pady = 10, padx = (5,10))
btnII_8.pack(anchor= "nw", side = "right", pady = 10)
btnII_9.pack(anchor= "nw", side = "right", pady = 10, padx = (0,5))

#-----End of Sheet2
notebook.add(canvas2, text = "Start with Transformix output")


notebook.pack(anchor="nw", fill="both",expand=True)
MainW_tvF.update()
frame1.update()
root.maxsize(frame6.winfo_width()+20, 5*wh)
#root.bind("<Map>", catch_maximize)

Prev_Win.protocol("WM_DELETE_WINDOW", exit)
root.protocol("WM_DELETE_WINDOW", exit )
Prev_Win.mainloop()




root.mainloop()
file_path = pyelastix.__file__
 
# storing the directory in dir variable
dir = os.path.dirname(file_path)
 
# printing the directory
print(dir)

