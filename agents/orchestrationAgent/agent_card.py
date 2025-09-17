# agents/orchestrationAgent/agent_card.py

class OrchestrationAgentCard:
    name = "Orchestration Agent"
    description = "새로운 배차 및 배송 전략을 보고하고, 리콜 진행 현황을 보고합니다."
    capabilities = [
        "report_new_dispatch_and_delivery_strategy",
        "report_recall_progress"
    ]
    tags = ["orchestration", "report"]
    endpoint = "http://localhost:5003" # Add endpoint here
    # Ollama Mistral integration point (example)
    llm_model = "mistral"

    # Redis integration point (example)
    redis_key_prefix = "orchestration_agent:"

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "capabilities": self.capabilities,
            "tags": self.tags, # Add tags here
            "endpoint": self.endpoint, # Add endpoint here
            "llm_model": self.llm_model,
            "redis_key_prefix": self.redis_key_prefix
        }