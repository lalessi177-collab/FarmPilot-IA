import streamlit as st
import google.generativeai as genai
import os

# 1. Configuración de la página
st.set_page_config(page_title="FarmPilot - Gestión Agro", page_icon="🚜")
st.title("🚜 FarmPilot Pro")
st.subheader("Asistente Inteligente de Gestión Agrícola")

# 2. Configuración de Seguridad (Secrets)
api_key = st.secrets["GEMINI_API_KEY"]

if api_key:
    genai.configure(api_key=api_key)
    
    # DEFINIMOS EL MODELO (Esto faltaba en tu versión)
    model = genai.GenerativeModel('gemini-1.5-flash')

    # 3. TU LÓGICA DE NEGOCIO (Pegá acá todo lo de AI Studio)
    SYSTEM_PROMPT = """
    Actuá como un experto en administración de agronegocios y logística. 
    Tu objetivo es ayudar con FarmPilot en: 
    - Gestión de stock de granos y hacienda.
    - Control de logística y cartas de porte.
    - Cálculos de raciones y suplementación.
    (Completá acá con el resto de tu lógica de Pehuajó y agro...)
    """

    # Inicializar el historial del chat
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Mostrar mensajes previos
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Entrada del usuario
    if prompt := st.chat_input("¿En qué te ayudo con el campo hoy?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generar respuesta de Gemini
        with st.chat_message("assistant"):
            # Usamos el modelo que definimos arriba
            full_prompt = f"{SYSTEM_PROMPT}\n\nUsuario: {prompt}"
            response = model.generate_content(full_prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
else:
    st.error("Falta la configuración de la API Key en los Secrets de Streamlit.")
