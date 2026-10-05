package org.tgcv.viatra.v002.observer;

import org.eclipse.viatra.transformation.evm.api.Activation;

/**
 * Supplies deterministic PRE/POST state digests for the V002 observer.
 *
 * The capture implementation belongs to the host/executor and is deliberately
 * kept outside the listener so the listener remains observational only.
 */
public interface V002StateCapture {

    String capturePreState(Activation<?> activation);

    String capturePostState(Activation<?> activation);
}
