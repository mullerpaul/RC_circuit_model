# initial conditions
vinit=10
r=1000
c=0.001
Q=c*vinit

# set up time variable and time step
t=0
dt=0.10

# loop - increment the time by the time step value until we hit the end
while (t<10):
	print ("at time ", t)
	dQ=Q*dt/(r*c)
	Q=Q-dQ
	v=Q/c
	i=c/r
	t=t+dt
	print("voltage is ", v)

# TODO: save i and v values so we can plot them over time
