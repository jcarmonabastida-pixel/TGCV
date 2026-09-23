# TR-131 — Runner V004 Construction Audit

**Status:** CONSTRUCTED — UNIT TEST EXECUTION PENDING / SCIENTIFIC EXECUTION NOT AUTHORIZED  
**Date:** 2026-09-23

V004 corrects the V003 release blocker: every input field outside the frozen analytical allow-list is now rejected. Explicit outcome/value fields retain a distinct error class.

One new unit test, `test_unknown_rejected`, verifies rejection of an arbitrary unauthorized field.

The previous 11 tests are preserved, yielding a 12-test minimum suite.

No scientific evidence is read or modified.

**Next gate:** execute the complete 12-test suite locally and audit the result.
