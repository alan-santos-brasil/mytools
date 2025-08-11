pi_int = str(1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679)
e_int =  str(7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274)

def pi_real(n_de_casas_decimais):
    casas_decimais = pi_int[:n_de_casas_decimais]
    pi ="3," + casas_decimais
    return pi

def e_real(n_de_casas_decimais):
    casas_decimais = e_int[:n_de_casas_decimais]
    euler ="2," + casas_decimais
    return euler
