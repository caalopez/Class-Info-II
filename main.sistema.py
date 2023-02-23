from veterinaria import*

def main():
    servicio_hospitalario = Sistema()

    while True:
        
        menu= int (input(" \nIngrese una opción: \n1- Ingresar una mascota \n2- Ver fecha de ingreso\n3- Ver número de mascotas en el servicio  \n4- Ver medicamentos que se están administrando\n5- Eliminar mascota \n6- Salir \nUsted ingresó la opción: ))"))
        

        if menu == 1: # ingresar            
            if  servicio_hospitalario.verNumeroMascotas() >=10:
                print("No hay espacio")
                continue
            historia = int(input("Ingrese el numero de historia"))
            
            if servicio_hospitalario.verificarExiste(historia) == False:
            
                nombre=input("Ingrese nombre")
                tipo=input("Ingrese tipo de mascota")
                peso=input("Ingrese el peso")
                fecha=input("Ingrese fecha ingreso")
                nm=int(input("Ingrese la cantidad de medicamentos de la mascota "))
                lista_med=[]

                for i in range (o,nm):
                    nombre_medicamentos = input("Ingrese nombre: ")
                    dosis= int(input("Ingrese dosis:  "))
                    medicamento=Medicamento()
                    medicamento.asignarDosis(dosis)
                    medicamento.asignarNombre(nombre_medicamentos)
                    lista_med.append(medicamento)
                
                
                mas=Mascota()
                mas.asignarNombre(nombre)
                mas.asignarHistoria(historia)
                mas.asignarTipo(tipo)
                mas.asignarPeso(peso)
                mas.asignarFecha(fecha)
                mas.asignarMedicamento(medicamento)
                servicio_hospitalario.ingresarMascotas(mas)

            else:
                print("Ya existe la mascota")
                

        elif menu== 2: # fecha ingreso
            q= int(input("INGRESE NUMERO DE HISTORIA"))
            fecha = servicio_hospitalario.VerFechaIngreso(q)
            if fecha != None:
                print("La fecha de ingreso es" + fecha)
            else:
                print("La hisotira no correponde a ninguna mascota")
        
        elif menu== 3: #numero de mascotas
            numero=servicio_hospitalario.verNumeroMascotas
            print("El numero de mascotas es de" + str(numero))
        
        elif menu==4: #ver medicamento
            q= int(input("INGRESE NUMERO DE HISTORIA"))
            medicamento=servicio_hospitalario.VerMedicamento(q)
            if medicamento != None:
                print("Medicamento es {medicamento}")
                for m in medicamento:
                    print(f"\n- {m.verNombre()}")
            else:
                print("La hisotira no correponde a ninguna mascota")    
        
        elif menu==5: #eliminar
            q=int(input("INGRESE NUMERO DE HISTORIA A ELIMINAR"))
            elimminar=servicio_hospitalario.EliminarMascota(q)
            if elimminar== True:
                print("ELIMINADA")
            else:
                print("NO SE ELIMINO")
        
        elif menu==6: # salir
            print("SALIR DEL SISTEMA!")
            break
        
        else:
            print("OPCION INVALIAD")

if __name__ == "__main__":
    main()

