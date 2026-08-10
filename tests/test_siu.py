import hashlib
import pytest
from uidisa_core.siu.packet import SmartInformationUnit

def test_siu_creation_and_payload_extraction():
    payload = b"TEST_PAYLOAD_DATA"
    valid_hash = hashlib.sha256(b"NODE_TEST_01").hexdigest()

    siu = SmartInformationUnit(payload, 0.8, valid_hash)
    
    assert siu.semantic_weight == 0.8
    assert siu.context_signature == valid_hash
    assert siu.entropy_delta == 0
    assert siu.extract_payload() == payload

def test_siu_invalid_semantic_weight():
    valid_hash = hashlib.sha256(b"NODE_TEST_01").hexdigest()
    
    with pytest.raises(ValueError):
        SmartInformationUnit(b"TEST", 1.5, valid_hash)

def test_siu_self_destruction():
    payload = b"CONFIDENTIAL_DATA"
    valid_hash = hashlib.sha256(b"NODE_TEST_01").hexdigest()

    siu = SmartInformationUnit(payload, 0.9, valid_hash)
    siu.trigger_self_destruct()

    assert siu.entropy_delta == 1
    assert siu.payload_tensor != payload

    with pytest.raises(PermissionError):
        siu.extract_payload()
