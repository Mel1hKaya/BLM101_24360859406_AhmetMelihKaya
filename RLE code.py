def rle_encode(data):
    #hata almamak için güvenlik kontrolü
    if not data:
        return ""

    encode = ""
    bakılan_harf = data[0]
    sayac = 1
    
    #sıkıştırma döngüsü
    for i in range(1, len(data)):
        if data[i] == bakılan_harf:
            sayac += 1
        else:
            encode += str(sayac) + bakılan_harf
            bakılan_harf = data[i]
            sayac = 1
    
    # Son grup için döngüden çıktıktan sonra encode metinine ekleme
    encode += str(sayac) + bakılan_harf
    #Fonksiyon sonucunu döndürür.
    return encode

def rle_decode(data):
    #hata almamak için güvenlik kontrolü
    if not data:
        return""
    decode = ""
    sayac = ""
    #verideki her karakteri tek tek inceleme
    for char in data:
        #bir stringin içeriğinin tamamen rakamlardan oluşup
        #oluşmadığını kontrol etme (rakam:true  diğer:false)
        if char.isdigit():
            sayac += char
        else:
            decode += char * int(sayac)
            sayac = ""
    return decode

            

# Test 
orijinal_metin = input("sıkıştırmak istediğiniz metni girin: ")
sıkıştırılmış = rle_encode(orijinal_metin)
geri_açılmış = rle_decode(sıkıştırılmış)

#yüzde hesaplama
yüzde = 0
o = len(orijinal_metin)
s = len(sıkıştırılmış)
if(o>0):
    yüzde = (s / o) * 100

print(f"Orijinal: {orijinal_metin}")
print(f"Sıkıştırılmış: {sıkıştırılmış}")
print(f"Sıkıştırma yüzdesi: %{yüzde}")
print(f"Geri Açılmış: {geri_açılmış}")