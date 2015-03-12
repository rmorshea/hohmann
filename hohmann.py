from astropy import units as u
from poliastro.util import norm
from poliastro.bodies import Body, Sun, Earth
from poliastro.twobody import State
from poliastro.maneuver import Maneuver
from IPython.html import widgets

def hoh_data(hoh):
    data = {'transfer time' : hoh.get_total_time().to(u.yr),
            'delta v' : hoh.get_total_cost()}
    return data

def ss_data(state):
    data = {'period' : state.period.to(u.day),
            'velocity' : abs(state.v[1])}
    return data

def create_states(attractor, rad_init, rad_final, unit):
	ssi = State.circular(attractor, alt=rad_init.value*unit)
	hoh = Maneuver.hohmann(ssi, r_f=rad_final.value*unit)
	ssa, ssf = ssi.apply_maneuver(hoh, intermediate=True)
	return ssi, ssa, ssf, hoh

def display_data(state_init, hohmann, state_final):
	print 'initial orbit\n-------------'
	for k,v in ss_data(state_init).items():
	    print k,':',v
	print; print 'hohmann transfer\n----------------'
	for k,v in hoh_data(hohmann).items():
	    print k,':',v
	print; print 'final orbit\n-----------'
	for k,v in ss_data(state_final).items():
	    print k,':',v

def create_widgets():
	ddm = widgets.Dropdown(
	    options=['earth masses','sun masses'],
	    value='sun masses',
	    description='mass units:')
	ms = widgets.FloatText(value=1.0,
	    description='central mass:')

	ddu = widgets.Dropdown(
	    options=['km', 'au'],
	    value='au',
	    description='dist units:')
	ri = widgets.FloatText(value=1.0,
	    description='initial radius:')
	rf = widgets.FloatText(value=1.524,
	    description='final radius:')

	ms.width = '50px'
	ri.width = '56px'
	rf.width = '62px'

	return ddm,ms,ddu,ri,rf