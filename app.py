import json
#from tkinter.filedialog import dialogstates
from flask import  Flask,app, jsonify, request
from flask_cors import CORS
import datetime
from datetime import timedelta
from libros import libros
from usuarios import usuarios
#from Prestamos import Prestamos

app = Flask(__name__)
CORS(app)
Libro=[]
Usuario=[]
Prestamos=[]
cont=0
num=[]
@app.route("/Catalogo", methods = ["GET"])
def Obtener():
    global Libro
    Datos=[]
    for libro in Libro:
        Dato={

            "id_book": libro.getID(),
            "book_title": libro.getTitle(),
            "book_type": libro.getType(),
            "author": libro.getAuthor(),
            "book_count": libro.getCount(),
            "book_available": libro.getAvailable(),
            "book_not_available": libro.getNotAvailable(),
            "book_year": libro.getYear(),
            "book_editorial": libro.getEditorial()
        }
        Datos.append(Dato)
    return(jsonify(Datos))

@app.route("/EliminarLibro", methods = ["DELETE"])
def Eliminar():
    global Libro
    eliminado=False
    Libroeliminado=request.json["id_book"]
    for libro in Libro:
        if Libroeliminado == libro.getID():
            Indice=Libro.index(libro)
            eliminado=True
    if eliminado==True:
        Libro.pop(Indice)
        respuesta=jsonify({
           # "Error":False,
            "Mensaje":"se elimino con exito"
            #,"Registro":True
        })
        return(respuesta)
    elif eliminado==False:
        respuesta=jsonify({
            #"Error":False,
            "Mensaje":"ID no encontrado"
            #,"Registro":True
        })
        return(respuesta),404





@app.route("/CrearLibro", methods = ["POST"])
def CrearLibros():
    global Libro
    Libro_repetido=False
    Nuevo_libro=libros(request.json["id_book"], request.json["book_title"],
    request.json["book_type"],request.json["author"],
    request.json["book_count"],request.json["book_available"],
    request.json["book_not_available"],request.json["book_year"],
    request.json["book_editorial"])
    for libro in Libro:
        if libro.getID()==request.json["id_book"]:
            Libro_repetido=True
    if Libro_repetido==False:

        Libro.append(Nuevo_libro)
        respuesta=jsonify({
           # "Error":False,
            "Mensaje":"se registro con exito"
            #,"Registro":True
        })
        return(respuesta),201
    else:
        respuesta=jsonify({
            #"error":True,
            "Mensaje":"el libro esta repetido"
            #,"Registro":False
        })
        return(respuesta),403



@app.route("/ActualizarLibro", methods = ["PUT"])
def ActualizarLibro():
    global Libro
    Actualizar_libro=request.json["id_book"]
    Libro_agregado=False

    for libro in Libro:
        if Actualizar_libro == libro.getID():
            
            if request.json["id_book"]=="":
                pass ##no hara nada
            else:
                Libro_agregado=True
                libro.setID(request.json["id_book"])

            if request.json["book_title"]=="":
                pass ##no hara nada
            else:
                libro.setTitle(request.json["book_title"])
            if request.json["book_type"]=="":
                pass ##no hara nada
            else:
                libro.setType(request.json["book_type"])
            if request.json["author"]=="":
                pass ##no hara nada
            else:
                libro.setAuthor(request.json["author"])
            if request.json["book_count"]=="":
                pass ##no hara nada
            else:
                libro.setCount(request.json["book_count"])
            if request.json["book_available"]=="":
                pass ##no hara nada
            else:
                libro.setAvailable(request.json["book_available"])
            if request.json["book_not_available"]=="":
                pass ##no hara nada
            else:
                libro.setNotAvailable(request.json["book_not_available"])
            if request.json["book_year"]=="":
                pass ##no hara nada
            else:
                libro.setYear(request.json["book_year"])
            if request.json["book_editorial"]=="":
                pass ##no hara nada
            else:
                libro.setEditorial(request.json["book_editorial"])
    if  Libro_agregado==False:
        respuesta=jsonify({
            #"Error":False,
            "Mensaje":"ID no encontrado"
            #,"Registro":True
        })
        return(respuesta),404
    else:
        respuesta=jsonify({
            "Mensaje":"se actualizo con exito"
        })
        return(respuesta),201


