def get_pointed_ip(int_ip):
    """
    Prend en paramètre ip_int, une ip sous forme de nombre et retourne l'ip sous forme décimale pointée
    """
    quotient1 = int_ip//2**8
    reste1 = int_ip%2**8
    quotient2 = quotient1//2**8
    reste2 = quotient1%2**8
    quotient3 = quotient2//2**8
    reste3 = quotient2%2**8
    reste4 = quotient3%2**8
    return '.'.join([str(reste4), str(reste3), str(reste2), str(reste1)])

assert get_pointed_ip(3232235816) == '192.168.1.40'
get_pointed_ip(3232235816)

def get_int_ip(pointed_ip):
    """
    Prend en paramètre ip_pointed, une ip sous forme déciame pointée et retourne l'ip sous forme de nombre
    """
    numbers = [int(elt) for elt in pointed_ip.split('.')]
    number = 0
    number += numbers[0] << 24
    number += numbers[1] << 16
    number += numbers[2] << 8
    number += numbers[3]
    return number

assert get_int_ip('192.168.1.40') == 3232235816
get_int_ip('192.168.1.40')

def get_pointed_mask(cidr):
    get_pointed_ip((2**cidr-1)<<(32-cidr))

assert get_pointed_mask(13) == '255.248.0.0'
get_pointed_mask(13)