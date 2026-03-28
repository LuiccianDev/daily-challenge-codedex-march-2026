import re
def check_url(address):
    
    pattern = r"^https?://[A-Za-z0-9.-]+\.[A-Za-z0-9.-]+$"
    
    if re.fullmatch(pattern, address):
        return "valid"
    else:
        return "invalid"