#import lib
import json

#load data from json
def load_data():
    with open('../data/export.json', 'r') as f:
        expor = json.load(f)

    with open('../data/import.json', 'r') as f:
        impor = json.load(f)
    return expor,impor

#untuk memproses data menjadi bentuk yang diinginkan
def proses(tipe):
    for data in tipe :
        data['Tahun']=int(data['Tahun'])
        data['Nilai/Value (US $)']=float((data['Nilai/Value (US $)'].replace(" ","")).replace(",","."))
        data['Berat/Weight (KG)']=float((data['Berat/Weight (KG)'].replace(" ","")).replace(",","."))
        if data['Bulan/Month'] == 'Januari/January' :
            data['Bulan/Month'] = 1
        elif data['Bulan/Month'] == 'Pebruari/February' :
            data['Bulan/Month'] = 2
        elif data['Bulan/Month'] == 'Maret/March' :
            data['Bulan/Month'] = 3
        elif data['Bulan/Month'] == 'April/April' :
            data['Bulan/Month'] = 4
        elif data['Bulan/Month'] == 'Mei/May' :
            data['Bulan/Month'] = 5
        elif data['Bulan/Month'] == 'Juni/June' :
            data['Bulan/Month'] = 6
        elif data['Bulan/Month'] == 'Juli/July' :
            data['Bulan/Month'] = 7
        elif data['Bulan/Month'] == 'Agustus/August' :
            data['Bulan/Month'] = 8
        elif data['Bulan/Month'] == 'September/September' :
            data['Bulan/Month'] = 9
        elif data['Bulan/Month'] == 'Oktober/October' :
            data['Bulan/Month'] = 10
        elif data['Bulan/Month'] == 'Nopember/November' :
            data['Bulan/Month'] = 11
        elif data['Bulan/Month'] == 'Desember/December' :
            data['Bulan/Month'] = 12

#mengganti nama bulan dari angka menjadi huruf        
def conv_bulan(n):
    switcher = {
        1: "Januari",
        2: "Februari",
        3: "Maret",
        4: "April",
        5: "Mei",
        6: "Juni",
        7: "Juli",
        8: "Agustus",
        9: "September",
        10: "Oktober",
        11: "November",
        12: "Desember"
    }
    return switcher.get(n, "Invalid month")

#get sum 
def sum(tahun,pil,tipe):
    sum = 0
    for data in tipe:
        if(data['Tahun']==tahun):
            # print(data['Bulan/Month'], data['Nilai/Value (US $)'])
            if pil == 1 :
                sum +=  data['Nilai/Value (US $)']
            elif pil == 2 :
                sum += data['Berat/Weight (KG)']
    return sum

#mencari data
def search(b,t,pil,tipe):
    for data in tipe:
        if (data['Tahun']==t and data['Bulan/Month']==b):
            if(pil==1):
                return data['Nilai/Value (US $)']
            elif pil==2:
                return data['Berat/Weight (KG)']

#content dari program
def content(tipe):
    if pilihan1 == 1:
        print("Input Tahun(2010-2018)")
        tahun = int(input())
        while (tahun<2010 or tahun>2018):
            print("Tahun salah! Input Tahun(2010-2018)")
            tahun = int(input())
        if (pilihan2 == 1):
            print("Jumlah nilai pada tahun " + str(tahun) + " sebesar " + str(sum(tahun,1,tipe)) + " US dollar")
        elif (pilihan2 == 2):
            print("Jumlah massa pada tahun " + str(tahun) + " sebesar " + str(sum(tahun,2,tipe)) + " kg")
    elif pilihan1 == 2 :
        print("Masukkan bulan (dalam angka) dan tahun awal")
        masukan = input().split(' ')
        bulan1 = int(masukan[0])
        tahun1 = int(masukan[1])
        print("Masukkan bulan (dalam angka) dan tahun akhir")
        masukan = input().split(' ')
        bulan2 = int(masukan[0])
        tahun2 = int(masukan[1])
        if (pilihan2 == 1):
            x = search(bulan1,tahun1,1,tipe)
            y = search(bulan2,tahun2,1,tipe)
            if (y-x<0):
                print("Nilai mengalami deflasi sebesar " + str((y-x)*-1) + " US dolar")
            else:
                print("Nilai mengalami inflasi sebesar " + str(x-y) + " US dolar")           
        elif (pilihan2 == 2):
            x = search(bulan1,tahun1,2,tipe)
            y = search(bulan2,tahun2,2,tipe)
            if (x-y<0):
                print("Terdapat penurunan massa sebesar " + str((x-y)*-1) + " kg")
            else:
                print("Terdapat kenaikan massa sebesar " + str(x-y) + " kg")
    elif (pilihan1 == 3):
        print("Masukkan bulan (dalam angka) dan tahun")
        masukan = input().split(' ')
        bulan = int(masukan[0])
        tahun = int(masukan[1])
        if (pilihan2 == 1):
            print("Nilai pada bulan " + conv_bulan(bulan) + " " + str(tahun) + " adalah " + str(search(bulan,tahun,1,tipe)) + "  US dolar")
        elif pilihan2 == 2:
            print("Massa pada bulan " + conv_bulan(bulan) + " " + str(tahun) + " adalah " + str(search(bulan,tahun,2,tipe)) + " kg")

#main
expor, impor = load_data()
proses(expor)
proses(impor)
running = True
while running:
    print("Ingin melihat data ekspor/impor")
    print("1. Ekspor")
    print("2. Impor")
    print("3. Quit")
    pilihan = int(input())
    if pilihan == 1:
        print("Ingin melihat: ")
        print("1. Jumlah per Tahun")
        print("2. Perkembangan")
        print("3. Data")
        pilihan1 = int(input())
        print("1. Nilai")
        print("2. Berat")
        pilihan2 = int(input())
        content(expor)
        print("--Ekspor--\n")
    elif pilihan == 2:
        print("Ingin melihat: ")
        print("1. Jumlah per Tahun")
        print("2. Perkembangan")
        print("3. Data")
        pilihan1 = int(input())
        print("1. Nilai")
        print("2. Berat")
        pilihan2 = int(input())
        content(impor)
        print("--Impor--\n")
    elif pilihan == 3:
        running = False
    else :
        print("Wrong input")