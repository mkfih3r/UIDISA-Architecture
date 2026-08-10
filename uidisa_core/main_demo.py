import hashlib
from siu.packet import SmartInformationUnit
from ivem.matrix import IntentVector
from ivem.audit import IVEMAuditEngine

def run_uidisa_demo():
    print("==========================================================")
    print(" UIDISA CORE SYSTEM: ACTIVE SELF-DEFENSE RUNTIME DEMO ")
    print("==========================================================\n")

    # 1. Define Authorized System Hashes & Policies
    valid_env = hashlib.sha256(b"Node_ECU_V2X_Primary").hexdigest()
    hacker_env = hashlib.sha256(b"Interception_Node_Proxy").hexdigest()

    auth_intent = IntentVector("EXECUTE_AUTO_BRAKE", valid_env, ["CAN_BUS_SECURE", "MAX_SPEED_60"])
    unauth_intent = IntentVector("EXECUTE_AUTO_BRAKE", hacker_env, ["CAN_BUS_SECURE"])

    # 2. Package Data into Smart Information Unit
    siu_packet = SmartInformationUnit(
        raw_payload=b"CRITICAL_BRAKE_COMMAND_FORCE_80PCT",
        semantic_weight=0.98,
        context_signature=valid_env
    )

    auditor = IVEMAuditEngine()

    # TEST CASE A: Authorized Request
    print("--- [SCENARIO A: Authorized V2X Execution] ---")
    res_a = auditor.evaluate_access_request(siu_packet, auth_intent, auth_intent)
    print(f"Status  : {res_a['status']}")
    print(f"Action  : {res_a['action']}")
    print(f"Data    : {res_a['data']}\n")

    # TEST CASE B: Interception / Hacker Threat Attack
    print("--- [SCENARIO B: Interception / Unauthorized Context Breach] ---")
    siu_packet_b = SmartInformationUnit(
        raw_payload=b"CRITICAL_BRAKE_COMMAND_FORCE_80PCT",
        semantic_weight=0.98,
        context_signature=valid_env
    )
    res_b = auditor.evaluate_access_request(siu_packet_b, unauth_intent, auth_intent)
    print(f"Status  : {res_b['status']}")
    print(f"Action  : {res_b['action']}")
    print(f"Reason  : {res_b['reason']}\n")

if __name__ == "__main__":
    run_uidisa_demo()
