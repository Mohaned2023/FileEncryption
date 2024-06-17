
from src.Encryption_Decryption import EncryptionDecryption
from argparse import ArgumentParser
from src.files import Files

class Main:
    @staticmethod
    def main(arges) -> None:
        try:
            is_there: bool = Files.find(arges.path)
            if not is_there:
                raise Exception(f"No search file '{arges.path}'")
            if arges.decrypt:
                if not Files.check_file_encrypt(arges.path):
                    raise Exception("The File is not encrypt")
                key: bytes = input("[\033[0;32m~\033[0m] Enter The Decryption key\033[0;32m:\033[0m ").encode()
                en_data: bytes = Files.read(arges.path)
                de_data: bytes = EncryptionDecryption.decryption(en_data, key)
                Files.write(arges.path.removesuffix('.x'), de_data)
                print(f"[\033[0;32m?\033[0m] Do you want to remove the file `{arges.path}` \033[0;32m?\033[0m")
                if input("[\033[0;32mYes/No\033[0m]\033[0;32m:\033[0m ").lower() in ['yes','y']: 
                    Files.remove_file(arges.path)

            else :
                have_key: bool = True if input("[\033[0;32m?\033[0m] Do you have 32 url-safe base64-encoded bytes key\033[0;32m?\033[0m ").lower() in ['yes','y'] else False
                data: bytes = Files.read(arges.path)
                en_object: dict = EncryptionDecryption.encryption(
                    data,
                    key= None if not have_key else input("[\033[0;32m~\033[0m] Enter the key\033[0;32m:\033[0m ").encode()
                )
                Files.write( arges.path+'.x', en_object['en_data'])
                print(f"[\033[0;34m*\033[0m] Your decryption key is \033[0;34m:\033[0m {en_object['key'].decode()}")
                print(f"[\033[0;32m?\033[0m] Do you want to remove the file `{arges.path}` \033[0;32m?\033[0m")
                if input("[\033[0;32mYes/No\033[0m]\033[0;32m:\033[0m ").lower() in ['yes','y']: 
                    Files.remove_file(arges.path)
                print("[\033[0;31m+\033[0m] Note\033[0;31m:\033[0m You need to save the key, if you lose the key you will not be able to decrypt the file\033[0;31m!!\033[0m")
        except Exception as error: 
            print(f"[\033[0;31m!\033[0m] {error}\033[0;31m!\033[0m")

if __name__=="__main__":
    parser: ArgumentParser = ArgumentParser(
		prog="main.py",
		epilog="This Tool Was Created by `Mohaned Sherhan (MR.X)`.",
	)
    parser.add_argument(
        '-p',
        '--path',
        type=str,
        required=True,
        help='File Path.'
    )
    parser.add_argument(
        '-de',
        '--decrypt',
        action='store_true',
        help='To Decrypt The File.'
    )
    Main.main(  parser.parse_args()  )