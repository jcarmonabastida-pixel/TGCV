package org.tgcv.viatra.v002.observer.fixture;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Objects;

import javax.xml.parsers.DocumentBuilderFactory;
import org.w3c.dom.Document;
import org.w3c.dom.Element;

import org.eclipse.emf.common.util.URI;
import org.eclipse.emf.ecore.EObject;
import org.eclipse.emf.ecore.EPackage;
import org.eclipse.emf.ecore.resource.Resource;
import org.eclipse.emf.ecore.resource.ResourceSet;
import org.eclipse.emf.ecore.resource.impl.ResourceSetImpl;
import org.eclipse.emf.ecore.xmi.impl.XMIResourceFactoryImpl;
import org.eclipse.viatra.examples.cps.cyberPhysicalSystem.CyberPhysicalSystemPackage;
import org.eclipse.viatra.examples.cps.deployment.DeploymentPackage;
import org.eclipse.viatra.examples.cps.traceability.TraceabilityPackage;

public final class V002FixtureLoader {

    public static final String CPS_SHA256 =
        "8d432da0d3fd49ba88f809611f222614ef588809691e66bcc954a4cd509f66bb";
    public static final String DEPLOYMENT_INITIAL_SHA256 =
        "fea5bc84929e99145ebe07f4eabeb1d04eaceb805b3e35d7975aff793bd9af8e";
    public static final String DEPLOYMENT_EXPECTED_SHA256 =
        "92addffad49e828a8c3c7f0ca7b00c870f00e9c419415c3b997e06cc36b0e966";
    public static final String TRACEABILITY_INITIAL_SHA256 =
        "1ce4c0c69f324e43d87b41dee2561a55668d06c815294919011a2d5c3d1d88c1";
    public static final String TRACEABILITY_EXPECTED_SHA256 =
        "29ebb291e72ff061618aa809af2e16527464f2475e21bfe558de00bd36de33e3";

    public static final String CPS_NS_URI =
        "http://org.eclipse.viatra/model/cps";
    public static final String DEPLOYMENT_NS_URI =
        "http://org.eclipse.viatra/model/deployment";
    public static final String TRACEABILITY_NS_URI =
        "http://org.eclipse.viatra/model/cps-traceability";

    public static final class FixtureSet {
        private final Path cps;
        private final Path deploymentInitial;
        private final Path deploymentExpected;
        private final Path traceabilityInitial;
        private final Path traceabilityExpected;

        public FixtureSet(Path cps, Path deploymentInitial, Path deploymentExpected,
                          Path traceabilityInitial, Path traceabilityExpected) {
            this.cps = Objects.requireNonNull(cps);
            this.deploymentInitial = Objects.requireNonNull(deploymentInitial);
            this.deploymentExpected = Objects.requireNonNull(deploymentExpected);
            this.traceabilityInitial = Objects.requireNonNull(traceabilityInitial);
            this.traceabilityExpected = Objects.requireNonNull(traceabilityExpected);
        }

        public Path cps() { return cps; }
        public Path deploymentInitial() { return deploymentInitial; }
        public Path deploymentExpected() { return deploymentExpected; }
        public Path traceabilityInitial() { return traceabilityInitial; }
        public Path traceabilityExpected() { return traceabilityExpected; }
    }

    public static final class SemanticFixtureSet {
        private final ResourceSet resourceSet;
        private final Resource cps;
        private final Resource deploymentInitial;
        private final Resource deploymentExpected;
        private final Resource traceabilityInitial;
        private final Path traceabilityExpected;

        private SemanticFixtureSet(ResourceSet resourceSet, Resource cps,
                                    Resource deploymentInitial, Resource deploymentExpected,
                                    Resource traceabilityInitial, Resource traceabilityExpected) {
            this.resourceSet = resourceSet;
            this.cps = cps;
            this.deploymentInitial = deploymentInitial;
            this.deploymentExpected = deploymentExpected;
            this.traceabilityInitial = traceabilityInitial;
            this.traceabilityExpected = traceabilityExpected;
        }

        public ResourceSet resourceSet() { return resourceSet; }
        public Resource cps() { return cps; }
        public Resource deploymentInitial() { return deploymentInitial; }
        public Resource deploymentExpected() { return deploymentExpected; }
        public Resource traceabilityInitial() { return traceabilityInitial; }
        public Path traceabilityExpected() { return traceabilityExpected; }
    }

    public FixtureSet bind(Path cps, Path deploymentInitial, Path deploymentExpected,
                           Path traceabilityInitial, Path traceabilityExpected) {
        return new FixtureSet(cps, deploymentInitial, deploymentExpected,
            traceabilityInitial, traceabilityExpected);
    }

    public void verifyBytes(FixtureSet fixtures) throws IOException {
        verify(fixtures.cps(), CPS_SHA256);
        verify(fixtures.deploymentInitial(), DEPLOYMENT_INITIAL_SHA256);
        verify(fixtures.deploymentExpected(), DEPLOYMENT_EXPECTED_SHA256);
        verify(fixtures.traceabilityInitial(), TRACEABILITY_INITIAL_SHA256);
        verify(fixtures.traceabilityExpected(), TRACEABILITY_EXPECTED_SHA256);
    }

