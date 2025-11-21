from flask import Flask, jsonify
import os
import sys

app = Flask(__name__)

@app.route('/')
def home():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Demo - BTP Deployment</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        .container {
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            padding: 60px 40px;
            max-width: 600px;
            text-align: center;
            animation: slideIn 0.5s ease-out;
        }
        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        .icon {
            font-size: 80px;
            margin-bottom: 20px;
            animation: bounce 2s infinite;
        }
        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }
        h1 {
            color: #333;
            font-size: 2.5em;
            margin-bottom: 20px;
            font-weight: 700;
        }
        .subtitle {
            color: #666;
            font-size: 1.2em;
            margin-bottom: 30px;
        }
        .badge {
            display: inline-block;
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            color: white;
            padding: 12px 30px;
            border-radius: 25px;
            font-weight: 600;
            margin: 10px 5px;
            font-size: 0.95em;
        }
        .info-box {
            background: #f8f9fa;
            border-left: 4px solid #f5576c;
            padding: 20px;
            margin: 30px 0;
            text-align: left;
            border-radius: 5px;
        }
        .info-box h3 {
            color: #f5576c;
            margin-bottom: 10px;
        }
        .info-box p {
            color: #555;
            line-height: 1.6;
            margin: 5px 0;
        }
        .status {
            display: inline-block;
            width: 12px;
            height: 12px;
            background: #10b981;
            border-radius: 50%;
            margin-right: 8px;
            animation: pulse 2s infinite;
        }
        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.5; }
        }
        .footer {
            margin-top: 30px;
            color: #999;
            font-size: 0.9em;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="icon">🐍</div>
        <h1>Deployment Successful!</h1>
        <p class="subtitle">Your Python application is running on SAP BTP</p>
        
        <div>
            <span class="badge">Python ''' + sys.version.split()[0] + '''</span>
            <span class="badge">Flask</span>
            <span class="badge">Cloud Foundry</span>
        </div>
        
        <div class="info-box">
            <h3><span class="status"></span>Application Status</h3>
            <p><strong>Platform:</strong> SAP Business Technology Platform</p>
            <p><strong>Runtime:</strong> Python ''' + sys.version.split()[0] + '''</p>
            <p><strong>Port:</strong> ''' + str(os.environ.get('PORT', 8080)) + '''</p>
            <p><strong>Environment:</strong> ''' + os.environ.get('FLASK_ENV', 'production') + '''</p>
        </div>
        
        <div class="footer">
            <p>Deployed via BTP Deployment Agent 🤖</p>
            <p>Powered by Model Context Protocol (MCP)</p>
        </div>
    </div>
</body>
</html>
    '''

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'python_version': sys.version,
        'flask_version': '3.0.0'
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)
