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
    """
    paramètre : ip_cidr une addresse ip décimale pointée avec son cidr exemple 192.168.1.40/24
    Retourne, sous forme d'adresse IP pointée, l'adresse du réseau
    """
    return get_pointed_ip((2**cidr-1)<<(32-cidr)) # Donne le masque à partir du /CIDR

assert get_pointed_mask(13) == '255.248.0.0'
get_pointed_mask(13)

def get_int_cidr(mask):
    """
    pointed_mask : le masque sous forme d'une adresse ip décimale pointée
    retourne le nombre d'adresses ip possibles
    """
    intmask = get_int_ip(mask) # Transforme le masque en entier
    return bin(intmask).count("1") # retourne le CIDR en comptant le nombre de 1

assert get_int_cidr('255.248.0.0') == 13
get_int_cidr('255.248.0.0')

def get_network_address(ip_cidr):
    """
    paramètre : ip_cidr une addresse ip décimale pointée avec son cidr exemple 192.168.1.40/24
    Retourne, sous forme d'adresse IP pointée, l'adresse du réseau
    """
    ip , cidr = ip_cidr.split("/") # divise l'adresse ip du cidr
    intip = get_int_ip(ip) # transforme en entier l'adresse ip
    mask = get_pointed_mask(int(cidr)) # transforme en entier le cidr
    intmask = get_int_ip(mask) # Donne le masque à partir du CIDR
    network_address = intip & intmask # Fait un "ET" entre le masque et l'adresse ip pour avoir l'ip du réseau
    return get_pointed_ip(network_address) #retourne l'adresse ip du réseau


assert get_network_address('192.168.1.40/13') == '192.168.0.0'
get_network_address('192.168.1.40/13')    
    

# def get_nb_ip(pointed_mask):
#     """
#     pointed_mask : le masque sous forme d'une adresse ip décimale pointée
#     retourne le nombre d'adresses ip possibles
#     """
#     intip = get_int_ip(pointed_mask)
#     binip = bin(intip)[2:]
#     notbin = 
#     
    
    
    