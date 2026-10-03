package org.tgcv.viatra.v002.observer;

import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public final class V002CanonicalStateSerializer {
    private V002CanonicalStateSerializer() {
    }

    public static final String SCHEMA_ID = "TGCV_VIATRA_V002_STATE_v001";

    public static byte[] serialize(String hostInstanceId, String nodeIp,
            String deploymentHostId, boolean tracePresent) {
        if (hostInstanceId == null || nodeIp == null || deploymentHostId == null) {
            throw new IllegalArgumentException("V002 state fields must be non-null");
        }
        String canonical =
            "schema=" + SCHEMA_ID + "\n"
            + "cps.hostInstance=" + escape(hostInstanceId) + "\n"
            + "cps.nodeIp=" + escape(nodeIp) + "\n"
            + "deployment.host=" + escape(deploymentHostId) + "\n"
            + "trace.present=" + tracePresent + "\n";
        return canonical.getBytes(StandardCharsets.UTF_8);
    }

    public static String sha256(byte[] canonicalBytes) {
        try {
            MessageDigest md = MessageDigest.getInstance("SHA-256");
            byte[] digest = md.digest(canonicalBytes);
            StringBuilder out = new StringBuilder(digest.length * 2);
            for (byte b : digest) {
                out.append(String.format("%02x", b & 0xff));
            }
            return out.toString();
        } catch (NoSuchAlgorithmException e) {
            throw new IllegalStateException("SHA-256 is required by the V002 contract", e);
        }
    }

    private static String escape(String value) {
        return value.replace("\\", "\\\\").replace("\n", "\\n");
    }
}
