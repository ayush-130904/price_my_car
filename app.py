from flask import Flask, render_template, request
from flask_cors import cross_origin
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)
df = pd.read_csv("Cleaned_car.csv")

model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))

@app.route('/')
def index():
    companies = sorted(df['company_name'].unique())
    car_names = sorted(df['car_name'].unique())
    years = sorted(df['year'].unique(), reverse=True)
    fuel_types = sorted(df['fuel_type'].unique())

    # Build a dict mapping company -> list of car names for JS filtering
    company_car_map = (
        df.groupby('company_name')['car_name']
        .apply(lambda x: sorted(x.unique().tolist()))
        .to_dict()
    )

    companies.insert(0, 'Select Company')

    return render_template(
        "index.html",
        companies=companies,
        car_names=car_names,
        years=years,
        fuel_types=fuel_types,
        company_car_map=company_car_map
    )


@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():
    company = request.form.get('company')
    car_name = request.form.get('car_name')
    year = request.form.get('year')
    fuel_type = request.form.get('fuel_type')
    kms_driven = request.form.get('kms_driven')

    prediction = model.predict(
        pd.DataFrame({
            'car_name': [car_name],
            'company_name': [company],
            'year': [int(year)],
            'kms_driven': [int(kms_driven)],
            'fuel_type': [fuel_type]
        })
    )
    print(prediction)
    return str(np.round(prediction[0], 2))


if __name__ == '__main__':
    app.run(debug=True)