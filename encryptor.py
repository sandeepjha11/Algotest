import marshal

# The same key from the original script
_KEY = b"ALGODESK247_STATIC_KEY"
_SOURCE_FILE = "core_logic.py"
_OUTPUT_FILE = "_core.enc"

# Read the source code
with open(_SOURCE_FILE, "r") as f:
    source_code = f.read()

# Compile the source code into a code object
compiled_code = compile(source_code, _SOURCE_FILE, "exec")

# Marshal the code object
marshaled_code = marshal.dumps(compiled_code)

# Prepend a 16-byte header, similar to the original.
# In the original, this was likely for metadata, but here we'll just use null bytes.
header = b'\x00' * 16
data_to_encrypt = header + marshaled_code

# Encrypt the marshaled code with the XOR cipher
encrypted_code = bytes(b ^ _KEY[i % len(_KEY)] for i, b in enumerate(data_to_encrypt))

# Write the encrypted code to the output file
with open(_OUTPUT_FILE, "wb") as f:
    f.write(encrypted_code)

print(f"Successfully encrypted '{_SOURCE_FILE}' to '{_OUTPUT_FILE}'")
