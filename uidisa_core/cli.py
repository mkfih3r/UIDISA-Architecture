import sys
import time
import hashlib
from siu.packet import SmartInformationUnit
from ivem.matrix import IntentVector
from ivem.audit import IVEMAuditEngine
from defense.memory_wiper import MemorySanitizationEngine

def print_banner():
    print("=========================================================================")
    print(" 🛡️  UIDISA: UNIFIED INTENT-DRIVEN INFORMATION SECURITY ARCHITECTURE")
    print("    Active Entropic Self-Defense Runtime Engine & Inspection Workbench")
    print("=========================================================================\n")
import os

def display_banner():
    # Terminal Colour Code (Color Styling)
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'

    banner = f"""{CYAN}
  _   _  ___  ____  ___  ____    _    
 | | | ||_ _||  _ \\|_ _|/ ___|  / \\   
 | | | | | | | | | || | \\___ \\ / _ \\  
 | |_| | | | | |_| || |  ___) / ___ \\ 
  \\___/ |___||____/|___||____/_/   \\_\\
                                      
{RESET}=========================================================
{YELLOW} Unified Intent-Driven Information Security Architecture{RESET}
=========================================================
 {GREEN}[+]{RESET} Core Engine       : Online
 {GREEN}[+]{RESET} Entropic Barrier  : Standby
 {GREEN}[+]{RESET} IVEM Matrix       : Active
 {GREEN}[+]{RESET} Version           : 1.0.0
=========================================================
    """
    
    # Screen clear bannar
    os.system('cls' if os.name == 'nt' else 'clear')
    print(banner)
    
def run_interactive_cli():
    print_banner()
    
    while True:
        print("\n[ SELECT OPERATION MODE ]")
        print("1. Package Payload into Smart Information Unit (SIU)")
        print("2. Simulate Authorized Decryption Sequence")
        print("3. Simulate MITM Attack / Context Hijack (Trigger Self-Destruct)")
        print("4. Inspect Volatile Memory State Wiper")
        print("5. Exit Workbench")
        
        choice = input("\nEnter choice (1-5): ").strip()
        
        if choice == '1':
            data = input("\nEnter raw sensitive data string: ").encode('utf-8')
            weight = float(input("Enter Semantic Weight (Sigma: 0.0 - 1.0): "))
            env_id = input("Enter Target Node ID (e.g., ECU_NODE_01): ")
            
            env_hash = hashlib.sha256(env_id.encode('utf-8')).hexdigest()
            siu = SmartInformationUnit(data, weight, env_hash)
            
            print("\n✅ SIU Packet Successfully Packaged!")
            print(f" - Semantic Weight (Sigma) : {siu.semantic_weight}")
            print(f" - Environment Hash        : {siu.context_signature[:20]}...")
            print(f" - Encrypted Payload Tensor: {siu.payload_tensor.hex()[:32]}...")
            
        elif choice == '2':
            print("\n[ Running Authorized Verification ]")
            valid_hash = hashlib.sha256(b"ECU_NODE_01").hexdigest()
            intent = IntentVector("EXECUTE_COMMAND", valid_hash, ["SECURE_BUS"])
            
            packet = SmartInformationUnit(b"SYSTEM_PARAM_OPTIMIZATION", 0.9, valid_hash)
            auditor = IVEMAuditEngine()
            
            result = auditor.evaluate_access_request(packet, intent, intent)
            print(f" -> Status: {result['status']}")
            print(f" -> Unlocked Payload: {result['data']}")
            
        elif choice == '3':
            print("\n🚨 [ Simulating Adversarial Context Hijack / MITM Interception ]")
            valid_hash = hashlib.sha256(b"ECU_NODE_01").hexdigest()
            hacker_hash = hashlib.sha256(b"ROGUE_INTERCEPTOR_NODE").hexdigest()
            
            target_intent = IntentVector("EXECUTE_COMMAND", valid_hash, ["SECURE_BUS"])
            attacker_intent = IntentVector("EXECUTE_COMMAND", hacker_hash, ["SECURE_BUS"])
            
            packet = SmartInformationUnit(b"CRITICAL_BRAKE_COMMAND", 0.99, valid_hash)
            auditor = IVEMAuditEngine()
            
            time.sleep(0.5)
            print("⚡ Evaluating Intent Matrix (IVEM)...")
            result = auditor.evaluate_access_request(packet, attacker_intent, target_intent)
            
            print(f"\n❌ ATTACK NEUTRALIZED!")
            print(f" -> Status: {result['status']}")
            print(f" -> Action: {result['action']}")
            print(f" -> Reason: {result['reason']}")
            print(f" -> Corrupted Payload State: {packet.payload_tensor.hex()[:32]}... (Irreversible Noise)")

        elif choice == '4':
            print("\n[ Running Memory Sanitization Sweep ]")
            buffer = bytearray(b"SENSITIVE_SECRET_KEY_IN_RAM_BUFFER")
            print(f" -> Pre-wipe RAM Address Contents : {buffer.decode('utf-8')}")
            
            MemorySanitizationEngine.secure_wipe_bytearray(buffer)
            print(f" -> Post-wipe Sanitized State (Hex): {buffer.hex()}")
            print("✅ Volatile RAM Sanitized (Zero Residue Left).")

        elif choice == '5':
            print("\nExiting UIDISA Workbench. Stay secure!")
            sys.exit(0)
        else:
            print("Invalid choice. Please select 1 to 5.")

if __name__ == "__main__":
    run_interactive_cli()