@app.route("/CrearUsuario", methods = ["POST"])
def CrearUsuario():
    global Usuario
    usuario_repetido=False
    Nuevo_usuario=usuarios(request.json["id_user"],request.json["user_display_name"],request.json["user_nickname"],
    request.json["user_password"],request.json["user_age"],request.json["user_career"],request.json["user_carnet"])
    for usuario in Usuario:
        if usuario.getID()==request.json["id_user"]:
            usuario_repetido=True
    if usuario_repetido == False:
        Usuario.append(Nuevo_usuario)
        respuesta=jsonify({
        # "Error":False,
            "Mensaje":"se registro con exito"
            #,"Registro":True
        })
        return(respuesta),201
    else:
        respuesta=jsonify({
            #"error":True,
            "Mensaje":"el usuario esta repetido"
            #,"Registro":False
        })
        return(respuesta),403
    
@app.route("/Login", methods = ["POST"])
def login():
    global Usuario
    usuario_existe=False
    pass_existe=False
    user_login=request.json["user_nickname"]
    password_login=request.json["user_password"]
    for usuario in Usuario:
        if user_login== usuario.getNickname():
            usuario_existe=True
        if password_login == usuario.getPassword():
            pass_existe=True
    if (usuario_existe == True and pass_existe==True):
        for usuario in Usuario:
            #usuarios = usuario.getID().find(user_login)
            if usuario.getNickname().find(user_login) != -1:
                respuesta=jsonify({})
                respuesta=jsonify({
                    
                

                    
                        
                        "id_user": usuario.getID(),
                        "user_display_name": usuario.getDisplay(),
                        "user_nickname": usuario.getNickname(),
                        "user_password": usuario.getPassword(),
                        "user_age": usuario.getAge(),
                        "user_career": usuario.getCareer(),
                        "user_carnet":usuario.getCarnet()
                            #"Mensaje":"Libro no encontrado"

                        
                        
                })
                return(respuesta),200
            #else:
             #   respuesta=jsonify({
              #      #"error":True,
               #     "Mensaje":"usuario o contraseña incorrectos"
                #    #,"Registro":False
                #})
                #return(respuesta)
    elif (usuario_existe == False or pass_existe==False):
        respuesta=jsonify({
            #"error":True,
            "Mensaje":"usuario o contraseña incorrectos"
            #,"Registro":False
            })
        return(respuesta),404


