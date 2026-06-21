import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def main():
    # inputs
    Tpi = 40
    # input(' Temperature of Primary air at inlet (°C) = ');

    V = 7
    # input(' Velocity of primary air at inlet (m/s) = ');

    Twi = 18
    # input(' Temperature of Water (°C) = ');

    RH = 30
    # input(' relative humidity (%) = ');

    N = 33
    # input('number of Floors = ');

    L = 0.8  # input('Length of plates (m) = ');

    W = 0.6  # input('Width of plates (m) = ');

    WP = 0.05  # input('width of product channals (m) = ');

    H = 0.003  # input('height of Product channals (m) = ');

    HW = 0.006  # input('height of Wet channals (m) = ');

    delta = 0.0025  # input(' film of water (m) = ');

    NP = 8  # input('number of product channal (m) = ');

    NW = 10  # input('number of wet channal (m) = ');

    Tetta = 0.5  # input('angle of plate (degree) = ');

    # air and water properties
    P_air = 101000  # pa
    density_air = 1.127  # kg/m3
    density_water = 978  # kg/m3
    Cp_air = 1.005  # kj/kg.k
    Cp_water = 4.200  # kj/kg.k
    Cp_vaper = 2.100  # kj/kg.k
    K_air = 0.027  # w/m.k
    Pr_air = 0.711
    noo_air = 16.97 * 10 ** -6
    h_fg = 2256

    # channels area
    A_dry = N * ((W - (NP * WP)) * H)  # m2
    A_product = (N * NP * (WP * H))  # m2
    A_wet = 2 * N * NW * ((L / NW) * (HW - delta))  # m2
    A_film = 2 * N * L * delta  # m2

    # flow's velocity
    V_dry = V  # m/s
    V_product = V  # m/s
    V_wet = V_dry * (A_dry / A_wet)  # m/s
    V_film = ((np.sin(3.14 * Tetta / 180)) ** 0.5) * (delta ** (2 / 3)) / 0.012  # m/s

    # mass flow rate
    M_product = (density_air * A_product * V_product) * 3600  # kg/h
    M_dry = (density_air * A_dry * V_dry) * 3600  # kg/h
    M_wet = (density_air * A_wet * V_wet) * 3600  # kg/h
    M_film = (density_water * A_film * V_film) * 3600  # kg/h

    # Equivalent diameter for product and wet channels
    D_h_product = 4 * ((WP * H) / (2 * (WP + H)))  # m
    D_h_wet = 4 * ((L / NW) * (HW - delta) / (2 * ((L / NW) + (HW - delta))))  # m

    # reynoldz number for product and wet flows
    Re_product = (V_product * D_h_product) / (noo_air)
    Re_wet = (V_wet * D_h_wet) / (noo_air)

    # nuselt number for product flow
    if Re_product < 2300:
        if WP / H == 1.43:
            Nu_product = 3.08
        elif WP / H == 2.0:
            Nu_product = 3.39
        elif WP / H == 3.0:
            Nu_product = 3.96
        elif WP / H == 4.0:
            Nu_product = 4.44
        elif WP / H == 8.0:
            Nu_product = 5.6
        elif WP / H < 1.43:
            pp = WP / H
            Nu_product = 3.08 - (1.43 - pp) * (0.31 / 0.57)
        elif 1.43 < WP / H < 2.0:
            pp = WP / H
            Nu_product = 3.08 + (1.43 - pp) * (0.31 / 0.57)
        elif 2.0 < WP / H < 3.0:
            pp = WP / H
            Nu_product = 3.39 + (pp - 2.0) * 0.57
        elif 3.0 < WP / H < 4.0:
            pp = WP / H
            Nu_product = 3.96 + (pp - 3.0) * 0.48
        elif 4.0 < WP / H < 8.0:
            pp = WP / H
            Nu_product = 4.44 + (pp - 4.0) * 0.29
        elif WP / H > 8.0:
            pp = WP / H
            Nu_product = 5.6 + (pp - 8.0) * 0.29
    else:
        Nu_product = 0.023 * (Re_product ** 0.8) * (Pr_air ** 0.3)

    # nuselt number for wet flow
    if Re_wet < 2300:
        if (L / NW) / (HW - delta) == 1.43:
            Nu_wet = 3.08
        elif (L / NW) / (HW - delta) == 2.0:
            Nu_wet = 3.39
        elif (L / NW) / (HW - delta) == 3.0:
            Nu_wet = 3.96
        elif (L / NW) / (HW - delta) == 4.0:
            Nu_wet = 4.44
        elif (L / NW) / (HW - delta) == 8.0:
            Nu_wet = 5.6
        elif (L / NW) / (HW - delta) < 1.43:
            ww = (L / NW) / (HW - delta)
            Nu_wet = 3.08 - (1.43 - ww) * (0.31 / 0.57)
        elif 1.43 < (L / NW) / (HW - delta) < 2.0:
            ww = (L / NW) / (HW - delta)
            Nu_wet = 3.08 + (1.43 - ww) * (0.31 / 0.57)
        elif 2.0 < (L / NW) / (HW - delta) < 3.0:
            ww = (L / NW) / (HW - delta)
            Nu_wet = 3.39 + (ww - 2.0) * 0.57
        elif 3.0 < (L / NW) / (HW - delta) < 4.0:
            ww = (L / NW) / (HW - delta)
            Nu_wet = 3.96 + (ww - 3.0) * 0.48
        elif 4.0 < (L / NW) / (HW - delta) < 8.0:
            ww = (L / NW) / (HW - delta)
            Nu_wet = 4.44 + (ww - 4.0) * 0.29
        elif (L / NW) / (HW - delta) > 8.0:
            ww = (L / NW) / (HW - delta)
            Nu_wet = 5.6 + (ww - 8.0) * 0.29
    else:
        Nu_wet = 0.023 * (Re_wet ** 0.8) * (Pr_air ** 0.3)

    # Determine the coefficient (h) for wet and product flows
    h_product = (Nu_product * K_air) / D_h_product  # W^2/k.m^2
    h_wet = (Nu_wet * K_air) / D_h_wet  # W^2/k.m^2

    # Draw temperature graph of product air in terms of length of heat exchanger
    x = np.arange(0, L + 0.001, 0.001)

    z = (-h_product * WP) / (((M_product) / ((N) * NP * 3600)) * (Cp_air) * 1000)

    T_product = (Tpi - Twi) * np.exp(z * x) + Twi  # C

    plt.figure(1)
    plt.plot(x, T_product)
    plt.grid(True)
    plt.xlabel('length of HMX (m)')
    plt.ylabel('Temperature of product channel (°C)')

    # Calculates the inlet temperature of each wet channel
    WW = L / NW  # width of wet channel         #m
    CW = WW / 2  # m
    TCW = np.zeros(NW)

    i = 0  # 0-based index
    while CW < L:
        TCW[i] = (Tpi - Twi) * np.exp(z * CW) + Twi  # C
        CW = CW + WW
        i = i + 1

    # Calculate absolute humidity and amount of water consumed
    evaporation = np.zeros(NW)
    evp = 0

    MWC = M_wet / (2 * (N * NW))  # kg/h

    for i in range(NW):
        P_g = 0.13332239 * 1000 * np.exp(20.386 - (5132 / (TCW[i] + 273.15)))  # pa
        abs_humidity = 0.622 * (((RH / 100) * P_g) / (P_air - ((RH / 100) * P_g)))  # kg/kg
        abs_humidity_sat = 0.622 * (P_g / (P_air - P_g))  # kg/kg
        evaporation[i] = MWC * (abs_humidity_sat - abs_humidity)  # kg/h
        evp = evp + evaporation[i]

    evporation_total = N * 2 * evp  # kg/h
    Water_Usage = evporation_total * (1000 / density_water)  # Li/h

    # pressure loss in product channel
    if Re_product < 3000:
        f_product = 64 / Re_product
    else:
        f_product = 1 * (-1.8 * np.log10((((0.15 * 0.001 / D_h_product) / 3.7) ** 1.11) + (6.9 / Re_product))) ** (-2)

    h_L_product = f_product * (L / D_h_product) * ((V_product ** 2) / (2 * 9.81))  # m
    PL_product1 = h_L_product * density_air * 9.81  # pa
    PL_product2 = ((8 * V_product * noo_air) * (density_air) / (((D_h_product / 2) ** 2))) * (1.1 * L)  # pa

    # pressure loss in wet channel
    if Re_wet < 3000:
        f_wet = 64 / Re_wet
    else:
        f_wet = 1 * (-1.8 * np.log10((((0.15 * 0.001 / D_h_wet) / 3.7) ** 1.11) + (6.9 / Re_wet))) ** (-2)

    h_L_wet = f_wet * ((W / 2) / D_h_wet) * ((V_wet ** 2) / (2 * 9.81))  # m
    PL_wet1 = h_L_wet * density_air * 9.81 + PL_product1  # pa
    PL_wet2 = ((8 * V_wet * noo_air) * (density_air) / (((D_h_wet / 2) ** 2))) * (1.1 * (W / 2)) + PL_product2  # pa

    # Determine fan power
    Q_fan = ((M_product + M_dry) / 3600) / density_air  # m^3/s

    if PL_wet1 < PL_wet2:
        Power_fan = Q_fan * PL_wet2 * 2.5  # W
    else:
        Power_fan = Q_fan * PL_wet1 * 2.5  # W

    # Determine pump power
    Q_film = 2 * N * ((np.sin(3.14 * Tetta / 180)) ** 0.5) * (delta ** (5 / 3)) * 0.8 / 0.012  # m^3/s
    pressure_of_tank = 3.5 * (delta ** (4 / 3)) * np.sin(Tetta * 3.14 / 180) + 200  # pa
    Power_pump = Q_film * pressure_of_tank * 2.5  # W

    # HMX properties
    NTU = z * L

    Ti = 1.8 * Tpi + 32  # °F
    To = 1.8 * ((Tpi - Twi) * np.exp(z * L) + Twi) + 32  # °F
    cfm = (M_product * 27 / 60)  # Ft^3/min
    Cooling_capacity = (1.08 * cfm * (Ti - To))  # Btu/hr
    EER = (1.08 * cfm * (Ti - To)) / (Power_fan + Power_pump)  # Btu/hr.W
    COP = EER * 0.293  # W/W
    seer = EER / 0.9
    AAA = (Power_fan + Power_pump)

    # Determine the pressure drop and hole diameter of each wet channel
    PL_dry = np.zeros(NW)
    CW = WW / 2

    PL_max = Power_fan / (Q_fan * 2.5)  # pa

    for i in range(NW):
        PL_dry[i] = (((8 * V_dry * noo_air) * (density_air) / (((D_h_product / 2) ** 2))) * (1.1 * CW) - PL_max) / 6895
        CW = CW + WW

    Q_wet = (M_wet / (NW * 2 * N * density_air * 3600)) * 100000 / 6.31

    diameter = np.zeros(NW)
    cd = 0.61  # input(' cd  0.98 or 0.61  =  ')

    for i in range(NW):
        diameter[i] = (1 / (((abs((PL_dry[i] ** (0.5))) * 29.81 * cd / (Q_wet / 2))) ** (0.5))) * 0.0254  # m

    # Thermal analysis
    num_i = int(L / 0.001) + 1
    num_j = int(W / 2 / 0.001) + 1

    TPC = np.zeros((num_i, num_j))
    TWC = np.zeros((num_i, num_j))
    TF = np.zeros((num_i, num_j))

    # Initialize first row of TPC
    for k in range(num_j):
        TPC[0, k] = Tpi

    X = 0
    for k in range(num_i):
        TF[k, 0] = Twi
        TWC[k, 0] = (Tpi - Twi) * np.exp(z * X) + Twi
        X = X + 0.001

    d_evaporation = np.zeros((num_i, 1))
    dm_wet = (0.001 * (HW - delta)) * V_wet * density_air

    for k in range(num_i):
        P_g = 0.13332239 * 1000 * np.exp(20.386 - (5132 / (TWC[k, 0] + 273.15)))  # pa
        abs_humidity = 0.622 * (((RH / 100) * P_g) / (P_air - ((RH / 100) * P_g)))  # kg/kg
        abs_humidity_sat = 0.622 * (P_g / (P_air - P_g))  # kg/kg
        d_evaporation[k, 0] = dm_wet * (abs_humidity_sat - abs_humidity)  # kg/h

    A_cell = 0.001 * 0.001

    dm_in_film = 0.001 * delta * V_film * density_water

    for k in range(num_i - 1):
        dm_vapor = d_evaporation[k, 0] / num_i

        for q in range(num_j - 1):
            q_ptf = h_product * A_cell * (TPC[k, q] - TF[k, q])
            q_wtf = h_wet * A_cell * (TWC[k, q] - TF[k, q])
            q_vapor = dm_vapor * h_fg * 1000

            dm_in_film = dm_in_film - dm_vapor

            TF[k, q + 1] = ((q_ptf + q_wtf - 0.8 * q_vapor) / (dm_in_film * Cp_water * 1000)) + TF[k, q]
            TPC[k + 1, q] = (TPC[k, q] - TF[k, q]) * np.exp(z * 0.001) + TF[k, q]
            TWC[k, q + 1] = ((-0.2 * q_vapor - q_wtf) / (dm_vapor * Cp_vaper * 1000 + dm_wet * Cp_air * 1000)) + (
                        dm_vapor * Cp_vaper * 1000 * TF[k, q] + dm_wet * Cp_air * 1000 * TWC[k, q]) / (
                                        dm_vapor * Cp_vaper * 1000 + dm_wet * Cp_air * 1000)

    # Create mesh plots
    x_vals = np.arange(0, L + 0.001, 0.001)
    y_vals = np.arange(0, W / 2 + 0.001, 0.001)
    X_mesh, Y_mesh = np.meshgrid(x_vals, y_vals)

    # Figure 2: Temperature of air in wet floor
    fig2 = plt.figure(2)
    ax2 = fig2.add_subplot(111, projection='3d')
    surf2 = ax2.plot_surface(X_mesh, Y_mesh, TWC[:, :len(y_vals)].T, cmap='viridis')
    ax2.set_xlabel('Length of HMX (m)')
    ax2.set_ylabel('Width of HMX (m)')
    ax2.set_zlabel('Temperature of air in wet floor (°C)')
    fig2.colorbar(surf2)

    # Figure 3: Temperature of film in wet floor
    fig3 = plt.figure(3)
    ax3 = fig3.add_subplot(111, projection='3d')
    surf3 = ax3.plot_surface(X_mesh, Y_mesh, TF[:, :len(y_vals)].T, cmap='plasma')
    ax3.set_xlabel('Length of HMX (m)')
    ax3.set_ylabel('Width of HMX (m)')
    ax3.set_zlabel('Temperature of film in wet floor (°C)')
    fig3.colorbar(surf3)

    # Figure 4: Temperature of air in dry floor
    x_vals2 = np.arange(0, L + 0.001, 0.001)
    y_vals2 = np.arange(0, W / 2 + 0.001, 0.001)
    X_mesh2, Y_mesh2 = np.meshgrid(x_vals2, y_vals2)

    fig4 = plt.figure(4)
    ax4 = fig4.add_subplot(111, projection='3d')
    surf4 = ax4.plot_surface(X_mesh2, Y_mesh2, TPC[:len(x_vals2), :len(y_vals2)].T, cmap='coolwarm')
    ax4.set_xlabel('Length of HMX (m)')
    ax4.set_ylabel('Width of HMX (m)')
    ax4.set_zlabel('Temperature of air in dry floor (°C)')
    fig4.colorbar(surf4)
    ax4.grid(True)

    plt.show()


if __name__ == "__main__":
    main()