import os


#ergebnis csv
speicherpfad=os.path.join(os.getcwd(),'..','ergebnis.csv')
ergebnis=open(speicherpfad,'a+')



def durchsuche(path):
    #liste alle dir und files im path auf
    eintraege=os.listdir(path)

    for element in eintraege:
        
        #element als pfad
        elementpfad=os.path.join(path,element)
        #wenn dir durchsuche rekursiv
        if (os.path.isdir(elementpfad)):
            durchsuche(elementpfad)
        #wenn file mit .csv bearbeite und schreib in das ergebnisfile
        if (".csv" in elementpfad or ".CSV" in elementpfad):
            with open(elementpfad,'r') as file:
                temp=file.read()
                #print(temp)
                #schreibe in ergebnisfile
                #ergebnis.write(temp)
                
                ##falls du das zeilenweise einlesen willst
                linecounter=0
                for line in temp:
                    ##übersrpinge die ersten beiden zeilen
                    #n zeilen überspringen
                    n=0
                    if(linecounter>=n):
                        ergebnis.write(line)
                        
                    linecounter+=1
            
                
                    
    

durchsuche(os.getcwd())

ergebnis.close()   
