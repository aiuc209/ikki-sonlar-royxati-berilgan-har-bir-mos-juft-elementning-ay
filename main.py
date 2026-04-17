# Ikki sonlar ro‘yxati berilgan. Har bir mos juft elementning ayirmasini hisoblang (a - b).
def sonlar_ayirmani_hesobla(sonlar1, sonlar2):
    return [a - b for a, b in zip(sonlar1, sonlar2)]

# Talabalar ismlari va ularning ballari (ikki ro‘yxat). Har biriga "Ism — Ball ball" formatida satr yarating.
def talabalar_bilgi(talabalar, ballar):
    return [f"{talaba} — {ball} ball" for talaba, ball in zip(talabalar, ballar)]

# Ikki ro‘yxat: narxlar va chegirmalar foizda. Har bir mahsulotning chegirmadan keyingi narxini hisoblang.
def narxlar_chegirmasi(narxlar, chegirmalar):
    return [narx * (1 - chegirma / 100) for narx, chegirma in zip(narxlar, chegirmalar)]

# Nuqtalar ro‘yxati [(x1,y1), (x2,y2), ...]. Har bir nuqtaning x va y koordinatalarining yig‘indisini toping.
def nuqtalar_yigindisi(nuqtalar):
    return [x + y for x, y in nuqtalar]

# Satrlar ro‘yxati va ularning kerakli uzunliklari (ikki ro‘yxat). Har bir satrni berilgan uzunlikka qisqartiring yoki bo‘sh joy qo‘shib to‘ldiring.
def satrlar_uzunligi(satrlar, uzunliklar):
    return [satr.ljust(uzunlik) for satr, uzunlik in zip(satrlar, uzunliklar)]

# Ro‘yxat ichidagi tuplar: [(ism, yosh), ...]. Har biriga "Ism yoshda" formatida satr yarating.
def ism_yosh(tuplar):
    return [f"{ism} {yosh} yoshda" for ism, yosh in tuplar]

# Ikki ro‘yxat: uzunliklar (metr) va kengliklar. Har birining yuzasini (length * width) hisoblang.
def yuzalar_uzunlik_kenglik(uzunliklar, kengliklar):
    return [uzunlik * kenglik for uzunlik, kenglik in zip(uzunliklar, kengliklar)]

# Fayl nomlari ro‘yxati. Har bir fayl nomiga ".bak" qo‘shib, backup nomini yarating.
def fayl_backup(fayllar):
    return [fayl + ".bak" for fayl in fayllar]

# Ikki ro‘yxat: kalitlar va qiymatlar. Ulardan map orqali juftliklar yarating va dict ga aylantiring.
def kalit_qiymat(kalitlar, qiymatlar):
    return dict(zip(kalitlar, qiymatlar))

# Haroratlar (Celsiy) va shahar nomlari. Har biriga "Shahar: XX.X °C (Farengeyt: YY.Y °F)" formatida chiqaring.
def harorat_shahar(haroratlar, shaharlar):
    return [f"{shahar}: {harorat} °C (Farengeyt: {(harorat * 9/5) + 32} °F)" for harorat, shahar in zip(haroratlar, shaharlar)]

# Nested ro‘yxat: [[1,2,3], [4,5], [6]]. Har bir ichki ro‘yxatning o‘rtacha qiymatini hisoblang.
def oortacha_qiymat(roxyat):
    return [sum(ichki_roxyat) / len(ichki_roxyat) for ichki_roxyat in roxyat]

# Foydalanuvchi nomlari ro‘yxati. Har biriga "@" qo‘shib va pastki chiziq bilan username yarating (masalan: "ali" → "@ali_user").
def foydalanuvchi_nomi(foydalanuvchilar):
    return [f"@{foydalanuvchi}_user" for foydalanuvchi in foydalanuvchilar]

# Ikki son ro‘yxati. Har bir juft elementning ko‘paytmasini hisoblang va natijani 10 ga bo‘ling.
def sonlar_kopaytmasi(sonlar1, sonlar2):
    return [(son1 * son2) / 10 for son1, son2 in zip(sonlar1, sonlar2)]

# Matnlar ro‘yxati. Har bir matndan faqat harflarni qoldirib, katta harflarga aylantiring (raqam va belgilarni olib tashlang).
def matn_harflar(matnlar):
    return ["".join([harf for harf in matn if harf.isalpha()]).upper() for matn in matnlar]

# RGB ranglar ro‘yxati [(r,g,b), ...]. Har birini HEX formatga aylantiring (masalan: (255,0,0) → "#FF0000").
def rgb_hex(rgb_ranglar):
    return [f"#{r:02X}{g:02X}{b:02X}" for r, g, b in rgb_ranglar]

# So‘zlar ro‘yxati va ularning chastotalari (ikki ro‘yxat). Har birini "so‘z (chastota marta)" ko‘rinishida chiqaring.
def soz_chastota(sozlar, chastotalar):
    return [f"{soz} ({chastota} marta)" for soz, chastota in zip(sozlar, chastotalar)]

