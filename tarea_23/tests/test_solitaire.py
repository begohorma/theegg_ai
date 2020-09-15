from src.solitaire import Solitaire

def test_encrypt_with_blank_key():
    s = Solitaire()
    output = s.encrypt("DO NOT USE PC", "")
    assert output == "OSKJJ JGTMW"

def test_decrypt_with_blank_key():
    s = Solitaire()
    output = s.decrypt("OSKJJ JGTMW", "")
    assert  output == "DO NOT USE PC"
