from tkinter import *
from tkinter import messagebox

main_window = Tk()
main_window.geometry('400x500')
main_window.resizable(False, False)
main_window.title('Imagi Laundry')

class Pengunjung():
    def __init__(self, pengunjung, tanggal, nomor, kasir):
        self.pengunjung = pengunjung
        self.tanggal = tanggal
        self.nomor = nomor
        self.kasir = kasir
    
    def dataPengunjung(self):
        head= 'Imagi Laundry \nJl. Peterpan No 12, Neverwood, Neverland \nNomor Pengunjung : ' + self.nomor
        space = '\n'+('=' *20)
        tanggal = '\nTanggal : ' + self.tanggal
        nama = '\nNama    : ' + self.pengunjung
        kasir = '\nKasir   : ' +self.kasir
        
        return head + space + tanggal + nama + kasir + space

class cucian():
    def __init__(self, pewangi, berat, diskon, bayar):#tipe layanan sama pewangin di gui kasih listview
        self.pewangi= pewangi
        self.berat = berat
        self.diskon = diskon
        self.bayar = bayar

    def harga(self):
        subtotal = 5000 * self.berat
        lb_nSubtotal.config(text = 'Rp.' + str(subtotal) + ',-')
        hargatotal = (5000 * self.berat) - self.diskon
        lb_nTotal.config(text = 'Rp.' + str(hargatotal) + ',-')
        kembali = self.bayar - hargatotal
        if kembali >=0 :
            lb_nKembali.config(text = 'Rp.' + str(kembali) + ',-')
        
        if (hargatotal - self.bayar) <= 0 :
            status = 'Lunas'
            lb_ketstatus.config(text = 'Lunas', fg= 'green')
        else :
            status = 'Belum Lunas'
        space = '\n' + '=' *20
        head = '\nLaundry Kiloan Mikom Laundry (Rp.5000,- / kg)'
        Jpewangi = '\nJenis Pewangi     : ' + self.pewangi
        berat = '\nBerat (kg)        : ' + str(self.berat) +' kg'
        subharga =  '\nSubtotal Harga    : Rp.' + str(subtotal) + ',-'
        diskon = '\nDiskon            : Rp.' + str(self.diskon) + ',-'
        totharga =  '\nSubtotal Harga    : Rp.' + str(hargatotal) + ',-'
        bayar =  '\nPembayaran        : Rp.' + str(self.bayar) + ',-'
        kembalian = '\nKembali           : Rp.'+ str(kembali) + ',-'
        status_= '\nStatus Pembayaran : ' + status
        return head + Jpewangi + berat + subharga + diskon + totharga + bayar + kembalian + space + status_

class aturan():
    def __init__(self):
        pass
    def output(self):
        space = '\n' + '='*20
        out = '\nTelah membaca dan memahami : \n1. Pengambilan barang harap disertai nota \n2. Benda berharga yang tertinggal dalam cucian \n   bukan tanggung jawab kami \n3. Barang yang tidak diambil lebih dari 1 bulan \n   bukan tanggung jawab kami atau konsumen akan dikenakan \n   denda penitipan sebesar Rp. 10.000 setiap bulan selama \n   penitipan pakaian \n4. Klaim luntur tidak dipisah diluar tanggung jawab kami \n5. Komplain tidak membawa nota tidak dilayani \n6. Komplain pakaian kami layani 1x24 jam sejak pakaian \n   diambil \n7. Setiap konsumen dianggap setuju dengan jumlah pcs \n   pakaian yang kami hitung'
        return space + out + space
def submit():
    if varPengunjung.get() == '' :
        messagebox.showwarning('error', 'Harap Isikan Nama Pengunjung')
    elif int(varBerat.get()) == 0 :
        messagebox.showwarning('error', 'Berat Cucian harus lebih dari 0')
    elif varNomor.get() == '' :
        messagebox.showwarning('error', 'Harap Isikan Nomor HP  Pengunjung')
    pengunjung = varPengunjung.get()
    tanggal = str(varHari.get() +' ' + varBulan.get() +' ' + varTahun.get())
    nomor = varNomor.get()
    kasir = varKasir.get()
    pewangi = varPewangi.get()
    berat = int(varBerat.get())
    diskon = int(varDiskon.get())
    bayar = int(varBayar.get())
    x = Pengunjung(pengunjung, tanggal, nomor, kasir)
    y = cucian(pewangi, berat, diskon, bayar)
    z= aturan()
    namaFile = pengunjung + nomor + '.txt'
    file = open(namaFile, 'w')
    file.write(x.dataPengunjung() + y.harga() +z.output())
    file.close()
    message = 'Rincial transaksi telah disimpan dengan nama ' + namaFile
    messagebox.showinfo('Saved', message)
def reset():
    varPengunjung.set('')
    varHari.set(1)
    varBulan.set('Januari')
    varTahun.set(2021)
    varNomor.set('')
    varKasir.set('')
    varPewangi.set('Downy')
    varBerat.set(0)
    varDiskon.set(0)
    varBayar.set(0)
    lb_nSubtotal.config(text = 'Rp.0,-')
    lb_nTotal.config(text = 'Rp.0,-')
    lb_nKembali.config(text = 'Rp.0,-')
    lb_ketstatus.config(text = 'Belum Lunas', fg= 'red')


