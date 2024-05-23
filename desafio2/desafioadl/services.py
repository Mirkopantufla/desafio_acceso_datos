from .models import Tarea, SubTarea

def recuperar_tareas_subtareas():
    tareas = Tarea.objects.prefetch_related('subtareas').filter(eliminada = False)
    lista_tareas_y_subtareas = []
    for tarea in tareas:
        subtareas = tarea.subtareas.filter(eliminada = False)
        lista_subtareas = []
        for subtarea in subtareas:
            lista_subtareas.append(subtarea)
        tareas_ordenadas = {
            'tarea' : tarea,
            'subtareas' : lista_subtareas
        }
        lista_tareas_y_subtareas.append(tareas_ordenadas)

    return lista_tareas_y_subtareas

#Crea una tarea nueva y envia un mensaje de confirmación
def crear_nueva_tarea(newDescripcion, newEliminada):
    tarea = Tarea(descripcion=newDescripcion, eliminada = newEliminada)
    tarea.save()

    return print('Tarea Creada')

#Crea una subtarea nueva y envia un mensaje de confirmación
def crear_sub_tarea(newDescripcion, newEliminada, tarea):
    subtarea = SubTarea(descripcion = newDescripcion, eliminada = newEliminada, tarea = tarea)
    subtarea.save()

    return print('Subtarea Creada')

#Elimina una tarea y envia un mensaje de confirmación
def eliminar_tarea(id):
    tarea = Tarea.objects.get(id=id)
    #En caso de no existir enviará otro mensaje
    if not tarea:
        return print('Tarea no encontrada')
    
    #Si la validación esta correcta, se prosigue a cambiar el estado y guardado en la db
    tarea.eliminada = True
    tarea.save()
    return print('Tarea Eliminada')

#Elimina una subtarea y envia un mensaje de confirmación
def eliminar_sub_tarea(id):
    subtarea = SubTarea.objects.get(id=id)
    #En caso de no existir enviará otro mensaje
    if not subtarea:
        return print('Subtarea no encontrada')
    
    #Si la validación esta correcta, se prosigue a cambiar el estado y guardado en la db
    subtarea.eliminada = True
    subtarea.save()
    return print('SubTarea Eliminada')

def imprimir_en_pantalla(lista_ordenada):
    print('-------------------------------------------')
    #El primer ciclo imprimira las tareas con el id, descripcion y el indice segun lo requerido
    for indiceTarea, element in enumerate(lista_ordenada):
        print(
            f"""[{element["tarea"].id}] {element["tarea"].descripcion} {indiceTarea+1}"""
        )
        #El segundo ciclo imprimira las subtareas con el id, descripcion y el indice segun lo requerido
        for indiceSubTarea, subElement in enumerate(element["subtareas"]):
            print(
            f""".... [{subElement.id}] {subElement.descripcion} {indiceSubTarea+1}"""
            )
    print('-------------------------------------------')