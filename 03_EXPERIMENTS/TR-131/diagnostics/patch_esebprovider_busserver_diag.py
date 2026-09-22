#!/usr/bin/env python3
from pathlib import Path

TARGET = Path("rainbow/rainbow-core/src/main/java/org/sa/rainbow/core/ports/eseb/ESEBProvider.java")

text = TARGET.read_text(encoding="utf-8")
if "[TR131-DIAG-ESEB-PROVIDER]" in text:
    print("ALREADY_PATCHED")
    raise SystemExit(0)

old = """            catch (Exception e) {
                ESEBConnector.LOGGER.warn (MessageFormat.format ("BusServer could not be created on port {0}", port));
            }
"""
new = """            catch (Exception e) {
                System.err.println("[TR131-DIAG-ESEB-PROVIDER] PORT=" + port);
                System.err.println("[TR131-DIAG-ESEB-PROVIDER] CACHE_PRESENT=" + s_servers.containsKey(port));
                System.err.println("[TR131-DIAG-ESEB-PROVIDER] CACHE_SIZE=" + s_servers.size());
                System.err.println("[TR131-DIAG-ESEB-PROVIDER] CACHED_BUS=" + s_servers.get(port));
                System.err.println("[TR131-DIAG-ESEB-PROVIDER] EXCEPTION_CLASS=" + e.getClass().getName());
                System.err.println("[TR131-DIAG-ESEB-PROVIDER] EXCEPTION_MESSAGE=" + e.getMessage());
                e.printStackTrace(System.err);
                ESEBConnector.LOGGER.warn (MessageFormat.format ("BusServer could not be created on port {0}", port));
            }
"""
if old not in text:
    raise SystemExit("PATCH_BLOCK_NOT_FOUND")

text = text.replace(old, new, 1)
TARGET.write_text(text, encoding="utf-8")
print("PATCH_OK")
