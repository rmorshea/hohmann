from astropy import units as u
from poliastro.util import norm
from poliastro.bodies import Body, Sun, Earth
from poliastro.twobody import State
from poliastro.maneuver import Maneuver
from poliastro.plotting import OrbitPlotter

def hoh_data(hoh):
    data = {'transfer time' : hoh.get_total_time().to(u.yr),
            'delta v' : hoh.get_total_cost()}
    return data

def ss_data(state):
    data = {'period' : state.period.to(u.day),
            'velocity' : abs(state.v[1])}
    return data

def create_states(attractor, rad_init, rad_final):
	ssi = State.circular(attractor, alt=rad_init.value*u.AU)
	hoh = Maneuver.hohmann(ssi, r_f=rad_final.value*u.AU)
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
