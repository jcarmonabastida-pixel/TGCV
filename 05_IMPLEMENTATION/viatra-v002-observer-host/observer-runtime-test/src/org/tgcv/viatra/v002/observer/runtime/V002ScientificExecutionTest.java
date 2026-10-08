package org.tgcv.viatra.v002.observer.runtime;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;

import org.junit.Test;
import org.tgcv.viatra.v002.observer.V002ObserverEvent;
import org.tgcv.viatra.v002.observer.V002SerialExecutor;

public class V002ScientificExecutionTest {

    @Test
    public void executeCanonicalScientificRunExactlyOnce() throws Exception {
        Path fixtureDirectory = Paths.get(
            "../../../../00_GOVERNANCE/architecture/fixtures");

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

        assertEquals(2, events.size());
        assertEquals(V002ObserverEvent.Type.TRANSFORMATION_BEGIN,
            events.get(0).getType());
        assertEquals(V002ObserverEvent.Type.TRANSFORMATION_END,
            events.get(1).getType());
        assertTrue(events.get(0).getActivationInstanceId() != null);
    }
}
