from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>Secure Cloud System</title>
            <style>
                body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; text-align: center; margin-top: 100px; background-color: #f4f6f9; }
                .container { border: 2px solid #27ae60; padding: 30px; display: inline-block; background: white; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
                h1 { color: #2c3e50; }
                .status { color: #27ae60; font-size: 22px; font-weight: bold; }
                .details { color: #7f8c8d; font-size: 16px; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Secure Cloud K8s DevSecOps System (Python-Engine)</h1>
                <p class="status">✔ Tizim muvaffaqiyatli joriy etildi (Status: Running)</p>
                <p class="details">Infratuzilma auditi: SonarQube Passed | Trivy Container Verified</p>
            </div>
        </body>
    </html>
    """

if __name__ == '__main__':
    # Konteyner ichida default 5000-portda ishga tushadi
    app.run(host='0.0.0.0', port=5000)