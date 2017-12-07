# Send to single device.
from pyfcm import FCMNotification

push_service = FCMNotification(api_key="<api-key>")

# OR initialize with proxies

proxy_dict = {
          "http"  : "http://127.0.0.1",
          "https" : "http://127.0.0.1",
        }
push_service = FCMNotification(api_key="<api-key>", proxy_dict=proxy_dict)

def notificar():
	# Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging

	# Send to multiple devices by passing a list of ids.
	registration_ids = []
	message_title = "RaspCam"
	message_body = "Se activo su alarma"
	result = push_service.notify_multiple_devices(registration_ids=registration_ids, message_title=message_title, message_body=message_body)
