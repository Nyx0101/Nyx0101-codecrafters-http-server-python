import asyncio
import argparse
import re
import sys
from aiohttp import web
from pathlib import Path

GLOBALS = {}

def stderr(*args, **kwargs):
    print(*args, **kwargs, file=sys.stderr)

def parse_request(content: bytes) -> tuple[str, str, dict[str, str], str]:
    first_line, *tail = content.split(b"\r\n")
    method, path, _ = first_line.split(b" ")
    headers: dict[str, str] = {}
    while (line := tail.pop(0)) != b"":
        key, value = line.split(b": ")
        headers[key.decode()] = value.decode()
    return method.decode(), path.decode(), headers, b"".join(tail).decode()

def make_response(
    status: int,
    headers: dict[str, str] | None = None,
    body: str = "",
) -> bytes:
    headers = headers or {}
    msg = {
        200: "OK",
        201: "CREATED",
        404: "NOT FOUND",
    }
    return b"\r\n".join(
        map(
            lambda i: i.encode(),
            [
                f"HTTP/1.1 {status} {msg[status]}".encode(),
                *[f"{k}: {v}".encode() for k, v in headers.items()],
                f"Content-Length: {len(body)}".encode(),
                "".encode(),
                body.encode(),
            ],
        ),
    )

async def handle(request):
    method, path, headers, body = parse_request(await request.read())
    
    if re.fullmatch(r"/", path):
        return web.Response(text="", status=200)
    elif re.fullmatch(r"/user-agent", path):
        ua =  headers.get("User-Agent", "")
        return web.Response(text=ua, content_type="text/plain", status=200)
    elif match := re.fullmatch(r"/echo/(.+)", path):
        msg = match.group(1)
        return web.Response(text=msg, content_type="text/plain", status=200)
    elif match := re.fullmatch(r"/files/(.+)", path):
        p = Path(GLOBALS["DIR"]) / match.group(1)
        if method.upper() == "GET" and p.is_file():
            return web.Response(body=p.read_text(), content_type="application/octet-stream", status=200)
        elif method.upper() == "POST":
            p.write_bytes(body.encode())
            return web.Response(status=201)
    else:
        return web.Response(text="", status=404)

async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", default=".")
    args = parser.parse_args()
    
    GLOBALS["DIR"] = args.directory
    
    app = web.Application()
    app.add_routes([web.post("/{path:.+}", handle)]
                  + [web.get("/{path:.+}", handle)]
    
    runner = web.AppRunner(app)
    site = web.TCPSite(runner, "localhost", 4221)
    
    await site.start()
    
if __name__ == "__main__":
    asyncio.run(main())



    
           





    
    

                
                
           
        
   
