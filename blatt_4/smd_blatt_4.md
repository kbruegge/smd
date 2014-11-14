#SMD Blatt 4

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

Wenn der Startwert auf 0.5m gesetzt wird, tritt der Wert mindestens einmal auf. Nämlich am Anfang. 




