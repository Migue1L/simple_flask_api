import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Simulate training data
np.random.seed(42)
X = np.random.randint(0, 100, (200, 3))  # features: files_changed, lines_added, lines_removed
y = (X[:, 0] + X[:, 1] * 2 + X[:, 2] * 0.5 > 150).astype(int)  # arbitrary rule to simulate failure

df = pd.DataFrame(X, columns=['files_changed', 'lines_added', 'lines_removed'])
df['failed'] = y

X = df[['files_changed', 'lines_added', 'lines_removed']]
y = df['failed']

model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

joblib.dump(model, 'model.pkl')
print("Model trained and saved!")