@app.route("/BuscarLibro", methods = ["GET"])
def BuscarLibro():
    Libro_buscado=False
    id=request.get_json()
    global Libro
    if "id_book" in id:
        Datos2=[]
        id_book = str(id["id_book"])
        #producto_query = { "id_book": {"$gte": id_book}}
        for libro in Libro:
            if( id_book==libro.getID()):
                Libro_buscado=True
                if libro.getID().find(id_book) != -1:
                    Datos2.append({
                        "id_book": libro.getID(),
                        "book_title": libro.getTitle(),
                        "book_type": libro.getType(),
                        "author": libro.getAuthor(),
                        "book_count": libro.getCount(),
                        "book_available": libro.getAvailable(),
                        "book_not_available": libro.getNotAvailable(),
                        "book_year": libro.getYear(),
                        "book_editorial": libro.getEditorial()
                    }
                    )
        if Libro_buscado==False:
            respuesta=jsonify({
            "Mensaje":"Libro no encontrado"
            })
            return(respuesta),404
        else:
            return(jsonify(Datos2)),200


    elif "book_type" in id:
        Datos2=[]
        book_type = str(id["book_type"])
        #producto_query = { "id_book": {"$gte": id_book}}
        for libro in Libro:
            if( book_type==libro.getType()):
                Libro_buscado=True
                if libro.getType().find(book_type) != -1:
                    Datos2.append({
                        
                        "id_book": libro.getID(),
                        "book_title": libro.getTitle(),
                        "book_type": libro.getType(),
                        "author": libro.getAuthor(),
                        "book_count": libro.getCount(),
                        "book_available": libro.getAvailable(),
                        "book_not_available": libro.getNotAvailable(),
                        "book_year": libro.getYear(),
                        "book_editorial": libro.getEditorial()
                    }
                    )
        if Libro_buscado==False:
            respuesta=jsonify({
            "Mensaje":"Libro no encontrado"
            })
            return(respuesta),404
        else:
            return(jsonify(Datos2)),200
    

    elif "book_title" in id:
        Datos2=[]
        book_title = str(id["book_title"])
        #producto_query = { "id_book": {"$gte": id_book}}
        for libro in Libro:
            if( book_title==libro.getTitle()):
                Libro_buscado=True
                if libro.getTitle().find(book_title) != -1:
                    Datos2.append({
                        "id_book": libro.getID(),
                        "book_title": libro.getTitle(),
                        "book_type": libro.getType(),
                        "author": libro.getAuthor(),
                        "book_count": libro.getCount(),
                        "book_available": libro.getAvailable(),
                        "book_not_available": libro.getNotAvailable(),
                        "book_year": libro.getYear(),
                        "book_editorial": libro.getEditorial(),
                        
                    }
                    )
                    
        if Libro_buscado==False:
            respuesta=jsonify({
            "Mensaje":"Libro no encontrado"
            })
            return(respuesta),404
        else:
            return(jsonify(Datos2)),200


#REVISAR 
@app.route("/RegistrarPrestamo", methods = ["POST"])
def RegistrarPrestamo():
    global cont
    repetido=False
    global Libro
    global Usuario
    global num
    global Prestamos
    id_libro=request.json["id_book"]
    id_user=request.json["id_user"]
    exlibro=False
    exusuario=False
    for libro in Libro:
        if id_libro== libro.getID():
            exlibro=True
    for usuario in Usuario:
        if id_user == usuario.getID():
            exusuario=True
    if exlibro== True and exusuario==True:
        ahora=datetime.datetime.now()
        diaent=ahora+timedelta(days=7)
        dfianl=diaent.strftime("%d/%m/%Y")

        

        dia=ahora.strftime("%d/%m/%Y")
        delta=diaent-ahora
        d1=ahora.strftime("%d")
        d2=diaent.strftime("%d")
        delta=diaent-ahora
        delt=delta.days
        penalty=int(delt)
        
        dd=int(d1)
        ddd=int(d2)
        multa =0

        hora=ahora.strftime("%H:%M:%S")
        
        if ahora > diaent :
            multa = penalty*-1
        


        
        for libro in Libro:
            for usuario in Usuario:
                if (usuario.getID().find(id_user) != -1 and libro.getID().find(id_libro)!= -1):
                    if libro.getAvailable() > 0:

                        loan=0
                        cont+=1
                        loan=cont
                        loano=str(loan)
       

                        Prestamos.append({

                            "id_loan":loano,
                            "id_book": libro.getID(),
                            "book_title": libro.getTitle(),
                            "book_type": libro.getType(),
                            "author": libro.getAuthor(),
                            "book_year": libro.getYear(),
                            "book_editorial": libro.getEditorial(),
                            "book_available": libro.getAvailable(),
                            "id_user": usuario.getID(),
                            "user_display_name": usuario.getDisplay(),
                            "user_nickname": usuario.getNickname(),
                            "user_password": usuario.getPassword(),
                            "user_age": usuario.getAge(),
                            "user_career": usuario.getCareer(),
                            "user_carnet":usuario.getCarnet(),
                            "loan_hora":hora,
                            "loan_date":dia,
                            "return_date":dfianl,
                            "penalty_fee":multa
                        }
                        )
                        respuesta=jsonify({})
                        respuesta=jsonify({
                            "id_loan":loano,
                            "id_book": libro.getID(),
                            "book_title": libro.getTitle(),
                            "book_type": libro.getType(),
                            "author": libro.getAuthor(),
                            "book_year": libro.getYear(),
                            "book_editorial": libro.getEditorial(),
                            "id_user": usuario.getID(),
                            "user_display_name": usuario.getDisplay(),
                            "user_nickname": usuario.getNickname(),
                            "user_password": usuario.getPassword(),
                            "user_age": usuario.getAge(),
                            "user_career": usuario.getCareer(),
                            "user_carnet":usuario.getCarnet(),
                            "loan_hora":hora,
                            "loan_date":dia,
                            "return_date":dfianl
                        })
                        libro.setAvailable(libro.getAvailable()-1)
                        for prestamo in Prestamos:
                            prestamo["book_available"]=prestamo["book_available"]-1

                        return(respuesta),201
                    else:

                        respuesta=jsonify({


                          #  #"error":True,
                            "Mensaje":"Libros agotados"
                           # #,"Registro":False
                        })
                        return(respuesta),403
    elif exlibro== False:
        respuesta=jsonify({
            "Mensaje":"no existe el libro"
            })       
        return(respuesta),404
    elif exusuario==False:
        respuesta=jsonify({
            "mensaje":"no existe el usuario"
        })
        return(respuesta),404




