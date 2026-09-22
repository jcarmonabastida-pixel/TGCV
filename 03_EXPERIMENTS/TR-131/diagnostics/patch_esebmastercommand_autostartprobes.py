#!/usr/bin/env python3
from pathlib import Path

TARGET = Path("rainbow/rainbow-core/src/main/java/org/sa/rainbow/core/ports/eseb/rpc/IESEBMasterCommandPortRemoteInterface.java")
METHOD = '    boolean allDelegatesOK ();'
INSERT = '''    @Override
    @ReturnTypeMapping ("bool")
    boolean autoStartProbes ();

'''

def main():
    if not TARGET.exists():
        raise SystemExit(f"TARGET_NOT_FOUND: {TARGET}")

    text = TARGET.read_text()
    if "boolean autoStartProbes" in text:
        print("ALREADY_PATCHED")
        return

    if text.count(METHOD) != 1:
        raise SystemExit(f"TARGET_ANCHOR_COUNT={text.count(METHOD)}")

    text = text.replace(METHOD + "\n\n}", METHOD + "\n\n" + INSERT + "}", 1)
    TARGET.write_text(text)
    print("PATCH_OK")

if __name__ == "__main__":
    main()
