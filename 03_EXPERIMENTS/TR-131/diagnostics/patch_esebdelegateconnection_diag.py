#!/usr/bin/env python3
from pathlib import Path

TARGET = Path("rainbow/rainbow-core/src/main/java/org/sa/rainbow/core/ports/eseb/ESEBDelegateConnectionPort.java")
METHOD = "public IDelegateManagementPort connectDelegate(String delegateID, Properties connectionProperties)"

def marker(indent, name):
    return f'{indent}System.err.println("[TR131-DIAG-DELEGATE] {name}");'

def main():
    if not TARGET.exists():
        raise SystemExit(f"TARGET_NOT_FOUND: {TARGET}")
    text = TARGET.read_text()
    if "[TR131-DIAG-DELEGATE] REPLY_CLASS" in text:
        print("ALREADY_PATCHED")
        return
    pos = text.find(METHOD)
    if pos < 0:
        raise SystemExit("CONNECT_DELEGATE_METHOD_NOT_FOUND")
    end = text.find("\n\t@Override", pos + len(METHOD))
    if end < 0:
        raise SystemExit("CONNECT_DELEGATE_METHOD_END_NOT_FOUND")
    method = text[pos:end]
    lines = method.splitlines(keepends=True)
    out = []
    for line in lines:
        s = line.strip()
        indent = line[:len(line)-len(line.lstrip())]
        if s == 'String reply = (String) msgRcvd.getProperty(ESEBConstants.MSG_CONNECT_REPLY);':
            out.append(line)
            out.append(indent + 'System.err.println("[TR131-DIAG-DELEGATE] REPLY_CLASS=" + (reply == null ? "null" : reply.getClass().getName()));\n')
            out.append(indent + 'System.err.println("[TR131-DIAG-DELEGATE] REPLY_VALUE=" + String.valueOf(reply));\n')
        else:
            out.append(line)
    TARGET.write_text(text[:pos] + "".join(out) + text[end:])
    print("PATCH_OK")

if __name__ == "__main__":
    main()
