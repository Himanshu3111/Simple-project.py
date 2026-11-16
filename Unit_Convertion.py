def inch_to_cm(num):
    return round(num * 2.54, 4)


def cm_to_inch(num):
    return round(num / 2.54, 4)


def ft_to_m(num):
    return round(num * 0.3048, 4)


def m_to_ft(num):
    return round(num / 0.3048, 4)


def yd_to_m(num):
    return round(num * 0.9144, 4)


def m_to_yd(num):
    return round(num / 0.9144, 4)


def mile_to_km(num):
    return round(num * 1.609344, 4)


def km_to_mile(num):
    return round(num / 1.609344, 4)

def n_mile_to_m(num1):
    return round(num1*1852, 4)

def m_to_n_mile(num):
    return round(num/1852, 4)


def acre_to_m2(num):
    return round(num * 4046.8564224, 4)


def m2_to_acre(num):
    return round(num / 4046.8564224, 4)


def gal_us_to_l(num):
    return round(num * 3.785411784, 4)


def l_to_gal_us(num):
    return round(num / 3.785411784, 4)


def gal_uk_to_l(num):
    return round(num * 4.54609, 4)


def l_to_gal_uk(num):
    return round(num / 4.54609, 4)


def pc_to_km(num):
    return round(num * 30_856_775_814_913.672, 4)


def km_to_pc(num):
    return round(num / 30_856_775_814_913.672, 4)


def kmh_to_ms(num):
    return round(num / 3.6, 4)


def ms_to_kmh(num):
    return round(num * 3.6, 4)


def oz_to_g(num):
    return round(num * 28.349523125, 4)


def g_to_oz(num):
    return round(num / 28.349523125, 4)


def lb_to_kg(num):
    return round(num * 0.45359237, 4)


def kg_to_lb(num):
    return round(num / 0.45359237, 4)


def atm_to_pa(num):
    return round(num * 101325, 4)


def pa_to_atm(num):
    return round(num / 101325, 4)


def mmhg_to_pa(num):
    return round(num * 133.322387415, 4)


def pa_to_mmhg(num):
    return round(num / 133.322387415, 4)


def hp_to_kw(num):
    return round(num * 0.7456998715822702, 4)


def kw_to_hp(num):
    return round(num / 0.7456998715822702, 4)


def kgf_cm2_to_pa(num):
    return round(num * 98066.5, 4)


def pa_to_kgf_cm2(num):
    return round(num / 98066.5, 4)


def kgf_m_to_j(num):
    return round(num * 9.80665, 4)


def j_to_kgf_m(num):
    return round(num / 9.80665, 4)


def psi_to_kpa(num):
    return round(num * 6.894757293168, 4)


def kpa_to_psi(num):
    return round(num / 6.894757293168, 4)


def f_to_c(num):
    return round((num - 32) * 5 / 9, 4)


def c_to_f(num):
    return round(num * 9 / 5 + 32, 4)


def j_to_cal(num):
    return round(num / 4.184, 4)


def cal_to_j(num):
    return round(num * 4.184, 4)




