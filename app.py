from acinoyx_jubatus import crear_app

app = crear_app()
if __name__ == '__app__':  #Solo si se corre esta archivo (no si se importa)
    app.run(debug = True)   #Esta linea sera ejecutada y el servidor de flask sera creado, a la vez que se activan
                            #los cambios en vivo en la pagina (para que se actualice la pagina cada vez que se haga un cambio en el codigo fuente)
                            

