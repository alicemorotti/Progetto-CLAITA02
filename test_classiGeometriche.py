import pytest
import classiGeometriche as cG 

def test_Poligono():
    # 1. Creo un oggetto di tipo Poligono
    p1= cG.Poligono(lati = [3,3,3], angoli = [60,60,60])

    # 2. Testo le sue funzionalità (i suoi metodi, i suoi attributi, i suoi metodi dunder, ed il suo tipo)
    assert p1.calcolaPerimetro() == 9 
    assert p1.sommaAngoli() <200

    assert isinstance(p1.lati, list)
    assert isinstance(p1.sommaAngoli, int | float)
    assert isinstance(p1, cG.Poligono)
    # NB: ricorda che puoi verificare con un assert il tipo di un oggetto con la funzione isinstance(nomeOggetto, tipo)

def test_Triangolo():
    pass # Questa parte la fa Francesco

def test_TriangoloRettangolo():
    # 1. Creo un oggetto di tipo TriangoloRettangolo
    tr1 = cG.TriangoloRettangolo(3, 4, 5, 90, 45, 45)
    # 2. Testo le sue funzionalità (i suoi metodi, i suoi attributi, i suoi metodi dunder, ed il suo tipo)
    assert 90 in tr1.angoli
    assert tr1.calcolaPerimetro() == 12
    assert tr1.calcolaArea() > (tr1.altezza / 2)

    assert isinstance(tr1.altezza, int | float)
    assert isinstance(tr1, cG.TriangoloRettangolo)

def test_TriangoloIsoscele():
    # 1. Creo un oggetto di tipo TriangoloIsoscele
    ti1 = cG.TriangoloIsoscele(6, 5, 30, 120)
    # 2. Testo le sue funzionalità (i suoi metodi, i suoi attributi, i suoi metodi dunder, ed il suo tipo)
    assert ti1.sommaAngoli == 180 
    assert ti1.calcolaPerimetro() == 6 + 5 + 5
    assert ti1.calcolaArea() == ti1.base * ti1.altezza / 2

    assert isinstance(ti1, cG.TriangoloIsoscele)

def test_TriangoloEquilatero():
    # 1. Creo un oggetto di tipo TriangoloEquilatero
    te1= cG.TriangoloEquilatero(4,4,4)

    # 2. Testo le sue funzionalità (i suoi metodi, i suoi attributi, i suoi metodi dunder, ed il suo tipo)
    assert te1.calcolaPerimetro() > te1.lati[0] 
    assert te1.angoli == [60, 60, 60]
    assert te1.lati[0] == te1.lati[1] == te1.lati[2] 
    assert isinstance(te1, cG.TriangoloEquilatero)