    public SemanticFixtureSet loadSemantic(FixtureSet fixtures) throws IOException {
        Objects.requireNonNull(fixtures);
        verifyBytes(fixtures);
        registerMetamodels();

        ResourceSet resourceSet = new ResourceSetImpl();
        resourceSet.getPackageRegistry().put(CPS_NS_URI, CyberPhysicalSystemPackage.eINSTANCE);
        resourceSet.getPackageRegistry().put(DEPLOYMENT_NS_URI, DeploymentPackage.eINSTANCE);
        resourceSet.getPackageRegistry().put(TRACEABILITY_NS_URI, TraceabilityPackage.eINSTANCE);
        resourceSet.getResourceFactoryRegistry().getExtensionToFactoryMap()
            .put("xmi", new XMIResourceFactoryImpl());

        Resource cps = load(resourceSet, fixtures.cps(), CPS_NS_URI);
        Resource deploymentInitial =
            load(resourceSet, fixtures.deploymentInitial(), DEPLOYMENT_NS_URI);
        Resource deploymentExpected =
            load(resourceSet, fixtures.deploymentExpected(), DEPLOYMENT_NS_URI);
        Resource traceabilityInitial =
            load(resourceSet, fixtures.traceabilityInitial(), TRACEABILITY_NS_URI);
        validateExpectedTraceabilityProjection(
            fixtures.traceabilityExpected(), deploymentExpected);

        org.eclipse.emf.ecore.util.EcoreUtil.resolveAll(resourceSet);

        return new SemanticFixtureSet(resourceSet, cps, deploymentInitial,
            deploymentExpected, traceabilityInitial, fixtures.traceabilityExpected());
    }

    private void validateExpectedTraceabilityProjection(Path path,
            Resource expectedDeployment) throws IOException {
        try {
            DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
            factory.setNamespaceAware(true);
            factory.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true);
            factory.setFeature("http://xml.org/sax/features/external-general-entities", false);
            factory.setFeature("http://xml.org/sax/features/external-parameter-entities", false);
            Document document = factory.newDocumentBuilder().parse(path.toFile());
            Element root = document.getDocumentElement();
            if (root.getElementsByTagNameNS("*", "traces").getLength() != 1) {
                throw new IllegalStateException(
                    "EXPECTED traceability XMI must contain exactly one trace: " + path);
            }
            Element trace = (Element) root.getElementsByTagNameNS("*", "traces").item(0);
            Element cps = (Element) trace.getElementsByTagNameNS("*", "cpsElements").item(0);
            Element deployment = (Element) trace.getElementsByTagNameNS("*", "deploymentElements").item(0);
            if (cps == null || deployment == null
                    || cps.getAttribute("href").indexOf('#') < 0
                    || deployment.getAttribute("href").indexOf('#') < 0) {
                throw new IllegalStateException(
                    "EXPECTED traceability XMI must contain valid cps/deployment hrefs: " + path);
            }
            if (expectedDeployment.getContents().isEmpty()) {
                throw new IllegalStateException(
                    "EXPECTED deployment fixture has no root object: " + expectedDeployment.getURI());
            }
        } catch (IOException e) {
            throw e;
        } catch (Exception e) {
            throw new IllegalStateException(
                "Unable to validate EXPECTED traceability projection: " + path, e);
        }
    }

    private void registerMetamodels() {
        CyberPhysicalSystemPackage.eINSTANCE.eClass();
        DeploymentPackage.eINSTANCE.eClass();
        TraceabilityPackage.eINSTANCE.eClass();

        requirePackage(CPS_NS_URI);
        requirePackage(DEPLOYMENT_NS_URI);
        requirePackage(TRACEABILITY_NS_URI);
    }

    private void requirePackage(String nsUri) {
        if (EPackage.Registry.INSTANCE.getEPackage(nsUri) == null) {
            throw new IllegalStateException("Metamodel not registered: " + nsUri);
        }
    }

    private Resource load(ResourceSet resourceSet, Path path, String expectedNsUri)
        throws IOException {
        Resource resource = resourceSet.getResource(
            URI.createFileURI(path.toAbsolutePath().toString()), true);

        if (resource.getContents().isEmpty()) {
            throw new IllegalStateException("Fixture has no root object: " + path);
        }

        EObject root = resource.getContents().get(0);
        if (root.eClass().getEPackage() == null
            || !expectedNsUri.equals(root.eClass().getEPackage().getNsURI())) {
            throw new IllegalStateException(
                "Unexpected fixture metamodel: " + path + " expected=" + expectedNsUri);
        }

        return resource;
    }

    private void verify(Path path, String expectedSha256) throws IOException {
        byte[] bytes = Files.readAllBytes(path);
        String actual = sha256(bytes);
        if (!expectedSha256.equals(actual)) {
            throw new IllegalStateException(
                "Fixture SHA-256 mismatch: " + path + " expected=" +
                expectedSha256 + " actual=" + actual);
        }
    }

    private String sha256(byte[] bytes) {
        try {
            MessageDigest digest = MessageDigest.getInstance("SHA-256");
            byte[] hash = digest.digest(bytes);
            StringBuilder hex = new StringBuilder(hash.length * 2);
            for (byte value : hash) {
                hex.append(String.format("%02x", value & 0xff));
            }
            return hex.toString();
        } catch (NoSuchAlgorithmException e) {
            throw new IllegalStateException("SHA-256 unavailable", e);
        }
    }
}
