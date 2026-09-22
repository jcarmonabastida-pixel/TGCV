#!/usr/bin/env python3
from pathlib import Path

TARGET = Path("rainbow/rainbow-core/src/main/java/org/sa/rainbow/core/RainbowMaster.java")
METHOD = "public IDelegateManagementPort connectDelegate(String delegateID, Properties connectionProperties)"
LINE = "m_delegateConfigurtationPorts.put(delegateID, delegateConfigurationPort);"

def marker(indent, name):
    return f'{indent}System.err.println("[TR131-DIAG-CONNECT] {name}");'

def main():
    if not TARGET.exists():
        raise SystemExit(f"TARGET_NOT_FOUND: {TARGET}")

    text = TARGET.read_text()
    if "[TR131-DIAG-CONNECT] BEFORE_CONFIG_MAP_PUT" in text:
        print("ALREADY_PATCHED")
        return

    method_pos = text.find(METHOD)
    if method_pos < 0:
        raise SystemExit("CONNECT_DELEGATE_METHOD_NOT_FOUND")

    method_end = text.find("\n        /**", method_pos)
    if method_end < 0:
        method_end = len(text)

    method = text[method_pos:method_end]
    if method.count(LINE) != 1:
        raise SystemExit(f"TARGET_LINE_COUNT_IN_CONNECT_DELEGATE={method.count(LINE)}")

    lines = method.splitlines(keepends=True)
    out = []
    patched = False

    for line in lines:
        stripped = line.strip()
        if stripped == LINE:
            indent = line[:len(line) - len(line.lstrip())]
            out.append(marker(indent, "BEFORE_CONFIG_MAP_PUT") + "\n")
            out.append(line)
            out.append(marker(indent, "AFTER_CONFIG_MAP_PUT") + "\n")
            patched = True
        elif stripped == "Beacon beacon = new Beacon(Long.parseLong(":
            indent = line[:len(line) - len(line.lstrip())]
            out.append(marker(indent, "BEFORE_BEACON_CREATE") + "\n")
            out.append(line)
        elif stripped == 'm_rainbowEnvironment.getProperty(RainbowConstants.PROPKEY_DELEGATE_BEACONPERIOD, "1000")) + 1000);':
            out.append(line)
            indent = line[:len(line) - len(line.lstrip())]
            out.append(marker(indent, "AFTER_BEACON_CREATE") + "\n")
        elif stripped == "synchronized (m_heartbeats) {":
            indent = line[:len(line) - len(line.lstrip())]
            out.append(marker(indent, "BEFORE_HEARTBEAT_PUT") + "\n")
            out.append(line)
        elif stripped == "}":
            if out and any("BEFORE_HEARTBEAT_PUT" in x for x in out[-4:]):
                out.append(line)
                indent = line[:len(line) - len(line.lstrip())]
                out.append(marker(indent, "AFTER_HEARTBEAT_PUT") + "\n")
            else:
                out.append(line)
        elif stripped == "m_nonCompliantDelegates.add(delegatePort.getDelegateId());":
            indent = line[:len(line) - len(line.lstrip())]
            out.append(marker(indent, "BEFORE_NONCOMPLIANT_ADD") + "\n")
            out.append(line)
            out.append(marker(indent, "AFTER_NONCOMPLIANT_ADD") + "\n")
        elif stripped == "beacon.mark();":
            indent = line[:len(line) - len(line.lstrip())]
            out.append(marker(indent, "BEFORE_BEACON_MARK") + "\n")
            out.append(line)
            out.append(marker(indent, "AFTER_BEACON_MARK") + "\n")
        elif stripped == "return delegatePort;":
            indent = line[:len(line) - len(line.lstrip())]
            out.append(marker(indent, "BEFORE_RETURN") + "\n")
            out.append(line)
        else:
            out.append(line)

    if not patched:
        raise SystemExit("TARGET_LINE_NOT_FOUND_IN_CONNECT_DELEGATE")

    new_method = "".join(out)
    TARGET.write_text(text[:method_pos] + new_method + text[method_pos + len(method):])
    print("PATCH_OK")

if __name__ == "__main__":
    main()
