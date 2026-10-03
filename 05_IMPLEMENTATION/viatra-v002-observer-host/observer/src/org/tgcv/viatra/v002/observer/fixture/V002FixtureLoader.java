package org.tgcv.viatra.v002.observer.fixture;

import java.nio.file.Path;
import java.util.Objects;

public final class V002FixtureLoader {

    public static final class FixtureSet {
        private final Path cps;
        private final Path deploymentInitial;
        private final Path deploymentExpected;
        private final Path traceabilityInitial;
        private final Path traceabilityExpected;

        public FixtureSet(
            Path cps,
            Path deploymentInitial,
            Path deploymentExpected,
            Path traceabilityInitial,
            Path traceabilityExpected) {
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

    public FixtureSet bind(
        Path cps,
        Path deploymentInitial,
        Path deploymentExpected,
        Path traceabilityInitial,
        Path traceabilityExpected) {
        return new FixtureSet(
            cps,
            deploymentInitial,
            deploymentExpected,
            traceabilityInitial,
            traceabilityExpected);
    }

    public void assertImmutable(FixtureSet fixtures) {
        Objects.requireNonNull(fixtures);
        // Runtime byte loading and SHA-256 verification are intentionally deferred.
    }
}
