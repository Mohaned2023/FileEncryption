
from cryptography.fernet import Fernet

class EncryptionDecryption:
    """
    # EncryptionDecryption :
        1- Encryption.
        2- Decryption.
    """
    @staticmethod
    def encryption( data:bytes, key:bytes = None) -> dict[str,bytes] :
        if not key :
            key = Fernet.generate_key()
        cypher: Fernet = Fernet( key )
        en_data: bytes = cypher.encrypt(data)
        return {'en_data': en_data, 'key': key}

    @staticmethod
    def decryption( en_data: bytes, key:bytes ) -> bytes:
        cypher: Fernet = Fernet(key)
        try:
            return cypher.decrypt(en_data)
        except:
            raise Exception("Wrong key")