def get_pointed_ip(int_ip):
    """
    Prend en paramètre ip_int, une ip sous forme de nombre et 
    retourne l'ip sous forme décimale pointée
    """
    quotient1 = int_ip//2**8
    reste1 = int_ip%2**8
    quotient2 = quotient1//2**8
    reste2 = quotient1%2**8
    quotient3 = quotient2//2**8
    reste3 = quotient2%2**8
    reste4 = quotient3%2**8
    return '.'.join([str(reste4), str(reste3), str(reste2), str(reste1)])


def get_int_ip(pointed_ip):
    """
    Prend en paramètre ip_pointed, une ip sous forme déciame pointée 
    et retourne l'ip sous forme de nombre
    """
    numbers = [int(elt) for elt in pointed_ip.split('.')]
    number = 0
    number += numbers[0] << 24
    number += numbers[1] << 16
    number += numbers[2] << 8
    number += numbers[3]
    return number


def get_pointed_mask(cidr):
    """
    retourne le masque sous forme d'une ip décimale pointée. 
    Si le CIDR n'est pas conforme, retourne une string vide.
    """
    cidr = int(cidr)
    if cidr <32 :
        fullcidr = 32 * "1"
        cutcidr = fullcidr[:cidr] + "0" * (32-cidr)
        return get_pointed_ip(int(cutcidr, 2))
    else :
        return None


def get_int_cidr(mask):
    """
    retourne le cidr correspondant au masque sous forme déciamle pointée
    """
    binmask = (bin(get_int_ip(mask)))[2:]
    return binmask.count("1")


def get_network_address(ip_cidr):
    """
    paramètre : ip_cidr une addresse ip décimale pointée avec son cidr exemple 192.168.1.40/24
    Retourne, sous forme d'adresse IP pointée, l'adresse du réseau
    """
    ip, cidr = ip_cidr.split("/")
    mask = get_pointed_mask(int(cidr))
    intip = get_int_ip(ip)
    intmask = get_int_ip(mask)
    intnetwork_adress = intip & intmask
    pointednetwork_adress = get_pointed_ip(intnetwork_adress)
    return pointednetwork_adress


def get_nb_ip(pointed_mask):
    """
    pointed_mask : le masque sous forme d'une adresse ip décimale pointée
    retourne le nombre d'adresses ip possibles
    """
    cidr = get_int_cidr(pointed_mask)
    remainingbytes = (32-int(cidr)) * "1"
    nb_ip = int(remainingbytes, 2)
    return nb_ip +1


def get_nb_hosts(pointed_mask):
    """
    pointed_mask : le masque sous forme d'une adresse ip décimale pointée
    retourne le nombre d'hôtes possibles
    """
    nbip = get_nb_ip(pointed_mask)
    nbhosts = nbip-2
    return nbhosts


def get_first_ip(ip_cidr):
    """
    ip_cidr une addresse ip décimale pointée avec son cidr exemple 192.168.1.40/24
    Retourne la première ip utilisable
    """
    network_adress = get_network_address(ip_cidr)
    return get_pointed_ip(get_int_ip(network_adress)+1)


def get_last_ip(ip_cidr):
    """
    ip_cidr une addresse ip décimale pointée avec son cidr exemple 192.168.1.40/24
    Retourne la dernière ip utilisable
    """
    _, cidr = ip_cidr.split("/")
    network_adress = get_network_address(ip_cidr)

    return get_pointed_ip(get_int_ip(network_adress) + \
        int(get_nb_ip(get_pointed_mask(int(cidr))) - 2))


def get_broadcast_ip(ip_cidr):
    """
    ip_cidr une addresse ip décimale pointée avec son cidr exemple 192.168.1.40/24
    Retourne l'ip de boradcast
    """
    _, cidr = ip_cidr.split("/")
    network_adress = get_network_address(ip_cidr)
    return get_pointed_ip(get_int_ip(network_adress) + \
        int(get_nb_ip(get_pointed_mask(int(cidr)))-1))


def get_summary(ip_cidr):
    """
    Retourne un résumé
    >>> get_summary('192.168.1.20/21')

    Adresse IP : 192.168.1.20/21
    Masque de sous-réseau : 255.255.248.0
    Adresse réseau : 192.168.0.0
    Adresse de broadcast : 192.168.8.0
    Nombre d'hôtes possibles : 2046
    Première machine : 192.168.0.1
    Dernière machine : 192.168.7.255
    """
    _, cidr = ip_cidr.split("/")
    print(f"Adresse IP : {ip_cidr}\
        \nMasque de sous-réseau : {get_pointed_mask(int(cidr))}\
        \nAdresse réseau : {get_network_address(ip_cidr)}\
        \nAdresse de broadcast : {get_broadcast_ip(ip_cidr)}\
        \nNombre d'hôtes possibles :{get_nb_hosts(get_pointed_mask(cidr))}\
        \nPremière Machine : {get_first_ip(ip_cidr)}\
        \nDernière Machine : {get_last_ip(ip_cidr)}")

assert get_network_address('192.168.1.40/13') == '192.168.0.0'
assert get_nb_hosts('255.255.0.0') == 65534
assert get_nb_ip('255.255.0.0') == 65536
assert get_network_address('192.168.1.40/8') == '192.0.0.0'
assert get_network_address('192.168.1.40/13') == '192.168.0.0'
assert get_int_cidr('255.248.0.0') == 13
assert get_pointed_mask(131) is None
assert get_pointed_mask(13) == '255.248.0.0'
assert get_first_ip('192.168.1.40/13') == '192.168.0.1'
assert get_last_ip('192.168.0.0/30') == '192.168.0.2'
