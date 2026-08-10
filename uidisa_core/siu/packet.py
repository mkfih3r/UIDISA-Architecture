import time
from .crypto import SIUCryptoEngine

class SmartInformationUnit:
    """
    Smart Information Unit (SIU) representing data payload integrated with 
    Semantic Weight (Sigma) and Entropy Delta Barrier tracking.
    """
    def __init__(self, raw_payload: bytes, semantic_weight: float, context_signature: str):
        if not (0.0 <= semantic_weight <= 1.0):
            raise ValueError("Semantic Weight (Sigma) must be between 0.0 and 1.0")

        self.semantic_weight = semantic_weight
        self.context_signature = context_signature
        self.created_at = time.time()
        self.entropy_delta = 0  # 0 = Valid State, > 0 = Anomaly Breach

        self._internal_key = SIUCryptoEngine.generate_entropy_key()
        self.payload_tensor = SIUCryptoEngine.apply_state_scramble(raw_payload, self._internal_key)

    def trigger_self_destruct(self):
        """Irreversibly corrupts payload tensor into pure entropy noise."""
        self.entropy_delta = 1
        noise = SIUCryptoEngine.generate_irreversible_noise(len(self.payload_tensor))
        self.payload_tensor = SIUCryptoEngine.apply_state_scramble(self.payload_tensor, noise)
        self._internal_key = SIUCryptoEngine.generate_entropy_key()

    def extract_payload(self) -> bytes:
        if self.entropy_delta != 0:
            raise PermissionError("Access Denied: Dynamic Entropy Barrier Breached.")
        return SIUCryptoEngine.apply_state_scramble(self.payload_tensor, self._internal_key)
