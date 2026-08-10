import hashlib
from uidisa_core.siu.packet import SmartInformationUnit
from uidisa_core.ivem.matrix import IntentVector
from uidisa_core.ivem.audit import IVEMAuditEngine

def test_authorized_access():
    valid_hash = hashlib.sha256(b"SECURE_NODE").hexdigest()
    intent = IntentVector("EXECUTE", valid_hash, ["RULE_1"])
    siu = SmartInformationUnit(b"PAYLOAD_OK", 0.95, valid_hash)
    
    auditor = IVEMAuditEngine()
    result = auditor.evaluate_access_request(siu, intent, intent)

    assert result["status"] == "SUCCESS"
    assert result["data"] == "PAYLOAD_OK"

def test_unauthorized_context_hijack():
    valid_hash = hashlib.sha256(b"SECURE_NODE").hexdigest()
    rogue_hash = hashlib.sha256(b"ROGUE_NODE").hexdigest()

    auth_intent = IntentVector("EXECUTE", valid_hash, ["RULE_1"])
    attacker_intent = IntentVector("EXECUTE", rogue_hash, ["RULE_1"])

    siu = SmartInformationUnit(b"CRITICAL_PAYLOAD", 0.99, valid_hash)
    auditor = IVEMAuditEngine()
    result = auditor.evaluate_access_request(siu, attacker_intent, auth_intent)

    assert result["status"] == "TERMINATED"
    assert result["action"] == "ENTROPIC_SELF_DESTRUCTION"
