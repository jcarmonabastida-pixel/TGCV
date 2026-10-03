package org.tgcv.viatra.v002.observer.serial;

import java.util.Objects;
import org.tgcv.viatra.v002.observer.serial.model.ObservationRecord;

public final class DeterministicObservationSerializer {

    public String serialize(ObservationRecord record) {
        Objects.requireNonNull(record);
        StringBuilder out = new StringBuilder();
        out.append("event=").append(record.event());
        if (record.rule() != null) {
            out.append("|rule=").append(record.rule());
        }
        if (record.activationIdentity() != null) {
            out.append("|activation=").append(record.activationIdentity());
        }
        return out.toString();
    }
}
