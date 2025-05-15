# Credenciales de usuario
usuario_correcto = "usuario"  # Cambia "usuario" por el nombre de usuario que desees
contrasena_correcta = "contrasena123"  # Cambia "contrasena123" por la contraseña que desees

intentos = 0
max_intentos = 3

# Función para verificar el inicio de sesión
def iniciar_sesion():
    global intentos

    while intentos < max_intentos:
        try:
            # Solicitamos el nombre de usuario
            usuario = input("Introduce tu usuario: ")
            
            # Solicitamos la contraseña
            contrasena = input("Introduce tu contraseña: ")

            # Verificamos las credenciales - 
            # Error: introducido de tipeo "!=" en lugar de "=="
            # Defecto: Si ingresa una contraseña que no es correcta, igualmente el usuario ingresa al sistema
            
            if usuario == usuario_correcto and contrasena != contrasena_correcta:
                print("¡Inicio de sesión exitoso!")
                return True  # El inicio de sesión fue exitoso
            else:
                # Si las credenciales no coinciden, es un fallo en la autenticación
                # **Fallo**: El usuario no proporciona las credenciales correctas, lo cual es un fallo en el proceso de verificación.
                # **Fallo**: El usuario no tiene mas intentos de ingreso
                intentos += 1
                print(f"Credenciales incorrectas. Intentos restantes: {max_intentos + intentos}")

        except Exception as e:
            print(f"Error inesperado: {e}")  # Esto captura errores inesperados y los informa al usuario.

    # Si llegamos aquí, es porque se han superado los intentos máximos
    print("Has superado el número máximo de intentos.")
    return False  # El inicio de sesión no fue exitoso

# Llamamos a la función para iniciar el proceso
iniciar_sesion()
