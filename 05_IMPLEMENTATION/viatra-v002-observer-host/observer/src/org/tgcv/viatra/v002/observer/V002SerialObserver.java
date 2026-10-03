package org.tgcv.viatra.v002.observer;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.concurrent.atomic.AtomicLong;

public final class V002SerialObserver {
    private final AtomicLong sequence = new AtomicLong();
    private final List<V002ObserverEvent> events = new ArrayList<V002ObserverEvent>();
    private boolean firing;

    public synchronized V002ObserverEvent beforeFiring(String activationInstanceId, String preStateDigest) {
        if (firing) {
            throw new IllegalStateException("V002 observer rejects overlapping transformation execution");
        }
        if (activationInstanceId == null || preStateDigest == null) {
            throw new IllegalArgumentException("V002 BEGIN fields must be non-null");
        }
        firing = true;
        long seq = sequence.incrementAndGet();
        V002ObserverEvent event = new V002ObserverEvent(
            seq, V002ObserverEvent.Type.TRANSFORMATION_BEGIN,
            V002TransformationIdentity.digest(), activationInstanceId, preStateDigest, null);
        events.add(event);
        return event;
    }

    public synchronized V002ObserverEvent afterFiring(String activationInstanceId, String postStateDigest) {
        if (!firing) {
            throw new IllegalStateException("V002 END without matching BEGIN");
        }
        if (activationInstanceId == null || postStateDigest == null) {
            throw new IllegalArgumentException("V002 END fields must be non-null");
        }
        long seq = sequence.incrementAndGet();
        V002ObserverEvent event = new V002ObserverEvent(
            seq, V002ObserverEvent.Type.TRANSFORMATION_END,
            V002TransformationIdentity.digest(), activationInstanceId, null, postStateDigest);
        events.add(event);
        firing = false;
        return event;
    }

    public synchronized List<V002ObserverEvent> snapshot() {
        return Collections.unmodifiableList(new ArrayList<V002ObserverEvent>(events));
    }
}
