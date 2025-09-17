# agents/ItemAgent/agent_card.py

class ItemAgentCard:
    name = "상품 Agent"
    description = (
        "상품 정보를 관리하고, 재고를 추적하며, 상품 관련 작업을 처리합니다."
    )
    capabilities = [
        "get_item_details",        # 상품 상세 정보 조회
        "track_item_inventory",    # 상품 재고 추적
        "update_item_status"       # 상품 상태 업데이트
    ]
    tags = ["item", "inventory"]
    endpoint = "http://localhost:5002" # Add endpoint here
    # Ollama Mistral integration point (example)
    llm_model = "mistral"

    # Redis integration point (example)
    redis_key_prefix = "item_agent:"

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