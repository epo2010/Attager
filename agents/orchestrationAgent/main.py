# agents/orchestrationAgent/main.py

from .executor import OrchestrationAgentExecutor

def run_orchestration_agent_task(task_name, payload):
    executor = OrchestrationAgentExecutor()
    return executor.execute_task(task_name, payload)

if __name__ == "__main__":
    print("\n--- Running Orchestration Agent: Report New Strategy ---")
    strategy_result = run_orchestration_agent_task(
        "report_new_dispatch_and_delivery_strategy",
        {"excluded_vehicles": 2, "processing_rate": 95, "rental_vehicles": 1}
    )
    print(f"Report New Strategy Result: {strategy_result}")

    print("\n--- Running Orchestration Agent: Report Recall Progress ---")
    recall_result = run_orchestration_agent_task(
        "report_recall_progress",
        {"recall_quantity": 2300, "num_recall_vehicles": 3}
    )
    print(f"Report Recall Progress Result: {recall_result}")
