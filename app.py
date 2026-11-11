"""Streamlit dashboard for measured model evaluation results."""
from pathlib import Path
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Cognitive Decision Intelligence", page_icon="📊",
                   layout="wide")
st.title("Cognitive Decision Intelligence Framework")
st.caption("Predictive analytics • Model comparison • Business decision support")

RESULTS = Path("results/unified_model_results.csv")

@st.cache_data
def load_results(uploaded_file=None):
    if uploaded_file is not None:
        return pd.read_csv(uploaded_file)
    if RESULTS.exists():
        return pd.read_csv(RESULTS)
    return pd.DataFrame(columns=["Dataset", "Model", "Metric", "Value"])

with st.sidebar:
    st.header("Data source")
    uploaded = st.file_uploader("Upload model results CSV", type=["csv"])
    st.caption("Expected columns: Dataset, Model, Metric, Value")

df = load_results(uploaded)
if df.empty:
    st.info("No evaluation results found yet. Train your models and save "
            "`results/unified_model_results.csv`, or upload a results CSV.")
    st.subheader("Project modules")
    st.markdown("""
    - **Walmart:** retail sales forecasting
    - **Amazon Reviews:** sentiment classification
    - **M5:** demand forecasting
    """)
    st.stop()

required = {"Dataset", "Model", "Metric", "Value"}
if not required.issubset(df.columns):
    st.error(f"CSV must contain: {', '.join(sorted(required))}")
    st.stop()

df["Value"] = pd.to_numeric(df["Value"], errors="coerce")
df = df.dropna(subset=["Value"])
if df.empty:
    st.warning("No numeric metric values were found.")
    st.stop()

datasets = ["All"] + sorted(df["Dataset"].dropna().unique().tolist())
selected = st.selectbox("Select dataset", datasets)
view = df if selected == "All" else df[df["Dataset"] == selected]

c1, c2, c3 = st.columns(3)
c1.metric("Datasets", view["Dataset"].nunique())
c2.metric("Models evaluated", view["Model"].nunique())
c3.metric("Metric observations", len(view))

st.subheader("Model performance comparison")
metrics = sorted(view["Metric"].dropna().unique().tolist())
metric = st.selectbox("Metric", metrics)
metric_df = view[view["Metric"] == metric]
fig = px.bar(metric_df, x="Model", y="Value", color="Dataset",
             barmode="group", title=f"{metric} by model")
st.plotly_chart(fig, use_container_width=True)

st.subheader("Evaluation results")
st.dataframe(view.sort_values(["Dataset", "Metric", "Value"]),
             use_container_width=True, hide_index=True)

st.subheader("Business interpretation")
st.write(
    "Interpret each metric within its dataset and task. Lower MAE/RMSE is "
    "generally better for forecasting; higher accuracy/F1 is generally better "
    "for classification. Do not compare unlike metrics across tasks."
)
st.download_button("Download displayed results",
                   data=view.to_csv(index=False).encode("utf-8"),
                   file_name="model_results.csv", mime="text/csv")
