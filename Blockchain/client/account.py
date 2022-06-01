""" 
Copyright (c) 2021 Codiesalert.com
These scripts should be used for commercial purpose without Codies Alert Permission
Any violations may lead to legal action
"""
import sys

sys.path.append("/Users/Vmaha/Desktop/Bitcoin")
from Blockchain.Backend.core.EllepticCurve.EllepticCurve import Sha256Point
from Blockchain.Backend.util.util import hash160, hash256
from Blockchain.Backend.core.database.database import AccountDB
import secrets


class account:
    def createKeys(self):
        """Secp256k1 Curve Generator Points"""
        Gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
        Gy = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8

        """Create an Instance of Class Sha256Point"""
        G = Sha256Point(Gx, Gy)

        """ Generate Secure Private Key """
        self.privateKey = secrets.randbits(256)

        """ 
         # Multiply Private Key with Generator Point
         # Returns X-coordinate and Y-Coordinate 
        """
        unCompressesPublicKey = self.privateKey * G
        xpoint = unCompressesPublicKey.x
        ypoint = unCompressesPublicKey.y

        """ Address Prefix for Odd or even value of YPoint """
        if ypoint.num % 2 == 0:
            compressesKey = b"\x02" + xpoint.num.to_bytes(32, "big")
        else:
            compressesKey = b"\x03" + xpoint.num.to_bytes(32, "big")

        """ RIPEMD160 Hashing Algorithm returns the hash of Compressed Public Key"""
        
        hsh160 = hash160(compressesKey)

        """Prefix for Mainnet"""
        main_prefix = b"\x00"

        newAddr = main_prefix + hsh160

        """Checksum"""
        checksum = hash256(newAddr)[:4]

        newAddr = newAddr + checksum
       
        BASE58_ALPHABET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

        """Counter to find Leading zeros """
        count = 0
        for c in newAddr:
            if c == 0:
                count += 1
            else:
                break
        """ Convert to Numeric from Bytes """
        num = int.from_bytes(newAddr, "big")
        prefix = "1" * count

        result = ""

        """ BASE58 Encoding """
        while num > 0:
            num, mod = divmod(num, 58)
            result = BASE58_ALPHABET[mod] + result

        self.PublicAddress = prefix + result

        print(f"Private Key {self.privateKey}")
        print(f"Public Key {self.PublicAddress}")
        print(f"Xpoint {xpoint} \n Ypoint {ypoint}")


if __name__ == "__main__":
    acct = account()
    acct.createKeys()
    AccountDB().write([acct.__dict__])
