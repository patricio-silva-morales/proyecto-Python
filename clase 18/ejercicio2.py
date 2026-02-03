from datetime import date


class ReservaError(Exception):
    pass


class FechaInvalidaError(ReservaError):
    pass


class PasajerosInvalidosError(ReservaError):
    pass


class ClaseVueloInvalidaError(ReservaError):
    pass


def validar_reserva(fecha, pasajeros, clase):
    if fecha < date.today():
        raise FechaInvalidaError("La fecha del vuelo es anterior a hoy")

    if pasajeros <= 0:
        raise PasajerosInvalidosError("La cantidad de pasajeros debe ser mayor a cero")

    if clase.lower() not in ("economica", "ejecutiva", "primera"):
        raise ClaseVueloInvalidaError("Clase de vuelo no valida")


def procesar_reserva(fecha, pasajeros, clase):
    try:
        validar_reserva(fecha, pasajeros, clase)
        print("Reserva valida")

    except ReservaError as e:
        raise ReservaError(f"Error en la reserva: {e}")

    finally:
        print("Intento de reserva finalizado")


if __name__ == "__main__":
    try:
        procesar_reserva(date(2023, 3, 1), 1000, "economica")
    except ReservaError as e:
        print(e)