import requests
import concurrent.futures
import socket
import math

import requests.adapters


class HostHeaderSSLAdapter(requests.adapters.HTTPAdapter):
    def __init__(self, resolved_ip):
        super().__init__()
        self.resolved_ip = resolved_ip

    def send(self, request, **kwargs):
        from urllib.parse import urlparse

        connection_pool_kwargs = self.poolmanager.connection_pool_kw

        result = urlparse(request.url)

        if result.scheme == "https" and self.resolved_ip:
            request.url = request.url.replace(
                "https://" + result.hostname,
                "https://" + self.resolved_ip,
            )
            connection_pool_kwargs["assert_hostname"] = result.hostname
            # overwrite the host header
            request.headers["Host"] = result.hostname
        else:
            # theses headers from a previous request may have been left
            connection_pool_kwargs.pop("assert_hostname", None)

        return super(HostHeaderSSLAdapter, self).send(request, **kwargs)


def resolve_dns(domain):
    print("resolving" + domain)
    try:
        ip_addresses = socket.getaddrinfo(domain, None)
        return [addr[4][0] for addr in ip_addresses]
    except socket.gaierror as e:
        print(f"Failed to resolve DNS for {domain}: {e}")
        return []


def scrape_urls(start, end, ip_address, base, trd):
    session = requests.Session()
    session.mount("https://", HostHeaderSSLAdapter(ip_address))
    for i in range(start, end):
        url = f"{base}{i}.ts"
        try:
            with open(f"{i}.ts", "wb", 8192) as file, session.get(url, timeout=30) as a:
                file.write(a.content)
                print(f"{i}{a.headers.get('Etag')}")
        except requests.RequestException as e:
            print(f"Error accessing {url}: {e}")


def main(base_url: str, target):
    domain = base_url.split("/")[1]
    ip_addresses = resolve_dns(domain)

    num_ips = len(ip_addresses)
    print(f"Resolved {domain} to {num_ips} IP address(es)")

    num_threads = num_ips  # You can adjust the number of threads as needed
    chunk_size = math.ceil((target + 1) / num_threads)
    chunks = [
        (i * chunk_size, min((i + 1) * chunk_size, target + 1))
        for i in range(num_threads)
    ]
    print(chunks)
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = []
        for xx in range(num_threads):
            futures.append(
                executor.submit(
                    scrape_urls,
                    chunks[xx][0],
                    chunks[xx][1],
                    ip_addresses[xx],
                    base_url,
                    xx,
                )
            )

        # Wait for all futures to complete
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"An error occurred: {e}")


if __name__ == "__main__":
    base = "xxx"
    main(base, 0)
