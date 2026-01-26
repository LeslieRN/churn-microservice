# 🎯 Microservicio de Predicción de Churn — Netflix

Este microservicio expone una API REST para consultar información de clientes y generar predicciones de abandono usando un modelo de Machine Learning.
Está desarrollado con **FastAPI** y es consumido por un **backend en Spring Boot**, que luego sirve los datos al **frontend en HTML/JavaScript**.

---

## 🧩 Rol en la Arquitectura

Este servicio forma parte de una arquitectura de 3 capas:

```
Frontend (HTML / JS)
        ↓
Backend (Spring Boot)
        ↓
Microservicio ML (FastAPI)  ← Este servicio
```

El microservicio no se comunica directamente con el frontend en producción.

---

## 🛠 Tecnologías

* Python 3.9+
* FastAPI
* Uvicorn
* Pandas
* Scikit-learn 1.6.1
* Joblib
* Pydantic

---

## 📂 Estructura del Proyecto

```
app/
 ├── main.py                 # Rutas de la API
 ├── preprocessing.py        # Preprocesamiento de datos
 ├── schemas.py              # Esquemas de entrada (Pydantic)
 |__ Dockerfile
 |__ docker-compose.yml
 ├── model/
 │    └── model_service.py   # Lógica de predicción ML
 └── clientes_limpio.csv     # Dataset
```

---

## Ejecución del Servicio

### Requisitos

* Python 3.9 o superior
* pip

### Instalar dependencias

```bash
docker compose up --build --no-cache
```

### Iniciar el servidor

Servicio disponible en:

```
http://localhost:8000
```

---

##  Endpoints Principales

### 🔹 Obtener todos los clientes

```
GET /items
```

---

### 🔹 Obtener cliente por ID

```
GET /item/{item_id}
```

Retorna **404** si no existe.

---

### 🔹 Predicción manual de churn

```
POST /predict
```

Envía los datos del cliente y retorna la predicción.

---

### 🔹 Predicción de un cliente existente

```
GET /item/predictions/{item_id}
```

Retorna datos del cliente + resultado de churn.

---

## Endpoints de Probabilidad Agrupada

Estos endpoints calculan promedios de probabilidad por grupo:

| Endpoint                        | Agrupación              |
| ------------------------------- | ----------------------- |
| `GET /probability/age`          | Por edad                |
| `GET /probability/gender`       | Por género              |
| `GET /probability/subscription` | Por tipo de suscripción |
| `GET /probability/region`       | Por región              |

---

## Machine Learning

La lógica del modelo se encuentra en:

```
app/model/model_service.py
```

Funciones principales:

* `predict(df)` → predicción individual
* `predict_batch(df)` → predicciones en lote para estadísticas

El modelo puede cambiarse sin modificar la API.

---

## Manejo de Errores

| Código | Descripción                 |
| ------ | --------------------------- |
| 400    | Error en datos o predicción |
| 404    | Cliente no encontrado       |

Ejemplo:

```json
{
  "detail": "Información con id 'A1023' no fue encontrado"
}
```

---

## Mejoras Futuras

* Reemplazar CSV por base de datos
* Autenticación (JWT / API Keys)
* Pruebas automatizadas

---