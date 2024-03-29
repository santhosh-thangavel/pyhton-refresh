import socket


class Resolver:
    """
    An example of functions with state between calls
    """

    def __init__(self):
        self._cache = {}

    def __call__(self, host):
        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host)

        print(self._cache[host])

    def clear(self):
        print(self._cache.clear())

    def has_host(self, host):
        print(host in self._cache)


resolve = Resolver()
resolve.has_host("google.com")
resolve("google.com")
resolve.has_host("google.com")
resolve.clear()
resolve.has_host("google.com")

# Results

# False - "No host "google.com"
# 52.24.147.215 "host is now "google.com"
# True has_host is true now
# None cache is cleared
# False As cache is cleared, no_host and hence False