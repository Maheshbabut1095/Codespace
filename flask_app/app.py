from flask import Flask
import os
import subprocess
import datetime
import pytz  

app = Flask(__name__)

@app.route('/htop')
def ihtop():
    username = "K.MAHESH BABU"
    ist = pytz.timezone("Asia/Kolkata")
    current_time = datetime.datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S")

    try:
        top_output = subprocess.getoutput("top -b -n 1 | head -10")
    except Exception as e:
        top_output = f"Error fetching top output: {str(e)}"

    return f"""
    <html>
    <head>
        <title>HTOP Endpoint</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            pre {{ background: #f4f4f4; padding: 10px; border-radius: 5px; }}
        </style>
    </head>
    <body>
        <h1>HTOP System Info</h1>
        <p><b>Name:</b> Your Full Name</p>
        <p><b>Username:</b> {username}</p>
        <p><b>Server Time (IST):</b> {current_time}</p>
        <pre><b>Top Output:</b><br>{top_output}</pre>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
