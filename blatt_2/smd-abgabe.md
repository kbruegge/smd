# SMD-Abgabe
Blatt 2, Kai Brügge (<kai.bruegge@tu-dortmund.de>) und Marian Bruns (<marian.bruns@tu-dortmund.de>)

##Aufgabe 5



![](/Users/Kai/Development/smd/blatt_2/aufgabe_5.png)

### a)

* für $x<10^2$ sind numerisches und algabraisches Ergebnis ungefähr gleich
* Abweichung $<1\%$ liegt im gleichen bereich vor
* für $x>10^{35}$ wird das numerische Ergebis 0

###b)
* Übereinstimmung für $|x|>10^{-4}$
* ebenso
* für $-8\cdot 10^{-6}<x<8\cdot 10^{-6}$ wird das numerische Ergebnis 0

##Aufgabe 6


### a)
Die Gleichung ist numerisch nicht stabil, da für gewisse $\theta$ durch kleine Zahlen geteilt wird.
Beim graphischen Darstellen mit Python ist diese jedoch nicht zu sehen...

Zu erwarten wäre Ungenauigkeit für $\theta$ gegen $n\cdot\pi$, wobei $n$ eine ganze Zahl ist, denn da $\beta\approx1$ ist, geht dann der Nenner gegen 0.

### b)
Umgeformte Funktion:

$\frac{d\sigma}{d\Omega}=\frac{\alpha^2}{s}\left(\frac{2+\sin^2(\theta)}{\frac{1}{\gamma^2}\cos^2(\theta)+\sin^2(\theta)}+\frac{2\sin^4{\theta}}{(\frac{1}{\gamma^2}\cos^2(\theta)+\sin^2(\theta))^2}\right)$

### c)

Was man nicht sieht kann man nicht beheben (ansonsten siehe e) ).

### d)
Konditionszahl nach WolframAlpha wobei x dem Winkel entspricht:

![](/Users/Kai/Development/smd/blatt_2/screenshot.png)

### e)

![](/Users/Kai/Development/smd/blatt_2/aufgabe_6.png)


##Aufgabe 7
![](/Users/Kai/Development/smd/blatt_2/histogram_gewicht.png)
![](/Users/Kai/Development/smd/blatt_2/histogram_groesse.png)
![](/Users/Kai/Development/smd/blatt_2/histogram_log.png)


### a)

* Binning zu fein -> Verteilung nicht erkennbar da Stichprobe zu klein
* Bei der Größe irgendwas zwischen 5 und 15. 
* Beim Gewicht etwa 20 Bins. Wenn weniger Bins gewählt werden ist die Zentrierung nicht erkennbar. 
  
### b)
* Je mehr desto besser
* Unterschiedliche Binanzahl aufgrund unterscheidlicher Streuung (Varianz) der Daten
* Bei Größe Binbreite nicht kleiner als 1.0 cm. Dann ist die Position des i-ten bins zentriert bei (0.5 + 1 * i) cm
* Beim Gewicht Binbreite nicht kleiner als 1.0 kg. Dann ist die Position des i-ten bins zentriert bei (0.5 + 1 * i) kg

### c)
* Bei zu feinem Binning werden niedrige Bins eventuell nicht gefüllt da die Logarithmusfunktion in dem Bereich sehr steil ist.

## Aufgabe 8

* a) 1/9
* b) 1/2
* c) 1/18
* d) 1/36
* e) 1/6
* f) 1/3
* g) 1/6