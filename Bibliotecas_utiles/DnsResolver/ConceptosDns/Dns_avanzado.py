import dns.resolver
import ipaddress
import requests

# URL to fetch Cloudflare IP ranges
CLOUDFLARE_IP_RANGES_URLS = [
    "https://www.cloudflare.com/ips-v4",
    "https://www.cloudflare.com/ips-v6"
]

def fetch_cloudflare_ip_ranges():
    ip_ranges = []
    for url in CLOUDFLARE_IP_RANGES_URLS:
        response = requests.get(url)
        if response.status_code == 200:
            ip_ranges.extend(response.text.splitlines())
        else:
            print(f"Failed to fetch IP ranges from {url}")
    return ip_ranges

def is_cloudflare_ip(ip, ip_ranges):
    ip_obj = ipaddress.ip_address(ip)
    for range in ip_ranges:
        if ip_obj in ipaddress.ip_network(range):
            return True
    return False

def query_dns(domain, ip_ranges):
    try:
        res_ipv4 = dns.resolver.resolve(domain, "A")
        res_ipv6 = dns.resolver.resolve(domain, "AAAA")

        for ip in res_ipv4:
            ip_str = ip.to_text()
            if is_cloudflare_ip(ip_str, ip_ranges):
                print(f"IPv4 Address: {ip_str} (Cloudflare Proxy)")
            else:
                print(f"IPv4 Address: {ip_str} (Origin Server)")

        for ip in res_ipv6:
            ip_str = ip.to_text()
            if is_cloudflare_ip(ip_str, ip_ranges):
                print(f"IPv6 Address: {ip_str} (Cloudflare Proxy)")
            else:
                print(f"IPv6 Address: {ip_str} (Origin Server)")

        # Mail servers
        response_mx = dns.resolver.resolve(domain, "MX")
        for record in response_mx:
            print(f"Mail server: {record.exchange}, Priority: {record.preference}")

    except dns.resolver.NoAnswer:
        print(f"No records found for {domain}")
    except dns.resolver.NXDOMAIN:
        print(f"The domain {domain} does not exist")
    except dns.exception.Timeout:
        print(f"Timeout while querying {domain}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    # Fetch the latest Cloudflare IP ranges
    cloudflare_ip_ranges = fetch_cloudflare_ip_ranges()
    
    # Example usage
    domain = "forocoches.com"
    query_dns(domain, cloudflare_ip_ranges)