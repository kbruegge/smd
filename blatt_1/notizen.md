Aufgabe 1
===
ROOT is halt immernoch kacke.
Mit PYROOT geht das so:
	
	x = np.zeros(1, dtype=float)
	
	tree.Branch('x', x, 'x/D')
	
	for i in range(1000):
		x[0] = somevalue
		tree.Fill()

Aber es gibt auch noch das Paket root_numpy. Das machts ein bisschen schöner. [Github](http://rootpy.github.io/root_numpy/)


	
Aufgabe 2
===

Sehr unspektakulär.
Python code ausführbar machen mit:

	#!/usr/bin/env python
	
	
	
Aufgabe 3
===
Berechne den Grenzwert zunächst analytisch. Das geht mit dem Satz von L'Hopital.

Dann wird der Grenzwert für verschiedene x numerisch bestimmt werden. Dabei wird x in jedem Durchlauf um eine Zehnerpotenz kleiner.

Der verlauf sollte intepretiert werden.

<img src="/Users/Kai/Development/smd/blatt_1/verlauf.png" width="400px" />

![alt](/Users/Kai/Development/smd/blatt_1/verlauf.png)


Wurde jetzt aber auch nicht so richtig erklärt.