def somma(a: int | float, b: int | float) -> int | float:
    return a + b

def divisione(num: int | float, den: int | float) -> float:
    if den == 0:
        raise ValueError
    return num / den

# Aggiungi le funzioni moltiplicazione e sottrazione
def sottrazione(a: int | float, b: int | float) -> int | float:
    return a - b

def moltiplicazione(a: int | float, b: int | float) -> int | float:
    return a * b

# Aggiungi una funzione magicNumbers per restituire una lista di tutti e soli i numeri interi dispari e multipli di 5 tra start e stop
def magicNumbers(start: int | float, stop: int | float) -> list[int | float]:
    if start > stop:
        print("Il numero di partenza è minore di quello finale.")
    return [x for x in range(start, stop+1) if x % 2 != 0 and x % 5 == 0]
