#!/usr/bin/env python3
from pathlib import Path

TARGET = Path("rainbow/rainbow-core/src/main/java/org/sa/rainbow/core/RainbowMaster.java")

METHODS = {
    "connectDelegate": "public IDelegateManagementPort connectDelegate(String delegateID, Properties connectionProperties)",
    "processHeartbeat": "public void processHeartbeat(String delegateID)",
    "checkHeartbeats": "private void checkHeartbeats()",
    "flushDelegate": "public void flushDelegate(String id)",
}

MARKERS = {
    "connectDelegate": ("[TR131-DIAG-HEARTBEAT] BEFORE_HEARTBEAT_PUT", "[TR131-DIAG-HEARTBEAT] AFTER_HEARTBEAT_PUT"),
    "processHeartbeat": ("[TR131-DIAG-HEARTBEAT] BEFORE_HEARTBEAT_GET", "[TR131-DIAG-HEARTBEAT] AFTER_HEARTBEAT_GET"),
    "checkHeartbeats": ("[TR131-DIAG-HEARTBEAT] BEFORE_HEARTBEAT_SCAN", "[TR131-DIAG-HEARTBEAT] AFTER_HEARTBEAT_SCAN"),
    "flushDelegate": ("[TR131-DIAG-HEARTBEAT] BEFORE_HEARTBEAT_REMOVE", "[TR131-DIAG-HEARTBEAT] AFTER_HEARTBEAT_REMOVE"),
}

def bounds(text, start):
    positions = [text.find(sig, start + 1) for sig in METHODS.values()]
    positions = [p for p in positions if p >= 0]
    end = min(positions) if positions else len(text)
    return start, end

def patch_method(text, name, signature):
    start = text.find(signature)
    if start < 0:
        raise SystemExit(f"{name.upper()}_METHOD_NOT_FOUND")
    start, end = bounds(text, start)
    method = text[start:end]
    before, after = MARKERS[name]
    if before in method:
        return text, False
    sync = "synchronized (m_heartbeats) {"
    count = method.count(sync)
    if count != 1:
        raise SystemExit(f"{name.upper()}_HEARTBEAT_SYNC_COUNT={count}")
    pos = method.find(sync)
    line_start = method.rfind("\n", 0, pos) + 1
    indent = method[line_start:pos]
    method = method[:line_start] + indent + f'System.err.println("{before}");\n' + method[line_start:]
    # Locate the matching synchronized block by brace balance from the original opening.
    open_pos = method.find(sync, line_start)
    depth = 0
    close_pos = None
    for i in range(open_pos, len(method)):
        if method[i] == "{":
            depth += 1
        elif method[i] == "}":
            depth -= 1
            if depth == 0:
                close_pos = i
                break
    if close_pos is None:
        raise SystemExit(f"{name.upper()}_HEARTBEAT_BLOCK_UNCLOSED")
    close_line_end = method.find("\n", close_pos)
    if close_line_end < 0:
        close_line_end = len(method)
    close_indent_start = method.rfind("\n", 0, close_pos) + 1
    close_indent = method[close_indent_start:close_pos]
    method = method[:close_line_end] + f'\n{close_indent}System.err.println("{after}");' + method[close_line_end:]
    return text[:start] + method + text[end:], True

def main():
    if not TARGET.exists():
        raise SystemExit(f"TARGET_NOT_FOUND: {TARGET}")
    text = TARGET.read_text()
    changed = 0
    for name, signature in METHODS.items():
        text, did = patch_method(text, name, signature)
        changed += int(did)
    if changed == 0:
        print("ALREADY_PATCHED")
        return
    TARGET.write_text(text)
    print(f"PATCH_OK METHODS_CHANGED={changed}")

if __name__ == "__main__":
    main()
