import numpy as np

def cutting_speed(D, N):
    return (np.pi * D * N) / 1000


def feed_per_tooth(F, N, z):
    return F / (N * z)


def cutting_force(vc, fz, ap, w,
                  Cf=15, a_vc=0.2, a_fz=0.5, a_ap=1.0, a_w=0.4):
    
    Fc = Cf * (vc / 120)**a_vc \
           * (fz / 0.08)**a_fz \
           * (ap**a_ap) \
           * (w**a_w)

    return Fc


def surface_roughness(fz, r=1.0):
    Ra = (fz / (8 * r)) * 1000
    return Ra


def tool_wear_rate(vc, fz, ap, w,
                   Cw=2.5e-6,
                   x_vc=0.6,
                   x_fz=0.4,
                   x_ap=0.3,
                   x_w=0.2):

    TWR = Cw * (vc/120)**x_vc \
            * (fz/0.08)**x_fz \
            * (ap**x_ap) \
            * (w**x_w)

    return TWR


def cutting_temperature(Fc, vc, ap, w, Ct=5):
    return (Ct * Fc * (vc / 60)) / (ap * w)


def chip_load_deviation(fz, ideal=0.08):
    return abs((fz - ideal) / ideal)


def power_consumption(Fc, vc):
    return Fc * (vc / 60)
