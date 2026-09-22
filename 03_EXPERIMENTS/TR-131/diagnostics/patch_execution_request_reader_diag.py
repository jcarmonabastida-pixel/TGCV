#!/usr/bin/env python3
from pathlib import Path

TARGET = Path("libs/eseblib/src/main/java/edu/cmu/cs/able/eseb/rpc/ExecutionRequestReader.java")

MARK = "[TR131-DIAG-RPC-READER]"

def main():
    if not TARGET.exists():
        raise SystemExit(f"TARGET_NOT_FOUND: {TARGET}")
    text = TARGET.read_text()
    if MARK in text:
        print("ALREADY_PATCHED")
        return

    inserts = {
        'Ensure.is_true(m_information.is_execution_request(data.value()),':
            '        System.err.println("[TR131-DIAG-RPC-READER] HANDLES_ENTER");\n'
            '        System.err.println("[TR131-DIAG-RPC-READER] PARTICIPANT_ID=" + m_participant_id);\n'
            '        System.err.println("[TR131-DIAG-RPC-READER] REQUEST_DST=" + m_information.execution_request_dst(data.value()));\n',
        'String obj_id = m_information.execution_request_obj_id(data.value());':
            '        System.err.println("[TR131-DIAG-RPC-READER] OBJ_ID=" + obj_id);\n'
            '        System.err.println("[TR131-DIAG-RPC-READER] SERVICE_COUNT=" + m_services.size());\n'
            '        System.err.println("[TR131-DIAG-RPC-READER] SERVICE_IDS=" + m_services.keySet());\n',
        'String op_name = m_information.execution_request_operation(':
            '          System.err.println("[TR131-DIAG-RPC-READER] SERVICE_FOUND");\n',
        'm_dispatcher.dispatch(new Runnable() {':
            '        System.err.println("[TR131-DIAG-RPC-READER] DISPATCH");\n',
        'result = soe.execute(operation, args);':
            '                          System.err.println("[TR131-DIAG-RPC-READER] EXECUTE_ENTER");\n'
            '                          result = soe.execute(operation, args);\n'
            '                          System.err.println("[TR131-DIAG-RPC-READER] EXECUTE_RETURN");\n',
        'send_success(data.value(), operation, result.first(),':
            '                      System.err.println("[TR131-DIAG-RPC-READER] SEND_SUCCESS");\n',
        'send_failure(data.value(), result.second(), sink);':
            '                      System.err.println("[TR131-DIAG-RPC-READER] SEND_FAILURE");\n',
    }

    for needle in inserts:
        if text.count(needle) != 1:
            raise SystemExit(f"EXPECTED_SINGLE_MATCH_FAILED: {needle}")

    out = text
    for needle, insertion in inserts.items():
        out = out.replace(needle, insertion + needle, 1)

    TARGET.write_text(out)
    print("PATCH_OK")

if __name__ == "__main__":
    main()
