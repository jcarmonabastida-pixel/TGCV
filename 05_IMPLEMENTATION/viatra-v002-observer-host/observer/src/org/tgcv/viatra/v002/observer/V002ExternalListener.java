package org.tgcv.viatra.v002.observer;

import org.eclipse.viatra.transformation.evm.api.Activation;
import org.eclipse.viatra.transformation.evm.api.event.AbstractTransformationListener;

/**
 * External V002 EVM listener.
 *
 * This class is intentionally separate from the historical VIATRA
 * transformation implementation. It observes activation firing through the
 * public listener API and delegates lifecycle recording to V002SerialObserver.
 *
 * No transformation rule is created, fired, reordered, or modified here.
 */
public final class V002ExternalListener extends AbstractTransformationListener {

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
    public void beforeFiring(Activation<?> activation) {
        if (activation == null) {
            throw new IllegalArgumentException("activation must not be null");
        }

        String activationIdentity = activation.toString();

        observer.beforeFiring(
            activationIdentity,
            stateCapture.capturePreState(activation));
    }

    @Override
    public void afterFiring(Activation<?> activation) {
        if (activation == null) {
            throw new IllegalArgumentException("activation must not be null");
        }

        String activationIdentity = activation.toString();

        observer.afterFiring(
            activationIdentity,
            stateCapture.capturePostState(activation));
    }
}
