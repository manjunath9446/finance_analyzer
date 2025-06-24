# Zeru Finance: AI-Powered Decentralized Credit Scoring

This project delivers an end-to-end machine learning system to assess the creditworthiness of wallets on the Compound V2 protocol. The system analyzes raw on-chain transaction data to generate a credit score from 0 to 100, reflecting a wallet's behavioral profile and reliability.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-name.streamlit.app) <!-- Replace with your live Streamlit app URL -->

---

## 🚀 Live Demo

An interactive web application has been deployed using Streamlit to demonstrate the model's predictions. Enter a wallet address from the dataset to view its AI-generated credit score and key behavioral features.

**[Access the Live Credit Scoring App Here](https://your-app-name.streamlit.app)** <!-- Replace with your live Streamlit app URL -->

---

## 📖 Project Narrative & Methodology

The project began with the goal of predicting credit risk, but an initial exploratory data analysis revealed a critical challenge: the absence of `liquidation` events (defaults) in the 20-file data sample. This required a strategic pivot.

The problem was reframed from predicting *risk* to classifying *behavioral profiles*. A pseudo-labeling strategy was designed to categorize wallets based on their on-chain liquidity behavior:

*   **Good Profile (Label 1): "Liquidity Providers"** - Established wallets that are significant net depositors to the protocol.
*   **Bad Profile (Label 0): "Liquidity Takers"** - Wallets that are significant net withdrawers while still having outstanding debt.

This approach successfully generated a labeled dataset, enabling the training of a supervised learning model.

### Model Selection

Three different classification models were trained and evaluated to ensure the most effective algorithm was chosen. The features used to create the labels were carefully excluded from the training set to prevent data leakage.

| Model                 | ROC AUC Score |
| :-------------------- | :------------ |
| Logistic Regression   | 0.83          |
| Random Forest         | 0.99          |
| **LightGBM**          | **0.9987**    |

![ROC Curve Comparison](roc_curve_image.png) <!-- Optional: Add a screenshot of your ROC curve plot to the repo and link it here -->

**LightGBM was selected as the final model** due to its superior performance. The final credit score represents the model's predicted probability that a wallet exhibits the behavior of a stable, long-term Liquidity Provider.

---

## 🛠️ Technology Stack

*   **Data Analysis:** Pandas, NumPy
*   **Machine Learning:** Scikit-learn, LightGBM
*   **Visualization:** Matplotlib, Seaborn
*   **Web Application:** Streamlit
*   **Development Environment:** Jupyter Notebooks, Python 3.9+

---

## 📂 Repository Structure
app.py # The Streamlit web application
├── notebooks/
│ ├── 01_Feature_Engineering.ipynb
│ ├── 02_Baseline_Rule_Based_Model.ipynb
│ └── 03_ML_Model_Comparison_and_Selection.ipynb
├── output/
│ └── final_scored_wallets.csv # The final data used by the app
├── processed_data/
│ └── wallet_features.pkl
├── requirements.txt # Python dependencies
└── README.md


---

## ⚙️ How to Run This Project Locally

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/your-username/zeru-credit-scoring.git
    cd zeru-credit-scoring
    ```

2.  **Set up a Virtual Environment (Recommended)**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Reproduce the Analysis**
    *   Run the Jupyter Notebooks in numerical order (`01_...` then `02_...` then `03_...`) to see the full data processing and model training pipeline.
    *   *Note: You will need to place the raw data files in a `data/` directory in the project root for the first notebook to run.*

5.  **Launch the Web App**
    ```bash
    streamlit run app.py
    ```
    Your browser will automatically open with the local version of the application.
