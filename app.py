import streamlit as st
import google.generativeai as genai

# 1. Configuración de la interfaz (Ancha, como en la PC)
st.set_page_config(page_title="FarmPilot Pro - Gestión", page_icon="🚜", layout="wide")

# 2. Configuración de Seguridad (Secrets de Streamlit)
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# 3. TU SYSTEM PROMPT (Acá es donde vive la inteligencia de FarmPilot)
# Podés pegar acá mismo el texto largo que tenías en AI Studio
SYSTEM_PROMPT = """
Actuá como un experto en administración de agronegocios y logística. 
Tu objetivo es ayudar con FarmPilot en la gestión de stock, 
hacienda y cálculos agrícolas para la zona de Pehuajó.
"""

st.title("🚜 FarmPilot Pro")
st.subheader("Interfaz de Gestión Agrícola Inteligente")
st.markdown("---")

# 4. BARRA LATERAL: Los campos que antes completabas en AI Studio
with st.sidebar:
    st.header("Panel de Datos")
    st.write("Completá la información para procesar:")
    
    # Estos son los "Inputs" de tu app. Podés cambiarlos por lo que necesites.
    input_lote = st.text_input("Lote o Establecimiento", placeholder="Ej: La Posta - Lote 4")
    input_categoria = st.selectbox("Categoría", ["Hacienda", "Granos", "Maquinaria", "Logística"])
    input_novedad = st.text_area("Descripción de la novedad o consulta:", height=200, 
                                placeholder="Ej: Se realizó pesaje de 50 novillos...")

    # El botón "RUN"
    ejecutar = st.button("🚀 Procesar con FarmPilot")

# 5. ÁREA PRINCIPAL: Donde aparece el resultado
if ejecutar:
    if input_lote and input_novedad:
        with st.spinner("FarmPilot está analizando los datos..."):
            # Armamos el prompt final uniendo el sistema con los datos que escribió el usuario
            prompt_final = f"{SYSTEM_PROMPT}\n\nESTABLECIMIENTO: {input_lote}\nCATEGORÍA: {input_categoria}\nDATOS: {input_novedad}"
            
            # Pedimos la respuesta a Gemini
            response = model.generate_content(prompt_final)
            
            # Mostramos el resultado de forma elegante
            st.success("✅ Análisis Completado")
            st.markdown("### Informe de Gestión:")
            st.write(response.text)
    else:
        st.warning("⚠️ Por favor, completá los campos en la barra lateral antes de ejecutar.")

# Pie de página
st.markdown("---")
st.caption("FarmPilot - Sistema desarrollado por Lorena | Lic. en Sistemas")
