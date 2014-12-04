#SMD Blatt 5
Abgabe von Marian Bruns und Kai Brügge

##Aufgabe "Mehrdimensionale Verteilungen"

#### a)
Korrelationskoeffizent beträgt 0.8

#### b) 

Für eine Konstante Wahrscheinlichtkeit, muss der Exponent konstant sein. 

$$ - \frac{1}{2 \cdot d \cdot (1-\rho^2)} ((\frac{x_m}{\sigma_x})^2 + (\frac{y_m}{\sigma_y})^2  +  2 \frac{x_m \cdot y_m}{\sigma_x \sigma_y} \rho) = Const $$

Das ist offensichtlich eine Ellispengleichung.

#### c)

![](ellipse.png =650x)


#### d)


Winkel zur x-Achse:   20.0151296359

Ellipsen Ausdehnungen:  

* $$7.42426591305 = 2 \sigma_x $$

* $$ 1.69713748774 = 2 \sigma_y $$

#### e)
Die Rotationsmatrix lautet
$$\left(
\begin{matrix}
\cos(\alpha) & -\sin(\alpha)\\\
\sin(\alpha) & \cos(\alpha)
\end{matrix}\right)
$$
Wobei $$$\alpha$$$ der Winkel aus dem vorherigen Aufgabenteil ist.
Die 'neuen' Halbachsen ergeben sich entweder nach den in der Vorlesung ermittelten Formeln oder aus den Eigenwerten der Kovarianzmatrix.

$$
\begin{aligned}
\sigma\_{x'}&=3.710\\\
\sigma\_{y'}&=0.845
\end{aligned}
$$


##Aufgabe "Zwei Populationen"

#### a)

Die Populationen werden zunächst einzeln und dann gemeinsam
in einem Histogram dargestellt.

![Histogramme der Gaußverteilungen](populationen.png =500x)

#### b)

Die Stichprobenmittelwerte der einzelnen Verteilungen lauten

* Verteilung A: (0.0047031104860435838, 3.9967748156064422)
* Verteilung B:  (4.0029264219117229, 2.005293094717822)
* Gesamt : (2.0038147661988828, 3.0010339551621326)

Die Standardabweichungen lauten

* (1.4953849601359293, 1.4987705226138697)
* (1.5048650546024045, 1.046639687105708)
* (2.499368903901352, 1.6316812550859521)

Die stichprobengeschätzen Kovarianzmatrizen lauten:

*  $$\left(
\begin{matrix} 
2.23622 & -0.00620 \\\
-0.00620 & 2.23622
\end{matrix}\right)
$$

*   $$\left(
\begin{matrix} 
2.26466413 & 0.79436375 \\\
0.79436375&  1.09547654
\end{matrix}\right)
$$

*   $$\left(
\begin{matrix} 
6.24690739& -1.59654167 \\\
-1.59654167&  2.66241034
\end{matrix}\right)
$$

Die Korrelationskoeffizienten lauten: 

* -0.00276
* 0.5043
* -0.3914

##Aufgabe "Mehrere Messungen"
###a)
Am besten werden Ergebnis 1 und 2 Kombiniert (es wird das aritmetische Mittel gebildet und der entsprechene Fehler berechnet):
$$
299793599\pm4527.69
$$
###b)
Wir berechnen das geometrische Mittel (Fehler aus Gaußscher Fehlerfortpflanzung):
$$
\bar N=\sqrt{N_1\cdot N_2}\approx405.64\pm14.25
$$

Die 405.3 enstrpechen dem harmonischen Mittel. Das ist aber falsch.
##Aufgabe "Teilchenspuren"

###a) 
Es ergibt sich
$$a_1=\frac{x_2-x_1}{z_2-z_1}$$
und
$$a_2=x_1$$
sodass
$$x(z)=\frac{x_2-x_1}{z_2-z_1}(z-z_1)+x_1$$

