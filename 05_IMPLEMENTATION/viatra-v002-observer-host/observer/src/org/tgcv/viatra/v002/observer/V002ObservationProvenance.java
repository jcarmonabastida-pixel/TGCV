package org.tgcv.viatra.v002.observer;

import java.util.Objects;

/**
 * Frozen provenance contract for one V002 runtime observation.
 *
 * Canonical state digests deliberately exclude these run/provenance fields.
 * Implementation revision is supplied by the execution environment so the
 * runtime gate can bind an observation to the exact source revision.
 */
public final class V002ObservationProvenance {
    public static final String FIXTURE_REVISION = "TGCV_VIATRA_MINIMAL_FIXTURE_v002";
    public static final String FIXTURE_SHA256_MANIFEST_REVISION =
        "TGCV_VIATRA_V002_FIXTURE_SHA256_MANIFEST_v001";
    public static final String INSTRUMENTATION_REVISION =
        "TGCV_VIATRA_V002_SERIAL_RUNTIME_OBSERVATION_v001";

    private final String sourceRepository;
    private final String implementationRevision;
    private final String runtimeIdentity;

    public V002ObservationProvenance(String sourceRepository,
            String implementationRevision, String runtimeIdentity) {
        this.sourceRepository = require(sourceRepository, "sourceRepository");
        this.implementationRevision = require(implementationRevision, "implementationRevision");
        this.runtimeIdentity = require(runtimeIdentity, "runtimeIdentity");
    }

    public String getSourceRepository() { return sourceRepository; }
    public String getImplementationRevision() { return implementationRevision; }
    public String getRuntimeIdentity() { return runtimeIdentity; }
    public String getFixtureRevision() { return FIXTURE_REVISION; }
    public String getFixtureSha256ManifestRevision() { return FIXTURE_SHA256_MANIFEST_REVISION; }
    public String getInstrumentationRevision() { return INSTRUMENTATION_REVISION; }

    private static String require(String value, String field) {
        return Objects.requireNonNull(value, field + " must not be null");
    }
}
