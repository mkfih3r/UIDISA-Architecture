import hashlib
import os

# =====================================================================
# UIDISA: Unified Intent-Driven Information Security Architecture
# PROOF OF CONCEPT SIMULATOR (src/prototype.py)
# Author: md kazi Fuadul islam | Copyright (c) 2026
# =====================================================================

class IntentVector:
    def __init__(self, goal: str, context_hash: str, boundary_rules: list):
        self.goal = goal
        self.context_hash = context_hash
        self.boundary_rules = boundary_rules

class SmartInformationUnit:
    def __init__(self, raw_data: bytes, semantic_weight: float, target_intent: IntentVector):
        self.semantic_weight = semantic_weight
        self.target_intent = target_intent
        self.entropy_delta = 0
        self.secret_key = os.urandom(32)
        self.payload = self._scramble(raw_data, self.secret_key)

    def _scramble(self, data: bytes, key: bytes) -> bytes:
        return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

    def evaluate_delta(self, current_context_hash: str) -> int:
        return 0 if current_context_hash == self.target_intent.context_hash else 1

class UIDISAExecutionEngine:
    def execute(self, packet: SmartInformationUnit, accessor_intent: IntentVector, current_context_hash: str):
        goal_match = (accessor_intent.goal == packet.target_intent.goal)
        boundary_check = all(r in packet.target_intent.boundary_rules for r in accessor_intent.boundary_rules)

        if not goal_match or not boundary_check:
            return self._self_destruct(packet, "INTENT_VIOLATION")

        packet.entropy_delta = packet.evaluate_delta(current_context_hash)
        if packet.entropy_delta == 0:
            unlocked = packet._scramble(packet.payload, packet.secret_key)
            return {"status": "SUCCESS", "data": unlocked.decode('utf-8')}
        else:
            return self._self_destruct(packet, "ENVIRONMENT_ANOMALY")

    def _self_destruct(self, packet: SmartInformationUnit, reason: str):
        noise = os.urandom(len(packet.payload))
        packet.payload = bytes([p ^ noise[i] for i, p in enumerate(packet.payload)])
        packet.secret_key = os.urandom(32)
        return {"status": "TERMINATED", "reason": reason, "corrupted_hex": packet.payload.hex()[:32]}

if __name__ == "__main__":
    env_valid = hashlib.sha256(b"SecureNode_100").hexdigest()
    env_hacker = hashlib.sha256(b"RogueNode_200").hexdigest()

    intent_valid = IntentVector("SYSTEM_UPDATE", env_valid, ["NO_EXPORT"])
    intent_hacker = IntentVector("SYSTEM_UPDATE", env_hacker, ["NO_EXPORT"])

    packet = SmartInformationUnit(b"CONFIDENTIAL_PATCH_V1", 0.9, intent_valid)
    engine = UIDISAExecutionEngine()

    print("--- TEST 1: AUTHORIZED ACCESS ---")
    print(engine.execute(packet, intent_valid, env_valid))

    packet2 = SmartInformationUnit(b"CONFIDENTIAL_PATCH_V1", 0.9, intent_valid)
    print("\n--- TEST 2: MITM ATTACK ---")
    print(engine.execute(packet2, intent_hacker, env_hacker))
