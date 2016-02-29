#!/usr/bin/env python
# -*- coding: utf-8 -*-
from colored import fg, bg, attr # Yazıları renklendirmek için kullanacağımız modül
import itertools                           # Kombinasyon işlemlerinde kullanacağımız modül
print """
#####################
# w0rld Li5t 4uth0r #
#       v1.0        #
#      h4yuc3       #
#####################
"""
print "Hedef Türü"
print "1 - Wireless %sAKTİF%s" % (fg(10), attr(0))
print "2 - Web Uygulaması %sPASİF%s" % (fg(1), attr(0))
hedef = 0   # hedef değişkenini while döngüsünde koşul olarak kullanabilmek için 0 değeri ile döngüden önce tanımlıyoruz.
while hedef != "1" and hedef != "2":    # 1 yada 2 değeri girilmediği sürece
    hedef = raw_input ("hedef (1/2) ")   ## Sormaya devam et !
if hedef == "1":    # WIFI
    wifi = []    # Kullanıcıdan aldığımız değerleri eklemek için wifi adında bir liste oluşturuyoruz.
    

    # sehirler adında bir liste oluşturuyoruz ve içerisine 81 ilimizide ekliyoruz.
    sehirler = ['ADANA', 'ADIYAMAN', 'AFYON', 'AĞRI', 'AMASYA', 'ANKARA', 'ANTALYA', 'ARTVİN', 'AYDIN', 'BALIKESİR', 'BİLECİK', 'BİNGÖL', 'BİTLİS', 'BOLU', 'BURDUR', 'BURSA', 'ÇANAKKALE', 'ÇANKIRI', 'ÇORUM', 'DENİZLİ',
               'DİYARBAKIR', 'EDİRNE', 'ELAZIĞ', 'ERZİNCAN', 'ERZURUM', 'ESKİŞEHİR', 'GAZİANTEP', 'GİRESUN', 'GÜMÜŞHANE', 'HAKKARİ', 'HATAY', 'ISPARTA', 'MERSİN', 'İSTANBUL', 'İZMİR', 'KARS', 'KASTAMONU', 'KAYSERİ',
               'KIRKLARELİ', 'KIRŞEHİR', 'KOCAELİ', 'KONYA', 'KÜTAHYA', 'MALATYA', 'MANİSA', 'MARAŞ', 'MARDİN', 'MUĞLA', 'MUŞ', 'NEVŞEHİR', 'NİĞDE', 'ORDU', 'RİZE', 'SAKARYA', 'SAMSUN', 'SİİRT',
               'SİNOP', 'SİVAS', 'TEKİRDAĞ', 'TOKAT', 'TRABZON', 'TUNCELİ', 'ŞANLIURFA', 'UŞAK', 'VAN', 'YOZGAT', 'ZONGULDAK', 'AKSARAY', 'BAYBURT', 'KARAMAN', 'KIRIKKALE', 'BATMAN', 'ŞIRNAK', 'BARTIN', 'ARDAHAN',
               'IĞDIR', 'YALOVA', 'KARABÜK', 'OSMANİYE', 'DÜZCE']

    ssid = raw_input("SSID : ") # Kullanıcıdan SSID için bir değer istiyoruz.
    wifi.append(ssid)                # Başta oluşturduğumuz 'wifi' listesine, kullanıcıdan değer alındıktan sonra ssid değişkenimizi ekliyoruz.
    if ssid != ssid.upper():           #Girilen değerin bütün harfleri BÜYÜK değilse
        wifi.append(ssid.upper())  ## Tüm harfleri BÜYÜK halinide ekle
    if ssid != ssid.lower():            #Girilen değerin bütün harfleri KÜÇÜK değilse
        wifi.append(ssid.lower())   ## Tüm harfleri KÜÇÜK halinide ekle
    print ('%s [!]Aşağıdakilerden sahip olmadığınız bilgilere \"-\" değerini giriniz %s' % (fg(3), attr(0)))
    print ('%sSistem Sahibinin%s;' % (fg(2), attr(0)))
    ad = raw_input("Adı : ")
    if ad != "-":
        wifi.append(ad)
        if ad != ad.upper():
            wifi.append(ad.upper())
        if ad != ad.lower:
            wifi.append(ad.lower())
    soyad = raw_input("Soyadı : ")
    if soyad != "-":
        wifi.append(soyad)
        if soyad != soyad.upper():
            wifi.append(soyad.upper())
        if soyad != soyad.lower:
            wifi.append(soyad.lower())
    dogumGun = raw_input("Doğum Tarihi (GÜN) : ")
    if dogumGun != "-":
        wifi.append(str(dogumGun))
    dogumAy = raw_input("Doğum Tarihi (AY) : ")
    if dogumAy != "-":
        wifi.append(str(dogumAy))
    dogumYil = raw_input("Doğum Tarihi (YIL) : ")
    if dogumYil != "-":
        wifi.append(str(dogumYil))
    sehir = raw_input("Yaşadığı Şehir : ")
    if sehir != "-":
        wifi.append(sehir)
        if sehir != sehir.upper():
            wifi.append(sehir.upper())
        if sehir != sehir.lower():
            wifi.append(sehir.lower())
        sehirPlaka = sehirler.index(sehir.upper()) + 1
        if sehirPlaka < 10:
            sehirPlaka = '0' + str(sehirPlaka)
        wifi.append(str(sehirPlaka))
    memleket = raw_input("Memleketi : ")
    if memleket != "-":
        wifi.append(memleket)
        if memleket != memleket.upper():
            wifi.append(memleket.upper())
        if memleket != memleket.lower():
            wifi.append(memleket.lower())
        memleketPlaka = sehirler.index(memleket.upper()) + 1
        if memleketPlaka < 10:
            memleketPlaka = '0' + str(memleketPlaka)
        wifi.append(str(memleketPlaka))

    cocuk1Kontrol = ""
    while cocuk1Kontrol.upper() != "E" and cocuk1Kontrol.upper() != "H": 
        cocuk1Kontrol = raw_input("Çocuğu var mı ? (E/h) ")
        if cocuk1Kontrol.upper() == "E":
            print ('%s [!]Aşağıdakilerden sahip olmadığınız bilgilere \"-\" değerini giriniz %s' % (fg(3), attr(0)))
            print ('%sÇocuğun%s;' % (fg(2), attr(0)))
            c1Adi = raw_input("Adı : ")
            if c1Adi != "-":
                wifi.append(c1Adi)
                if c1Adi != c1Adi.upper():
                    wifi.append(c1Adi.upper())
                if c1Adi != c1Adi.lower():
                    wifi.append(c1Adi.lower())
            c1Adi2 = raw_input("İkinci Adı : ")
            if c1Adi2 != "-":
                wifi.append(c1Adi2)
                if c1Adi2 != c1Adi2.upper():
                    wifi.append(c1Adi2.upper())
                if c1Adi2 != c1Adi2.lower():
                    wifi.append(c1Adi2.lower())
            c1dogumGun = raw_input("Doğum Tarihi (GÜN) : ")
            if c1dogumGun != "-":
                wifi.append(c1dogumGun)
            c1dogumAy = raw_input("Doğum Tarihi (AY) : ")
            if c1dogumAy != "-":
                wifi.append(c1dogumAy)
            c1dogumYil = raw_input("Doğum Tarihi (YIL) : ")
            if c1dogumYil != "-":
                wifi.append(c1dogumYil)
            cocuk2Kontrol = ""
            
            print ('%sSistem Sahibinin%s;' % (fg(2), attr(0)))
            while cocuk2Kontrol.upper() != "E" and cocuk2Kontrol.upper() != "H":
                cocuk2Kontrol = raw_input("2. Çocuğu var mı ? (E/h) ")
                if cocuk2Kontrol.upper() == "E":
                    print ('%s [!]Aşağıdakilerden sahip olmadığınız bilgilere \"-\" değerini giriniz %s' % (fg(3), attr(0)))
                    print ('%sÇocuğun (2)%s;' % (fg(2), attr(0)))
                    c2Adi = raw_input("Adı : ")
                    if c2Adi != "-":
                        wifi.append(c2Adi)
                        if c2Adi != c2Adi.upper():
                            wifi.append(c2Adi.upper())
                        if c2Adi != c2Adi.lower():
                            wifi.append(c2Adi.lower())
                    c2Adi2 = raw_input("İkinci Adı : ")
                    if c2Adi2 != "-":
                        wifi.append(c2Adi2)
                        if c2Adi2 != c2Adi2.upper():
                            wifi.append(c2Adi2.upper())
                        if c2Adi2 != c2Adi2.lower():
                            wifi.append(c2Adi2.lower())
                    c2dogumGun = raw_input("Doğum Tarihi (GÜN) : ")
                    if c2dogumGun != "-":
                        wifi.append(c2dogumGun)
                    c2dogumAy = raw_input("Doğum Tarihi (AY) : ")
                    if c2dogumAy != "-":
                        wifi.append(c2dogumAy)
                    c2dogumYil = raw_input("Doğum Tarihi (YIL) : ")
                    if c2dogumYil != "-":
                        wifi.append(c2dogumYil)
                        
                    print ('%sSistem Sahibinin%s;' % (fg(2), attr(0)))
                    while cocuk3Kontrol.upper() != "E" and cocuk3Kontrol.upper() != "H":
                        cocuk3Kontrol = raw_input("3. Çocuğu var mı ? (E/h) ")
                        if cocuk3Kontrol.upper() == "E":
                            print ('%s [!]Aşağıdakilerden sahip olmadığınız bilgilere \"-\" değerini giriniz %s' % (fg(3), attr(0)))
                            print ('%sÇocuğun (2)%s;' % (fg(2), attr(0)))
                            c3Adi = raw_input("Adı : ")
                            if c3Adi != "-":
                                wifi.append(c3Adi)
                                if c3Adi != c3Adi.upper():
                                    wifi.append(c3Adi.upper())
                                if c3Adi != c3Adi.lower():
                                    wifi.append(c3Adi.lower())
                            c3Adi2 = raw_input("İkinci Adı : ")
                            if c3Adi2 != "-":
                                wifi.append(c3Adi2)
                                if c3Adi2 != c3Adi2.upper():
                                    wifi.append(c2Adi2.upper())
                                if c3Adi2 != c3Adi2.lower():
                                    wifi.append(c3Adi2.lower())
                            c3dogumGun = raw_input("Doğum Tarihi (GÜN) : ")
                            if c3dogumGun != "-":
                                wifi.append(c3dogumGun)
                            c3dogumAy = raw_input("Doğum Tarihi (AY) : ")
                            if c3dogumAy != "-":
                                wifi.append(c3dogumAy)
                            c3dogumYil = raw_input("Doğum Tarihi (YIL) : ")
                            if c3dogumYil != "-":
                                wifi.append(c3dogumYil)   

    hayvanKontrol = ""
    print ('%sSistem Sahibinin%s;' % (fg(2), attr(0)))
    while hayvanKontrol.upper() != "E" and hayvanKontrol.upper() != "H":
        hayvanKontrol = raw_input("Evcil hayvanı var mı ? (E/h) ")
        if hayvanKontrol.upper() == "E":
            print ('%sEvcil Hayvanın%s;' % (fg(2), attr(0)))
            hayvanAd = raw_input("Adı : ")
            if hayvanAd != "-":
                wifi.append(hayvanAd)
                if hayvanAd != hayvanAd.upper():
                    wifi.append(hayvanAd.upper())
                if hayvanAd != hayvanAd.lower():
                    wifi.append(hayvanAd.lower())

    dosya = raw_input("dosya adı : ")
    print("%sTavsiye edilen en büyük değer : 5%s"  % (fg(48), attr(0)))
    comb = input("%s(Bütün kombinasyonlar için \"0\")%s\nKaç kombinasyon oluşturulsun ? " % (fg(1), attr(0)))
    if comb == 0:
        hepsi = len(wifi)
        print("%s[!]DİKKAT%s" % (fg(1), attr(0)))
        devammi = ""
        while devammi.upper() != "E" and devammi.upper() != "H":
            print(str(hepsi) + "%sFarklı değer var, bütün kombinasyonları kullanmak gereksiz olacak ve sistemi aşırı derecede yoracaktır.%s" % (fg(125), attr(0)))
            devammi = raw_input("Yinede devam etmek istiyor musunuz ? (E/h) ")
            if devammi.upper() == "E":
                comb = hepsi
            elif devammi.upper() == "H":
                comb = input("Kaç kombinasyon oluşturulsun ? ")
    D = open(dosya + '.txt', 'a')        
    for wl in itertools.product(wifi, repeat=comb):
        print ''.join(wl)
        D.write(''.join(wl) + '\n')

elif hedef == 2: # Web Uygulaması
    print"Web Uygulaması şuan için pasiftir."
    

    
        
    

