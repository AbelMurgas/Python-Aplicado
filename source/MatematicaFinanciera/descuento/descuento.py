class Descuento:

    def obtener_descuento(total_pagar: float, interes: float) -> float:
        return round(total_pagar*interes, 2)

    def obtener_descuento_racional(tiempo_anual: float, periodo: int, interes_porcentual: float, valor_futuro: float) -> float:
        i = (interes_porcentual/100)/periodo
        n = tiempo_anual*periodo
        resultado = valor_futuro*(1-(1/(1+i)**n))
        return round(resultado, 2)

    def obtener_pago_con_descuento(total_pagar: float, interes_porcentual: float) -> float:
        i = interes_porcentual/100
        descuento_total = i*total_pagar
        respuesta = total_pagar - descuento_total
        return round(respuesta, 2)

    def obtener_descuento_mediante_pago(total_pagar: float, pago_realizado: float) -> float:
        decuento_total = total_pagar - pago_realizado
        respuesta = (decuento_total/total_pagar)*100
        return round(respuesta, 2)

    def obtener_descuento_simple(tiempo_mensual: float, interes_porcentual: float, valor_deuda: float):
        i = interes_porcentual/100
        t = tiempo_mensual/12
        respuesta = valor_deuda*i*t
        return round(respuesta, 2)
