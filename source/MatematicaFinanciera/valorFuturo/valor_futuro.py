class Valor_Futuro:
    
    def obtener_valor_futuro(tiempo_anual: float, periodo: int, interes_porcentual: float, valor_presente=float):
        i = (interes_porcentual/100)/periodo
        n = tiempo_anual*periodo
        resultado = valor_presente*(1+i)**n
        return round(resultado,2)
