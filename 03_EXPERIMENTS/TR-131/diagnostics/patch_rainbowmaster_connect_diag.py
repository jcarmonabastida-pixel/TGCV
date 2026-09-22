#!/usr/bin/env python3
from pathlib import Path

TARGET = Path("rainbow/rainbow-core/src/main/java/org/sa/rainbow/core/RainbowMaster.java")

OLD = """                        m_delegateConfigurtationPorts.put(delegateID, delegateConfigurationPort);
                        // Add a second to the heartbeat to allow for communication time
                        // TODO: Must be a better way to do this...
                        Beacon beacon = new Beacon(Long.parseLong(
                                        m_rainbowEnvironment.getProperty(RainbowConstants.PROPKEY_DELEGATE_BEACONPERIOD, "1000")) + 1000);
                        synchronized (m_heartbeats) {
                                m_heartbeats.put(delegatePort.getDelegateId(), beacon);
                        }
                        m_nonCompliantDelegates.add(delegatePort.getDelegateId());
                        beacon.mark();
                        LOGGER.info(MessageFormat.format("Master created management connection with delegate {0}", delegateID));
                        return delegatePort;"""

NEW = """                        System.err.println("[TR131-DIAG-CONNECT] BEFORE_CONFIG_MAP_PUT");
                        m_delegateConfigurtationPorts.put(delegateID, delegateConfigurationPort);
                        System.err.println("[TR131-DIAG-CONNECT] AFTER_CONFIG_MAP_PUT");
                        System.err.println("[TR131-DIAG-CONNECT] BEFORE_BEACON_CREATE");
                        // Add a second to the heartbeat to allow for communication time
                        // TODO: Must be a better way to do this...
                        Beacon beacon = new Beacon(Long.parseLong(
                                        m_rainbowEnvironment.getProperty(RainbowConstants.PROPKEY_DELEGATE_BEACONPERIOD, "1000")) + 1000);
                        System.err.println("[TR131-DIAG-CONNECT] AFTER_BEACON_CREATE");
                        System.err.println("[TR131-DIAG-CONNECT] BEFORE_HEARTBEAT_PUT");
                        synchronized (m_heartbeats) {
                                m_heartbeats.put(delegatePort.getDelegateId(), beacon);
                        }
                        System.err.println("[TR131-DIAG-CONNECT] AFTER_HEARTBEAT_PUT");
                        System.err.println("[TR131-DIAG-CONNECT] BEFORE_NONCOMPLIANT_ADD");
                        m_nonCompliantDelegates.add(delegatePort.getDelegateId());
                        System.err.println("[TR131-DIAG-CONNECT] AFTER_NONCOMPLIANT_ADD");
                        System.err.println("[TR131-DIAG-CONNECT] BEFORE_BEACON_MARK");
                        beacon.mark();
                        System.err.println("[TR131-DIAG-CONNECT] AFTER_BEACON_MARK");
                        LOGGER.info(MessageFormat.format("Master created management connection with delegate {0}", delegateID));
                        System.err.println("[TR131-DIAG-CONNECT] BEFORE_RETURN");
                        return delegatePort;"""

def main():
    if not TARGET.exists():
        raise SystemExit(f"TARGET_NOT_FOUND: {TARGET}")
    text = TARGET.read_text()
    if "[TR131-DIAG-CONNECT] BEFORE_CONFIG_MAP_PUT" in text:
        print("ALREADY_PATCHED")
        return
    if OLD not in text:
        raise SystemExit("TARGET_BLOCK_NOT_FOUND")
    TARGET.write_text(text.replace(OLD, NEW, 1))
    print("PATCH_OK")

if __name__ == "__main__":
    main()
