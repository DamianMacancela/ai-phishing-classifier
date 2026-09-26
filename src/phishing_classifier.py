"""
phishing_classifier.py
Clasificador simple de correos de phishing vs. legitimos usando TF-IDF + Naive Bayes.

Objetivo:
Demostrar como un modelo de NLP basico puede apoyar la deteccion temprana de correos
de phishing, como capa complementaria a controles tecnicos (SPF/DKIM/DMARC) y a la
capacitacion de usuarios.

Nota: usa un dataset de ejemplo reducido incluido en este script para que sea 100%
reproducible sin descargas externas. Para un proyecto real, reemplaza EJEMPLOS por un
dataset publico como el "Phishing Email Dataset" de Kaggle o el corpus de SpamAssassin.
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix

# ---------------------------------------------------------------------------
# 1. Dataset de ejemplo (reemplazar por dataset real en produccion)
#    Etiqueta: 1 = phishing, 0 = legitimo
# ---------------------------------------------------------------------------
EJEMPLOS = [
    ("Tu cuenta ha sido suspendida, verifica tus datos aqui: http://banco-seguro-verificacion.com", 1),
    ("Ganaste un premio, haz clic para reclamar tu dinero ahora", 1),
    ("Actualiza tu contrasena urgentemente o perderas el acceso a tu cuenta", 1),
    ("Confirma tu informacion de pago para evitar el bloqueo de tu tarjeta", 1),
    ("Verifica ahora tu cuenta de correo o sera eliminada en 24 horas", 1),
    ("Tu paquete no pudo entregarse, actualiza tu direccion en este enlace", 1),
    ("Estimado cliente, su factura del mes de septiembre esta disponible en el portal oficial", 0),
    ("Adjunto encontrara el informe solicitado en la reunion de ayer", 0),
    ("Recordatorio: la reunion de equipo es manana a las 10:00", 0),
    ("Gracias por su compra, aqui esta su comprobante electronico", 0),
    ("El reporte trimestral de ventas ya esta disponible para su revision", 0),
    ("Buenos dias, les comparto la agenda de la capacitacion de este viernes", 0),
]

textos = [t for t, _ in EJEMPLOS]
etiquetas = [e for _, e in EJEMPLOS]

# ---------------------------------------------------------------------------
# 2. Vectorizacion y entrenamiento
# ---------------------------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    textos, etiquetas, test_size=0.3, random_state=42
)

vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

modelo = MultinomialNB()
modelo.fit(X_train_vec, y_train)

# ---------------------------------------------------------------------------
# 3. Evaluacion
# ---------------------------------------------------------------------------
predicciones = modelo.predict(X_test_vec)
print("Reporte de clasificacion:\n", classification_report(y_test, predicciones, zero_division=0))
print("Matriz de confusion:\n", confusion_matrix(y_test, predicciones))

# ---------------------------------------------------------------------------
# 4. Prueba con un correo nuevo
# ---------------------------------------------------------------------------
nuevo_correo = ["Verifica tu identidad inmediatamente en este enlace o tu cuenta sera bloqueada"]
nuevo_vec = vectorizer.transform(nuevo_correo)
resultado = modelo.predict(nuevo_vec)[0]

print(f"\nCorreo de prueba: {nuevo_correo[0]}")
print("Clasificacion:", "PHISHING" if resultado == 1 else "LEGITIMO")
