#IMPORTE DE FAKER
import webbrowser
from faker import Faker

#VALORES GENERADOS POR FAKER
fake= Faker()
nombre= fake.name()
nombre= nombre.replace(" ", "+")
ciudad= fake.city()
ciudad= ciudad.replace(" ", "+")
trabajo= fake.job()
trabajo= trabajo.replace(" ", "+")
lada= fake.country_calling_code()
lada= lada.replace(" ", "+")
placas= fake.license_plate()
placas= placas.replace(" ", "+")

#DATOS GENERADOS CON FAKER
#print(nombre)
#print(ciudad)
#print(trabajo)
#print(lada)
#print(placas)


#CREACION DE URL
url= "https://docs.google.com/forms/d/e/1FAIpQLSfWiwBefokqjTLPf9grPXGBDmnMaxTYQ391IwSJFcdGunkGJQ/viewform?usp=pp_url&entry.1248650163={}&entry.1762189026={}&entry.962020676={}&entry.1093429418={}&entry.515811145={}".format(nombre, ciudad, trabajo, lada, placas)


opc= input(("¿Desea abrir la url?  \n [s]: SI [n]: NO  \n:"))
if opc== "s":
    webbrowser.open_new(url)
elif opc== "n":
    print(url)
