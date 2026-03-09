import oqs

class PQCSecureTunnel:
    def __init__(self, kem_alg="ML-KEM-768"):
        self.kem_alg = kem_alg

    def generate_agent_keys(self):
        """Generates PQC keypair for the local Sanctum agent."""
        with oqs.KeyEncapsulation(self.kem_alg) as kem:
            public_key = kem.generate_keypair()
            private_key = kem.export_secret_key()
            return public_key, private_key

    def encapsulate_for_qpu(self, qpu_public_key):
        """Establishes a shared secret with the remote QPU."""
        with oqs.KeyEncapsulation(self.kem_alg) as kem:
            ciphertext, shared_secret = kem.encaps_secret(qpu_public_key)
            return ciphertext, shared_secret