#label_create
lb_head = Label(main_window, text = 'IMAGI LAUNDRY', font = ('Bahnschrift',15, 'bold', 'underline'))
lb_pengunjung = Label(main_window, text= 'Nama Pengunjung', font=('Bahnschrift',12, 'bold'))
lb_tanggal = Label(main_window, text= 'Tanggal (d/m/y)', font=('Bahnschrift',12, 'bold'))
'''pemisah tanggal'''
lb_1 = Label(main_window, text= '/', font=('Bahnschrift',12, 'bold'))
lb_2 = Label(main_window, text= '/', font=('Bahnschrift',12, 'bold'))
'''OwO'''
lb_nomor = Label(main_window, text= 'Nomor HP                (+62)', font=('Bahnschrift',12, 'bold'))
lb_kasir = Label(main_window, text= 'Nama Kasir', font=('Bahnschrift',12, 'bold'))
lb_pewangi = Label(main_window, text= 'Jenis Pewangi', font=('Bahnschrift',12, 'bold'))
lb_berat = Label(main_window, text= 'Berat Cucian', font=('Bahnschrift',12, 'bold'))
lb_subtotal = Label(main_window, text= 'Subtotal', font=('Bahnschrift',12, 'bold'))
lb_diskon = Label(main_window, text= 'Dikson', font=('Bahnschrift',12, 'bold'))
lb_total = Label(main_window, text= 'Total', font=('Bahnschrift',12, 'bold'))
lb_bayar = Label(main_window, text= 'Bayar', font=('Bahnschrift',12, 'bold'))
lb_kembali = Label(main_window, text= 'Kembali', font=('Bahnschrift',12, 'bold'))
lb_status = Label(main_window, text= 'Status', font=('Bahnschrift',12, 'bold'))
lb_ketstatus = Label(main_window, text= 'Belum Lunas', font=('Bahnschrift',12, 'bold'), fg='red')
'''Nominal Rupiah'''
lb_nBayar = Label(main_window, text= 'Rp.', font=('Bahnschrift',12, 'bold'))
lb_nDiskon = Label(main_window, text= 'Rp.', font=('Bahnschrift',12, 'bold'))
lb_nSubtotal = Label(main_window, text= 'Rp.0,-', font=('Bahnschrift',12, 'bold'))
lb_nTotal = Label(main_window, text= 'Rp.0,-', font=('Bahnschrift',12, 'bold'))
lb_nKembali = Label(main_window, text= 'Rp.0,-', font=('Bahnschrift',12, 'bold'))

#entry_create
varPengunjung= StringVar()
en_pengunjung = Entry(main_window, width = 25,textvariable = varPengunjung, font=('Bahnschrift',12, 'bold'))
varNomor = StringVar()
en_nomor = Entry(main_window, width = 20,textvariable = varNomor, font=('Bahnschrift',12, 'bold'))
varKasir= StringVar()
en_kasir = Entry(main_window, width = 25,textvariable = varKasir, font=('Bahnschrift',12, 'bold'))
varBayar = StringVar()
varBayar.set(0)
en_bayar = Entry(main_window, width = 22,textvariable = varBayar, font=('Bahnschrift',12, 'bold'))
varDiskon = StringVar()
varDiskon.set(0)
en_Diskon = Entry(main_window, width = 22,textvariable = varDiskon, font=('Bahnschrift',12, 'bold'))
#spinbox_create
'''Tanggal'''
varHari = StringVar()
sb_hari = Spinbox(main_window, width = 3, from_=1, to=31, textvariable = varHari,font=('Bahnschrift',12, 'bold'))
varTahun = StringVar()
sb_tahun = Spinbox(main_window, width = 4, from_=2021, to=4000, textvariable = varTahun,font=('Bahnschrift',12, 'bold'))
'''OwO'''
varBerat = StringVar()
sb_berat = Spinbox(main_window, width = 5, from_=0, to=50, textvariable = varBerat,font=('Bahnschrift',12, 'bold'))

#option_create
'''tanggal (bulan)'''
varBulan = StringVar()
varBulan.set('Januari')
op_bulan = OptionMenu(main_window, varBulan, 'Januari','Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember')
'''pewangi'''
varPewangi = StringVar()
varPewangi.set('Downy')
op_pewangi = OptionMenu(main_window, varPewangi, 'So Klin','Downy','Molto','Kispray','Rapika','Dolphin')
#button_create
bt_submit = Button(main_window, text = 'Submit', width = 20, command = submit)
bt_reset = Button(main_window, text = 'Reset', width = 20, command = reset)
#label_place
lb_head.place(relx= 0.5, anchor = N)
lb_pengunjung.place(x=10 ,y=50)
lb_tanggal.place(x=10, y=80)
'''pemisah tanggal'''
lb_1.place(x=200, y=78)
lb_2.place(x=310, y=78)
'''OwO'''
lb_nomor.place(x=10, y=110)
lb_kasir.place(x=10, y=140)
lb_pewangi.place(x=10, y=170)
lb_berat.place(x=10, y=200)
lb_subtotal.place(x=10, y=230)
lb_diskon.place(x=10, y=260)
lb_total.place(x=10, y=290)
lb_bayar.place(x=10, y=320)
lb_kembali.place(x=10, y=350)
lb_status.place(x=10, y=380)
lb_ketstatus.place(x=150, y=380)
'''Nominal Rupiah'''
lb_nBayar.place(x=150, y=320)
lb_nDiskon.place(x=150, y=260)
lb_nSubtotal.place(x=150, y=230)
lb_nTotal.place(x=150, y=290)
lb_nKembali.place(x=150, y=350)
#entry_place
en_pengunjung.place(x=150, y=50)
en_nomor.place(x=195, y=110)
en_kasir.place(x=150, y=140)
en_bayar.place(x=178, y=320)
en_Diskon.place(x=178, y=260)

#option_place
op_pewangi.place(x=148, y=167)
op_bulan.place(x=210, y=75)

#spinbox_place
sb_hari.place(x=150, y=80)
sb_tahun.place(x=327, y=80)
sb_berat.place(x=150, y=200)
#button_place
bt_submit.place(x=210,y=410)
bt_reset.place(x=50,y=410)

main_window.mainloop()


