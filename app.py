from flask import Flask, request, send_file, jsonify
import pandas as pd
import matplotlib.pyplot as plt
import io
import requests

app = Flask(__name__)


csv_url = 'https://public-paws.wmcloud.org/User:Pablo%20(WMF)/outreachy/round28/features_scores_climatechange_2022.csv.zip'


response = requests.get(csv_url)
response.raise_for_status()  
csv_content = response.content.decode('utf-8')

df_features_scores = pd.read_csv(io.StringIO(csv_content))
df_features_scores['revision_timestamp'] = pd.to_datetime(df_features_scores['revision_timestamp'], utc=True)
df_features_scores.set_index('revision_timestamp', inplace=True)

@app.route('/api/chart', methods=['GET'])
def get_chart():
    feature = request.args.get('feature', '')
    start_date = request.args.get('start', '')
    end_date = request.args.get('end', '')


    if feature not in df_features_scores.columns:
        return "Invalid feature specified", 400


    start = pd.to_datetime(start_date, errors='coerce', utc=True) if start_date else None
    end = pd.to_datetime(end_date, errors='coerce', utc=True) if end_date else None

    df_sorted = df_features_scores.sort_index()

    if start is not None and end is not None:
        filtered_data = df_sorted.truncate(before=start, after=end)
    else:
        filtered_data = df_sorted


    monthly_mean = filtered_data[feature].resample('M').mean()


    plt.figure(figsize=(10, 6))
    monthly_mean.plot(title=feature)
    plt.ylabel(feature)
    plt.xlabel('Date')
    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=300)
    buf.seek(0)
    plt.close()

    return send_file(buf, mimetype='image/png')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
