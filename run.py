import sys
try:
    import code
except ImportError:
    print("Module not found")
    sys.exit(1)

code.start()
