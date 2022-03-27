class Valor_Presente:

    def obtener_valor_presente(tiempo_anual: float, periodo: int, interes_porcentual: float, valor_futuro: float):
        i = (interes_porcentual/100)/periodo
        n = tiempo_anual*periodo
        resultado = valor_futuro/(1+i)**n
        return round(resultado, 2)

    def obtener_valor_presente_mediante_descuento(monto: float, descuento_simple: float) -> float:
        respuesta = monto-descuento_simple
        return round(respuesta, 2)
