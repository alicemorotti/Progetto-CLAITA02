import pytest
import classiGeometriche as cG 

def test_Poligono():
    # 1. Creo un oggetto di tipo Poligono
    p1= cG.Poligono(lati = [3,3,3], angoli = [60,60,60])

    # 2. Testo le sue funzionalità (i suoi metodi, i suoi attributi, i suoi metodi dunder, ed il suo tipo)
    assert p1.calcolaPerimetro() == 9 
    assert p1.calcolasommaAngoli() <200

    assert isinstance(p1.lati, list)
    assert isinstance(p1.sommaAngoli, int)
    assert isinstance(p1,cG.Poligono)
    # NB: ricorda che puoi verificare con un assert il tipo di un oggetto con la funzione isinstance(nomeOggetto, tipo)
    