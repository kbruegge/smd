#SMD Blatt 4

Von marian.bruns und kai.bruegge



##Aufgabe 13

#### a) - c)
Was zum Teufel ist dreidimensionales Histogram?
Ich hab Scatterplots gemacht.

![Eine lecker figur!](figure_1.png =500x)

#### e)
Der einfach TRandom von root ist als linear congruential implementiert. Die Ergebnisse sind also ähnlich zu dem selbst gebauten aus a)




##Aufgabe 14

#### a)
Sei die kummulative Verteilung definiert als

$$ F(x) = \int_{\Omega} f(x)$$


Dann ist die Wahrscheinlichkeit dafür das die Variable x einen Wert zwischen den Grenzen c = 1/2 und d = 1/3 annimmt

$$ P(c < x < d) = F(d) - F(c) = \frac{1}{6} $$

#### b) 

Mit Wahrscheinlichkeit 0. Siehe a)

##### c)
Der optimale Zufallsgenerator erzeugt ein Zufälliges Tupel von Bits

Verwendet man 32-bit IEEE Floats erzeugt der Zufallsgenerator somit, unabhängig von der Länge der Mantisse, jedes mögliche Tupel mit der gleichen Wahrscheinlichkeit.
Für 0.5 gibt es nur eine eindeutige Darstellung nach IEEE Standard. Dementsprechend ist die Wahrscheinlichkeit einfach 

$$ P(n) = \frac{1}{2^{32}} $$


#### d)

Die Zahl ist nicht exakt darstellbar im IEEE Standard
Die Wahrscheinlichkeit ist 0

##### e)

Wenn der Startwert auf 0.5*m gesetzt wird, tritt der Wert mindestens einmal auf. Nämlich am Anfang. Alle artefakte in den Histogrammen verschieben sich ebenfalls.

##Aufgabe 16

#### a)
	>>> np.random.random(N)*(x_max-x_min) + x_min

#### b) - d)

Lösung mittels Transformationsmethode. 

##### e)
Einmal würfeln bitte.
##Aufgabe 17

Bilde die Differenz der Binomialverteilung an den Punkten k und k+1

$$ f_p(k+1) - f_p(k+1) = \frac{n!}{k! (n-k)!} p^k (1-p)^{n-k}  (\frac{p}{1-p} \frac{n-k}{k+1}  - 1 ) $$ 

Daraus folgt für k

$$ k = pn - (1 - p) $$

mit entsprechender Rundung.

Bei der Poissonverteilung folgt mit analoger Rechnung

$$k = \lambda $$






