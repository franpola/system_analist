"""prueba3.py - Consulta sobre las fichas de FACe: búsqueda + modelo local.

Uso:
    python prueba3.py                      -> lanza la lista de preguntas de control
    python prueba3.py "tu pregunta aquí"   -> responde solo a esa pregunta
"""
import re
import sys
from pathlib import Path

from langchain_core.vectorstores import InMemoryVectorStore
from langchain_ollama import ChatOllama, OllamaEmbeddings

# --- Ajustes (lo que querrás cambiar al experimentar) ---
CARPETA_FICHAS = Path("fichas_face")
MODELO_LENGUAJE = "llama3.1:8b"
MODELO_EMBEDDINGS = "bge-m3"
FRAGMENTOS_A_RECUPERAR = 3
# Secciones que NO se indexan: el diagrama no es texto útil para buscar y las
# sugerencias son ideas del redactor, no hechos de las fuentes.
SECCIONES_EXCLUIDAS = ("Diagrama", "Qué preguntar")

INSTRUCCIONES = """Eres un asistente de soporte. Responde en español usando SOLO los fragmentos que se te dan.

Reglas:
1. Si algún fragmento responde a la pregunta, aunque sea de sí/no, respóndela directamente empezando por "Sí", "No" o la respuesta.
2. Si la pregunta menciona algo que no aparece en los fragmentos o los contradice, indícalo al empezar.
3. Si falta un dato concreto pero un fragmento indica dónde consultarlo, di que no tienes el dato e indica dónde consultarlo.
4. Solo si ningún fragmento trata el tema, responde exactamente: "No consta en las fichas."
5. No nombres ficheros ni fuentes. No hagas preguntas ni sugerencias."""

PREGUNTAS = [
    "¿Qué es una unidad tramitadora?",
    "¿Cuál es el código DIR3 de la oficina contable del organismo X?",
    "¿La unidad tramitadora envía la factura al SAT?",
    "¿Cómo resuelvo un error de firma XAdES en una factura?",
    "¿Es la unidad tramitadora la empresa que emite la factura?",
    "¿Qué es DIR3 y dónde se consulta?",
    "¿Qué relación hay entre FACe y el RCF?",
]


def cargar_fragmentos():
    """Lee las fichas y devuelve (textos, metadatos): un fragmento por sección."""
    textos, metadatos = [], []
    for fichero in sorted(CARPETA_FICHAS.glob("0*.md")):
        contenido = fichero.read_text(encoding="utf-8")
        concepto = re.search(r"^concepto:\s*(.+)$", contenido, re.M).group(1)
        # El primer trozo es la cabecera de la ficha (no es una sección): se descarta.
        for seccion in re.split(r"^## ", contenido, flags=re.M)[1:]:
            titulo, _, cuerpo = seccion.partition("\n")
            if titulo.strip().startswith(SECCIONES_EXCLUIDAS):
                continue
            # Se antepone el concepto para que el fragmento no pierda contexto.
            textos.append(f"{concepto} - {titulo}\n{cuerpo.strip()}")
            metadatos.append({"ficha": fichero.name, "seccion": titulo.strip()})
    return textos, metadatos


textos, metadatos = cargar_fragmentos()
print(f"Fragmentos indexados: {len(textos)}")
if not textos:
    raise SystemExit("No se encontró ninguna ficha. Revisa la carpeta 'fichas_face'.")

almacen = InMemoryVectorStore(OllamaEmbeddings(model=MODELO_EMBEDDINGS))
almacen.add_texts(textos, metadatas=metadatos)

llm = ChatOllama(model=MODELO_LENGUAJE, temperature=0)


def responder(pregunta):
    # 1) Búsqueda (código): los fragmentos más cercanos a la pregunta.
    docs = almacen.similarity_search(pregunta, k=FRAGMENTOS_A_RECUPERAR)
    contexto = "\n\n".join(d.page_content for d in docs)

    # 2) Respuesta (modelo): reglas fijas + fragmentos + pregunta.
    mensajes = [
        ("system", INSTRUCCIONES),
        ("human", f"Fragmentos:\n{contexto}\n\nPregunta: {pregunta}"),
    ]
    texto = llm.invoke(mensajes).content

    # 3) Fuentes (código): las escribe el programa, no el modelo, para que sean reales.
    fuentes = sorted({f"{d.metadata['ficha']} / {d.metadata['seccion']}" for d in docs})
    return texto + "\n\nFragmentos consultados:\n- " + "\n- ".join(fuentes)


if __name__ == "__main__":
    lista = [" ".join(sys.argv[1:])] if len(sys.argv) > 1 else PREGUNTAS
    for pregunta in lista:
        print("\n" + "=" * 70)
        print("PREGUNTA:", pregunta)
        print(responder(pregunta))
