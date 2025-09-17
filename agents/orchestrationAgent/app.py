from flask import Flask, request, jsonify
from .executor import OrchestrationAgentExecutor
from .agent_card import OrchestrationAgentCard  # Import the specific AgentCard
import requests # Import requests library

app = Flask(__name__)
executor = OrchestrationAgentExecutor()

@app.route('/run_task', methods=['POST'])
def run_task():
    data = request.json
    task_name = data.get('task_name')
    payload = data.get('payload')
    if not task_name or not payload:
        return jsonify({'error': 'task_name and payload are required'}), 400
    
    result = executor.execute_task(task_name, payload)
    return jsonify(result)

@app.route('/register_agent', methods=['POST'])
def register_agent():
    try:
        card = OrchestrationAgentCard().to_dict()
        res = requests.post("http://localhost:9000/register", json=card)
        res.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
        return jsonify(res.json()), res.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5003)
