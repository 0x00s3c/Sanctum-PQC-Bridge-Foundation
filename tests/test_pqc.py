import oqs
import unittest

class TestPQCFoundation(unittest.TestCase):
    def test_ml_kem_handshake(self):
        """Validates that ML-KEM-768 is functioning on local hardware."""
        alg = "ML-KEM-768"
        
        # Client side (Sanctum Agent)
        with oqs.KeyEncapsulation(alg) as client:
            pk = client.generate_keypair()
            
            # Server side (Quantum Provider)
            with oqs.KeyEncapsulation(alg) as server:
                ciphertext, secret_server = server.encaps_secret(pk)
            
            # Client recovers secret
            secret_client = client.decaps_secret(ciphertext)
            
            self.assertEqual(secret_client, secret_server)
            print(f"✅ PQC Handshake Verified: {alg}")

if __name__ == "__main__":
    unittest.main()