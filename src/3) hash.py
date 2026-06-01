import hashlib

def md5hash(txt):
    md5=hashlib.md5(txt)
    print(md5.hexdigest())

def sha256hash(txt):
    sha256 = hashlib.sha256(txt)
    print(sha256.hexdigest())

def sha512hash(txt):
    sha512=hashlib.sha512(txt)
    print(sha512.hexdigest())

plaintxt=str(input("Enter a plain text ")).encode()
print("-----------Hashing-----------")
print("1. md5")
print("2. sha256")
print("3. sha512")

inp1= input("Enter the hash hash you want to perform ")

match inp1:
    case "1" | "md5":
        md5hash(plaintxt)
    case "2" | "sha256":
        sha256hash(plaintxt)
    case "3" | "sha512":
        sha512hash(plaintxt)