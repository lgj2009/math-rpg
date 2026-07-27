"""Send pixso-export.html to Pixso via MCP code_to_design."""
import json
import urllib.request
import sys

HTML_PATH = "d:/编程/Python/stutdy/.claude/worktrees/math-rpg-implementation/pixso-export.html"
SESSION_ID = "7d7a30a6-f90c-430b-87ad-bfdb3f4332e5"
MCP_URL = "http://127.0.0.1:3667/mcp"

# Read HTML
with open(HTML_PATH, "r", encoding="utf-8") as f:
    html_str = f.read()

print(f"HTML size: {len(html_str)} chars")

# Build JSON-RPC payload
payload = {
    "jsonrpc": "2.0",
    "id": 10,
    "method": "tools/call",
    "params": {
        "name": "code_to_design",
        "arguments": {"htmlStr": html_str}
    }
}

data = json.dumps(payload).encode("utf-8")
print(f"Payload size: {len(data)} bytes")

# Send request
req = urllib.request.Request(
    MCP_URL,
    data=data,
    headers={
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream",
        "mcp-session-id": SESSION_ID,
    },
    method="POST",
)

print("Sending to Pixso MCP...")
try:
    with urllib.request.urlopen(req, timeout=120) as resp:
        result = resp.read().decode("utf-8")
        print(f"Response ({len(result)} chars):")
        # Parse SSE response
        for line in result.split("\n"):
            if line.startswith("data: "):
                data_part = line[6:]
                try:
                    parsed = json.loads(data_part)
                    # Pretty-print result content
                    if "result" in parsed:
                        r = parsed["result"]
                        if "content" in r:
                            for c in r["content"]:
                                if c.get("type") == "text":
                                    print(c["text"][:2000])
                                else:
                                    print(json.dumps(c, ensure_ascii=False, indent=2)[:1000])
                        else:
                            print(json.dumps(r, ensure_ascii=False, indent=2)[:2000])
                    elif "error" in parsed:
                        print(f"ERROR: {json.dumps(parsed['error'], ensure_ascii=False)}")
                except json.JSONDecodeError:
                    print(f"Raw data: {data_part[:500]}")
except Exception as e:
    print(f"Request failed: {e}")