@app.route("/CalcularMulta", methods = ["PUT"])
def CalcularMulta():
    global Libro
    global Prestamos
    global Usuario
    repetido=False
    loann=request.json["id_loan"]
    for usuario in Usuario:
        for libro in Libro:
            for prestamo in Prestamos:
                if( loann==prestamo["id_loan"]):
                    repetido=True
                    if prestamo["id_loan"].find(loann) != -1:
                        
                       # c=prestamo["book_available"]
                       # if c > 0:
                        respuesta=jsonify({})
                        respuesta=jsonify({



                            
                            "id_loan":prestamo["id_loan"],
                            "book_title": prestamo["book_title"],
                            "user_display_name": prestamo["user_display_name"],
                            "loan_date":prestamo["loan_date"],
                            "return_date":prestamo["return_date"],
                            "penalty_fee":prestamo["penalty_fee"]
                            
                                
                        })
                        return(respuesta)
                        
                            
    if (repetido==False):
        respuesta=jsonify({
            #"error":True,
            "Mensaje":"prestamo no encontrado"
            #,"Registro":False
            })
        return(respuesta),404

@app.route("/EstadoPrestamo", methods = ["GET"])
def EstadoPrestamo():
    global Libro
    global Prestamos
    global Usuario
    repetido=False
    loann=request.json["id_loan"]
    for usuario in Usuario:
        for libro in Libro:
            for prestamo in Prestamos:
                if( loann==prestamo["id_loan"]):
                    repetido=True
                    if prestamo["id_loan"].find(loann) != -1:
                        
                       # c=prestamo["book_available"]
                       # if c > 0:
                        respuesta=jsonify({})
                        respuesta=jsonify({
                            "id_loan":prestamo["id_loan"],
                            "id_book": prestamo["id_book"],
                            "loan_date":prestamo["loan_date"],
                            "return_date":prestamo["return_date"],
                            "id_user":prestamo["id_user"]
                        })
                        return(respuesta)
                        
                            
    if (repetido==False):
        respuesta=jsonify({
            "Mensaje":"prestamo no encontrado"
            })
        return(respuesta),404







if __name__ == "__main__":
    app.run( host="localhost", port = "5000", debug=True)