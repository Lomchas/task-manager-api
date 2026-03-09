# Task Manager API

<p align="center">
  <img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" alt="FastAPI">
  <img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite" alt="SQLite">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=JSON%20Web%20Tokens" alt="JWT">
</p>

> API RESTful para la gestión de tareas personales con autenticación segura basada en JWT.

## 📋 Descripción

Task Manager API es una aplicación backend desarrollada con FastAPI que permite a los usuarios gestionar sus tareas diarias de manera segura. Incluye autenticación robusta con tokens JWT y persistencia de datos en SQLite.

### Características Principales

- 🔐 **Autenticación segura** - Registro e inicio de sesión con JWT
- 🔒 **Hash de contraseñas** - Seguridad usando bcrypt
- 📝 **Gestión de tareas** - CRUD completo de tareas
- 🗄️ **Base de datos** - SQLite con SQLAlchemy ORM
- ⚡ **Alto rendimiento** - Construido sobre FastAPI y Uvicorn

## 🛠️ Tecnologías

| Tecnología | Propósito |
|------------|------------|
| **FastAPI** | Framework web moderno y de alto rendimiento |
| **SQLAlchemy** | ORM para la gestión de la base de datos |
| **SQLite** | Base de datos embebida y ligera |
| **Pydantic** | Validación de datos y esquemas |
| **python-jose** | Manejo de tokens JWT |
| **bcrypt** | Hash de contraseñas (versión 4.0.1) |
| **Uvicorn** | Servidor ASGI de producción |

> **Nota importante**: Este proyecto utiliza `bcrypt==4.0.1` debido a un problema de compatibilidad con versiones posteriores. Las versiones de bcrypt >= 4.1.0 eliminan el atributo `__about__` que es usado internamente por `passlib`.

## 📦 Instalación

### Prerrequisitos

- Python 3.8+
- Entorno virtual (recomendado)

### Pasos de Instalación

1. **Clonar el repositorio**

```bash
git clone <repository-url>
cd task-manager-api
```

2. **Crear y activar el entorno virtual**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. **Instalar dependencias**

```bash
pip install -r requirements.txt
```

4. **Configurar variables de entorno**

```bash
# Copiar el archivo de ejemplo
cp .env.example .env

# Editar .env con tu configuración
```

5. **Ejecutar el servidor**

```bash
uvicorn app.main:app --reload
```

La API estará disponible en: `http://localhost:8000`

## 📚 Documentación de la API

FastAPI proporciona documentación automática interactiva:

| Documentación | URL |
|---------------|-----|
| **Swagger UI** | http://localhost:8000/docs |
| **ReDoc** | http://localhost:8000/redoc |

### Endpoints Disponibles

#### Autenticación

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `POST` | `/auth/register` | Registrar un nuevo usuario |
| `POST` | `/auth/login` | Iniciar sesión y obtener token JWT |

#### Tareas

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/tasks` | Obtener todas las tareas del usuario |
| `POST` | `/tasks` | Crear una nueva tarea |
| `PUT` | `/tasks/{id}` | Actualizar una tarea |
| `DELETE` | `/tasks/{id}` | Eliminar una tarea |

### Uso de la API

#### 1. Registrar un Usuario

```bash
curl -X POST "http://localhost:8000/auth/register" \
  -H "Content-Type: application/json" \
  -d '{"email": "usuario@ejemplo.com", "password": "mi_contraseña123"}'
```

#### 2. Iniciar Sesión

```bash
curl -X POST "http://localhost:8000/auth/login" \
  -H "Content-Type: application/json" \
  -d '{"email": "usuario@ejemplo.com", "password": "mi_contraseña123"}'
```

Respuesta:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

#### 3. Acceder a Endpoints Protegidos

```bash
curl -X GET "http://localhost:8000/tasks" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## 🗂️ Estructura del Proyecto

```
task-manager-api/
├── app/
│   ├── auth/
│   │   ├── jwt_handler.py    # Manejo de tokens JWT
│   │   └── security.py       # Hash de contraseñas
│   ├── models/
│   │   ├── task.py           # Modelo de tarea
│   │   └── user.py           # Modelo de usuario
│   ├── routers/
│   │   └── auth.py           # Endpoints de autenticación
│   ├── schemas/
│   │   ├── task.py           # Esquemas de tarea (Pydantic)
│   │   └── user.py           # Esquemas de usuario (Pydantic)
│   ├── database.py           # Configuración de la base de datos
│   └── main.py               # Punto de entrada de la aplicación
├── .env                      # Variables de entorno
├── .env.example              # Ejemplo de configuración
├── requirements.txt          # Dependencias del proyecto
└── README.md                 # Este archivo
```

## 🏗️ Arquitectura

### Modelos de Datos

**Usuario**
- `id`: Identificador único
- `email`: Correo electrónico único
- `password_hash`: Contraseña hasheada
- `created_at`: Fecha de creación

**Tarea**
- `id`: Identificador único
- `title`: Título de la tarea
- `description`: Descripción opcional
- `status`: Estado de la tarea (pending/completed)
- `owner_id`: Referencia al usuario propietario
- `created_at`: Fecha de creación

### Flujo de Autenticación

```
┌──────────┐     ┌──────────┐     ┌──────────┐
│  Client  │────▶│  FastAPI │────▶│   JWT    │
└──────────┘     └──────────┘     └──────────┘
     │                │                │
     │  POST /login   │                │
     │───────────────▶│                │
     │                │  Validate      │
     │                │───────────────▶│
     │                │◀───────────────│
     │◀───────────────│                │
     │  Token JWT     │                │
```

## 🔧 Variables de Entorno

| Variable | Descripción | Ejemplo |
|----------|-------------|---------|
| `SECRET_KEY` | Clave secreta para firmar tokens JWT | (generada aleatoriamente) |
| `DATABASE_URL` | URL de conexión a la base de datos | `sqlite:///./tasks.db` |

## ⚙️ Configuración de Desarrollo

### Ejecutar en Modo Desarrollo

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Verificar que la API Funciona

```bash
curl http://localhost:8000/
```

Debería devolver: `{"message": "Task Manager API"}`

## 📄 Licencia

Este proyecto está disponible para uso educativo y personal.

---

<p align="center">
  Desarrollado con ❤️ usando FastAPI
</p>