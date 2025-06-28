from app.db.connection import connect_db

#Insertar a un usuario en la tabla usuarios
def insert_user(email: str, password: str) -> dict:
    try:
        with connect_db() as conn:
            with conn.cursor() as cursor:
                cursor.execute("INSERT INTO Usuarios (email, password) VALUES (%s, %s)", (email, password))
                conn.commit()
                return {"msg": "Usuario registrado exitosamente"}
    except Exception as e:
        return {"err": f"Usuario no se pudo registrar: {e}"}

#Obtener usuario por email (por ejemplo)
def get_user_by_email(email: str) -> dict:
    try:
        with connect_db() as conn:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT id, password FROM Usuarios WHERE email = %s", (email,))
                return cursor.fetchone()
    except Exception as e:
        raise Exception(f"Error interno al iniciar sesion: {e}")