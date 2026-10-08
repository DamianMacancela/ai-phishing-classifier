# AI Phishing Classifier

Este proyecto es un experimento para combinar el **Machine Learning clásico** con la **Ciberseguridad**. Es un clasificador de correos electrónicos diseñado para distinguir entre correos legítimos y phishing utilizando procesamiento de lenguaje natural (NLP).

Aunque hoy en día existen controles robustos como SPF, DKIM y DMARC a nivel de infraestructura, la detección basada en el *contenido* del mensaje (identificando urgencia, engaños y anomalías lingüísticas) sigue siendo una capa de defensa crucial. 

## 🛠️ Cómo funciona

El modelo está escrito en Python y utiliza `scikit-learn` para procesar y clasificar el texto.

1. **Extracción de Características (TF-IDF):** Transforma el texto crudo de los correos en vectores numéricos, evaluando qué palabras son estadísticamente importantes en correos maliciosos frente a los normales.
2. **Clasificación (Naive Bayes):** Utiliza el algoritmo Multinomial Naive Bayes, que es excelente y extremadamente rápido para problemas de clasificación de texto.

## 🚀 Uso Rápido

1. Clona el repositorio:
   ```bash
   git clone https://github.com/DamianMacancela/ai-phishing-classifier.git
   cd ai-phishing-classifier
   ```

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
   *(Dependencias principales: `pandas`, `scikit-learn`, `numpy`)*

3. Ejecuta el script de prueba o entrena tu propio modelo (revisa la carpeta de `notebooks` o `src`).

## 🧠 ¿Por qué hice este proyecto?

Quería entender las matemáticas y la lógica detrás de los filtros de spam y phishing antes de saltar a arquitecturas de Redes Neuronales complejas (Deep Learning/LLMs). Construir un clasificador desde cero me ayudó a comprender el valor de los datos limpios y cómo características muy simples (frecuencia de ciertas palabras clave como "urgent", "password", "verify") pueden proporcionar resultados sorprendentemente buenos.

## Siguientes Pasos

- Incorporar características estructuradas del correo (e.g., presencia de enlaces, URLs malformadas, discrepancias en dominios del remitente).
- Probar algoritmos más avanzados como Random Forest o SVM para comparar exactitud y falsos positivos.

## Licencia

[MIT License](LICENSE)
