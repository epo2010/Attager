# agents/itemAgent/main.py

from .executor import ItemAgentExecutor

def run_item_agent_task(task_name, payload):
    executor = ItemAgentExecutor()
    return executor.execute_task(task_name, payload)

if __name__ == "__main__":
    print("\n--- Running Item Agent: Get Recall Product Inventory ---")
    result = run_item_agent_task(
        "get_recall_product_inventory",
        {"product_id": "E123"}
    )
    print(f"Get Recall Product Inventory Result: {result}")
