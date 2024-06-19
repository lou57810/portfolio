import http.server
import socketserver
# import functools
from functools import partial
from pathlib import Path
# from controller.run_epic import Controller


HOST = "172.16.1.108"
PORT = 9999


def main():
    pass
    # epic_events = Controller(http.server.SimpleHTTPRequestHandler)
    # epic_events.run()


if __name__ == "__main__":
    main()

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer((HOST, PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()






