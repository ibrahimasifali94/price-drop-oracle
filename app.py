import gradio as gr
import numpy as np
from sklearn.linear_model import LinearRegression

# Dummy model trained on synthetic data
X = np.array([[100, 0.1, 80], [200, 0.2, 60], [50, 0.05, 90]])
y = np.array([0, 1, 0])  # 0=Don't wait, 1=Price drop likely
model = LinearRegression().fit(X, y)

def predict(price, avg_discount, popularity):
    X_in = np.array([[price, avg_discount, popularity]])
    score = model.predict(X_in)[0]
    rec = "Wait, price may drop" if score>0.5 else "Buy now"
    return f"{rec} (score={score:.2f})"

with gr.Blocks() as demo:
    gr.Markdown("# 🛒🔮 Price Drop Oracle")
    price = gr.Slider(10,1000,100,label="Current Price ($)")
    avg_discount = gr.Slider(0,0.5,0.1,step=0.01,label="Average Historical Discount Fraction")
    popularity = gr.Slider(0,100,50,label="Category Popularity (0-100)")
    btn = gr.Button("Consult Oracle")
    out = gr.Markdown()
    btn.click(predict,[price,avg_discount,popularity],[out])

if __name__ == "__main__":
    demo.launch()
