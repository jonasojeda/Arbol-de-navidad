import os
import time
def saludo(color):
    print("")
    print(" ")
    print("__________(█)           :::::::::: :::::::::: :::        ::::::::::: :::::::::")
    print("_______██████           :+:        :+:        :+:            :+:          :+: ")
    print(" _____ ████████         +:+        +:+        +:+            +:+         +:+ ")
    print("___███████████          :#::+::#   +#++:++#   +#+            +#+        +#+")
    print("___(░░░░░░░)░░░)        +#+        +#+        +#+            +#+       +#+")
    print("___(░(░█░░█░)░░░)       #+#        #+#        #+#            #+#      #+#")
    print("__(░░(░░●░░░)░░░)       ###        ########## ########## ########### #########")
    print(" __(░░░░◡░░)░░░░)")
    print(" _██(░░░░░░░░░░)██")
    print(" _███(░░░░░░░░░)███          ::::    :::     :::     :::     ::: ::::::::::: :::::::::      :::     :::::::::")
    print( "████ ██(░░░)██ ████          :+:+:   :+:   :+: :+:   :+:     :+:     :+:     :+:    :+:   :+: :+:   :+:    :+:")
    print("  ████ █████████ ███         :+:+:+  +:+  +:+   +:+  +:+     +:+     +:+     +:+    +:+  +:+   +:+  +:+    +:+")
    print("  ████ ████░████ ███         +#+ +:+ +#+ +#++:++#++: +#+     +:+     +#+     +#+    +:+ +#++:++#++: +#+    +:+")
    print(" (░░)_▓▓▓▓▌▓▐▓▓▓_(░░)        +#+  +#+#+# +#+     +#+  +#+   +#+      +#+     +#+    +#+ +#+     +#+ +#+    +#+")
    print("(██) ███████████ (██)        #+#   #+#+# #+#     #+#   #+#+#+#       #+#     #+#    #+# #+#     #+# #+#    #+#")
    print("_____█████░█████_▓▓▓ \       ###    #### ###     ###     ###     ########### #########  ###     ### #########")
    print("_____█████░█████_▓▓▓ \ ")
    print("_____█████-,█████▓▓▓▓▓)")
    print("_____█████-,█████▓▓▓▓▓)")
    print("___(░░░░░░)(░░░░░) ▓▓▓▓)")
    print("______(███)_(███)▓▓▓▓▓▓)")
    print("____(████)_(████)▓▓▓▓▓)")

def estrella(color):
    print(color+"                        /\             ")
    print(color+"                       <  >            ")
    print(color+"                        \/             ")
#descripcion: inserta esferas dentro del arbol
def esfera(color,camb):
    time.sleep(0.10)
    if camb==1:
        print(color.RED+ "( )", end="")
    else:
        print(color.BLUE+"( )",end="")

#descripcion: realiza siclos de iteracion con espacios vacios y '/'
def arbol(espaciosext,espacioint,colores,esf):
    #ESPACIOS EXTERNOS
    i=1
    while i<espaciosext:
        print(" ",end=" ")
        i=i+1

    time.sleep(0.10)
    print(colores.GREEN+" / ",end="")
    i = 1
    camb=2
    #ESPACIOS INTERNOS
    while i<espacioint:
        if i==int(i/2)*2:
            if esf==True:
                if camb==1:
                    esfera(colores, camb)
                    camb=2
                    i=i+2
                elif camb==2:
                    esfera(colores, camb)
                    camb=1
                    i=i+2
        time.sleep(0.10)
        print(colores.GREEN+"V",end=" ")
        i=i+1
    time.sleep(0.10)
    print(colores.GREEN+" \ ")

def tronco(color,n):
    i=0
    while i<n:

        time.sleep(0.10)
        print(color+"                    |||||       ")
        i=i+1

#programa principal
class colores:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    RESET = '\033[39m'
estrella(colores.YELLOW)
i=0
ext=12
inter=0
while i<12:
    esf=False
    if i ==int(i/2)*2:
        esf=True

    arbol(ext,inter,colores,esf)
    ext=ext-1
    inter=inter+2
    i=i+1
tronco(colores.BLACK,3)
time.sleep(1)
saludo(colores)