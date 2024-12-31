
pip install requests flask
import requests
from flask import Flask, jsonify


FASTEX_API_URL = "https://www.fastex.com/"
API_KEY = "01941c22-350f-7e38-95c7-be03402012ac:500c29587d25d0342c06ec693224b73c4a19274d50af56929273ef3834e2cd88"

# Flask app initialization
app = Flask(__name__)

# Function to fetch FTN price from Fastex
def fetch_ftn_price():
    try:
        headers = {
            "Authorization": f"Bearer {01941c22-350f-7e38-95c7-be03402012ac:500c29587d25d0342c06ec693224b73c4a19274d50af56929273ef3834e2cd88}"  # Adjust header if necessary
        }
        response = requests.get(https://www.fastex.com/, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()

        # Extract the price from the API response
        price = data.get("price")  # Adjust based on the actual API response
        if price is None:
            return {"status": "error", "message": "Price data not found"}

        return {"status": "success", "price": price}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# API endpoint to get FTN price
@app.route("/price", methods=["GET"])
def get_price():
    return jsonify(fetch_ftn_price())

# Main entry point
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

export FASTEX_API_KEY="https://www.fastex.com/"



