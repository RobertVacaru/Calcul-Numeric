import math
from decimal import Decimal


def get_u():
    u = 1
    while Decimal(1) + Decimal(u) != Decimal(1):
        u = Decimal(u) / Decimal(10)
    return Decimal(u)


# def get_u():
#     u = Decimal(1)
#     next = 1.1
#     while Decimal(u) != Decimal(next):
#         next = Decimal(u)
#         u = Decimal(u) / 10
#     return Decimal(u)

def numere_inmultite_non_asociative():
    a = 0.6
    b = 0.2
    c = 0.4
    p1 = (Decimal(a) * Decimal(b)) * Decimal(c)
    p2 = Decimal(a) * (Decimal(b) * Decimal(c))
    while p1 == p2:
        a = pow(Decimal(a), 2)
        b = pow(Decimal(b), 2)
        c = pow(Decimal(c), 2)
        p1 = (Decimal(a) * Decimal(b)) * Decimal(c)
        p2 = Decimal(a) * (Decimal(b) * Decimal(c))
    if Decimal(p1) != Decimal(p2):
        print("Operatia de inmulire data nu este asociativa.")
    print("Numerele pentru care operatia de inmultire nu mai este asociativa sunt:")
    print(Decimal(a), Decimal(b), Decimal(c))
    return a, b, c


def sin_coef(x):
    a = [
        1805490264.690988571178600370234394843221,
        -164384678.227499837726129612587952660511,
        3664210.647581261810227924465160827365,
        -28904.140246461781357223741935980097,
        76.568981088717405810132543523682
    ]
    b = [
        2298821602.638922662086487520330827251172,
        27037050.118894436776624866648235591988,
        155791.388546947693206469423979505671,
        540.567501261284024767779280700089,
        1.0
    ]
    x = x / math.pi * 4
    x2 = x ** 2
    P = a[0] + x2 * (a[1] + x2 * (a[2] + x2 * (a[3] + x2 * a[4])))
    Q = b[0] + x2 * (b[1] + x2 * (b[2] + x2 * (b[3] + x2 * b[4])))
    return (P / Q) * x


def cos_coef(x):
    a = [
        1090157078.174871420428849017262549038606,
        -321324810.993150712401352959397648541681,
        12787876.849523878944051885325593878177,
        -150026.206045948110568310887166405972,
        538.333564203182661664319151379451,
    ]

    b = [
        1090157078.174871420428867295670039506886,
        14907035.776643879767410969509628406502,
        101855.811943661368302608146695082218,
        429.772865107391823245671264489311,
        1.0,
    ]
    x = x / math.pi * 4
    x2 = x ** 2
    P = a[0] + x2 * (a[1] + x2 * (a[2] + x2 * (a[3] + x2 * a[4])))
    Q = b[0] + x2 * (b[1] + x2 * (b[2] + x2 * (b[3] + x2 * b[4])))

    return P / Q


def coef_ln(x):
    a = [
        75.151856149910794642732375452928,
        -134.730399688659339844586721162914,
        74.201101420634257326499008275515,
        -12.777143401490740103758406454323,
        0.332579601824389206151063529971,
    ]

    b = [
        37.575928074955397321366156007781,
        -79.890509202648135695909995521310,
        56.215534829542094277143417404711,
        -14.516971195056682948719125661717,
        1.0
    ]
    z = (x - 1) / (x + 1)
    z2 = z ** 2
    P = a[0] + z2 * (a[1] + z2 * (a[2] + z2 * (a[3] + z2 * a[4])))
    Q = b[0] + z2 * (b[1] + z2 * (b[2] + z2 * (b[3] + z2 * b[4])))
    if Q < 10 ** (-12):
        Q = 10 ** (-12)
    return z * P / Q
