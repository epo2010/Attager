# agents/qualityAgent/main.py

from .executor import QualityAgentExecutor

def run_quality_agent_task(task_name, payload):
    executor = QualityAgentExecutor()
    return executor.execute_task(task_name, payload)

if __name__ == "__main__":
    print("\n--- Running Quality Agent: Extract Defective Recall Product List ---")
    result = run_quality_agent_task(
        "extract_defective_recall_product_list",
        {"product_category": "E-상품"}
    )
    print(f"Extract Defective Recall Product List Result: {result}")
