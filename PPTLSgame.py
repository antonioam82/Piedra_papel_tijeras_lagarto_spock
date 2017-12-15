from VALID import ns
import random
import pickle
import subprocess
            
while True:
    print("JUGANDO A PIEDRA, PAPEL O TIJERAS, LAGARTO, SPOCK")
    Comp=random.choice(["Piedra","Papel","Tijeras","Lagarto","Spock"])#Comp=(ppt(n)).lower()
    Tu=input("Piedra, Papel, Tijeras, Lagarto, Spock: ")
    Tu=Tu.lower()
    while Tu!=("piedra") and Tu!=("papel") and Tu!=("tijeras") and Tu!=("lagarto") and Tu!=("spock"):
        Tu=input("Escribe\'piedra\',\'papel\',\'tijeras\',\'lagarto\' o \'Spock\' según su opción: ")
        Tu=Tu.lower()
    print("Tu:",Tu.upper())
    print("Ordenador:",Comp.upper())
    Comp=Comp.lower()
    
    puntoss=pickle.load(open("marcadorbis.mio","rb"))
    if Tu!=Comp:   #OBVIAMENTE, NECESITO UNA FUNCION QUE SIMPLIQUE ESTE BLOQUE
        if Tu==("papel") and Comp==("tijeras"):
            print("PERDISTE: Las tijeras cortan el papel")
            puntoss[0]=puntoss[0]+1;puntoss[2]=puntoss[2]+1
        if Tu==("papel") and Comp==("piedra"):
            print("GANASTE: El papel envuelve la piedra")
            puntoss[0]=puntoss[0]+1;puntoss[1]=puntoss[1]+1
        if Tu==("piedra") and Comp==("papel"):
            print("PERDISTE: El papel envuelve la piedra")
            puntoss[0]=puntoss[0]+1;puntoss[2]=puntoss[2]+1
        if Tu==("piedra") and Comp==("tijeras"):
            print("GANASTE: La piedra machaca las tijeras")
            puntoss[0]=puntoss[0]+1;puntoss[1]=puntoss[1]+1
        if Tu==("tijeras") and Comp==("piedra"):
            print("PERDISTE: La piedra machaca las tijeras")
            puntoss[0]=puntoss[0]+1;puntoss[2]=puntoss[2]+1
        if Tu==("tijeras") and Comp==("papel"):
            print("GANASTE: Las tijeras cortan el papel")
            puntoss[0]=puntoss[0]+1;puntoss[1]=puntoss[1]+1
        if Tu==("piedra") and Comp==("lagarto"):
            print("GANASTE: La piedra aplasta al lagarto")
            puntoss[0]=puntoss[0]+1;puntoss[1]=puntoss[1]+1
        if Tu==("lagarto") and Comp==("piedra"):
            print("PERDISTE: La piedra aplasta al lagarto")
            puntoss[0]=puntoss[0]+1;puntoss[2]=puntoss[2]+1
        if Tu==("lagarto") and Comp==("spock"):
            print("GANASTE: El lagarto envenena a Spock")
            puntoss[0]=puntoss[0]+1;puntoss[1]=puntoss[1]+1
        if Tu==("spock") and Comp==("lagarto"):
            print("PERDISTE: El lagarto envenena a Spock")
            puntoss[0]=puntoss[0]+1;puntoss[2]=puntoss[2]+1
        if Tu==("spock") and Comp==("tijeras"):
            print("GANASTE: Spock rompe las tijeras")
            puntoss[0]=puntoss[0]+1;puntoss[1]=puntoss[1]+1
        if Tu==("tijeras") and Comp==("spock"):
            print("PERDISTE: Spock rompe las tijeras")
            puntoss[0]=puntoss[0]+1;puntoss[2]=puntoss[2]+1
        if Tu==("tijeras") and Comp==("lagarto"):
            print("GANASTE: Las tijeras decapitan al lagarto")
            puntoss[0]=puntoss[0]+1;puntoss[1]=puntoss[1]+1
        if Tu==("lagarto") and Comp==("tijeras"):
            print("PERDISTE: Las tijeras decapitan al lagarto")
            puntoss[0]=puntoss[0]+1;puntoss[2]=puntoss[2]+1
        if Tu==("lagarto") and Comp==("papel"):
            print("GANASTE: El lagarto devora el papel")
            puntoss[0]=puntoss[0]+1;puntoss[1]=puntoss[1]+1
        if Tu==("papel") and Comp==("lagarto"):
            print("PERDISTE:  El lagarto devora el papel")
            puntoss[0]=puntoss[0]+1;puntoss[2]=puntoss[2]+1
        if Tu==("papel") and Comp==("spock"):
            print("GANASTE: papel desautoriza a Spock")
            puntoss[0]=puntoss[0]+1;puntoss[1]=puntoss[1]+1
        if Tu==("spock") and Comp==("papel"):
            print("PERDISTE: papel desautoriza a Spock")
            puntoss[0]=puntoss[0]+1;puntoss[2]=puntoss[2]+1
        if Tu==("spock") and Comp==("piedra"):
            print("GANASTE: Spock vaporiza piedra")
            puntoss[0]=puntoss[0]+1;puntoss[1]=puntoss[1]+1
        if Tu==("piedra") and Comp==("spock"):
            print("PERDISTE: Spock vaporiza piedra")
            puntoss[0]=puntoss[0]+1;puntoss[2]=puntoss[2]+1
             
    else:
        print("EMPATE")
        puntoss[0]=puntoss[0]+1;puntoss[3]=puntoss[3]+1
    pickle.dump(puntoss,open("marcadorbis.mio","wb"))
    Res=input("¿Desea ver la puntuación actual?: ")
    if Res!=("C"):
        Res=ns(Res)
    else:
        puntoss=pickle.load(open("marcadorbis.mio","rb"))#PONER A 0 EL MARCADOR
        puntoss[0]=0;puntoss[1]=0;puntoss[2]=0;puntoss[3]=0
        pickle.dump(puntoss,open("marcadorbis.mio","wb"))
    if Res==("s"):
        print("PARTIDAS JUGADAS:",puntoss[0],"GANADAS:",puntoss[1],"PERDIDAS:",puntoss[2],"EMPATES:",puntoss[3])
    C=ns(input("¿Jugar otra vez?: "))
    if C==("n"):
        break
    else:
        subprocess.call(["cmd.exe","/C","cls"])


