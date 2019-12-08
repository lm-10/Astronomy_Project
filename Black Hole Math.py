import scipy.constants as sc
from decimal import Decimal as dec
import math as m


_pi = sc.pi             #pi
pi = dec(_pi)

_speed_of_light = sc.c      #Speed of Light
c = dec(_speed_of_light)

_G = sc.G                   #Gravitational Cosntant 
G = dec(_G)
h_bar = sc.hbar
ℏ = dec(h_bar)


Boltzmann_constant = sc.Boltzmann
k = dec(Boltzmann_constant)

#--------------------------------------------------------------------------------------------------------
d_unit = input('which unit you will like to you use \nAU or meters?\n')

if d_unit == 'au' or d_unit == 'AU':
    r_periAU = dec( input("\nEnter radius at Peristron: ")) #120
    r_appiAU = dec( input("\nEnter radius at Apustron: ")) #1800
    r_appi = dec(r_appiAU*149597900000)
    r_peri = dec(r_periAU*149597900000)
elif d_unit  == 'metemrs' or d_unit == 'meter' or d_unit == 'm' :
    r_appi = dec( input("\nEnter radius at Apustron: "))
    r_peri = dec( input("\nEnter radius at Periastron: "))
else:
    print("Invalid Unit") 

t_unit = input('\nEnter unit for time period! \nyear or second?\n')
if t_unit == 'years' or t_unit == 'year' or t_unit == 'yrs' or t_unit == 'yr':
    t_yr = dec( input("\nEnter orbital period: ")) #15.6
    t = t_yr*dec(sc.year)
elif t_unit == 'sec' or t_unit   == "seconds" or t_unit == 's':
    t_yr = dec( input("\nEnter orbital period: ")) #491961600
    t = dec(t_yr)
else:
    print("\nInvalid Unit")


mass1= pow(pi,2)*pow(r_appi+r_peri,3)
mass2 = 2*G*pow(t,2)
mass = dec(mass1/mass2)

print("\nMass of the Object is %s Kg" %mass)

m_sun = 1.9889200011445836e30
mass_of_sun = dec(m_sun)
solar_mass = dec(mass/mass_of_sun)
print('\nIts equal to %s Solar Masses'%solar_mass)

#---------------------------------------------------------------------------------------------------------------
v1_peri = dec((2*G*mass*r_appi))
v2_peri = dec(r_appi*r_peri+pow(r_peri,2))
v_peri = dec(m.sqrt(v1_peri/v2_peri))
print("\nVelocity of the object at closest path is %s m/s"%v_peri)
v_light = v_peri/c*100
print("\nIt's velocity is about %s percent of speed of light"%v_light)
#--------------------------------------------------------------------------------------------------------


r_s = (2*G*mass)/(pow(c,2))
print("\nThe value for Schwarzchild Radius is found to be %s meters"%r_s)

#-------------------------------------------------------------------------------------------------------
Area = (4*pi*pow(r_s,2))
print("\nThe Event Horizon of Black Hole is %s meters"%Area)

time = 1
time_observer = dec(sc.Julian_year)

lorentz_factor =dec(m.sqrt((1)-(r_s/(r_peri))))
T_sec = time_observer/lorentz_factor

T_year = T_sec/dec(sc.Julian_year)
print("\nThe time dilation at Periastron %s years"%T_year)
#-----------------------------------------------------------------------------------------
g1 = (G*mass)
g2 = pow(r_peri,2)    
g = g1/g2 
print("\nForce of gravity at Periastron is %s N"%g)
g_bh1 = dec(G*mass)
g_bh2 = dec(pow(r_s,2))    
g_bh = g_bh1/g_bh2
print("\nForce of gravity near event horizon %s N"%g_bh)
#-----------------------------------------------------------------------------------------

Temperature = (ℏ*pow(c,3))/(8*pi*G*k*mass)
print("\nThe value of temperature is found to be: %s Kelvin"%Temperature)