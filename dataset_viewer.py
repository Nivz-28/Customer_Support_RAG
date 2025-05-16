from datasets import load_dataset
import pandas as pd
import re

# Step 1: Load dataset from Hugging Face
print("🔄 Loading dataset...")
dataset = load_dataset("bitext/Bitext-customer-support-llm-chatbot-training-dataset")

# Step 2: Convert to DataFrame
df = dataset["train"].to_pandas()
print(f"✅ Loaded {len(df)} records.")

# Step 3: Select relevant columns
columns_needed = ["instruction", "response", "category", "intent"]
df_rag = df[columns_needed].dropna().copy()

# Step 4: Remove text templates like {{Order Number}} and trim whitespace
def clean_text(text: str) -> str:
    text = re.sub(r"\{\{.*?\}\}", "", text)  # Remove placeholders
    text = re.sub(r"\s{2,}", " ", text)      # Normalize extra spaces
    return text.strip()

df_rag["instruction"] = df_rag["instruction"].astype(str).apply(clean_text)
df_rag["response"] = df_rag["response"].astype(str).apply(clean_text)

# Step 5: Remove duplicates (optional but helpful)
before = len(df_rag)
df_rag.drop_duplicates(subset=["instruction", "response"], inplace=True)
after = len(df_rag)
print(f"🧹 Removed {before - after} duplicates. Final dataset size: {after} rows.")

# Step 6: Export to CSV
output_path = "rag_support_clean.csv"
df_rag.to_csv(output_path, index=False)
print(f"📁 Saved cleaned dataset to {output_path}")
