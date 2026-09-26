# Detector de Phishing con Machine Learning

> Clasificador de texto que distingue correos de phishing de correos legítimos usando
> TF-IDF + Naive Bayes, como capa complementaria a controles técnicos (SPF/DKIM/DMARC).

## 🎯 Objetivo

Explorar cómo un modelo de NLP simple puede apoyar la detección temprana de phishing,
entendiendo tanto sus capacidades como sus límites (falsos negativos/positivos) frente a
un problema de seguridad real.

## 🧭 Contexto y alcance

- Prototipo educativo con un dataset de ejemplo reducido e incluido en el propio script,
  para que sea 100% reproducible sin descargas externas.
- Para producción, este modelo debería entrenarse con un dataset real y balanceado
  (ej. "Phishing Email Dataset" de Kaggle o el corpus público de SpamAssassin), y
  complementarse con reglas de encabezado (SPF/DKIM/DMARC) y no usarse como único filtro.

## 🛠️ Metodología

1. Vectorización de texto con TF-IDF.
2. Clasificación binaria (phishing / legítimo) con Naive Bayes multinomial.
3. Evaluación con matriz de confusión y reporte de clasificación.
4. Prueba con un correo nuevo no visto durante el entrenamiento.

## 🧰 Stack técnico

Python · scikit-learn

## ▶️ Cómo ejecutarlo

```bash
pip install scikit-learn
python phishing_classifier.py
```

## 📊 Resultados

Con el dataset de ejemplo (10 correos), el modelo clasifica correctamente el correo de
prueba como *phishing*. Con un dataset real de miles de ejemplos, se esperaría reportar
aquí precisión, recall y F1-score reales — no se deben inflar métricas de un dataset de
juguete como si fueran de producción.

## 💡 Lecciones aprendidas

Un modelo de texto por sí solo tiene límites claros: no analiza encabezados técnicos del
correo (SPF/DKIM/DMARC) ni la reputación del dominio. Su valor real está en combinarse con
esas señales, no en reemplazarlas — es una lección tanto técnica como de honestidad al
presentar resultados.

## 📄 Licencia

MIT
