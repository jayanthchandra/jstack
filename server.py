from flask import Flask
k,current_app,render_template
import subprocess
app=Flask(__name__,static_url_path="")
app.debug=True
@app.route('/')
def index():
	return current_app.send_static_file('index.html')
	
@app.route('/nova')
def nova():
	a=subprocess.Popen(['ps -ef'],stdout=subprocess.PIPE,shell=True)
	f1 =subprocess.Popen(["grep","python"],stdin=a.stdout,stdout=subprocess.PIPE)
	novafilter=subprocess.Popen(["grep","nova"],stdin=f1.stdout,stdout=subprocess.PIPE)
	novaout=novafilter.communicate()[0]
	rawnova=novaout.split()
	new=[item for item in rawnova if not item.isdigit()]
	ind=[5,13,21,29,37,45,55]
	nova=[]
	try:
		for i in ind:
		    nova.append(new[i])
		    novastatus=['Nova-Certificate process Started','Nova-Console Auth working','nova-noVNC proxy intiated','nova-Scheduler Working and Connected to AMQP Server',
		    	   'Nova-Conductor Conducting','Nova-Network Configured','Nova-Compute Engine Started']
	except :
		novastatus = ['Nova-Certificate Not Verified','Nova-Console Auth not-working','nova-noVNC proxy not intiated','nova-Scheduler not Working and not connected to AMQP Server',
		    	   'Nova-Conductor not Conducting','Nova-Network not Configured','Nova-Compute Engine not Started']
	
	return render_template('nova.html',**locals())
@app.route('/cinder')
def cinder():
	a=subprocess.Popen(['ps -ef'],stdout=subprocess.PIPE,shell=True)
	f1 =subprocess.Popen(["grep","python"],stdin=a.stdout,stdout=subprocess.PIPE)
	cinderfilter=subprocess.Popen(["grep","cinder"],stdin=f1.stdout,stdout=subprocess.PIPE)
	cindout=cinderfilter.communicate()[0]
	cinder=[]
	c=cindout.split()
	new=[item for item in c if not item.isdigit()]
	ind=[5,13,21,29,37,45]
	try:
		for i in ind:
		    cinder.append(new[i])
		    status=['cinder-volume working','cinder-scheduler working','cinder-api  working']
	except :
		status = ['cinder-volume not working','cinder-scheduler not working','cinder-api not working',]
    
 	return render_template('cinder.html',**locals())

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=12345)