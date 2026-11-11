# lean-construction-ppc-analytics
Pipeline en Python para análisis de PPC y variabilidad en Lean Construction.
# Lean Construction PPC & Production Control Analytics

Este repositorio contiene un pipeline de datos desarrollado en Python para procesar, auditar y analizar métricas de control de producción en obras bajo la metodología **Lean Construction (Last Planner System)**.

## 🎯 Objetivo
Automatisar el cálculo del **Percent Plan Complete (PPC)**, identificar las Causas de No Cumplimiento (CNC) recurrentes y medir la variabilidad del flujo de producción en proyectos de infraestructura pública y privada.

## 🛠️ Tecnologías y Arquitectura
- **Lenguaje:** Python 3.10+
- **Librerías principales:** `pandas`, `numpy`, `matplotlib`, `seaborn`
- **Output:** Archivos estructurados para consumo directo en modelos de **Power BI** y Gemelos Digitales (Digital Twins).

## 📊 Métricas Calculadas
1. **PPC Semanal:** $\text{PPC} = \left(\frac{\text{Tareas Completadas}}{\text{Tareas Programadas}}\right) \times 100$
2. **Distribución de Causas de No Cumplimiento (CNC):** Análisis de Pareto para priorizar cuellos de botella en la cadena de suministro, mano de obra y liberación de restricciones.
3. **Índice de Variabilidad:** Medición de la estabilidad del flujo operativo.

## 🚀 Uso Rápido

```bash
# Clonar repositorio
git clone [https://github.com/tu-usuario/lean-construction-ppc-analytics.git](https://github.com/tu-usuario/lean-construction-ppc-analytics.git)

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar pipeline
python src/main.py























