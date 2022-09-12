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

