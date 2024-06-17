
from os import path, remove

class Files:
    """
    # Files :
        1- Read.
        2- Write and Create.
        3- Find.
        4- Check Encryption File.
        5- Remove File.
    """
    @staticmethod
    def read( file_path:str ) -> bytes :
        with open( file_path , 'rb') as file:
            data: bytes = file.read()
            file.close()
        return data

    @staticmethod
    def write( file_path: str, data: bytes ) -> None :
        with open( file_path, 'wb' ) as file: 
            file.write(data)
            file.close()

    @staticmethod
    def check_file_encrypt( file_path:str ) -> bool :
        return True if file_path.split('.')[-1] == "x" else False

    @staticmethod
    def find( full_path: str ) -> bool:
        return path.exists(full_path) 

    @staticmethod
    def remove_file( file_path:str ) -> None :
        remove(file_path)
