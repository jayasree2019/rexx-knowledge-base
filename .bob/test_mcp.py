import urllib.request
import json

url = "https://servicesessentials.ibm.com/mcp-gateway/service/gateway/servers/8ccdd203bdee4014b08e82eedb6046e2/mcp"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJjb250ZXh0LXN0dWRpby11c2VyQGV4YW1wbGUuY29tIiwianRpIjoiNzBjZThmZjUtZDQ2My00NjAyLWI2MzctOGI5NzExMTQyNDQ5IiwidG9rZW5fdXNlIjoiYXBpIiwiaWF0IjoxNzg0NDcxOTQxLCJpc3MiOiJtY3BnYXRld2F5IiwiYXVkIjoibWNwZ2F0ZXdheS1hcGkiLCJ1c2VyIjp7ImVtYWlsIjoiY29udGV4dC1zdHVkaW8tdXNlckBleGFtcGxlLmNvbSIsImZ1bGxfbmFtZSI6IkFQSSBUb2tlbiBVc2VyIiwiaXNfYWRtaW4iOmZhbHNlLCJhdXRoX3Byb3ZpZGVyIjoiYXBpX3Rva2VuIn0sInRlYW1zIjpbIjVhYTNiZDhkNDUxMDRlNzVhZDdhMzBjYTAzOTEyYzIwIl0sInNjb3BlcyI6eyJzZXJ2ZXJfaWQiOiI4Y2NkZDIwM2JkZWU0MDE0YjA4ZTgyZWVkYjYwNDZlMiIsInBlcm1pc3Npb25zIjpbImdhdGV3YXlzLnJlYWQiLCJzZXJ2ZXJzLnJlYWQiLCJzZXJ2ZXJzLnVzZSIsInRvb2xzLnJlYWQiLCJ0b29scy5leGVjdXRlIiwidGVhbXMucmVhZCIsInJlc291cmNlcy5yZWFkIiwicHJvbXB0cy5yZWFkIl0sImlwX3Jlc3RyaWN0aW9ucyI6W10sInRpbWVfcmVzdHJpY3Rpb25zIjp7fX0sImV4cCI6MTc5MDAwMTU0MX0.ZRnYtFtxal_XjHW5OC0NvLEU6ENdt3vMp5DCi_JgfuI"

payload = json.dumps({
    "jsonrpc": "2.0",
    "id": 1,
    "method": "initialize",
    "params": {
        "protocolVersion": "2024-11-05",
        "capabilities": {},
        "clientInfo": {"name": "bob", "version": "1.0"}
    }
}).encode()

req = urllib.request.Request(
    url,
    data=payload,
    headers={
        "Authorization": "Bearer " + token,
        "X-Context-ID": "ctx_45b2408bbb1d",
        "Content-Type": "application/json"
    },
    method="POST"
)

try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        body = resp.read().decode()
        print("HTTP Status :", resp.status)
        print("Response    :", body[:500])
        print()
        print("CONNECTION  : SUCCESS - Context Studio MCP is reachable")
except urllib.error.HTTPError as e:
    body = e.read().decode()
    print("HTTP Error  :", e.code, e.reason)
    print("Body        :", body[:300])
    if e.code == 401:
        print("ISSUE       : Token is invalid or expired")
    elif e.code == 403:
        print("ISSUE       : Token lacks permissions")
    elif e.code == 404:
        print("ISSUE       : Wrong URL or server ID")
except urllib.error.URLError as e:
    print("URL Error   :", e.reason)
    print("ISSUE       : Cannot reach the server - check network/VPN")
except Exception as e:
    print("Error       :", str(e))
