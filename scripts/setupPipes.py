import meerschaum as mrsm

# function to set up the pipes !
def setupPipes():
	powerPipe = mrsm.Pipe('sim', 'power', mrsm_instance='api:mrsm_server')
	powerPipe.columns = {'datetime':'datetime' , 'id':'sensorid'}
	# powerPipe.register()

	temperaturePipe = mrsm.Pipe('sim', 'temperature', mrsm_instance='api:mrsm_server')
	temperaturePipe.columns = {'datetime':'datetime' , 'id':'sensorid'}
	# temperaturePipe.register()

if __name__ == "__main__":
    setupPipes()
