# **about FileEncryption:**
This tool is used to encrypt and decrypt files using `Fernet` in Python.

# **SETUP:**
```sh
$ git clone https://github.com/Mohaned2023/FileEncryption.git
$ cd FileEncryption 
$ pip install requirements.txt
$ python main.py --help
```

# **HOW TO USE:**
1. **File Encryption:**
    - You need to set the file path using `-p` or `--path`.
    - The new file name will be `file.txt.x`, with `.x` appended to the end.
    - The tool will ask if you want to delete the original file (`file.txt`).
    - Enter `yes` or `y` if you want to delete the original file (`file.txt`). Otherwise, the file will not be deleted.
    - You can also specify a custom key if you have one.
    - The key should be `base64-encoded` bytes.
```sh
$ python main.py -p "user/folder/file.txt"
```
```txt
[?] Do you have 32 url-safe base64-encoded bytes key? yes
[~] Enter the key: Jt6k43aACjabWr7q3jHyGmpnzv2U8OPlJWEiqyO3vuw=
[*] Your decryption key is : Jt6k43aACjabWr7q3jHyGmpnzv2U8OPlJWEiqyO3vuw=
[?] Do you want to remove the file `user/folder/file.txt` ?
[Yes/No]: yes
[+] Note: You need to save the key, if you lose the key you will not be able to decrypt the file!!
```

2. **File Decryption:**

    - You need to set the file path using `-p` or `--path`, and specify decryption with `-de` or `--decrypt`.
    - The file type must be `.x` (`file.txt.x`). If you use a different file type, it will not be decrypted correctly.
    - You need to provide the decryption key to decrypt the file.
    - The tool will ask if you want to delete the original file (`file.txt.x`).
    - Enter `yes` or `y` if you want to delete the original file (`file.txt.x`). Otherwise, the file will not be deleted.
```sh
$ python main.py -p "user/folder/file.txt.x" -de
```

```txt
[~] Enter The Decryption key: Jt6k43aACjabWr7q3jHyGmpnzv2U8OPlJWEiqyO3vuw=
[?] Do you want to remove the file `user/folder/file.txt.x` ?
[Yes/No]: Yes
```

### **My Accounts:**
> - [**LinkedIn**](https://www.linkedin.com/in/mohaned2023)  
> - [**X**](https://x.com/MrX2023M)
> - [**Instagram**](https://www.instagram.com/mr.lxzl)