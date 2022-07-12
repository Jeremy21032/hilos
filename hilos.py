# Para esta implementación, se realizara una función que ejecute un código en segundo plano
# lo primero es importar la libreria threading

import threading
import time


def hola_mundo(nombre):  # en esta sección pasamos un parámetro, en mi caso el nombre
    # para ejecutarlo en segundo plano, haremos que el hilo duerma por algunos segundos
    print("Hola Mundo "+nombre)
    # aqui le decimos que se va a dormir el programa en n segundos
    time.sleep(5)


if __name__ == '__main__':
    # aqui se genera un nuevo objeto con un nonmbre aleatorio
    # A la clase thread le pasaremos el parametro target que corresponde al código apra ejecutarse en segundo plano, adicional pasamos el parámetro args()
    hilo = threading.Thread(target=hola_mundo, args=("Jere",))
    hilo.start()  # este metodo ejecuta el target en segundo plano
    # hasta este punto, se han ejecutado los hilos principales.
