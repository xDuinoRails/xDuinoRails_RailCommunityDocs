1 Allgemeines
===============
  
1.1 Zweck der Norm
--------------------
Diese Norm beschreibt die Übertragung von Daten vom Decoder über das Gleis zu einem
Empfänger, d.h. in der Gegenrichtung zu den Steuerungsprotokollen. Die hier beschriebene
Übertragungsmethode zusammen mit dem verwendeten Protokoll trägt die Bezeichnung
RailCom.
"RailCom" ist eine auf den Namen von Lenz Elektronik für die Klasse 9 "Elektronische
Steuerungen" unter der Nummer 301 16 303 eingetragene Deutsche Marke sowie ein für die
Klassen 21, 23, 26, 36 und 38 "Electronic Controls for Model Railways" in U.S.A. unter
Reg. Nr. 2,746,080 eingetragene Trademark. Das Europäische Patent 1 380 326 B1 wurde
aufgehoben. Damit ist RailCom unter Beachtung der Warenzeichen frei verwendbar.
Diese Spezifikation gilt ausschließlich für die Anwendung von RailCom innerhalb des DCCDatenformats (Protokolls). Die Anwendung von RailCom innerhalb anderer Datenformate ist
nicht zugelassen.

1.2 Anforderungen
--------------------
Um diese Norm zu erfüllen, müssen alle in dieser Norm definierten technischen Werte und
Protokolle eingehalten werden. Die Tabellen 5 bis 7 definieren, welche der Meldungen von
einem Decoder mindestens zu unterstützen sind.

1.3 Erläuterungen
--------------------
  
* Ein DCC-Datenpaket ist eine definierte Folge von Bits, die als Gleissignal in [RCN-210] beschrieben sind.
  
* Als Bytes werden Bitgruppen aus je acht Bits bezeichnet.
  
* Jedes Bit im Byte hat eine von seiner Position abhängende Wertigkeit, das erste 
  gesendete, in der Darstellung linke Bit, hat die höchste Wertigkeit und heißt MSB "most
  significant bit". Die Bits eines Bytes werden von links mit 7 beginnend nach rechts fallend
  bis 0 nummeriert. Das zuletzt gesendete, in der Darstellung rechte Bit, heißt LSB "least
  significant bit".

* „XF#“ bezeichnet die Binärzustandssteuerungsbefehle nach [RCN-212] Abschnitt 2.3.5.

* Folgende Zeichen werden zur Kennzeichnung der Bedeutung eines Bits verwendet:

  * 0 Bitwert 0
  * 1 Bitwert 1
  * A Adressbit
  * D Datenbit
  * P Ortsinformation (Position)
  * R Richtungsbit
  * S Sequenznummer
  * T Typ der Ortsinformation
  * X Subindex

Die in den DCC-Befehlen verwendeten Zeichen sind hier nicht nochmals aufgeführt.

Die in dieser Norm in den Kästen darstellten Bitkombinationen für DCC sind rein informativ
und haben keinen normativen Charakter. Hier gelten ausschließlich die angegeben RCNs.

Die Befehle von der Zentrale zum Decoder (►) sind jeweils ohne die Adressierungs-Daten
notiert. Die Adressierung erfolgt nach dem DCC-Standard.

(◄) kennzeichnet die vom Decoder zur Zentrale gesendeten RailCom-Daten.

Wenn nicht anders angegeben, beziehen sich Werte immer auf ein 8-Bit-Feld. Binäre Werte
sind entsprechend der Liste oben gekennzeichnet. Hexadezimale Werte sind durch ein
vorangestelltes 0x gekennzeichnet.

2 Physical Layer
===============
Dieses Kapitel beschreibt die physikalische Schicht von RailCom.

2.1 Allgemeines
--------------------

Der Informationsfluss im DCC-System erfolgt normalerweise von der Zentrale (Booster) über
das Gleis zu den Decodern. Für die umgekehrte Übertragungsrichtung ist es erforderlich,
diesen Energie- und Datenstrom zu unterbrechen. Dies geschieht durch die Booster, die dazu
am Ende eines jeden DCC-Paketes ein sogenanntes RailCom-Cutout erzeugen, indem sie die
beiden Track (Gleis)-Leitungen von der Spannungsversorgung trennen und kurzschließen.
Diese Funktionsgruppe innerhalb des Boosters wird "Cutout Device" genannt. Ein solches
Cutout Device könnte auch als separate Einheit außerhalb des Boosters ausgeführt werden.
Die eigentliche Datenübertragung erfolgt mittels einer Stromschleife. Den dazu notwendigen
Strom muss der Decoder aus seinem internen Puffer bereitstellen. Abbildung 1 zeigt die
Anordnung von Booster, Detector und Decoder während des RailCom-Cutout. 
