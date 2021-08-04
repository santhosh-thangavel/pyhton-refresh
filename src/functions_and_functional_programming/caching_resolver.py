import socket


class Resolver:
    """
    An example of fanctions with state between calls
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
resolve.has_host("pluralsight.com")
resolve("pluralsight.com")
resolve.has_host("pluralsight.com")
resolve.clear()
resolve.has_host("pluralsight.com")

# Results

# False - "No host "pluralsight.com"
# 52.24.147.215 "host is now "pluralsight"
# True has_host is true now
# None cache is cleared
# False As cache is cleared, no_host and hence False