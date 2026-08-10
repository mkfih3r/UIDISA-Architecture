from siu.packet import SmartInformationUnit
from ivem.matrix import IntentVector

class IVEMAuditEngine:
    """
    Intent Verification Engine Matrix auditor. Evaluates intent integrity 
    before unlocking or destroying the payload.
    """
    def evaluate_access_request(self, siu: SmartInformationUnit, request_intent: IntentVector, target_intent: IntentVector) -> dict:
        is_intent_valid = request_intent.evaluate_match(target_intent)

        if not is_intent_valid:
            siu.trigger_self_destruct()
            return {
                "status": "TERMINATED",
                "action": "ENTROPIC_SELF_DESTRUCTION",
                "reason": "Intent Vector mismatch or unauthorized environment boundary breach.",
                "payload_state": "MUTATED_NOISE"
            }

        return {
            "status": "SUCCESS",
            "action": "PAYLOAD_UNLOCKED",
            "data": siu.extract_payload().decode('utf-8')
        }
