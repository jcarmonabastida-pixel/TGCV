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
    if "[TR131-DIAG-DELEGATE] BEFORE_BLOCKING_SEND" in text:
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
        if s == "m_deploymentPort = null;":
            out.append(marker(indent, "BEFORE_DEPLOYMENT_PORT_RESET") + "\n")
            out.append(line)
            out.append(marker(indent, "AFTER_DEPLOYMENT_PORT_RESET") + "\n")
        elif s == "try {":
            out.append(marker(indent, "BEFORE_BLOCKING_SEND_TRY") + "\n")
            out.append(line)
        elif s.startswith("getConnectionRole().blockingSendAndReceive(msg, new IESEBListener()"):
            out.append(marker(indent, "BEFORE_BLOCKING_SEND") + "\n")
            out.append(line)
        elif "}, Rainbow.instance().getProperty(IRainbowEnvironment.PROPKEY_PORT_TIMEOUT, 10000));" in s:
            out.append(line)
            out.append(marker(indent, "AFTER_BLOCKING_SEND") + "\n")
        elif s == "public void receive(RainbowESEBMessage msgRcvd) {":
            out.append(line)
            out.append(marker(indent + "\t", "REPLY_RECEIVED") + "\n")
        elif s == 'String reply = (String) msgRcvd.getProperty(ESEBConstants.MSG_CONNECT_REPLY);':
            out.append(line)
            out.append(marker(indent, "REPLY_VALUE") + "\n")
        elif s == "m_deploymentPort = RainbowPortFactory.createDelegateDeploymentPort(m_delegate,":
            out.append(marker(indent, "BEFORE_DEPLOYMENT_PORT_CREATE") + "\n")
            out.append(line)
        elif s == "m_deploymentPort = DisconnectedRainbowManagementPort.instance();":
            out.append(marker(indent, "BEFORE_DISCONNECTED_PORT") + "\n")
            out.append(line)
        elif s == "return m_deploymentPort;":
            out.append(marker(indent, "BEFORE_CONNECT_RETURN") + "\n")
            out.append(line)
        else:
            out.append(line)
    TARGET.write_text(text[:pos] + "".join(out) + text[end:])
    print("PATCH_OK")

if __name__ == "__main__":
    main()
