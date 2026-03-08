##### Name                : Saeed Ahamed Mridha
##### Registration_number : 2020338012
### Fig.4.54
### Page: 190
### Book: Electronic Devices and Circuit Theory
### By Robert L. Boylestad, Louis Nashelsky
### 11th Edition 


import schemdraw
import matplotlib
import schemdraw.elements as elm
with schemdraw.Drawing() as d:
    npn = elm.BjtNpn(circle=True,fill='skyblue').label("$V_{CE_Q}$ = 10V").label("+",ofst=(0.015,0.54)).label("-",ofst=(0.02,-0.54),fontsize=20)
    d += npn
    d += elm.Line().length(0.5).at(npn.emitter).down()
    d += elm.Dot()
    d.push()
    d += elm.Line().length(1.5).right()
    d += elm.Capacitor2().label("$C_E$\n50$\mu$F",loc='bot').down()
    d += elm.Ground()
    d.pop()
    d += elm.Resistor().down().label('$R_E$',color='skyblue')
    d += elm.Ground()
    d += elm.Line().length(0.5).at(npn.collector).up()
    d += elm.Dot()
    d.push()
    d += elm.Capacitor2().label('$C_2$').label('10$\mu$F',loc='bot').right()
    d += elm.Dot().label("ac\noutput",loc='right')
    d.pop()
    d += elm.Resistor().label('$R_C$',color='skyblue',loc='bot')
    d += elm.CurrentLabel(0.5,0.75).reverse().at((d.here[0],d.here[1]-1.5)).label('$I_{C_Q}$ = 2 mA')
    d += elm.Line().length(1.5).left()
    d += elm.Dot()
    d.push()
    d += elm.Line().length(0.5).up()
    d += elm.Dot(open=True).label('$V_{CC}$ = 20V')
    d.pop()
    d += elm.Line().length(1.5).left()
    d += elm.Resistor().down().toy(npn.base).label('$R_B$',color='skyblue')
    d += elm.Dot().label('$V_B$',loc='bot')
    d.push()
    d += elm.Line().tox(npn.base).label('\n2N4401\n'r'($\beta$ = 150)',loc='bot',fontsize=10)
    d.pop()
    d += elm.Capacitor2().label('$C_1$').label('10$\mu$F',loc='bot').left()
    d += elm.Dot().label('ac\ninput',loc='left')
    #d += elm.CurrentLabel(0.5,1).reverse().at((d.here[0],d.here[1]-1)).label("$I_{C_Q}$ = 2 mA")
    d.draw()