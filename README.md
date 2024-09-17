### Version 0.0.0.0.1.3

### Funktionalitet 3/10

### Snabbhet 2/10

### Användarovänlighet 9,8/10

# Öbaot

Programmet arbetar i 2 steg

1. Hämta lista med låtlänkar från spellistan och spara i en excelfil
2. Läsa in länkarna från spellistan, hämta data och spara i en annan excelfil

Excelfilerna sparas över när man kör programmet så om du vill spara gammal data så flytta eller döp om de gamla excelfilerna innan du kör programmet igen.

Det kommer ta en jäkla tid. Mindfulness och whisky rekomenderas.

Ett fel som händer då och då (och jag har ingen aning om vaf varför) är att sidan misslyckas med att laddas in och det står bara

```
upstream timeout
```

Eller liknande

Trots frustration har jag ingen annan lösning än så länge än att prova igen.

I alla fall...

För att kunna köra programmet krävs att man installerar några hjälpbibliotek, vilket finns synnerligen halvdant förklarat här nedan.

# The Bruksanvisning

## Ladda ner programmet

Om du har git installerat

```
git clone git@github.com:olapiano/spotify.git
```

Annars ladda ner en zip genom att trycka på CODE -> Download ZIP och öppna på lämpligt ställe etc

## Virtual environment

### Starta cmd eller liknande

Gå in i mappen "spotify"

### Skapa en virtuell miljö

Ointressant varför. Men det är viktigt. Lovar.

```PowerShell
python -m venv .venv
```

Om det inte funkar kan man behöva installera virtualvenv. Det beror lite på vilken pythonversion man har. Eller slå en pling.

```python
pip install virtualvenv
```

Prova sedan att skapa igen.

### Aktivera virtuella miljön

CMD

```cmd
.venv\Scripts\activate.bat
```

PowerShell

```PowerShell
.venv\Scripts\activate.ps1
```

Om det står (.venv) före hårddisk och plats så är allt väl. Annars: Ring en datanörd!

```
(.venv) C:\...
```

## Installera nödvändiga bilbiotek

Gör detta endast när virtuella miljön är aktiverad! Annars får du alla bibliotek installerade globalt på datorn = Störigt och rörigt.

```cmd
python -m pip install -r requirements.txt
```

## Ändra inställningar

Lägg till länken till din spellista i settings.py

Ändra inte variabelnamn (t ex href_to_playlist)

Länken måste vara inom citationstecken

```python
href_to_playlist = "http://din.spotify.spellista.com"
```

Där går det även bra att byta namn på excelfilerna som skapas av programmet och lite annat smått och gått

## Skrapa

Kräver i nuläget att Chrome är installerat, samt att den virtuella miljön är aktiverad

```python
python main.py
```

Inte svårare än så

# Good Luck!!!

# Uppdateringar

- Buggfix: Lyssningar sparas som siffror, inte text

- Funktion: Totalsumman av lyssningarna sparas i ett eget blad

- En batch-fil som startar programmet i den virtuella miljön

- En batch-fin som skapar virtuell miljö och installarer biblioteken som behövs 
