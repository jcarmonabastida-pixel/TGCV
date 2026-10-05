package org.tgcv.viatra.v002.observer;

import org.eclipse.viatra.query.runtime.api.ViatraQueryEngine;
import org.eclipse.viatra.transformation.evm.api.Activation;
import org.eclipse.viatra.transformation.evm.api.RuleSpecification;
import org.eclipse.viatra.transformation.evm.api.adapter.IEVMListener;
import org.eclipse.viatra.transformation.evm.api.event.ActivationState;
import org.eclipse.viatra.transformation.evm.api.event.EventFilter;
import org.eclipse.viatra.transformation.evm.api.event.EventType;

/**
 * External V002 EVM listener.
 *
 * This class is intentionally separate from the historical VIATRA
 * transformation implementation. It observes activation firing through the
 * public VIATRA 2.0.2 listener API and delegates lifecycle recording to
 * V002SerialObserver.
 *
 * No transformation rule is created, fired, reordered, or modified here.
 */
public final class V002ExternalListener implements IEVMListener {

    private final V002SerialObserver observer;
    private final V002StateCapture stateCapture;

    public V002ExternalListener(V002SerialObserver observer, V002StateCapture stateCapture) {
        if (observer == null) {
            throw new IllegalArgumentException("observer must not be null");
        }
        if (stateCapture == null) {
            throw new IllegalArgumentException("stateCapture must not be null");
        }
        this.observer = observer;
        this.stateCapture = stateCapture;
    }

    @Override
    public void initializeListener(ViatraQueryEngine engine) {
        if (engine == null) {
            throw new IllegalArgumentException("engine must not be null");
        }
    }

    @Override
    public void beforeFiring(Activation<?> activation) {
        if (activation == null) {
            throw new IllegalArgumentException("activation must not be null");
        }
        observer.beforeFiring(
            activation.toString(),
            stateCapture.capturePreState(activation));
    }

    @Override
    public void afterFiring(Activation<?> activation) {
        if (activation == null) {
            throw new IllegalArgumentException("activation must not be null");
        }
        observer.afterFiring(
            activation.toString(),
            stateCapture.capturePostState(activation));
    }

    @Override
    public void startTransaction(String transactionID) {
    }

    @Override
    public void endTransaction(String transactionID) {
    }

    @Override
    public void activationChanged(Activation<?> activation, ActivationState oldState, EventType event) {
    }

    @Override
    public void activationCreated(Activation<?> activation, ActivationState inactiveState) {
    }

    @Override
    public void activationRemoved(Activation<?> activation, ActivationState oldState) {
    }

    @Override
    public void addedRule(RuleSpecification<?> specification, EventFilter<?> filter) {
    }

    @Override
    public void removedRule(RuleSpecification<?> specification, EventFilter<?> filter) {
    }

    @Override
    public void disposeListener() {
    }
}
