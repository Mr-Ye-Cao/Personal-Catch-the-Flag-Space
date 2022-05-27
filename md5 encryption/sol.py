import hashlib as hl
import requests as req

while True:
	response = req.get("http://159.65.88.44:31500/")

	to_encryt = response.text[response.text.find("<h3 align=\'center\'>")+18:response.text.find("</h3>")]

	encrypted = hl.md5(to_encryt.encode())

	to_subm = encrypted.hexdigest()

	print(req.post(response,to_subm).text)
