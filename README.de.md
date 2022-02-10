# Timesheets

**Erzeugt automatisch die für Minijobber nötigen Dokumente gemäß dem "Gesetz zur Regelung eines allgemeinen Mindestlohns" - genauer, der "MiLoG §17 Erstellen und Bereithalten von Dokumenten".**

In Deutschland sind Minijobber (unter anderem also auch Werksstudenten oder studentische Hilfskräfte) verpflichted, ihre Arbeitszeiten zu dokumentieren.
Der Arbeitgeber stellt also ein Formular als Exceldatei zur Verfügung, und möchte am Ende des Monats den unterschrieben Scan zugeschickt bekommen.
Dies kann gefühlt länger dauern als der Job selbst - hier ist die Lösung.
Viel Spaß!

## Wie nutze ich Timesheets?

1. Projekt klonen
2. Anforderungen installieren
3. Die erforderlichen Dateien in denselben Ordner wie die Python-Datei legen
   - `template.xlsx`
   - `sign.png`.
4. `main.py` ausführen
5. `result.pdf` drucken/verschicken

## Das Gesetz

Gemäß §17 MiLoG ist ein Arbeitgeber, der Arbeitnehmer nach §8 Absatz 1 des Vierten Buches Sozialgesetzbuch oder in den in §2a des Schwarzarbeitsbekämpfungsgesetzes genannten Wirtschaftsbereichen oder Wirtschaftszweigen beschäftigt, verpflichtet, _Beginn, Ende und Dauer der täglichen Arbeitszeit_ dieser Arbeitnehmer spätestens bis zum Ablauf des siebten auf den Tag der Arbeitsleistung folgenden Kalendertages _aufzuzeichnen_ und diese Aufzeichnungen mindestens zwei Jahre beginnend ab dem für die Aufzeichnung maßgeblichen Zeitpunkt aufzubewahren.
Die aktuell übliche Auslegung erlaubt, das Erstellen dieser Aufzeichnungen bis zum Ende des jeweiligen Kalendermonats zu verzögern.

## Erweiterungsmöglichkeiten

[ ] Schutz gegen schädliches XML im Template  
[ ] Import der Arbeitszeiten aus Jira  
[ ] Export als PDF  
[ ] Konfigurierbare Orte für die Unterschrift und die Arbeitstage in der Vorlage  
[ ] Feiertage eintragen  
[ ] Verschicken des Ergebnisses per Mail
