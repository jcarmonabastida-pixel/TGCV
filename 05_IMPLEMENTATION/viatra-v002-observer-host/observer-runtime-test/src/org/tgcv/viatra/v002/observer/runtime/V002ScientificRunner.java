package org.tgcv.viatra.v002.observer.runtime;

import java.nio.file.Path;
import java.nio.file.Paths;

import org.eclipse.emf.ecore.EObject;
import org.eclipse.emf.ecore.resource.Resource;
import org.eclipse.viatra.examples.cps.cyberPhysicalSystem.CyberPhysicalSystem;
import org.eclipse.viatra.examples.cps.deployment.Deployment;
import org.eclipse.viatra.examples.cps.traceability.CPSToDeployment;
import org.eclipse.viatra.examples.cps.traceability.TraceabilityFactory;
import org.eclipse.viatra.query.runtime.api.ViatraQueryEngine;
import org.eclipse.viatra.query.runtime.emf.EMFScope;
import org.tgcv.viatra.v002.observer.V002FixtureStateCapture;
import org.tgcv.viatra.v002.observer.V002ObservationProvenance;
import org.tgcv.viatra.v002.observer.V002SerialExecutor;
import org.tgcv.viatra.v002.observer.V002SerialObserver;
import org.tgcv.viatra.v002.observer.fixture.V002FixtureLoader;

/**
 * Minimal V002 runner boundary for pre-execution validation.
 *
 * This runner verifies fixture bytes, loads the frozen semantic fixture,
 * constructs the canonical executor binding, and stops before execute().
 * It is intentionally not a scientific execution entry point.
 */
public final class V002ScientificRunner {

    private V002ScientificRunner() {
    }

    public static Binding bind(Path fixtureDirectory) throws Exception {
        V002FixtureLoader loader = new V002FixtureLoader();
        V002FixtureLoader.FixtureSet fixtures = loader.bind(
            fixtureDirectory.resolve("TGCV_VIATRA_MINIMAL_FIXTURE_v002_CPS.xmi"),
            fixtureDirectory.resolve("TGCV_VIATRA_MINIMAL_FIXTURE_v002_Deployment_INITIAL.xmi"),
            fixtureDirectory.resolve("TGCV_VIATRA_MINIMAL_FIXTURE_v002_Deployment_EXPECTED.xmi"),
            fixtureDirectory.resolve("TGCV_VIATRA_MINIMAL_FIXTURE_v002_Traceability_INITIAL.xmi"),
            fixtureDirectory.resolve("TGCV_VIATRA_MINIMAL_FIXTURE_v002_Traceability_EXPECTED.xmi"));

        V002FixtureLoader.SemanticFixtureSet semantic = loader.loadSemantic(fixtures);

        CyberPhysicalSystem cps = root(semantic.cps(), CyberPhysicalSystem.class);
        Deployment deployment = root(semantic.deploymentInitial(), Deployment.class);
        CPSToDeployment mapping = TraceabilityFactory.eINSTANCE.createCPSToDeployment();
        mapping.setCps(cps);
        mapping.setDeployment(deployment);

        ViatraQueryEngine engine = ViatraQueryEngine.on(
            new EMFScope(semantic.resourceSet()));
        V002ObservationProvenance provenance = new V002ObservationProvenance(
            "https://github.com/jcarmonabastida-pixel/TGCV",
            "scientific-runner-preflight",
            "Tycho/JUnit8-VIATRA2.0.2");
        V002SerialObserver observer = new V002SerialObserver(provenance);
        V002SerialExecutor executor = new V002SerialExecutor(mapping, engine, observer);

        return new Binding(executor, semantic, fixtures);
    }

    private static <T extends EObject> T root(Resource resource, Class<T> type) {
        if (resource.getContents().size() != 1) {
            throw new IllegalStateException(
                "Expected exactly one fixture root: " + resource.getURI());
        }
        EObject root = resource.getContents().get(0);
        if (!type.isInstance(root)) {
            throw new IllegalStateException(
                "Unexpected fixture root type: " + root.eClass().getName());
        }
        return type.cast(root);
    }

    public static void main(String[] args) throws Exception {
        Path fixtureDirectory = args.length == 0
            ? Paths.get("../../../../00_GOVERNANCE/architecture/fixtures")
            : Paths.get(args[0]);

        Binding binding = bind(fixtureDirectory);

        System.out.println("TGCV_V002_RUNNER_BINDING=PASS");
        System.out.println("TGCV_V002_RUNNER_FIXTURE_BYTES=VERIFIED");
        System.out.println("TGCV_V002_RUNNER_EXECUTOR="
            + binding.executor().getClass().getName());
        System.out.println("TGCV_V002_RUNNER_EXECUTION=NOT_PERFORMED");
        System.out.println("TGCV_V002_RUNNER_NEXT_GATE=EXPLICIT_SCIENTIFIC_EXECUTION");
    }

    public static final class Binding {
        private final V002SerialExecutor executor;
        private final V002FixtureLoader.SemanticFixtureSet semantic;
        private final V002FixtureLoader.FixtureSet fixtures;

        private Binding(V002SerialExecutor executor,
                        V002FixtureLoader.SemanticFixtureSet semantic,
                        V002FixtureLoader.FixtureSet fixtures) {
            this.executor = executor;
            this.semantic = semantic;
            this.fixtures = fixtures;
        }

        public V002SerialExecutor executor() {
            return executor;
        }

        public V002FixtureLoader.SemanticFixtureSet semantic() {
            return semantic;
        }

        public V002FixtureLoader.FixtureSet fixtures() {
            return fixtures;
        }
    }
}
