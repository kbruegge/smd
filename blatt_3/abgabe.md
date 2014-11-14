#Blatt 3
Abgabe von Marian Bruns <marian.bruns@tu-dortmund.de> und Kai Brügge <kai.bruegge@tu-dortmund.de>

##Aufgabe 9
Die Maxwell-Boltzmann Verteilung. Der Normierungsfaktor N=1 ergibt sich aus dem Integral der Dichtefunktion über dem Gesamten Parameterbereich. Die genauen Rechungen gibts im Anhang Handschriftlich.

#### a)
Die Wahrscheinlichste Geschwindigkeit ist das Maximum der Wahrscheinlichkeitsdichtefunktion (pmf).

$$ \frac{ \partial f(v) }{\partial v} \stackrel{!}{=} 0  $$

$$ v_{max} = \sqrt{\frac{2 k_B T }{m}} $$

#### b)

Der Mittelwert der Verteilung wird wie üblich über

$$ <v> = \int_{0}^{\infty} v f(v) dv $$

bestimmt.

#### c)
Der Median lässt sich aus einem Histogramm der Verteilung bestimmen. Aber niemand hat Zeit für Monte-Carlo Simulationen.

#### d)

Man braucht die Lambertsche W Funktion. Aber auch dafür hat keiner Zeit.

#### e)

Die Varianz wird bestimmt durch

$$ \langle v^2 \rangle - (\langle v \rangle)^2  $$

![Rechnung zu Aufgabe 9](/Users/Kai/Development/smd/blatt_3/IMAG0239.jpg)


##Aufgabe 10

#### a)
Sehr spontante Schätzung liefert 22.5

#### b)

Für n = 23 gibt es insgesamt $$  365^{23} $$ Möglichkeiten Geburtstage auf Personen
aufzuteilen. Legt man einen Geburtstag fest so gibt es insgesamt

$$ 365 \cdot 364 \ldots \cdot (365 - ( n - 1)) $$

Möglichkeiten, dass kein anderer
an diesem Tag Geburtstag hat. Bei 23 Leuten ist die gesuchte Wahrscheinlichkeit also

$$ P = 1 -  \frac{365 \cdot 364 \ldots \cdot (365 - ( n - 1)) }{365^{23}} \approx 0.5 $$.


##Aufgabe 11

#### a)
Der Kandidat sollte wechseln. Für begründung siehe Teil b)

#### b)

Wenn der Kandidat auf jeden Fall wechselt, dann ist die Gewinnwahrscheinlichkeit bei 2/3.
Andernfalls bei 1/3. Zur begründung siehe den Wkeitsbaum im Anhang.

![Rechnung zu Aufgabe 11](/Users/Kai/Development/smd/blatt_3/IMAG0241.jpg)

##Aufgabe 12

Das Buffonsche Nadelproblem.  Sei y der Abstand von einem Nadelende zu einer Linie. Und
Theta der Winkel zu der Linie. Die Nadel schneidet die Linie wenn

$$ l * \sin(\theta) > y $$

Aus dem Verhältnis aus erlaubten und nicht erlaubten Bereich ergibt sich die Geschwindigkeit.


$$ \frac{1}{\pi}\int_0^\pi \sin(\theta) d\theta = \frac{2}{\pi} $$



![Rechnung zu Aufgabe 9.2](/Users/Kai/Development/smd/blatt_3/IMAG0240.jpg)
