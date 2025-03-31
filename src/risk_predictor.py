import pandas as pd
import argparse
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

def train_model(input_csv):
    df = pd.read_csv(input_csv)

    # Binary risk label (high-risk if fire size > 100 acres)
    df['RISK_LEVEL'] = df['FIRE_SIZE'].apply(lambda x: 1 if x > 100 else 0)

    features = ['FIRE_YEAR', 'LATITUDE', 'LONGITUDE']
    X = df[features]
    y = df['RISK_LEVEL']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Wildfire Risk Predictor")
    parser.add_argument('--input', type=str, default="data/processed/cleaned_fires.csv", help="Path to cleaned CSV file")
    args = parser.parse_args()

    train_model(args.input)
