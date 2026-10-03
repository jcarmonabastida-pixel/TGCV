package org.tgcv.viatra.v002.observer.serial.model;

import java.util.Objects;

public final class ObservationRecord {
    private final String event;
    private final String rule;
    private final String activationIdentity;

    private ObservationRecord(String event, String rule, String activationIdentity) {
        this.event = Objects.requireNonNull(event);
        this.rule = rule;
        this.activationIdentity = activationIdentity;
    }

    public static ObservationRecord lifecycle(String event) {
        return new ObservationRecord(event, null, null);
    }

    public static ObservationRecord activation(String rule, String activationIdentity) {
        return new ObservationRecord("ACTIVATION", Objects.requireNonNull(rule),
            Objects.requireNonNull(activationIdentity));
    }

    public String event() {
        return event;
    }

    public String rule() {
        return rule;
    }

    public String activationIdentity() {
        return activationIdentity;
    }
}
