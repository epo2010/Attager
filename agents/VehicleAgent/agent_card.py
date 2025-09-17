# agents/vehicleAgent/agent_card.py

class VehicleAgentCard:
    name = "배차/차량 운영 Agent"
    description = (
        "운행가능 차량과 배송 투입 차량의 가용 여부 및 운행 상태를 관리합니다. "
        "차량 상태 조회/업데이트, 배정·해제, 정비 스케줄 반영을 수행합니다."
    )
    capabilities = [
        "get_fleet_availability",          # 전체 가용 현황 요약
        "get_vehicle_status",              # 단일 차량 상태 조회
        "filter_available_vehicles",       # 운행 가능 차량(maintenance/out_of_service 제외) 필터링
        "reserve_vehicle_for_delivery",    # 배송 배차/예약
        "release_vehicle_reservation",     # 배차 해제/반납
        "update_vehicle_operation_status", # on_delivery/idle/maintenance/out_of_service 등 상태 업데이트
        "schedule_vehicle_maintenance",    # 정비 일정 등록/반영
        "assign_recall_vehicles"           # (옵션) 리콜 회수 전용 차량 배정
    ]
    tags = ["vehicle", "dispatch"]
    endpoint = "http://localhost:5006" # Add endpoint here

    # 상태 전이 모델(참고용 메타데이터)
    state_model = {
        "available": ["reserved", "maintenance", "out_of_service"],
        "reserved": ["on_delivery", "available", "maintenance"],
        "on_delivery": ["available", "maintenance"],
        "maintenance": ["available"],
        "out_of_service": ["maintenance"]
    }

    # Ollama Mistral integration point (example)
    llm_model = "mistral"

    # Redis integration point (example)
    redis_key_prefix = "vehicle_agent:"

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "capabilities": self.capabilities,
            "tags": self.tags, # Add tags here
            "endpoint": self.endpoint, # Add endpoint here
            "state_model": self.state_model,
            "llm_model": self.llm_model,
            "redis_key_prefix": self.redis_key_prefix
        }