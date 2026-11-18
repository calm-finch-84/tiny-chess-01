import base64
import hashlib
import lzma
from pathlib import Path
import py_compile

root = Path(__file__).resolve().parent
source = (root / "engine_src.py").read_bytes()

packages = []
for preset in (6, 9):
    payload = base64.b85encode(lzma.compress(source, preset=preset))
    stub = (
        b"import lzma,base64\n"
        b"exec(lzma.decompress(base64.b85decode("
        + repr(payload).encode("ascii")
        + b")))\n"
    )
    packages.append((stub, payload))

stub, payload = min(packages, key=lambda item: len(item[0]))
assert len(stub) <= 4096, f"Package too large: {len(stub)} bytes"

decoded = lzma.decompress(base64.b85decode(payload))
source_hash = hashlib.sha256(source).hexdigest()
decoded_hash = hashlib.sha256(decoded).hexdigest()
assert decoded == source
assert source_hash == decoded_hash

target = root / "main.py"
target.write_bytes(stub)
py_compile.compile(str(target), doraise=True)

print(f"main.py: {target.stat().st_size} bytes")
print(f"Round-trip: PASS (SHA-256 {source_hash})")
print("Syntax: PASS")