def converter():
    while True:
        print("================================")
        print("         UNIT  CONVERSION")
        print("================================")
        print("For Exit            = Press '0'")
        print("For in to cm        = Press '1'")
        print("For cm to in        = Press '2'")
        print("For ft to m         = Press '3'")
        print("For m to ft         = Press '4'")
        print("For yd to m         = Press '5'")
        print("For m to yd         = Press '6'")
        print("For mile to km      = Press '7'")
        print("For km to mile      = Press '8'")
        print("For n mile to m     = Press '9'")
        print("For m to n mile     = Press '10'")
        print("For acre to m^2     = Press '11'")
        print("For m^2 to acre     = Press '12'")
        print("For US gal to l     = Press '13'")
        print("For l to US gal     = Press '14'")
        print("For UK gal to l     = Press '15'")
        print("For l to UK gal     = Press '16'")
        print("For pc to km        = Press '17'")
        print("For km to pc        = Press '18'")
        print("For km/h to m/s     = Press '19'")
        print("For m/s to km/h     = Press '20'")
        print("For oz to g         = Press '21'")
        print("For g to oz         = Press '22'")
        print("For lb to kg        = Press '23'")
        print("For kg to lb        = Press '24'")
        print("For atm to Pa       = Press '25'")
        print("For Pa to atm       = Press '26'")
        print("For mmHg to Pa      = Press '27'")
        print("For Pa to mmHg      = Press '28'")
        print("For hp to kW        = Press '29'")
        print("For kW to hp        = Press '30'")
        print("For kgf/cm^2 to Pa  = Press '31'")
        print("For Pa to kgf/cm^2  = Press '32'")
        print("For kgf.m to J      = Press '33'")
        print("For J to kgf.m      = Press '34'")
        print("For lbf/in^2 to kPa = Press '35'")
        print("For kPa to lbf/in^2 = Press '36'")
        print("For F to C          = Press '37'")
        print("For C to F          = Press '38'")
        print("For J to cal        = Press '39'")
        print("For cal to J        = Press '40'")

        choice = int(input("Enter operator: "))

        if choice == 1:
            value = float(input("Enter value in inches: "))
            print(f"{value} in = {inch_to_cm(value)} cm")
        elif choice == 2:
            value = float(input("Enter value in cm: "))
            print(f"{value} cm = {cm_to_inch(value)} in")
        elif choice == 3:
            value = float(input("Enter value in feet: "))
            print(f"{value} ft = {ft_to_m(value)} m")
        elif choice == 4:
            value = float(input("Enter value in meters: "))
            print(f"{value} m = {m_to_ft(value)} ft")
        elif choice == 5:
            value = float(input("Enter value in yards: "))
            print(f"{value} yd = {yd_to_m(value)} m")
        elif choice == 6:
            value = float(input("Enter value in meters: "))
            print(f"{value} m = {m_to_yd(value)} yd")
        elif choice == 7:
            value = float(input("Enter value in miles: "))
            print(f"{value} mile = {mile_to_km(value)} km")
        elif choice == 8:
            value = float(input("Enter value in km: "))
            print(f"{value} km = {km_to_mile(value)} mile")
        elif choice == 9:
            value = float(input("Enter value in Nautical mile: "))
            print(f"{value} n mile = {n_mile_to_m(value)} meter")
        elif choice == 10:
            value = float(input("Enter value in meter: "))
            print(f"{value} meter = {m_to_n_mile(value)} n mile")
        elif choice == 11:
            value = float(input("Enter value in acres: "))
            print(f"{value} acre = {acre_to_m2(value)} m^2")
        elif choice == 12:
            value = float(input("Enter value in m^2: "))
            print(f"{value} m^2 = {m2_to_acre(value)} acre")
        elif choice == 13:
            value = float(input("Enter value in US gallons: "))
            print(f"{value} US gal = {gal_us_to_l(value)} l")
        elif choice == 14:
            value = float(input("Enter value in liters: "))
            print(f"{value} l = {l_to_gal_us(value)} US gal")
        elif choice == 15:
            value = float(input("Enter value in UK gallons: "))
            print(f"{value} UK gal = {gal_uk_to_l(value)} l")
        elif choice == 16:
            value = float(input("Enter value in liters: "))
            print(f"{value} l = {l_to_gal_uk(value)} UK gal")
        elif choice == 17:
            value = float(input("Enter value in parsecs: "))
            print(f"{value} pc = {pc_to_km(value)} km")
        elif choice == 18:
            value = float(input("Enter value in km: "))
            print(f"{value} km = {km_to_pc(value)} pc")
        elif choice == 19:
            value = float(input("Enter value in km/h: "))
            print(f"{value} km/h = {kmh_to_ms(value)} m/s")
        elif choice == 20:
            value = float(input("Enter value in m/s: "))
            print(f"{value} m/s = {ms_to_kmh(value)} km/h")
        elif choice == 21:
            value = float(input("Enter value in ounces: "))
            print(f"{value} oz = {oz_to_g(value)} g")
        elif choice == 22:
            value = float(input("Enter value in grams: "))
            print(f"{value} g = {g_to_oz(value)} oz")
        elif choice == 23:
            value = float(input("Enter value in pounds: "))
            print(f"{value} lb = {lb_to_kg(value)} kg")
        elif choice == 24:
            value = float(input("Enter value in kilograms: "))
            print(f"{value} kg = {kg_to_lb(value)} lb")
        elif choice == 25:
            value = float(input("Enter value in atmospheres: "))
            print(f"{value} atm = {atm_to_pa(value)} Pa")
        elif choice == 26:
            value = float(input("Enter value in pascals: "))
            print(f"{value} Pa = {pa_to_atm(value)} atm")
        elif choice == 27:
            value = float(input("Enter value in mmHg: "))
            print(f"{value} mmHg = {mmhg_to_pa(value)} Pa")
        elif choice == 28:
            value = float(input("Enter value in pascals: "))
            print(f"{value} Pa = {pa_to_mmhg(value)} mmHg")
        elif choice == 29:
            value = float(input("Enter value in horsepower: "))
            print(f"{value} hp = {hp_to_kw(value)} kW")
        elif choice == 30:
            value = float(input("Enter value in kilowatts: "))
            print(f"{value} kW = {kw_to_hp(value)} hp")
        elif choice == 31:
            value = float(input("Enter value in kgf/cm^2: "))
            print(f"{value} kgf/cm^2 = {kgf_cm2_to_pa(value)} Pa")
        elif choice == 32:
            value = float(input("Enter value in pascals: "))
            print(f"{value} Pa = {pa_to_kgf_cm2(value)} kgf/cm^2")
        elif choice == 33:
            value = float(input("Enter value in kgf.m: "))
            print(f"{value} kgf.m = {kgf_m_to_j(value)} J")
        elif choice == 34:
            value = float(input("Enter value in joules: "))
            print(f"{value} J = {j_to_kgf_m(value)} kgf.m")
        elif choice == 35:
            value = float(input("Enter value in lbf/in^2: "))
            print(f"{value} lbf/in^2 = {psi_to_kpa(value)} kPa")
        elif choice == 36:
            value = float(input("Enter value in kilopascals: "))
            print(f"{value} kPa = {kpa_to_psi(value)} lbf/in^2")
        elif choice == 37:
            value = float(input("Enter value in Fahrenheit: "))
            print(f"{value} F = {f_to_c(value)} C")
        elif choice == 38:
            value = float(input("Enter value in Celsius: "))
            print(f"{value} C = {c_to_f(value)} F")
        elif choice == 39:
            value = float(input("Enter value in joules: "))
            print(f"{value} J = {j_to_cal(value)} cal")
        elif choice == 40:
            value = float(input("Enter value in calories: "))
            print(f"{value} cal = {cal_to_j(value)} J")
        elif choice == 0:
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    converter()
