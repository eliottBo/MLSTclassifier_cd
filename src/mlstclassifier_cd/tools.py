import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os
import pandas as pd
from pathlib import Path


# Create a pie chart with the value counts
def create_pie_chart(df: pd.DataFrame, output_dir: Path) -> None:
    fig = make_subplots(1, 1, specs=[[{"type": "pie"}]])
    fig.add_trace(
        go.Pie(
            labels=df["predicted_clade"].value_counts().index,
            values=df["predicted_clade"].value_counts().values,
            textinfo="label+percent",
            showlegend=False,
        ),
        row=1,
        col=1,
    )
    fig.update_layout(title_text="Predicted Clade Distribution")

    # Save the pie chart as an HTML file:
    fig.write_html(os.path.join(output_dir, "pie_chart.html"))
