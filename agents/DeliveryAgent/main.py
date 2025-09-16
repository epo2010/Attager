# agents/deliveryAgent/main.py

from .executor import DeliveryAgentExecutor

def run_delivery_agent_task(task_name, payload):
    executor = DeliveryAgentExecutor()
    return executor.execute_task(task_name, payload)

if __name__ == "__main__":
    # Example usage for recalculating delivery routes
    print("\n--- Running Delivery Agent: Recalculate Routes ---")
    result_routes = run_delivery_agent_task(
        "recalculate_delivery_routes_with_maintenance_exclusion",
        {"excluded_vehicles": ["vehicle_2", "vehicle_5"]}
    )
    print(f"Recalculate Routes Result: {result_routes}")

    # Example usage for generating recall schedules
    print("\n--- Running Delivery Agent: Generate Recall Schedules ---")
    result_recall = run_delivery_agent_task(
        "generate_recall_delivery_schedules",
        {"product_id": "E123"}
    )
    print(f"Generate Recall Schedules Result: {result_recall}")
