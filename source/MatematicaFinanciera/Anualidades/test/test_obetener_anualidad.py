from re import S
from source.MatematicaFinanciera.Anualidades.anualidades import Anualidad as A 

def test_error_arg():
    objetivo = 0.0
    resultado = A.calcular_anualidad(0,0,5,2)
    assert objetivo == resultado

def test_error_sin_valores():
    objetivo = 0.0
    resultado = A.calcular_anualidad(0,0,5)
    assert objetivo == resultado
    
def test_correcto_formato_valor_presente():
    objetivo = 2357.28
    resultado = A.calcular_anualidad(15,4,7.4,85000)
    assert objetivo == resultado
    
def test_correcto_formato_valor_futuro():
    objetivo = 1054.78
    resultado = A.calcular_anualidad(10,2,3.5,valor_futuro=25000)
    assert objetivo == resultado