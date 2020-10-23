import meerschaum as mrsm

# function to set up the pipes !
def setupPipes(metrics):
    for metric in metrics:
    	pipe = mrsm.Pipe('csv', metric)
    	pipe.columns = {'datetime':'datetime' , 'id':'location'}
    	pipe.register()

if __name__ == "__main__":
    metrics = ['power','temperature','co2','humidity','occupancy','water']
    setupPipes(metrics)
