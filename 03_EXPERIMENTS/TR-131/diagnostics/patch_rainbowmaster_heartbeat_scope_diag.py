#!/usr/bin/env python3
from pathlib import Path

TARGET = Path("rainbow/rainbow-core/src/main/java/org/sa/rainbow/core/RainbowMaster.java")

METHODS = [
    ("connectDelegate", "public IDelegateManagementPort connectDelegate(String delegateID, Properties connectionProperties)"),
    ("processHeartbeat", "public void processHeartbeat(String delegateID)"),
    ("checkHeartbeats", "private void checkHeartbeats()"),
    ("flushDelegate", "void flushDelegate(String id)"),
]

MARKERS = {
    "connectDelegate": ("[TR131-DIAG-HEARTBEAT] CONNECT_DELEGATE_BEFORE_PUT", "[TR131-DIAG-HEARTBEAT] CONNECT_DELEGATE_AFTER_PUT"),
    "processHeartbeat": ("[TR131-DIAG-HEARTBEAT] PROCESS_HEARTBEAT_BEFORE_GET", "[TR131-DIAG-HEARTBEAT] PROCESS_HEARTBEAT_AFTER_GET"),
    "checkHeartbeats": ("[TR131-DIAG-HEARTBEAT] CHECK_HEARTBEATS_BEFORE_SCAN", "[TR131-DIAG-HEARTBEAT] CHECK_HEARTBEATS_AFTER_SCAN"),
    "flushDelegate": ("[TR131-DIAG-HEARTBEAT] FLUSH_DELEGATE_BEFORE_REMOVE", "[TR131-DIAG-HEARTBEAT] FLUSH_DELEGATE_AFTER_REMOVE"),
}

def method_bounds(text, start):
    ends = [text.find(sig, start + 1) for _, sig in METHODS]
    ends = [p for p in ends if p >= 0]
    return start, min(ends) if ends else len(text)

def patch_method(text, name, signature):
    start = text.find(signature)
    if start < 0:
        raise SystemExit(f"{name.upper()}_METHOD_NOT_FOUND")
    start, end = method_bounds(text, start)
    method = text[start:end]
    before, after = MARKERS[name]
    if before in method:
        return text, False
    sync = "synchronized (m_heartbeats) {"
    positions = []
    pos = method.find(sync)
    while pos >= 0:
        positions.append(pos)
        pos = method.find(sync, pos + 1)
    if len(positions) != 1:
        raise SystemExit(f"{name.upper()}_HEARTBEAT_SYNC_COUNT={len(positions)}")
    open_pos = positions[0]
    line_start = method.rfind("\n", 0, open_pos) + 1
    indent = method[line_start:open_pos]
    method = method[:line_start] + indent + f'System.err.println("{before}");\n' + method[line_start:]
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
    for name, signature in METHODS:
        text, did = patch_method(text, name, signature)
        changed += int(did)
    if changed == 0:
        print("ALREADY_PATCHED")
        return
    TARGET.write_text(text)
    print(f"PATCH_OK METHODS_CHANGED={changed}")

if __name__ == "__main__":
    main()
