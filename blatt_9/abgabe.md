#Blatt 9

##Aufgabe 1


Die Daten werden mit dem Prozess namens 'retrieval.rmp' eingelesen und als Datensatz im lokalen repsoitory gespeichert. Folgende Prozesse bezuehen die Daten
direkt aus dem Repository. Aus effizienz Gründen wurde häufig nur ein Teilmenge der Daten betrachtet. (Siehe den Stratified Sampling Operator)

Hinweise:

  *Die Namen der Label lauten nicht wie in der Aufgabenstellung 0 und 1 sondern "proton" und "gamma".
  *Es wurde RapidMiner Version 6.20 verwendet.

### a)
Datei 'aufgabe_a.rmp'. Als Klassifizierer wurde der Weka-Random Forest gewählt. 

### b)

Das Modell wird zunächst trainiert und dann mit dem Apply Modell Operator angewandt. Ein Konfidenzschnitt macht bei Anwendung des Modells auf ungelabelte 
Daten zunächst keinen Sinn. Dies geschieht in Aufgabe c) und d)

### c) und d)

Diese beiden Aufgabenteile wurden mit einem einzigen Prozess erschlagen. 
Der confidence cut passiert mittels des 'Drop Uncertain Prediction' Operators und anschließendem Auffüllen fehlender Werte.