# Ro‘yxatdagi elementlar (aralash son va satr). Agar son bo‘lsa kvadrat, satr bo‘lsa uzunligini hisoblang.
def element_kvadrat_uzunlik(elementlar):
    return [element ** 2 if isinstance(element, (int, float)) else len(element) for element in elementlar]

# URL lar ro‘yxati. Har bir URL dan protokolni ajratib oling ("https://", "http://").
def url_protokol(url_lar):
    return [url.split("://")[0] for url in url_lar]

# Baholar ro‘yxati (0-100). Har bir bahoni 5 ballik tizimda harf bahosiga aylantiring (A, B, C, D, F).
def baho_harf(baholar):
    return ["A" if baho >= 90 else "B" if baho >= 80 else "C" if baho >= 70 else "D" if baho >= 60 else "F" for baho in baholar]

# Ismlar va familiyalar (ikki ro‘yxat). Ularni birlashtirib "Familiya, Ism" formatida chiqaring.
def ism_familiya(ismlar, familiyalar):
    return [f"{familiya}, {ism}" for ism, familiya in zip(ismlar, familiyalar)]

# Ikki ro‘yxat: vazn (kg) va bo‘y (metr). Har birining BMI (vazn / bo‘y²) ni hisoblang.
def bmi_hesobla(vaznlar, boylar):
    return [vazn / (boy ** 2) for vazn, boy in zip(vaznlar, boylar)]

# Satrlar ro‘yxati. Har bir satrni so‘zlarga bo‘lib, birinchi harfini katta qiling (title case).
def satr_title_case(satrlar):
    return [" ".join([soz.capitalize() for soz in satr.split()]) for satr in satrlar]

# Ro‘yxat ichidagi ro‘yxatlar. Har bir ichki ro‘yxatning maksimal elementini toping.
def ichki_roxyat_max(roxyat):
    return [max(ichki_roxyat) for ichki_roxyat in roxyat]

# Mahsulot nomlari va stok miqdorlari. Agar stok < 10 bo‘lsa "Kam stok", aks holda "Normal" deb belgilang.
def stok_belgilash(mahsulotlar, stoklar):
    return ["Kam stok" if stok < 10 else "Normal" for mahsulot, stok in zip(mahsulotlar, stoklar)]

# Ikki ro‘yxat: a va b. Har bir juft element uchun (a[i] ** 2 + b[i] ** 2) ni hisoblang.
def a_b_hesobla(a_lar, b_lar):
    return [a ** 2 + b ** 2 for a, b in zip(a_lar, b_lar)]

# Email manzillar ro‘yxati. Har biridan domen nomini ajratib oling (@ dan keyingi qism).
def email_domen(email_lar):
    return [email.split("@")[1] for email in email_lar]

# Sonlar ro‘yxati. Har bir sonni uning raqamlar yig‘indisi bo‘yicha saralash uchun kalit sifatida ishlating (map orqali kalit yarating).
def son_raqamlar_yigindisi(sonlar):
    return [sum(int(raqam) for raqam in str(son)) for son in sonlar]

# Tuplar ro‘yxati: (ism, ball1, ball2). Har bir talabaning o‘rtacha ballini hisoblang.
def talaba_ortacha_ball(tuplar):
    return [(ball1 + ball2) / 2 for _, ball1, ball2 in tuplar]

# Satrlar ro‘yxati. Har bir satrni teskari tartibda yozib, oxiriga "!" qo‘shing.
def satr_teskari(satrlar):
    return [satr[::-1] + "!" for satr in satrlar]

# Ikki ro‘yxat: narx va miqdor. Har bir mahsulotning umumiy summasini (narx * miqdor) hisoblang.
def narx_miqdor(narxlar, miqdorlar):
    return [narx * miqdor for narx, miqdor in zip(narxlar, miqdorlar)]

# Ro‘yxatdagi sonlar. Har bir sonni 0 dan 100 gacha bo‘lgan oraliqqa cheklang (min(100, max(0, son))).
def son_cheklang(sonlar):
    return [min(100, max(0, son)) for son in sonlar]

# Ismlar ro‘yxati. Har bir ismni uzunligiga qarab "Qisqa ism" yoki "Uzun ism" deb tasniflang.
def ism_tasnif(ismlar):
    return ["Qisqa ism" if len(ism) <= 5 else "Uzun ism" for ism in ismlar]

# Koordinatalar va radiuslar (ikki ro‘yxat). Har bir doiraning yuzasini hisoblang (πr²).
def doira_yuzasi(koordinatalar, radiuslar):
    import math
    return [math.pi * (radius ** 2) for _, radius in zip(koordinatalar, radiuslar)]

# Matnlar ro‘yxati. Har bir matndagi bo‘sh joylar sonini hisoblang.
def matn_bosh_joy(matnlar):
    return [matn.count(" ") for matn in matnlar]

