import sys
import os
import marshal
import types
import io

_KEY = b"ALGODESK247_STATIC_KEY"
_ENCRYPTED_FILE = "_core.enc"

# Get the absolute path to the encrypted file
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), _ENCRYPTED_FILE)

if not os.path.exists(path):
    raise RuntimeError(f"Missing component: '{_ENCRYPTED_FILE}' not found.")

# Read the encrypted file
with open(path, "rb") as f:
    encrypted_data = f.read()

# Decrypt the data
decrypted_data = bytes(b ^ _KEY[i % len(_KEY)] for i, b in enumerate(encrypted_data))

# Load the marshaled code object
# We skip the first 16 bytes, which was our dummy header
try:
    code_obj = marshal.loads(decrypted_data[16:])
except (ValueError, TypeError, EOFError) as e:
    raise RuntimeError(f"Failed to unmarshal the code object: {e}")

# Create a new module to host the code
core_module = types.ModuleType("_core")
core_module.__file__ = path

# Execute the code object in the context of the new module
# This populates the module with the functions and variables from our original script
exec(code_obj, core_module.__dict__)

# Add the new module to sys.modules so it can be imported elsewhere if needed
sys.modules["_core"] = core_module

# Now, we can call the main function from our dynamically loaded module
if hasattr(core_module, "main") and callable(core_module.main):
    core_module.main()
else:
    print("The '_core' module does not have a 'main' function.")
