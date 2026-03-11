import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.cluster import DBSCAN

# 1. load your data
csv_path = r"Classification_project/training/Dataset/synthetic_logs.csv"
df = pd.read_csv(csv_path, parse_dates=[0], keep_default_na=False)

# make sure the column exists and is text
messages = df['log_message'].astype(str).tolist()

# 2. embed with a sentence transformer
model = SentenceTransformer('all-MiniLM-L6-v2')  # lightweight & good for semantic similarity
embeddings = model.encode(messages, show_progress_bar=True, convert_to_numpy=True)

# 3. cluster with DBSCAN
# epsilon and min_samples will need tuning depending on dataset/closeness of messages.
# metric='cosine' works well for transformer vectors.
clustering = DBSCAN(eps=0.5, min_samples=5, metric='cosine')
labels = clustering.fit_predict(embeddings)

# 4. attach labels back to data frame
df['cluster'] = labels

# inspect some clusters
for cluster_id in sorted(df['cluster'].unique()):
    print(f"Cluster {cluster_id} (n={len(df[df['cluster'] == cluster_id])}):")
    for msg in df[df['cluster'] == cluster_id]['log_message'].head(5):
        print("    ", msg)
    print()

# 5. optionally save out
out_path = r"clustered_logs.csv"
df.to_csv(out_path, index=False)
print(f"Saved clustered data to {out_path}")
