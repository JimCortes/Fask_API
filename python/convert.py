import re
import ipaddress



class CidrMaskConvert:


    
    def cidr_to_mask(self, cidr):
        mask = str(ipaddress.IPv4Network(f"0.0.0.0/{cidr}").netmask)
        if mask == '0.0.0.0':
            return "Invalid"
        else:
            return mask
    def mask_to_cidr(self, mask):
        if mask == '0.0.0.0':
            return "Invalid"
        else:
            return str(ipaddress.IPv4Network(f"0.0.0.0/{mask}").prefixlen)

class IpValidate:
    def ipv4_validation(self, ip):
        try:
            return ipaddress.ip_address(ip).version == 4
        except:
            return False
