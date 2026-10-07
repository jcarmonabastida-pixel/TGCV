package org.tgcv.viatra.v002.observer.runtime;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotNull;
import static org.junit.Assert.assertTrue;

import java.util.List;

import org.eclipse.emf.common.util.URI;
import org.eclipse.emf.ecore.resource.Resource;
import org.eclipse.emf.ecore.resource.ResourceSet;
import org.eclipse.emf.ecore.resource.impl.ResourceSetImpl;
import org.eclipse.viatra.examples.cps.cyberPhysicalSystem.CyberPhysicalSystem;
import org.eclipse.viatra.examples.cps.cyberPhysicalSystem.CyberPhysicalSystemFactory;
import org.eclipse.viatra.examples.cps.cyberPhysicalSystem.HostInstance;
import org.eclipse.viatra.examples.cps.cyberPhysicalSystem.HostType;
import org.eclipse.viatra.examples.cps.deployment.Deployment;
import org.eclipse.viatra.examples.cps.deployment.DeploymentFactory;
import org.eclipse.viatra.examples.cps.traceability.CPSToDeployment;
import org.eclipse.viatra.examples.cps.traceability.TraceabilityFactory;
import org.eclipse.viatra.query.runtime.api.ViatraQueryEngine;
import org.eclipse.viatra.query.runtime.emf.EMFScope;
import org.junit.Test;
import org.tgcv.viatra.v002.observer.V002ObserverEvent;
import org.tgcv.viatra.v002.observer.V002ObservationProvenance;
import org.tgcv.viatra.v002.observer.V002SerialExecutor;
import org.tgcv.viatra.v002.observer.V002SerialObserver;
import org.tgcv.viatra.v002.observer.V002TransformationIdentity;

public class V002ObserverRuntimeTest {

    @Test
    public void observerListenerRuntimeIsBoundAndDeterministic() throws Exception {
        Observation first = runOnce();
        Observation second = runOnce();

        assertEquals(2, first.events.size());
        assertEquals(2, second.events.size());

        assertEquals(V002ObserverEvent.Type.TRANSFORMATION_BEGIN, first.events.get(0).getType());
        assertEquals(V002ObserverEvent.Type.TRANSFORMATION_END, first.events.get(1).getType());
        assertEquals(1L, first.events.get(0).getEventSeq());
        assertEquals(2L, first.events.get(1).getEventSeq());

        assertEquals(V002TransformationIdentity.digest(),
            first.events.get(0).getTransformationId());
        assertEquals(first.events.get(0).getTransformationId(),
            first.events.get(1).getTransformationId());

        assertNotNull(first.events.get(0).getActivationInstanceId());
        assertEquals(first.events.get(0).getActivationInstanceId(),
            first.events.get(1).getActivationInstanceId());
        assertNotNull(first.events.get(0).getPreStateDigest());
        assertNotNull(first.events.get(1).getPostStateDigest());

        assertEquals(first.events.get(0).getPreStateDigest(),
            second.events.get(0).getPreStateDigest());
        assertEquals(first.events.get(1).getPostStateDigest(),
            second.events.get(1).getPostStateDigest());

        assertEquals(1, first.hostCount);
        assertEquals(1, second.hostCount);
        assertTrue(first.traceCount == 1);
        assertTrue(second.traceCount == 1);

        assertEquals(V002ObservationProvenance.FIXTURE_REVISION,
            first.events.get(0).getProvenance().getFixtureRevision());
        assertEquals(V002ObservationProvenance.FIXTURE_SHA256_MANIFEST_REVISION,
            first.events.get(0).getProvenance().getFixtureSha256ManifestRevision());
        assertEquals(V002ObservationProvenance.INSTRUMENTATION_REVISION,
            first.events.get(0).getProvenance().getInstrumentationRevision());
    }

