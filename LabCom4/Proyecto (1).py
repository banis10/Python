import cv2, pytesseract, sqlite3, os
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
def voz(texto):
    import pyttsx3
    engine = pyttsx3.init()
    engine.setProperty("rate",150)
    engine.say(texto)
    engine.runAndWait()

def escuchar():
    import speech_recognition as sr
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print('Por favor diga su respuesta')
        audio = r.listen(source)
        vac = ''
        try:
            rec = r.recognize_google(audio, language='es-ES')
            print('Escuchado = : {}'.format(rec))
            vac = rec.split()
        except:
            print('Por favor, repita su respuesta')
    return vac


def fvacuna():
    voz('¿Para que tipo de vacuna viene?. Moderna, Astrazeneca, Sputnik, o Faiser')
    escuchado = ' '
    vacuna = ' '
    escuchado=escuchar()
    escuchado=str(escuchado)
    escuchado = escuchado.lower()
    # print(escuchado)
    if 'moderna' in escuchado:
        voz('  Viene para la vacuna moderna.')
        vacuna = 'Moderna'
    elif 'astrazeneca' in escuchado:
        voz('  Viene para la vacuna astrazeneca.') 
        vacuna = 'Astrazeneca'
    elif 'sputnik' in escuchado:
        voz('  Viene para la vacuna Sputnik')
        vacuna = 'SputnikV'
    elif 'pfizer' in escuchado:
        voz('  Viene para la vacuna Faiser')
        vacuna = 'Pfizer'
    elif 'fiser' in escuchado:
        voz('  Viene para la vacuna Faiser')
        vacuna = 'Pfizer'
    elif 'fisher' in escuchado:
        voz('  Viene para la vacuna Faiser')
        vacuna = 'Pfizer'
    elif 'freezer' in escuchado:
        voz('  Viene para la vacuna Faiser')
        vacuna = 'Pfizer'
    elif 'teaser' in escuchado:
        voz('  Viene para la vacuna Faiser')
        vacuna = 'Pfizer'
    else:
        voz('Por favor, repita su respuesta')
    return vacuna


def fdosis():
    voz('¿Viene para la primera o segunda dosis')
    escuchado = ' '
    dosis = ' '
    escuchado=escuchar()
    escuchado=str(escuchado)
    escuchado = escuchado.lower()
    # print(escuchado)
    if 'primera' in escuchado:
        voz('  Viene para la primera dosis')
        dosis = 'Primera'
    elif 'segunda' in escuchado:
        voz('  Viene para la segunda dosis') 
        dosis = 'Segunda'
    else:
        voz('Por favor, repita su respuesta')
    return dosis

def fmodulo(vacuna,dosis): 
    if vacuna == 'Moderna' and dosis == 'Primera':
        voz('Por favor dirijase al modulo, A')

    if vacuna == 'Moderna' and dosis == 'Segunda':
        voz ('Por favor dirijase al modulo, B')

    if vacuna == "Astrazeneca" and dosis == 'Primera':
        voz ('Por favor dirijase al modulo, C')

    if vacuna == 'Astrazeneca' and dosis == 'Segunda':
        voz ('Por favor dirijase al modulo, D')

    if vacuna =='SputnikV' and dosis == 'Primera':
        voz ('Por favor dirijase al modulo, E')

    if vacuna =='SputnikV' and dosis == 'Segunda':
        voz ('Por favor dirijase al modulo, F')

    if vacuna == 'Pfizer' and dosis == 'Primera':
        voz ('Por favor dirijase al modulo, G')
    
    if vacuna == 'Pfizer' and dosis == 'Segunda':
        voz ('Por favor dirijase al modulo, H')

vacunas = ('Moderna','Astrazeneca','Pfizer','SputnikV')
dosis1 = ('Primera','Segunda')

def proyecto():
    n = True
    while n == True:
        vacuna = fvacuna()
        if vacuna in vacunas:
            n = False
        else:
            n = True
    k = True
    while k == True:
        dosis = fdosis()
        if dosis in dosis1:
            k = False
        else:
            k = True
    # print(vacuna, dosis)
    fmodulo(vacuna,dosis)
    return vacuna,dosis

##################################################

voz('Buen día, por favor coloque su DPI')
################Analisis Imagen###################
image = cv2.imread('DPI.JPG')
imageout = image[250:320,5:400]
text = str(((pytesseract.image_to_string(imageout,lang='spa'))))
text = text.replace('\n', ' ')
text = text.replace('', ' ')
print('CUI: '+ text)
imageout2= image [240:320,440:700]
text2 = str(((pytesseract.image_to_string(imageout2,lang='spa'))))
text2 = text2.replace('\n', ' ')
text2 = text2.replace('', ' ')
print('Nombre: '+text2)
imageout3= image [350:440,440:700]
text3 = str(((pytesseract.image_to_string(imageout3,lang='spa'))))
text3 = text3.replace('\n', ' ')
text3 = text3.replace('', ' ')
print('Apellido: '+text3)
imageout4= image [490:550,440:650]
text4 = str(((pytesseract.image_to_string(imageout4,lang='spa'))))
text4 = text4.replace('\n', ' ')
text4 = text4.replace('', ' ')
print('Nacionalidad: '+text4)
imageout5= image [570:620,440:750]
text5 = str(((pytesseract.image_to_string(imageout5,lang='spa'))))
text5 = text5.replace('\n', ' ')
text5 = text5.replace('', ' ')
print('Sexo: '+text5)
imageout6= image [650:700,555:700]
text6 = str(((pytesseract.image_to_string(imageout6,lang='spa'))))
text6 = text6.replace('\n', ' ')
text6 = text6.replace('', ' ')
text6 = str(2021 - int(text6))
print(text6)
#cv2.imshow('Image rotated by 90 degrees',imageout6)
#cv2.waitKey(0) 
#cv2.destroyAllWindows()
vacuna,dosis = proyecto()
######################BBDD########################
Conexion = sqlite3.connect("BBDDCovid")
Cursor = Conexion.cursor()
Cursor.execute("CREATE TABLE IF NOT EXISTS CIUDADANOS (CUI VARCHAR(50), Nombre VARCHAR(50), Apellido VARCHAR(50), Nacionalidad VARCHAR(50), Sexo VARCHAR(50), Edad VARCHAR(50), Vacuna VARCHAR(50), Dosis VARCHAR(50))")
Cursor.execute("INSERT INTO CIUDADANOS VALUES ('"+text+"', '"+text2+"', '"+text3+"', '"+text4+"', '"+text5+"', '"+text6+"','"+vacuna+"','"+dosis+"')")
Conexion.commit()
Conexion.close()