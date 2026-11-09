from http.server import HTTPServer, BaseHTTPRequestHandler
from threading import Thread
from datetime import datetime, timezone
from urllib.request import Request, urlopen
from urllib.error import HTTPError

active_credential = "old-demo-key"


def timestamp():
    return datetime.now(timezone.utc).isoformat()


class APIHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        supplied = self.headers.get("Authorization", "")

        if supplied == f"Bearer {active_credential}":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Access granted")
        else:
            self.send_response(401)
            self.end_headers()
            self.wfile.write(b"Unauthorized")

    def log_message(self, *args):
        pass


server = HTTPServer(("127.0.0.1", 0), APIHandler)
Thread(target=server.serve_forever, daemon=True).start()

url = f"http://127.0.0.1:{server.server_port}/resource"


def api_call(credential):
    request = Request(
        url,
        headers={"Authorization": f"Bearer {credential}"}
    )

    try:
        with urlopen(request) as response:
            print(timestamp(), response.status, response.reason)
    except HTTPError as error:
        print(timestamp(), error.code, error.reason)


print("1. Testing original credential")
api_call("old-demo-key")

print("\n2. Rotating credentials")
active_credential = "new-demo-key"
print(timestamp(), "Credential rotated successfully")

print("\n3. Replaying old credential")
api_call("old-demo-key")

server.shutdown()
server.server_close()
