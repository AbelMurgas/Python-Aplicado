
class Anualidad:

    def calcular_anualidad(tiempo_anual: float, periodo: int, interes_porcentual: float, valor_presente: float = 0, valor_futuro: float = 0) -> float:
        """
        Esta funcion calcula la anualidad mediante ya sea el valor futuro o el valor presente.\n

        Args:
            tiempo_anual (float): El tiempo en año que se da el proceso.\n
            periodo (int): tiempo transcurrido entre cada pago sucesivo (mensual=12, anual=1,trimestral=4,semestral=2).\n
            interes_porcentual (float): interes en porcentaje.\n
            valor_presente (float, optional): monto o valor actual de la anualidad. Defaults to 0.\n
            valor_futuro (float, optional): monto o valor fucturo de la anualidad. Defaults to 0.\n

        Returns:
            float: Valor de la anualidad\n
        """
        if not valor_presente and not valor_futuro:
            print("Debe colocar al menos el valor futuro o el presente")
            return 0.0
        n = periodo*tiempo_anual
        if not n:
            print("Tanto el periodo como el tiempo debe ser distinto de 0")
            return 0.0
        i = (interes_porcentual/100)/periodo
        if valor_presente:
            resultado = (valor_presente*i)/(1-(i+1)**-n)
        else:
            resultado = (valor_futuro*i)/((1+i)**n - 1)
        return round(resultado, 2)
