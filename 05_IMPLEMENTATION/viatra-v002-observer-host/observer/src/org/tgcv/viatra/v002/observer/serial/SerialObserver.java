package org.tgcv.viatra.v002.observer.serial;

import org.tgcv.viatra.v002.observer.serial.model.ObservationRecord;

public final class SerialObserver {

    public ObservationRecord transformationBegin() {
        return ObservationRecord.lifecycle("TRANSFORMATION_BEGIN");
    }

    public ObservationRecord hostRuleActivation(String activationIdentity) {
        return ObservationRecord.activation("hostRule", activationIdentity);
    }

    public ObservationRecord transformationEnd() {
        return ObservationRecord.lifecycle("TRANSFORMATION_END");
    }
}
