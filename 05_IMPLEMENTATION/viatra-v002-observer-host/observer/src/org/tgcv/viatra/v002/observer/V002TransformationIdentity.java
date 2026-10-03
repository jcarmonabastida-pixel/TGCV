package org.tgcv.viatra.v002.observer;

import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public final class V002TransformationIdentity {
    public static final String IMPLEMENTATION_ID =
        "org.eclipse.viatra.examples.cps.xform.m2m.batch.viatra";
    public static final String TRANSFORMATION_ID =
        "CPS2DeploymentTransformationViatra";
    public static final String RULE_ID = "hostRule";
    public static final String FIXTURE_CONTRACT_REVISION = "V002";

    private V002TransformationIdentity() {
    }

    public static String canonicalTuple() {
        return IMPLEMENTATION_ID + "|" + TRANSFORMATION_ID + "|" + RULE_ID + "|"
            + FIXTURE_CONTRACT_REVISION;
    }

    public static String digest() {
        try {
            MessageDigest md = MessageDigest.getInstance("SHA-256");
            byte[] bytes = md.digest(canonicalTuple().getBytes(StandardCharsets.UTF_8));
            StringBuilder out = new StringBuilder(bytes.length * 2);
            for (byte b : bytes) {
                out.append(String.format("%02x", b & 0xff));
            }
            return out.toString();
        } catch (NoSuchAlgorithmException e) {
            throw new IllegalStateException("SHA-256 is required by the V002 contract", e);
        }
    }
}
