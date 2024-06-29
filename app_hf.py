import streamlit as st

# Función para la pestaña Home
def home():
    ##st.title("Nuestro proyecto")
    st.title(" La Inteligencia Artificial en la lucha contra el cáncer de mama: Clasificador de imagenes de ecografias mamarias")
    st.write("""
        Esta es la página principal de nuestra aplicación. Aquí puedes encontrar información general 
        y enlaces a otras secciones de la aplicación. Nuestro objetivo es proporcionarte una herramienta 
        útil y fácil de usar para clasificar ecografias mamarias y obtener información sobre nuestra organización.
    """)
    st.write("""
        ## Secciones de la Aplicación
        - **Quiénes Somos:** Conoce más sobre nosotros y nuestra misión.
        - **Clasificador:** Utiliza nuestra herramienta de clasificación de ecografias mamarias.
    """)

    #expander = st.expander("## Contexto")
    st.write("""
   
             ## Contexto

El cáncer de mama sigue siendo una de las principales amenazas para la salud de las mujeres en todo el mundo. La detección temprana es crucial para aumentar las tasas de supervivencia y ofrecer tratamientos efectivos. En este contexto, la Inteligencia Artificial (IA) emerge como una herramienta poderosa para apoyar a los profesionales médicos en la detección y clasificación de imágenes de ecografías mamarias, mejorando la precisión y eficiencia del diagnóstico.

### ¿Qué impacto tiene la IA en la detección del cáncer de mama con ecografías?

La IA ofrece un sinfín de posibilidades para transformar la lucha contra el cáncer de mama utilizando ecografías mamarias:

- **Detección más precisa:** Los sistemas de IA pueden analizar imágenes de ecografías mamarias con mayor precisión que los ojos humanos, identificando patrones sutiles y anomalías que podrían pasar desapercibidas. Esto permite una detección más temprana y oportuna del cáncer, aumentando las probabilidades de éxito del tratamiento.
- **Reducción de biopsias innecesarias:** La IA puede ayudar a reducir la cantidad de biopsias innecesarias en las ecografías mamarias, evitando procedimientos invasivos y la angustia que estos generan en las pacientes.
- **Optimización del tiempo de los médicos:** Al automatizar tareas repetitivas como la lectura de imágenes, la IA libera tiempo valioso para que los médicos se enfoquen en la atención personalizada de las pacientes y en la toma de decisiones complejas.
- **Acceso a la atención médica para más mujeres:** La IA puede ampliar el acceso a la detección temprana del cáncer de mama, especialmente en áreas con recursos médicos limitados. Los sistemas de IA pueden ser implementados en plataformas digitales o dispositivos móviles, permitiendo que las mujeres en zonas remotas tengan acceso a evaluaciones preliminares.
### ¿Cómo funciona la IA en la detección del cáncer de mama con ecografías?

Los sistemas de IA para la detección del cáncer de mama con ecografías se basan en el aprendizaje automático y el aprendizaje profundo. Estos algoritmos son entrenados con grandes conjuntos de datos de imágenes de ecografías mamarias, tanto con casos de cáncer como benignos. A través del análisis de estas imágenes, la IA aprende a identificar patrones y características asociadas con el cáncer, permitiéndole clasificar nuevas imágenes con alta precisión.

La IA **no reemplaza al médico, sino que lo complementa.** Es fundamental recordar que la IA es una herramienta de apoyo para el diagnóstico médico, no un reemplazo del juicio y la experiencia del médico especialista. La IA debe utilizarse en conjunto con la evaluación clínica para brindar a las pacientes la mejor atención posible.

Juntos, la IA y los profesionales de la salud pueden marcar una diferencia significativa en la lucha contra el cáncer de mama, ofreciendo una detección más precisa, oportuna y accesible para todas las mujeres.
             
Este proyecto fue desarrollado dentro del programa **Mil Mujeres en IA**:    
             https://milmujeresia.com/
             """)
    #st.write("Esperamos que encuentres esta aplicación útil e informativa. ¡Gracias por visitarnos!")

# Función para la pestaña Quiénes Somos
def quienes_somos():
    st.title("Quiénes Somos")
    st.write("Información sobre la organización o el proyecto.")
    expander = st.expander("Repositorio")
    expander.write("Este es nuestro repositorio")
    expander = st.expander("Agradecimientos")
    expander.write("""

    - **Nuestros docentes:**
                   Jonathan Castro y 
                   Santiago Barreiro
    - **Bounty, Positivo BGH, Intel**
    - **UTN**

""")

# Función para la pestaña Clasificador
def clasificador():
    st.write("⚠️ **Esta herramienta no ha sido validada para uso profesional, solo tiene fines educativos**")
    st.write('<iframe src="https://nancy1906-equipo-6-proyecto-breast-cancer.hf.space" width="800" height="600"></iframe>', unsafe_allow_html=True)
    # Aquí puedes agregar el código para tu clasificador
    # Por ejemplo, un clasificador simple de texto:
   
   

# Diccionario para navegar entre las pestañas
pages = {
    "Nuestro proyecto": home,
    "Quiénes Somos": quienes_somos,
    "Clasificador": clasificador
}

# Barra lateral para la navegación
st.sidebar.image("M1000ia.png", use_column_width=True)

#st.sidebar.title("M1000IA")
selection = st.sidebar.radio("Ir a", list(pages.keys()))

# Mostrar la página seleccionada
page = pages[selection]
page()


st.sidebar.markdown("⚠️ **Esta herramienta no ha sido validada para uso profesional, solo tiene fines educativos**")