Die Fehler auf $$$a_1$$$ und $$$a_2$$$ ergeben sich aus der Gauß'schen Fehlerfortpflanzung:
$$\sigma\_{a_1}=\frac{1}{z_2-z_1}\sqrt{\sigma\_{x_1}^2+\sigma\_{x_2}^2}$$
$$\sigma\_{a_2}=\sigma\_{x_1}$$

Die Kovarianzmatrix $$$C(a_1,a_2)$$$ berechnet sich folgendermaßen:
$$C(a_1,a_2)\_{k l}=\sum\_{i,j}\frac{\partial a_k}{\partial x_i}\frac{\partial a_l}{\partial x_j}C(x_1,x_1)\_{i j}$$

Wobei sich $$$C(x_1,x_2)$$$ mit den angegebenen Fehlern und aus der Unabhängigkeit ( => Unkorreliertheit) von $$$x_1$$$ und $$$x_2$$$ zu
$$C(x_1,x_1)=\left(
\begin{matrix} \sigma\_{x_1}^2 & 0 \\\
0 & \sigma\_{x_2}^2
\end{matrix}\right)
$$
ergibt.

Damit ergibt sich dann:$$
C(a_1,a_2)=\left(
\begin{matrix} \frac{1}{(z_2-z_2)^2}(\sigma\_{x_1}^2+\sigma\_{x_2}^2) & -\frac{\sigma\_{x_1}^2}{z_2-z_1} \\\
-\frac{\sigma\_{x_1}^2}{z_2-z_1} & \sigma\_{x_2}^2
\end{matrix}\right)
$$

Nun berechnet sich der Korrelationsfaktor $$$korr(a_1,a_2)$$$ zu
$$\begin{aligned}
korr(a_1,a_2)=korr(a_2,a_1) & =\frac{-\sigma\_{x_1}^2}{(z_2-z_1)\sqrt{\frac{\sigma\_{x_2}^2(\sigma\_{x_1}^2+\sigma\_{x_2}^2)}{(z_2-z_1)^2}}}\\\
& =\frac{-\sigma\_{x_1}^2}{\sigma\_{x_2}\sqrt{\sigma\_{x_1}^2+\sigma\_{x_2}^2}}
\end{aligned}
$$

##b)
Die Position des Teilchens ist
$$x(z)=\frac{x_2-x_1}{z_2-z_1}(z-z_1)+x_1$$
Der Fehler $$$\sigma\_{x}$$$ hierauf ergibt sich zu
$$\begin{aligned}
\sigma_x&=\sqrt{(\frac{\partial x(z)}{\partial a_1}\sigma\_{a_1})^2+(\frac{\partial x(z)}{\partial a_2}\sigma\_{a_2})^2+2\frac{\partial x(z)}{\partial a_1}\frac{\partial x(z)}{\partial a_2}C(a_1,a_2)\_{12}}\\\
&=\sqrt{\frac{(z-z_1)(\sigma\_{x_1}^2+\sigma\_{x_2}^2)}{(z_2-z_1)^2}+\sigma\_{x_2}^2+2\frac{(z-z_1)\sigma\_{x_1}^2}{z_2-z_1}}\end{aligned}
$$
Für $$$z=z_3$$$ müssen die Formeln dann an dieser Stelle ausgewertet werden.

##c)
Wird die Korrelation zwischen $$$a_1$$$ und $$$a_2$$$ vernachlässigt, ergibt sich für den Fehler auf $$$x(z)$$$:
$$
\sigma_x=\sqrt{(\frac{\partial x(z)}{\partial a_1}\sigma\_{a_1})^2+(\frac{\partial x(z)}{\partial a_2}\sigma\_{a_2})^2}
=\sqrt{\frac{(z-z_1)(\sigma\_{x_1}^2+\sigma\_{x_2}^2)}{(z_2-z_1)^2}+\sigma\_{x_2}^2}
$$