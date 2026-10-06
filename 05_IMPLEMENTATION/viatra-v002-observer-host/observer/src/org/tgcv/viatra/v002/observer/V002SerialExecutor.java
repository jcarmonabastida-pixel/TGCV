package org.tgcv.viatra.v002.observer;

import java.io.ByteArrayOutputStream;
import java.io.InputStream;
import java.nio.charset.StandardCharsets;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.function.Consumer;

import org.eclipse.viatra.examples.cps.cyberPhysicalSystem.HostInstance;
import org.eclipse.viatra.examples.cps.deployment.DeploymentFactory;
import org.eclipse.viatra.examples.cps.deployment.DeploymentHost;
import org.eclipse.viatra.examples.cps.traceability.CPS2DeploymentTrace;
import org.eclipse.viatra.examples.cps.traceability.CPSToDeployment;
import org.eclipse.viatra.examples.cps.traceability.TraceabilityFactory;
import org.eclipse.emf.ecore.EObject;
import org.eclipse.viatra.query.patternlanguage.emf.util.PatternParser;

import com.google.inject.Injector;
import org.eclipse.viatra.query.patternlanguage.emf.util.PatternParsingResults;
import org.eclipse.viatra.query.patternlanguage.emf.vql.Pattern;
import org.eclipse.viatra.query.runtime.api.IPatternMatch;
import org.eclipse.viatra.query.runtime.api.IQuerySpecification;
import org.eclipse.viatra.query.runtime.api.ViatraQueryEngine;
import org.eclipse.viatra.transformation.runtime.emf.rules.batch.BatchTransformationRule;
import org.eclipse.viatra.transformation.runtime.emf.rules.batch.BatchTransformationRuleFactory;
import org.eclipse.viatra.transformation.runtime.emf.transformation.batch.BatchTransformation;

/**
 * Concrete serial executor for the canonical V002 HostMapping transformation.
 *
 * The executor reconstructs the historical six-rule batch transformation
 * boundary from the frozen VQL/rule contract and uses only public VIATRA APIs.
 * The canonical minimal fixture is expected to activate HostRule exactly once.
 *
 * Runtime access is deliberately exposed through execute(), while the host
 * main entry point remains guarded until the execution authorization gate.
 */
public final class V002SerialExecutor {
    public static final List<String> HISTORICAL_RULE_ORDER =
        Collections.unmodifiableList(Arrays.asList(
            "HostRule", "ApplicationRule", "StateMachineRule",
            "StateRule", "TransitionRule", "ActionRule"));

    private final CPSToDeployment mapping;
    private final ViatraQueryEngine engine;
    private final V002SerialObserver observer;
    private final V002StateCapture stateCapture;
    private BatchTransformation transformation;

    private static boolean patternParserInitialized;
    private static Injector patternParserInjector;

    private static synchronized void initializePatternParser() {
        if (patternParserInitialized) {
            return;
        }
        ObserverPatternParserSetup setup = new ObserverPatternParserSetup();
        patternParserInjector = setup.createObserverInjector();
        patternParserInitialized = true;
    }

    public V002SerialExecutor(CPSToDeployment mapping, ViatraQueryEngine engine,
            V002SerialObserver observer) {
        if (mapping == null || engine == null || observer == null) {
            throw new IllegalArgumentException("mapping, engine and observer are required");
        }
        this.mapping = mapping;
        this.engine = engine;
        this.observer = observer;
        this.stateCapture = new V002FixtureStateCapture(mapping);
    }

    public List<String> historicalRuleOrder() { return HISTORICAL_RULE_ORDER; }

    public void assertHistoricalRuleOrder() {
        if (!HISTORICAL_RULE_ORDER.equals(Arrays.asList(
                "HostRule", "ApplicationRule", "StateMachineRule",
                "StateRule", "TransitionRule", "ActionRule"))) {
            throw new IllegalStateException("V002 historical rule order has changed");
        }
    }

    public synchronized void execute() throws Exception {
        assertHistoricalRuleOrder();
        requireCanonicalInputShape();

        BatchTransformationRule<?, ?> hostRule =
            buildRule("HostRule", "hostInstance", this::fireHost);
        BatchTransformationRule<?, ?> applicationRule =
            buildRule("ApplicationRule", "applicationInstance", this::rejectNonMinimal);
        BatchTransformationRule<?, ?> stateMachineRule =
            buildRule("StateMachineRule", "appInstanceWithStateMachine", this::rejectNonMinimal);
        BatchTransformationRule<?, ?> stateRule =
            buildRule("StateRule", "state", this::rejectNonMinimal);
        BatchTransformationRule<?, ?> transitionRule =
            buildRule("TransitionRule", "transition", this::rejectNonMinimal);
        BatchTransformationRule<?, ?> actionRule =
            buildRule("ActionRule", "actionPair", this::rejectNonMinimal);

        transformation = BatchTransformation.forEngine(engine)
            .addRule(hostRule)
            .addRule(applicationRule)
            .addRule(stateMachineRule)
            .addRule(stateRule)
            .addRule(transitionRule)
            .addRule(actionRule)
            .addListener(new V002ExternalListener(observer, stateCapture))
            .build();

        try {
            mapping.getTraces().clear();
            mapping.getDeployment().getHosts().clear();
            transformation.getTransformationStatements().fireAllCurrent(hostRule);
            transformation.getTransformationStatements().fireAllCurrent(applicationRule);
            transformation.getTransformationStatements().fireAllCurrent(stateMachineRule);
            transformation.getTransformationStatements().fireAllCurrent(stateRule);
            transformation.getTransformationStatements().fireAllCurrent(transitionRule);
            transformation.getTransformationStatements().fireAllCurrent(actionRule);
            assertMinimalV002Outcome();
        } finally {
            transformation.dispose();
            transformation = null;
        }
    }

