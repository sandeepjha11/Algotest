import sys
import os
import marshal
import types
import io
import streamlit as st

st.title("Streamlit Dynamic Code Loader")
st.write("This application demonstrates loading and executing encrypted code.")

_KEY = b"ALGODESK247_STATIC_KEY"
_ENCRYPTED_FILE = "_core.enc"

# Get the absolute path to the encrypted file
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), _ENCRYPTED_FILE)

if not os.path.exists(path):
    st.error(f"Missing component: '{_ENCRYPTED_FILE}' not found.")
else:
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
        st.error(f"Failed to unmarshal the code object: {e}")
        code_obj = None

    if code_obj:
        # Create a new module to host the code
        core_module = types.ModuleType("_core")
        core_module.__file__ = path

        # Execute the code object in the context of the new module
        # This will now execute the Streamlit commands in core_logic.py
        exec(code_obj, core_module.__dict__)

        # Add the new module to sys.modules so it can be imported elsewhere if needed
        sys.modules["_core"] = core_module
        st.info("Successfully loaded and executed the encrypted module.")
