package org.tgcv.viatra.v002.observer.fixture;

import java.nio.file.Path;
import java.util.Objects;

public final class V002FixtureLoader {

    public record FixtureSet(
        Path cps,
        Path deploymentInitial,
        Path deploymentExpected,
        Path traceabilityInitial,
        Path traceabilityExpected) {

        public FixtureSet {
            Objects.requireNonNull(cps);
            Objects.requireNonNull(deploymentInitial);
            Objects.requireNonNull(deploymentExpected);
            Objects.requireNonNull(traceabilityInitial);
            Objects.requireNonNull(traceabilityExpected);
        }
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
