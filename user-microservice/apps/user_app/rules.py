# Reglas de campos o tablas de la base de datos externas
# (EXTERNAL DATABASE, LOCAL DATABASE)
STAFF=('STAFF', 'staff',)
PREGRADO=('PREGRADO', 'pregrado',)
DOCENTE=('DOCENTE', 'docente',)

# Get appropiate role name from external database and return equivalent in local database
def get_role(role_name: str):
    if role_name in STAFF:
        return STAFF[1]
    elif role_name in PREGRADO:
        return PREGRADO[1]
    elif role_name in DOCENTE:
        return DOCENTE[1]
    else:
        return None