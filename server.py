from flask import Flask,current_app
app=Flask(__name__,static_url_path="")

@app.route('/')
def index():
	return current_app.send_static_file('index.html')
	
@app.route('/nova')
def nova():
	return current_app.send_static_file('nova.html')

@app.route('/keystone')
def keystone():
	return current_app.send_static_file('keystoe.html')

@app.route('/cinder')
def cinder():
	return current_app.send_static_file('cinder.html')


if __name__ == '__main__':
    app.run()