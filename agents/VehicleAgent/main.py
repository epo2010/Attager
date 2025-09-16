# agents/vehicleAgent/main.py

from .executor import VehicleAgentExecutor

def run_vehicle_agent_task(task_name, payload):
    executor = VehicleAgentExecutor()
    return executor.execute_task(task_name, payload)

if __name__ == "__main__":
    print("\n--- Running Vehicle Agent: Get Vehicle Status ---")
    status_result = run_vehicle_agent_task(
        "get_vehicle_status",
        {}
    )
    print(f"Get Vehicle Status Result: {status_result}")

    print("\n--- Running Vehicle Agent: Exclude Maintenance Vehicles ---")
    exclude_result = run_vehicle_agent_task(
        "exclude_maintenance_vehicles",
        {"all_vehicles": ["vehicle_1", "vehicle_2", "vehicle_3", "vehicle_4", "vehicle_5"], "maintenance_vehicles": ["vehicle_2", "vehicle_5"]}
    )
    print(f"Exclude Maintenance Vehicles Result: {exclude_result}")

    print("\n--- Running Vehicle Agent: Assign Recall Vehicles ---")
    assign_result = run_vehicle_agent_task(
        "assign_recall_vehicles",
        {"num_vehicles": 3}
    )
    print(f"Assign Recall Vehicles Result: {assign_result}")
