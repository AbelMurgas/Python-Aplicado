class Interes:
    
    def obtener_interes_simple(capital,interes_porcentual,tiempo):
        interes = capital*(interes_porcentual/100)*tiempo
        return interes
