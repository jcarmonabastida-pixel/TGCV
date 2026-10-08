package org.tgcv.viatra.v002.observer.runtime;

import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;

import org.tgcv.viatra.v002.observer.V002ObserverEvent;
import org.tgcv.viatra.v002.observer.V002SerialExecutor;

/**
 * Minimal V002 scientific execution runner.
 *
 * Uses the validated preflight binding and invokes the canonical scientific
 * executor exactly once. No statistical estimator or value/utility layer is
 * added here.
 */
public final class V002ScientificExecutionRunner {

    private V002ScientificExecutionRunner() {
    }

    public static void main(String[] args) throws Exception {
        Path fixtureDirectory = args.length == 0
            ? Paths.get("../../../../00_GOVERNANCE/architecture/fixtures")
            : Paths.get(args[0]);

        V002ScientificRunner.Binding binding =
            V002ScientificRunner.bind(fixtureDirectory);

        V002SerialExecutor executor = binding.executor();

        System.out.println("TGCV_V002_SCIENTIFIC_EXECUTION=START");
        executor.execute();

        List<V002ObserverEvent> events = executor.observationSnapshot();

        System.out.println("TGCV_V002_SCIENTIFIC_EXECUTION=COMPLETED");
        System.out.println("TGCV_V002_SCIENTIFIC_EVENT_COUNT=" + events.size());

        for (V002ObserverEvent event : events) {
            System.out.println(
                "TGCV_V002_EVENT"
                + "|seq=" + event.getEventSeq()
                + "|type=" + event.getType()
                + "|transformationId=" + event.getTransformationId()
                + "|activationInstanceId=" + event.getActivationInstanceId()
                + "|preStateDigest=" + event.getPreStateDigest()
                + "|postStateDigest=" + event.getPostStateDigest());
        }
    }
}
