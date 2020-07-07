# Recomendation-Algorithm

1)Installare Python: Python dovrebbe essere pre-installato in tutte le ultime distribuzioni di linux, per verificare se è installato si possono usare questi comandi:

$ python3 -V
$ python -V

1.1) In caso non fosse installato si può procedere con questi comandi, è necessario installare la versione "dev" che fornirà importanti tools per installare le librerie richieste nei prossimi punti:

$ sudo apt-get install python3 python-dev python3-dev \
     build-essential libssl-dev libffi-dev \
     libxml2-dev libxslt1-dev zlib1g-dev \
     python-pip

$ sudo apt-get install python-dev  \
     build-essential libssl-dev libffi-dev \
     libxml2-dev libxslt1-dev zlib1g-dev \
     python-pip

2)Installare SciPy, il pacchetto di librerie scientifiche standard per Python:

$ python -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose

3)Installare la libreria Surprise (Simple Python RecommendatIon System Engine), prima di tutto assicurarsi che numpy e un compilatore C siano installati:

$ pip install --user numpy
$ pip install --user scikit-surprise

4)Per lanciare lo script python, posizionarsi nella cartella "Recomendation algorithm" e da console utilizzare il comando:

$ python algo.py
