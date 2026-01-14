from models import assinger_llm
import inspect
import sys

print(f"Python executable: {sys.executable}")
print(f"assinger_llm module: {assinger_llm.__module__}")
try:
    print(f"Signature: {inspect.signature(assinger_llm)}")
except Exception as e:
    print(f"Error getting signature: {e}")

print(f"Doc: {assinger_llm.__doc__}")
