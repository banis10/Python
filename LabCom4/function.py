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
    voz('¿Para que tipo de vacuna viene?. Moderna, Astrazeneca, Sputnik o Faiser')
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

def proyecto():
    vacunas = ('Moderna','Astrazeneca','Pfizer','SputnikV')
    dosis1 = ('Primera','Segunda')
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

voz('Buen dia, por favor coloque su DPI')

vacuna,dosis = proyecto()

print(vacuna,dosis)

