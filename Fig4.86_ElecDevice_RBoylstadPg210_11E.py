### Name                : Saeed Ahamed Mridha
### Registration_number : 2020338012      
### This python script will produce a common Emitter PNP configuration BJT network
### Fig.4.86                                                                       
### Page: 210                                                                      
### Book: Electronic Devices and Circuit Theory                                    
### By Robert L. Boylestad, Louis Nashelsky                                        
### 11th Edition   

### Used python package "SchemDraw"
### For more about the SchemDraw package: https://schemdraw.readthedocs.io/en/latest/index.html
### The greek leter is produced with Unicode

###### Import Library Function #######
import schemdraw
import matplotlib
import schemdraw.elements as elm
with schemdraw.Drawing() as d:
    ####### PNP Transistor with label ######
    pnp = elm.BjtPnp(circle=True,fill='cyan').flip().label('$V_{CE}$\t',color='cyan').label(r'$\beta$=120',ofst=(0.9,0.06),fontsize=13).label('+',ofst=(0.01,0.54),color='cyan').label("-",ofst=(0.01,-0.54),color='cyan',fontsize=20)
    d += pnp
    d += elm.Line().length(0.25).at(pnp.emitter).down()
    d += elm.Dot(open=True).label('E',loc='right',fontsize=10)
    d += elm.Line().at(pnp.base).length(0.25).left()
    d += elm.Dot(open=True).label("B",fontsize=10)
    d += elm.Line().length(0.25).at(pnp.collector).up()
    d += elm.Dot(open=True).label('C',loc='right',fontsize=10)
    
    ######Calloctor to Output terminal Circuit Code (Using Coupling Capacitor)#######
    d +=elm.Line().at(pnp.collector).length(0.60).up()
    d += elm.Dot()
    d.push()
    d += elm.Capacitor2(label='10$\mu$F',fontsize=10).right()
    d += elm.Dot(open=True).label('$v_o$',loc='right',fontsize=10)
    d.pop()
    
    ###### Collector to Vcc Circuit Code #####
    d += elm.Resistor().up().label(label='2.4k$\Omega$',loc='bot',fontsize=10)
    d += elm.Dot()
    d.push()
    d += elm.Line().length(0.75).right()
    d += elm.Dot(open=True).label('-18V',loc='right',fontsize=10)
    d.pop()
    ###### Vcc to Base Circuit Code #####
    d += elm.Line().left()
    d += elm.Resistor().down().toy(pnp.base).label('47K$\Omega$',loc='bot',fontsize=10)
    d.push()
    d += elm.Line().tox(pnp.base)
    d.pop()
    d.push()
    
    ###### Input Tarminal to Base Circuit Code (Using Coupling Capacitor)######
    d += elm.Capacitor2(label='10$\mu$F',fontsize=10).left()
    d += elm.Dot(open=True).label('$v_i$',loc='left',fontsize=10)
    d.pop()
    
    ###### Base to Ground Circut Code #####
    d += elm.Resistor().length(4).down().label('10k$\Omega$',loc='bot',fontsize=10)
    d += elm.Line().length(1.5).right()
    d += elm.Dot()
    d += elm.Ground()
    
    ###### Ground to Emitter Circuit Code #####
    d += elm.Line().tox(pnp.emitter)
    d += elm.Resistor().label('1.1k$\Omega$',fontsize=10).toy(pnp.emitter)
    d.draw()