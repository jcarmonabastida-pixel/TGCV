package org.tgcv.viatra.v002.observer.fixture;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Objects;

public final class V002FixtureLoader {

    public static final String CPS_SHA256 =
        "8d432da0d3fd49ba88f809611f222614ef588809691e66bcc954a4cd509f66bb";
    public static final String DEPLOYMENT_INITIAL_SHA256 =
        "fea5bc84929e99145ebe07f4eabeb1d04eaceb805b3e35d7975aff793bd9af8e";
    public static final String DEPLOYMENT_EXPECTED_SHA256 =
        "92addffad49e828a8c3f7c0ca7b00c870f00e9c419415c3b997e06cc36b0e966";
    public static final String TRACEABILITY_INITIAL_SHA256 =
        "1ce4c0c69f324e43d87b41dee2561a55668d06c815294919011a2d5c3d1d88c1";
    public static final String TRACEABILITY_EXPECTED_SHA256 =
        "29ebb291e72ff061618aa809af2e16527464f2475e21bfe558de00bd36de33e3";

    public static final class FixtureSet {
        private final Path cps;
        private final Path deploymentInitial;
        private final Path deploymentExpected;
        private final Path traceabilityInitial;
        private final Path traceabilityExpected;

        public FixtureSet(Path cps, Path deploymentInitial, Path deploymentExpected,
                          Path traceabilityInitial, Path traceabilityExpected) {
            this.cps = Objects.requireNonNull(cps);
            this.deploymentInitial = Objects.requireNonNull(deploymentInitial);
            this.deploymentExpected = Objects.requireNonNull(deploymentExpected);
            this.traceabilityInitial = Objects.requireNonNull(traceabilityInitial);
            this.traceabilityExpected = Objects.requireNonNull(traceabilityExpected);
        }

        public Path cps() { return cps; }
        public Path deploymentInitial() { return deploymentInitial; }
        public Path deploymentExpected() { return deploymentExpected; }
        public Path traceabilityInitial() { return traceabilityInitial; }
        public Path traceabilityExpected() { return traceabilityExpected; }
    }

    public FixtureSet bind(Path cps, Path deploymentInitial, Path deploymentExpected,
                           Path traceabilityInitial, Path traceabilityExpected) {
        return new FixtureSet(cps, deploymentInitial, deploymentExpected,
            traceabilityInitial, traceabilityExpected);
    }

    public void verifyBytes(FixtureSet fixtures) throws IOException {
        verify(fixtures.cps(), CPS_SHA256);
        verify(fixtures.deploymentInitial(), DEPLOYMENT_INITIAL_SHA256);
        verify(fixtures.deploymentExpected(), DEPLOYMENT_EXPECTED_SHA256);
        verify(fixtures.traceabilityInitial(), TRACEABILITY_INITIAL_SHA256);
        verify(fixtures.traceabilityExpected(), TRACEABILITY_EXPECTED_SHA256);
    }

    private void verify(Path path, String expectedSha256) throws IOException {
        byte[] bytes = Files.readAllBytes(path);
        String actual = sha256(bytes);
        if (!expectedSha256.equals(actual)) {
            throw new IllegalStateException(
                "Fixture SHA-256 mismatch: " + path + " expected=" +
                expectedSha256 + " actual=" + actual);
        }
    }

    private String sha256(byte[] bytes) {
        try {
            MessageDigest digest = MessageDigest.getInstance("SHA-256");
            byte[] hash = digest.digest(bytes);
            StringBuilder hex = new StringBuilder(hash.length * 2);
            for (byte value : hash) {
                hex.append(String.format("%02x", value & 0xff));
            }
            return hex.toString();
        } catch (NoSuchAlgorithmException e) {
            throw new IllegalStateException("SHA-256 unavailable", e);
        }
    }
}
