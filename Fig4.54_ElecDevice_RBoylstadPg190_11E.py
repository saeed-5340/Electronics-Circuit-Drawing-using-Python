##### Name                : Saeed Ahamed Mridha
##### Registration_number : 2020338012
### Fig.4.54
### Page: 190
### Book: Electronic Devices and Circuit Theory
### By Robert L. Boylestad, Louis Nashelsky
### 11th Edition 

#### Declare Library Functions
import schemdraw
import matplotlib
import schemdraw.elements as elm
with schemdraw.Drawing() as d:
    #### NPN Transistor with label ####
    npn = elm.BjtNpn(circle=True,fill='skyblue').label(label=r'$\beta$=45',fontsize=12)
    d += npn
    #### V{EE} to Emitter Circuit ####
    d += elm.Line().down().at(npn.emitter).toy(-1.60)
    d += elm.Dot(open=True).label('$v_{EE}$ = -9V',loc='right')
    d += elm.Line().up().at(npn.collector).toy(1.45)
    d.push()
    #### Collector to Output terminal Circuit COde #### 
    d += elm.Capacitor2().right().label(label="10$\mu F$",loc='bot',fontsize=12).label('$C_2$',fontsize=12)
    d += elm.Dot(open=True).label(label='$v_0$',loc='right')
    d.pop()
    #### Collector to Ground Circuit code ####
    d += elm.Resistor(botlabel='1.2k$\Omega$',label='$R_c$',fontsize=12).up()
    d +=elm.Line().right().tox(1.45)
    d += elm.Ground()
    #### Base to Ground Circuit Code ####
    d += elm.Line().at(npn.base).left().tox(1.22)
    d.push()
    d +=elm.Resistor(label='$R_B$',botlabel='100k$\Omega$',fontsize=12).down()
    d += elm.Ground()
    d.pop()
    #### Input tarminal to Base Circuit Code ####
    d +=elm.Capacitor2(label='$C_1$',botlabel='10$\mu$F',fontsize=12).left()
    d +=elm.Dot(open=True).label('$v_i$',loc='left',fontsize=12)
    d.draw()