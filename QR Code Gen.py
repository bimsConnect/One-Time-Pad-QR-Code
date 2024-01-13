import secrets
import string
from tkinter import *
import tkinter as tk
from tkinter import ttk
import qrcode
from resizeimage import resizeimage
from PIL import Image, ImageTk
from tkinter import filedialog
import pad
from PIL import ImageTk as itk

LARGE_FONT= ("Verdana", 12)



class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self, bd=2, relief=RIDGE, bg='black')
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}

        for F in (StartPage, PageOne):

            frame = F(container, self)

            self.frames[F] = frame
            
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        ("QR Code Generator")
        
        title=Label(text="Pesan Rahasia Menggunakan OTP",font=("times new roman",40),bg='#053246',fg='white').place(x=0,y=0,relwidth=1)
        
        
        button = tk.Button(self, text="One Time Pad",
                            width= 20, height= 2, font = ("times new roman", 30), bg='#053246', fg='white', command=lambda: controller.show_frame(PageOne))
        button.pack(pady= 200, padx= 30)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.var_input = StringVar()
        self.download_Path = StringVar()
        self.var_chipertext = StringVar()
        bg = tk.Frame(self, bg="white")
        bg.pack(side="top", fill="both", expand = True)
        label = tk.Label(self, text="Enkripsi",font=LARGE_FONT)
        label.place(x= 200,
            y= 0,
            width= 100,
            height= 30)
        label1 = tk.Label(self, text = "Pesan :", font = LARGE_FONT, bg= "white")
        label1.place(x =-1,
            y= 70,
            width= 60,
            height= 30)              

        
        txt_code1 = Entry(self, textvariable= self.var_input, justify= LEFT, bg= 'white')
        txt_code1.place(x = 70,
            y = 70,
            width=580,
            height=30)           
        button1 = Button(self, text= "Hasil", command= self.Gen1, bg= '#053246' , fg= 'white', relief= RAISED)
        button1.place(x= 250, 
            y= 120,
            width= 150,
            height= 30)


        self.msg1 = ''
        self.lbl_msg = Label(self, text=self.msg1, font=("times new roman", 20), bg='white', fg='green')
        self.lbl_msg.place(x=0, y=390, width= 665, height= 40)
        

        qrFrame1 = tk.Frame(self, bd=2, relief=RIDGE, bg='white')
        qrFrame1.place(x=650, y=68, width=250, height=420)
        label1 = Label(qrFrame1, text="Enkripsi", font=("goudy old style", 20), bg='#053246', fg='white').place(x=0, y=0,
                                                                                                              relwidth=1)

        self.qrc1 = Label(qrFrame1, text='No QR Code \nAvailable', font=('times new roman', 15), bg='#053246', fg='white',
                         bd=1, relief=RIDGE)
        self.qrc1.place(x=35, y=100, width=170, height=170)



        qrFrame2 = tk.Frame(self, bd=2, relief=RIDGE, bg='white')
        qrFrame2.place(x=930, y=68, width=250, height=420)
        label2 = Label(qrFrame2, text="Deskripsi", font=("goudy old style", 20), bg='#053246', fg='white').place(x=0, y=0,
                                                                                                               relwidth=1)

        self.qrc2 = Label(qrFrame2, text='No QR Code \nAvailable', font=('times new roman', 15), bg='#053246', fg='white',
                         bd=1, relief=RIDGE)
        self.qrc2.place(x=35, y=100, width=170, height=170)






    def clr(self):
        self.var_input('')
        self.msg = ''
        self.lbl_msg.config(text=self.msg)
        self.qrc1.config(image='')
        self.qrc2.config(image='')
        self.download_Path.set('')

    def browse(self):
        download_Directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH")
        self.download_Path.set(download_Directory)
   
    def Gen1(self):
        pesan = str(self.var_input.get())
        otp_encryption = pad.otp(str(pesan))
        otp_cipher = otp_encryption[0]
        otp_key = otp_encryption[1]
        print(' '.join(str(e) for e in otp_key))
        ct = str(self.var_input.get())
        ct = pad.otp_decryption(otp_cipher, otp_key)
        print(ct)
        len(otp_key) == len(pad.otp_decryption(otp_cipher, otp_key))

        if  otp_cipher == '':
            self.msg1 = 'Kolom Harus Diisi!!!'
            self.lbl_msg.config(text=self.msg1, fg='red')
        else:
            self.qr1 = str(otp_cipher)
            self.qr1 = qrcode.make(self.qr1)
            self.qr1.save("Hasil.png")            
            self.qr1 = resizeimage.resize_cover(self.qr1, [180, 180])

            self.img1 = ImageTk.PhotoImage(self.qr1)
            self.qrc1.config(image=self.img1)


            self.msg1 = "Hasil QR Codenya!!!"
            self.lbl_msg.config(text=self.msg1, fg='green')


        if  ct == '':
            self.msg1 = 'Kolom Harus Diisi!!!'
            self.lbl_msg.config(text=self.msg1, fg='red')
        else:
            self.qr2 = str(ct)
            self.qr2 = qrcode.make(self.qr2)
            self.qr2.save("dekrip.png")            
            self.qr2 = resizeimage.resize_cover(self.qr2, [180, 180])

            self.img2 = ImageTk.PhotoImage(self.qr2)
            self.qrc2.config(image=self.img2)


            self.msg1 = "Hasil QR Codenya!!!"
            self.lbl_msg.config(text=self.msg1, fg='green')


app = SeaofBTCapp()
app.iconbitmap("Hasil.ico")

app.resizable(False,False)
app.title("QR Code")
app.geometry("1200x500+200+50")
app.mainloop()