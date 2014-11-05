#Blatt 2 Notizen

##Aufgabe 5
Alles relativ sinnfrei. Gefragt war der tatsächliche vergleich zwischen 2/3 und dem berechneten wert für versichiedene Werte von x. Das ganze sollte mit irgendweiner funktion erfolgen. Das geht aber garnicht. Schließlich springt diese Differenz.

##Aufgabe 6
Nahe 0 sollte man Stufen sehen in der Funktion. Einfach nahe bei 0 plotten mit sehr sehr vielen Schritten. Wenn man im folgenden bereich plottet sieht man Stufen im plot.

	ts = np.linspace(0, 0.0000001 , 1000)
	
	
![](stufen.png =400x)
	
Zumindest bei double genauigkeit. 

Zum plot für die Konditionszahl lässt sich die funktion eventuell auch numerisch ableiten. Dann muss man nicht diesen riesen Term aus Wolfram plotten.

Durch umformung kann ich die Funktion stabiler machen. Die konditionszahl ändert sich dadurch aber nicht.

##Aufgabe 7 

Ja ne is klar. Für binbreite gibts ein paar faustformeln bei [Wikipedia](http://de.wikipedia.org/wiki/Histogramm#Absch.C3.A4tzung_der_Anzahl_der_Klassen)


##Aufgabe 8

###### a) Mögliche tupel (4,5) (5,4) (3,6) (6,3). Also 4/36 =1/9
###### b) Da haben wir uns wohl verzählt. Es muss gelten P(>= 9) = P(=9) + P(=10) + P(=11) + P(=12) = 10/36

###### c) Is klar jetzt.