import urllib.request

class CommandHttp:
    def __init__(self, url):
        self.url = url

    def run(self):
        with urllib.request.urlopen(self.url) as res:
            res.read().decode("utf-8")
            print("http req " + self.url)
            return False