    private void assertHistoricalSignalUtilVisible() throws Exception {
        Class<?> signalUtil = Class.forName(
            "org.eclipse.viatra.examples.cps.xform.m2m.util.SignalUtil");
        assertNotNull(signalUtil);
        System.out.println("TGCV_SIGNAL_UTIL_CLASS=" + signalUtil.getName());
        System.out.println("TGCV_SIGNAL_UTIL_CLASSLOADER=" + signalUtil.getClassLoader());
        System.out.println("TGCV_CONTEXT_CLASSLOADER=" + Thread.currentThread().getContextClassLoader());
    }

    private Observation runOnce() throws Exception {
        assertHistoricalSignalUtilVisible();
        assertObserverRuntimeClassesLoadedFromExpectedBundle();
        ResourceSet resourceSet = new ResourceSetImpl();

        CyberPhysicalSystem cps = CyberPhysicalSystemFactory.eINSTANCE.createCyberPhysicalSystem();
        HostType hostType = CyberPhysicalSystemFactory.eINSTANCE.createHostType();
        HostInstance host = CyberPhysicalSystemFactory.eINSTANCE.createHostInstance();

        cps.getHostTypes().add(hostType);
        hostType.setIdentifier("HostType");
        hostType.getInstances().add(host);
        host.setIdentifier("HostInstance");
        host.setNodeIp("152.66.102.6");

        Deployment deployment = DeploymentFactory.eINSTANCE.createDeployment();
        Resource cpsResource = resourceSet.createResource(URI.createURI("memory:/v002-cps.xmi"));
        cpsResource.getContents().add(cps);
        Resource deploymentResource =
            resourceSet.createResource(URI.createURI("memory:/v002-deployment.xmi"));
        deploymentResource.getContents().add(deployment);

        CPSToDeployment mapping = TraceabilityFactory.eINSTANCE.createCPSToDeployment();
        mapping.setCps(cps);
        mapping.setDeployment(deployment);

        ViatraQueryEngine engine = ViatraQueryEngine.on(new EMFScope(resourceSet));
        V002ObservationProvenance provenance = new V002ObservationProvenance(
            "https://github.com/jcarmonabastida-pixel/TGCV",
            "runtime-test-source",
            "Tycho/JUnit8-VIATRA2.0.2");

        V002SerialObserver observer = new V002SerialObserver(provenance);
        V002SerialExecutor executor = new V002SerialExecutor(mapping, engine, observer);
        executor.execute();

        List<V002ObserverEvent> events = executor.observationSnapshot();
        return new Observation(events, deployment.getHosts().size(), mapping.getTraces().size());
    }

    private void assertObserverRuntimeClassesLoadedFromExpectedBundle() {
        Class<?> executorClass = V002SerialExecutor.class;
        Class<?> parserSetupClass = org.tgcv.viatra.v002.observer.ObserverPatternParserSetup.class;
        System.out.println("TGCV_OBSERVER_BUNDLE_IDENTITY=executorClass=" + executorClass.getName());
        System.out.println("TGCV_OBSERVER_BUNDLE_IDENTITY=executorClassLoader=" + executorClass.getClassLoader());
        System.out.println("TGCV_OBSERVER_BUNDLE_IDENTITY=executorCodeSource=" + executorClass.getProtectionDomain().getCodeSource());
        System.out.println("TGCV_OBSERVER_BUNDLE_IDENTITY=parserSetupClass=" + parserSetupClass.getName());
        System.out.println("TGCV_OBSERVER_BUNDLE_IDENTITY=parserSetupClassLoader=" + parserSetupClass.getClassLoader());
        System.out.println("TGCV_OBSERVER_BUNDLE_IDENTITY=parserSetupCodeSource=" + parserSetupClass.getProtectionDomain().getCodeSource());
        System.out.println("TGCV_OBSERVER_BUNDLE_IDENTITY=parserSetupResource=" + parserSetupClass.getResource("ObserverPatternParserSetup.class"));
    }

    private static final class Observation {
        private final List<V002ObserverEvent> events;
        private final int hostCount;
        private final int traceCount;

        private Observation(List<V002ObserverEvent> events, int hostCount, int traceCount) {
            this.events = events;
            this.hostCount = hostCount;
            this.traceCount = traceCount;
        }
    }
}