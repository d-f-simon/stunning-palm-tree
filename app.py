from flask import Flask, render_template, request, json, jsonify
import requests
 
app = Flask(__name__)
 
 
@app.route("/")
def home():
    return render_template("index.html")
 
@app.route("/get")
def get_bot_response():
	userText = request.args.get('msg')
	try:
		url = 'http://localhost:5005/webhooks/rest/webhook'
		payload = {"sender": "Rasa","message": userText}
		headers = {'content-type': 'application/json'}

		response = requests.post(url, data=json.dumps(payload), headers=headers)
		response = response.json()
		msg_new = response[0]["text"]
		return msg_new
	except Exception as e:
		print(e)
		error_msg = "Error: Sorry I cannot connect to server"
		return error_msg
 
 
if __name__ == "__main__":
    app.run()

