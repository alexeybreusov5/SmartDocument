import requests
import json
class SmartDocument:
  def __init__(self, file, payload):
    self.file = file
    self.payload = payload

  def generate():
    headers = { "Content-Type": "application/x-www-form-urlencoded" }
    self.file.set_attributes(private=False)
    data = { "file": self.file.url_for(external=True), "meta_form": json.dumps(self.payload) }
    response = requests.post("https://integraapi.azurewebsites.net/docassemble", data=data, headers=headers)
    return response.json()['url']