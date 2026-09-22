#!/usr/bin/env python3
from pathlib import Path

TARGET = Path("libs/eseblib/src/main/java/edu/cmu/cs/able/eseb/rpc/ExecutionResultReader.java")

text = TARGET.read_text(encoding="utf-8")
if "[TR131-DIAG-RPC-RESULT]" in text:
    print("ALREADY_PATCHED")
    raise SystemExit(0)

old = """\t\tlong id = m_information.execution_response_id(data.value());
\t\tRemoteExecution re = null;
\t\tsynchronized (this) {
\t\t\tWeakReference<RemoteExecution> wr = m_pending.get(id);
\t\t\tif (wr != null) {
\t\t\t\tre = wr.get();
\t\t\t}
\t\t\t
\t\t\tif (re != null) {
\t\t\t\tm_pending.remove(id);
\t\t\t}
\t\t}
"""
new = """\t\tlong id = m_information.execution_response_id(data.value());
\t\tRemoteExecution re = null;
\t\tSystem.err.println("[TR131-DIAG-RPC-RESULT] HANDLES_ENTER");
\t\tSystem.err.println("[TR131-DIAG-RPC-RESULT] RESPONSE_ID=" + id);
\t\tSystem.err.println("[TR131-DIAG-RPC-RESULT] PENDING_COUNT_BEFORE=" + m_pending.size());
\t\tsynchronized (this) {
\t\t\tWeakReference<RemoteExecution> wr = m_pending.get(id);
\t\t\tSystem.err.println("[TR131-DIAG-RPC-RESULT] WAIT_REF_FOUND=" + (wr != null));
\t\t\tif (wr != null) {
\t\t\t\tre = wr.get();
\t\t\t\tSystem.err.println("[TR131-DIAG-RPC-RESULT] REMOTE_EXECUTION_FOUND=" + (re != null));
\t\t\t}
\t\t\t
\t\t\tif (re != null) {
\t\t\t\tm_pending.remove(id);
\t\t\t\tSystem.err.println("[TR131-DIAG-RPC-RESULT] PENDING_REMOVED");
\t\t\t}
\t\t}
\t\tSystem.err.println("[TR131-DIAG-RPC-RESULT] PENDING_COUNT_AFTER=" + m_pending.size());
"""
if old not in text:
    raise SystemExit("PATCH_BLOCK_NOT_FOUND")

text = text.replace(old, new, 1)

old2 = """\t\tif (re == null) {
"""
new2 = """\t\tif (re == null) {
\t\t\tSystem.err.println("[TR131-DIAG-RPC-RESULT] NO_MATCH_RETURN_FALSE");
"""
text = text.replace(old2, new2, 1)

old3 = """\t\tif (m_information.is_successful_execution(data.value())) {
"""
new3 = """\t\tif (m_information.is_successful_execution(data.value())) {
\t\t\tSystem.err.println("[TR131-DIAG-RPC-RESULT] SUCCESS_RESPONSE");
"""
text = text.replace(old3, new3, 1)

old4 = """\t\t\tif (fi == null) {
\t\t\t\tre.done(new RemoteExecutionResult(output));
"""
new4 = """\t\t\tif (fi == null) {
\t\t\t\tSystem.err.println("[TR131-DIAG-RPC-RESULT] DONE_SUCCESS");
\t\t\t\tre.done(new RemoteExecutionResult(output));
"""
text = text.replace(old4, new4, 1)

old5 = """\t\t} else {
\t\t\tString type = m_information.execution_response_failure_type(
"""
new5 = """\t\t} else {
\t\t\tSystem.err.println("[TR131-DIAG-RPC-RESULT] FAILURE_RESPONSE");
\t\t\tString type = m_information.execution_response_failure_type(
"""
text = text.replace(old5, new5, 1)

TARGET.write_text(text, encoding="utf-8")
print("PATCH_OK")
