package org.tgcv.viatra.v002.observer;

public final class V002ObserverEvent {
    public enum Type {
        TRANSFORMATION_BEGIN,
        TRANSFORMATION_END
    }

    private final long eventSeq;
    private final Type type;
    private final String transformationId;
    private final String activationInstanceId;
    private final String preStateDigest;
    private final String postStateDigest;
    private final V002ObservationProvenance provenance;

    public V002ObserverEvent(long eventSeq, Type type, String transformationId,
            String activationInstanceId, String preStateDigest, String postStateDigest,
            V002ObservationProvenance provenance) {
        this.eventSeq = eventSeq;
        this.type = type;
        this.transformationId = transformationId;
        this.activationInstanceId = activationInstanceId;
        this.preStateDigest = preStateDigest;
        this.postStateDigest = postStateDigest;
        if (provenance == null) {
            throw new IllegalArgumentException("provenance must not be null");
        }
        this.provenance = provenance;
    }

    public long getEventSeq() { return eventSeq; }
    public Type getType() { return type; }
    public String getTransformationId() { return transformationId; }
    public String getActivationInstanceId() { return activationInstanceId; }
    public String getPreStateDigest() { return preStateDigest; }
    public String getPostStateDigest() { return postStateDigest; }
    public V002ObservationProvenance getProvenance() { return provenance; }
}