# Ikki ro‘yxat: yillar va voqealar. Har biriga "Yil — Voqea" formatida satr yarating.
def yil_voqea(yillar, voqealar):
    return [f"{yil} — {voqea}" for yil, voqea in zip(yillar, voqealar)]

# Sonlar ro‘yxati. Har bir sonni ikkilik sanoq tizimiga o‘tkazib, "0b" prefiksini olib tashlang.
def son_ikkilik(sonlar):
    return [bin(son)[2:] for son in sonlar]

# Nested dict lar ro‘yxati (masalan: [{'name': 'Ali', 'age': 25}, ...]). Har biridan faqat ism va yoshni olib, yangi tuple yarating.
def dict_tuple(dict_lar):
    return [(d["name"], d["age"]) for d in dict_lar]

# Satrlar ro‘yxati. Har bir satrni vowel (unli) harflarni "*" bilan almashtiring.
def satr_unli(satrlar):
    unli_harflar = "aeiouAEIOU"
    return ["".join([harf if harf not in unli_harflar else "*" for harf in satr]) for satr in satrlar]

# Ikki ro‘yxat: son va ularning kuchlari. Har bir sonni berilgan kuch darajasiga ko‘taring (x ** power).
def son_kuch(sonlar, kuchlar):
    return [son ** kuch for son, kuch in zip(sonlar, kuchlar)]

# Fayl yo‘llari ro‘yxati. Har biridan faqat fayl nomini (oxirgi qism) ajratib oling.
def fayl_nomi(fayl_yollari):
    return [fayl_yol.split("/")[-1] for fayl_yol in fayl_yollari]

# Baholar ro‘yxati. Har bir bahoni 10 ballik shkala bo‘yicha normallashtiring (bahoni 10 ga bo‘lish).
def baho_normallashtir(baholar):
    return [baho / 10 for baho in baholar]

# Ismlar va jinslar (ikki ro‘yxat). Har biriga "Mr." yoki "Ms." qo‘shib chiqaring.
def ism_jins(ismlar, jinslar):
    return [f"Mr. {ism}" if jins == "erkak" else f"Ms. {ism}" for ism, jins in zip(ismlar, jinslar)]

# Ro‘yxat ichidagi tuplar. Har bir tuplening elementlarini ko‘paytiring.
def tupla_ko-paytma(tuplar):
    return [tup[0] * tup[1] for tup in tuplar]

# Matnlar ro‘yxati. Har bir matnni so‘zlar soniga qarab "Qisqa", "O‘rta" yoki "Uzun" deb belgilang.
def matn_uzunligi(matnlar):
    return ["Qisqa" if len(matn.split()) <= 5 else "O‘rta" if len(matn.split()) <= 10 else "Uzun" for matn in matnlar]

# Ikki son ro‘yxati. Har bir juft element uchun GCD (eng katta umumiy bo‘luvchi) ni hisoblang.
def gcd_hesobla(sonlar1, sonlar2):
    import math
    return [math.gcd(son1, son2) for son1, son2 in zip(sonlar1, sonlar2)]

# Rang nomlari va RGB qiymatlari. Har birini "Rang: (R,G,B)" formatida chiqaring.
def rang_rgb(ranglar, rgb_lar):
    return [f"{rang}: ({rgb[0]},{rgb[1]},{rgb[2]})" for rang, rgb in zip(ranglar, rgb_lar)]

# Sonlar ro‘yxati. Har bir sonni uning eng yaqin tub songa aylantiring (oddiy funksiya yozib map qiling).
def son_tub_son(sonlar):
    def eng_yaqin_tub_son(son):
        tub_sonlar = [i for i in range(1, son + 1) if all(i % j != 0 for j in range(2, int(i ** 0.5) + 1))]
        return min(tub_sonlar, key=lambda x:abs(x-son))
    return [eng_yaqin_tub_son(son) for son in sonlar]

# Satrlar ro‘yxati. Har bir satrni Unicode kodlariga aylantiring (ord() bilan).
def satr_unicode(satrlar):
    return [[ord(harf) for harf in satr] for satr in satrlar]

# Ikki ro‘yxat: boshlang‘ich va tugash vaqtlari (sekundlarda). Har birining davomiyligini hisoblang.
def vaqt_davomiyligi(boshlangich_vaqtlar, tugash_vaqtlari):
    return [tugash - boshlangich for boshlangich, tugash in zip(boshlangich_vaqtlar, tugash_vaqtlari)]

# Foydalanuvchi ma’lumotlari (nested list). Har bir foydalanuvchining "Ism Familiya — Yosh yosh" formatida satr yarating.
def foydalanuvchi_ma-lumot(foydalanuvchilar):
    return [f"{ism} {familiya} — {yosh} yosh" for ism, familiya, yosh in foydalanuvchilar]
