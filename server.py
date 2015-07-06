from flask import Flask,current_app,render_template
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
@app.route('/glance')
def glance():
	a=subprocess.Popen(['ps -ef'],stdout=subprocess.PIPE,shell=True)
	f1 =subprocess.Popen(["grep","python"],stdin=a.stdout,stdout=subprocess.PIPE)
	glancefilter=subprocess.Popen(["grep","glance"],stdin=f1.stdout,stdout=subprocess.PIPE)
	glanceout=cinderfilter.communicate()[0]
	glance=[]
	c=glanceout.split()
	new=[item for item in c if not item.isdigit()]
	ind=[5,12,19,26,33,40]
	try:
		for i in ind:
			glance.append(new[i])
			status=['Glance API Intiated','Glance API registered','Glance API Working','Glance Service Started']
	except:
		status=['Glance API not Intiated','Glance API not registered','Glance API not  Working','Glance Service not Started']

	return render_template('glance.html',**locals())

@app.route('/swift')
def swift():
	a=subprocess.Popen(['ps -ef'],stdout=subprocess.PIPE,shell=True)
	apachefilter =subprocess.Popen(["grep","apache"],stdin=a.stdout,stdout=subprocess.PIPE)
	apacheout=apachefilter.communicate()[0]
	apache=[]
	c=apacheout.split()
	new=[item for item in c if not item.isdigit()]
	ind=[4,11,18,28,36,44,51,58,65]
	try:
		for i in ind:
			apache.append(new[i])
			status=['Apache Process Started','Swift Service Intiated','Keystone Process Running','Keystone Access Given','Horizon Log Service Started']
	except:
			status=['Apache Process Not Running','Swift Service Not Intiated','Keystone Process Not Running','Keystone Access Not  Given','Horizon Log Servive Not Started']

	return render_template('apache.html',**locals())


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=12345)