    private void requireCanonicalInputShape() {
        if (mapping.getCps() == null || mapping.getDeployment() == null) {
            throw new IllegalStateException("V002 mapping must reference CPS and Deployment");
        }
        if (mapping.getCps().getHostTypes().size() != 1
                || mapping.getCps().getHostTypes().get(0).getInstances().size() != 1) {
            throw new IllegalStateException(
                "Canonical V002 fixture must contain exactly one host instance");
        }
        if (!mapping.getDeployment().getHosts().isEmpty() || !mapping.getTraces().isEmpty()) {
            throw new IllegalStateException(
                "Canonical V002 initial state must have empty output and trace");
        }
    }

    @SuppressWarnings({"rawtypes", "unchecked"})
    private BatchTransformationRule<?, ?> buildRule(
            String name, String patternName, Consumer<IPatternMatch> action) throws Exception {
        IQuerySpecification specification = findSpecification(patternName);
        BatchTransformationRuleFactory factory = new BatchTransformationRuleFactory();
        return (BatchTransformationRule) factory.createRule()
            .precondition(specification)
            .name(name).action(action).build();
    }

    private IQuerySpecification<?> findSpecification(String patternName) throws Exception {
        ClassLoader previous = Thread.currentThread().getContextClassLoader();
        ClassLoader observerLoader = getClass().getClassLoader();
        try {
            Thread.currentThread().setContextClassLoader(observerLoader);
            initializePatternParser();
            try (InputStream in = getClass().getResourceAsStream(
                    "/org/tgcv/viatra/v002/observer/historical/cpsXformM2M.vql")) {
                if (in == null) {
                    throw new IllegalStateException("Frozen historical VQL resource is missing");
                }
                PatternParsingResults results = PatternParser.parser()
                    .withInjector(patternParserInjector)
                    .parse(new String(readAll(in), StandardCharsets.UTF_8));
                if (!results.validationOK()) {
                    throw new IllegalStateException("Historical VQL validation failed: " + results);
                }
                for (Pattern pattern : results.getPatterns()) {
                    if (patternName.equals(pattern.getName())) {
                        for (IQuerySpecification<?> specification : results.getQuerySpecifications()) {
                            if (specification.getFullyQualifiedName().endsWith("." + patternName)) {
                                return specification;
                            }
                        }
                    }
                }
            }
            throw new IllegalStateException("Historical VQL pattern not found: " + patternName);
        } finally {
            Thread.currentThread().setContextClassLoader(previous);
        }
    }

    private byte[] readAll(InputStream input) throws Exception {
        ByteArrayOutputStream out = new ByteArrayOutputStream();
        byte[] buffer = new byte[4096];
        int read;
        while ((read = input.read(buffer)) != -1) {
            out.write(buffer, 0, read);
        }
        return out.toByteArray();
    }

    private void fireHost(IPatternMatch match) {
        HostInstance host = (HostInstance) match.get("hostInstance");
        DeploymentHost deploymentHost = DeploymentFactory.eINSTANCE.createDeploymentHost();
        deploymentHost.setIp(host.getNodeIp());
        mapping.getDeployment().getHosts().add(deploymentHost);

        CPS2DeploymentTrace trace =
            TraceabilityFactory.eINSTANCE.createCPS2DeploymentTrace();
        trace.getCpsElements().add(host);
        trace.getDeploymentElements().add(deploymentHost);
        mapping.getTraces().add(trace);
    }

    private void rejectNonMinimal(IPatternMatch match) {
        throw new IllegalStateException(
            "Canonical V002 minimal fixture unexpectedly activated rule: " + match.patternName());
    }

    private void assertMinimalV002Outcome() {
        if (mapping.getDeployment().getHosts().size() != 1) {
            throw new IllegalStateException("Expected exactly one DeploymentHost");
        }
        DeploymentHost host = mapping.getDeployment().getHosts().get(0);
        if (!"152.66.102.6".equals(host.getIp())) {
            throw new IllegalStateException("Unexpected DeploymentHost.ip: " + host.getIp());
        }
        if (mapping.getTraces().size() != 1) {
            throw new IllegalStateException("Expected exactly one CPS2DeploymentTrace");
        }
        CPS2DeploymentTrace trace = mapping.getTraces().get(0);
        if (trace.getCpsElements().size() != 1
                || trace.getDeploymentElements().size() != 1
                || trace.getCpsElements().get(0)
                    != mapping.getCps().getHostTypes().get(0).getInstances().get(0)
                || trace.getDeploymentElements().get(0) != host) {
            throw new IllegalStateException("V002 HostMapping trace is not canonical");
        }
    }

    public List<V002ObserverEvent> observationSnapshot() { return observer.snapshot(); }
}
