#!/usr/bin/env python3
from pathlib import Path

TARGET = Path("rainbow/rainbow-core/src/main/java/org/sa/rainbow/core/RainbowMaster.java")

REPLACEMENTS = {
    '[TR131-DIAG-CONNECT] BEFORE_HEARTBEAT_PUT': '[TR131-DIAG-HEARTBEAT] BEFORE_HEARTBEAT_PUT',
    '[TR131-DIAG-CONNECT] AFTER_HEARTBEAT_PUT': '[TR131-DIAG-HEARTBEAT] AFTER_HEARTBEAT_PUT',
}

def main():
    if not TARGET.exists():
        raise SystemExit(f"TARGET_NOT_FOUND: {TARGET}")
    text = TARGET.read_text()
    if '[TR131-DIAG-HEARTBEAT] BEFORE_HEARTBEAT_PUT' in text:
        print('ALREADY_PATCHED')
        return
    counts = {k: text.count(k) for k in REPLACEMENTS}
    if counts['[TR131-DIAG-CONNECT] BEFORE_HEARTBEAT_PUT'] == 0:
        raise SystemExit('HEARTBEAT_MARKER_NOT_FOUND')
    for old, new in REPLACEMENTS.items():
        text = text.replace(old, new)
    TARGET.write_text(text)
    print('PATCH_OK')
    print(f"BEFORE_COUNT={counts['[TR131-DIAG-CONNECT] BEFORE_HEARTBEAT_PUT']}")
    print(f"AFTER_COUNT={counts['[TR131-DIAG-CONNECT] AFTER_HEARTBEAT_PUT']}")
    
if __name__ == '__main__':
    main()
