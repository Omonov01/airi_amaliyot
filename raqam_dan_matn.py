### Assalom alaykum bu airi.uz da amaliyot uchun qilinayotgan vazifa. 
### kod yurishi sep_num asosiy funksiya kiritilgan matndan int ,float va strni alohida ajratadi va typeni o'zgartiradi.
### check_float funksiyasi kiritilgan qiymatni aniq son ekanligini tekshiradi va sep_num ga faqat float qiymatni qaytaradi.
### KEYINGI VAZIFALAR  
### 1 text_store ni tugatish bu funksiya matnni olib g' va o' harfini o'z unicodiga o'zgartirib matnni kichraytirib qaytarishi kerak
### 2 num_store funksiya yozish kerak bunda u kiritilgan sonlarni matnga o'zgartirib sep_numga qaytarishi kerak
### va sep_num funksiyasini dfni ochishga to'g'irlash kerak.

### Takliflarni kutaman

#function for check value is float or not
def check_float(value):
    try:
        check = float(value)
        return True
    except ValueError:
        return False
    
#function for restore text
def text_restore(text):
    text = text.replace("g'",)


#function for separate number to text 
def sep_num(text):
    text = text.replace(',',' ')
    for word in text.split():
        if word.isdecimal():
            word = int(word)
        elif check_float(word):
            word = float(word)
        else:
            print(word)
sep_num("salom men sanjar 2000 yilda to'g'ilganman. 12.5 ,13.8")

###################################################################################################
def int_to_en(num):
    d = { 0 : 'nol', 1 : 'bir', 2 : 'ikki', 3 : 'uch', 4 : 'to\'rt', 5 : 'besh',
          6 : 'olti', 7 : 'yetti', 8 : 'sakkiz', 9 : 'to\'qqiz', 10 : 'o\'n',
          11 : 'o\'n_bir', 12 : 'o\'n_ikki', 13 : 'o\'n_uch', 14 : 'o\'n_to\'rt',
          15 : 'o\'n_besh', 16 : 'o\'n_olti', 17 : 'o\'n_yetti', 18 : 'o\'n_sakkiz',
          19 : 'o\'n_to\'qqiz', 20 : 'yigirma',
          30 : 'o\'ttiz', 40 : 'qirq', 50 : 'ellik', 60 : 'oltmish',
          70 : 'yetmish', 80 : 'sakson', 90 : 'to\'qson' }
    k = 1000
    m = k * 1000
    b = m * 1000
    t = b * 1000

    assert(0 <= num)

    if (num < 20):
        return d[num]

    if (num < 100):
        if num % 10 == 0: return d[num]
        else: return d[num // 10 * 10] + ' ' + d[num % 10]

    if (num < k):
        if num % 100 == 0: return d[num // 100] + ' yuz'
        else: return d[num // 100] + ' yuz ' + int_to_en(num % 100)

    if (num < m):
        if num % k == 0: return int_to_en(num // k) + ' ming'
        else: return int_to_en(num // k) + ' ming, ' + int_to_en(num % k)

    if (num < b):
        if (num % m) == 0: return int_to_en(num // m) + ' million'
        else: return int_to_en(num // m) + ' million, ' + int_to_en(num % m)

    if (num < t):
        if (num % b) == 0: return int_to_en(num // b) + ' milliard'
        else: return int_to_en(num // b) + ' milliard, ' + int_to_en(num % b)

    if (num % t == 0): return int_to_en(num // t) + ' trillion'
    else: return int_to_en(num // t) + ' trillion, ' + int_to_en(num % t)

    raise AssertionError('num is too large: %s' % str(num))

print(int_to_en(31))

########################################################################################
def numToWords(num,join=True):
    units = ['','bir','ikki','uch','to\'rt','besh','olti','yetti','sakkiz','to\'qqiz']
    teens = ['','o\'n_bir','o\'n_ikki','o\'n_uch','o\'n_to\'rt','o\'n_besh','o\'n_olti', 'o\'n_yetti','o\'n_sakkiz','o\'n_to\'qqiz']
    tens = ['','o\'n','yigirma','o\'ttiz','qirq','ellik','oltmish','yetmish', 'sakson','to\'qson']
    thousands = ['','ming','million','milliard','trillion','kvadrillion','kvintilion','sekstilion','septillion','oktilion', 'nonillion','dekillion','undekillion','duodekillion', 'tredekillion','quattuordekillion','sexdekillion', 'septendekillion','oktodekillion','novemdekillion', 'vigintillion']
    words = []
    if num==0: words.append('nol')
    else:
        numStr = '%d'%num
        numStrLen = len(numStr)
        groups = (numStrLen+2)//3
        numStr = numStr.zfill(groups*3)
        for i in range(0,groups*3,3):
            h,t,u = int(numStr[i]),int(numStr[i+1]),int(numStr[i+2])
            g = groups-(i//3+1)
            if h>=1:
                words.append(units[h])
                words.append('yuz')
            if t>1:
                words.append(tens[t])
                if u>=1: words.append(units[u])
            elif t==1:
                if u>=1: words.append(teens[u])
                else: words.append(tens[t])
            else:
                if u>=1: words.append(units[u])
            if (g>=1) and ((h+t+u)>0): words.append(thousands[g]+',')
    if join: return ' '.join(words)
    return words
