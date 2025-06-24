import streamlit as st
import pandas as pd

# --- Page Configuration ---
st.set_page_config(
    page_title="Zeru Finance Credit Scoring",
    page_icon="🤖",
    layout="centered"
)

# --- Load Data ---
# Use st.cache_data to load the data only once, making the app faster.
@st.cache_data
def load_data():
    try:
        df = pd.read_csv('output/final_scored_wallets.csv', index_col='wallet')
        return df
    except FileNotFoundError:
        st.error("The data file 'output/final_scored_wallets.csv' was not found. Please run the modeling notebook to generate it.")
        return None

data = load_data()

# --- App UI ---
st.title("🤖 Zeru Finance AI Credit Scoring")
st.write(
    "This app provides a credit score for wallets based on their historical "
    "on-chain activity on the Compound V2 protocol. Scores are based on a "
    "LightGBM model trained to identify a wallet's profile as a stable "
    "**Liquidity Provider** (high score) versus a **Liquidity Taker** (low score)."
)

st.divider()

# --- Input & Lookup Logic ---
if data is not None:
    wallet_address = st.text_input(
        "Enter a Wallet Address to Check",
        placeholder="0x...",
        help="Enter a wallet address that exists in our processed dataset."
    ).lower().strip()

    if st.button("Check Score", type="primary"):
        if not wallet_address:
            st.warning("Please enter a wallet address.")
        elif wallet_address in data.index:
            wallet_data = data.loc[wallet_address]
            score = wallet_data['credit_score']
            
            st.success(f"**Wallet Found!**")
            
            st.metric(label="AI Credit Score", value=f"{score:.2f}", delta_color="off")
            
            st.progress(int(score))
            
            with st.expander("See features that influenced this score"):
                st.write("This wallet's score was determined by a model that learned from these behavioral features:")
                features_to_show = {
                    "Net Deposit (USD)": wallet_data['net_deposit_usd'],
                    "Repayment Ratio": wallet_data['repay_borrow_ratio_usd'],
                    "Wallet Age (Days)": wallet_data['wallet_age_days'],
                    "Total Transactions": wallet_data['total_tx_count'],
                    "Was Liquidated?": "Yes" if wallet_data['is_liquidated'] == 1 else "No"
                }
                st.json(features_to_show)
        else:
            st.error("Wallet address not found in our dataset. This tool can only look up wallets from the processed data sample.")