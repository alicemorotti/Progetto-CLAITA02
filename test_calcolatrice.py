import pytest
import calcolatrice

def test_somma():
    assert calcolatrice.somma(2, 2) == 4, "la funzione somma(2, 2) non ha prodotto 4!"
    assert calcolatrice.somma(3, 3) != 7
    assert calcolatrice.somma(0, -1) < 0

def test_divisione():
    assert calcolatrice.divisione(6, 3) == 2
    assert calcolatrice.divisione(10, 5) == 2
    with pytest.raises(ValueError):
        calcolatrice.divisione(1, 0)



# Aggiungi le funzioni per testare moltiplicazione e sottrazione
def test_sottrazione():
    assert calcolatrice.sottrazione(68,33) == 35, "la funzione sottrazione(68,33) non ha prodotto 35!"
    assert calcolatrice.sottrazione(20,20) != 2, "la funzione sottrazione(20,20) non ha prodotto 0!"
    


def test_moltiplicazione():
    assert calcolatrice.moltiplicazione(3,9) == 27
    assert calcolatrice.moltiplicazione(-5,2) <0 

# Aggiungi una funzione per testare magicNumbers
def test_magicNumbers():
    assert 15 in calcolatrice.magicNumbers(2,18)
    
# bonus: prevedi di usare l'operatore in nell'assert
# def funzioneCheRestituisceUnaLista(a) -> list:
#     return [a]

# def test_funzioneCheRestituisceUnaLista():
#     assert 5 in funzioneCheRestituisceUnaLista(5)