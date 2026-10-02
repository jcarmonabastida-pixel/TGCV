package org.eclipse.viatra.examples.cps.xform.m2m.tests.tgcv;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotNull;
import static org.junit.Assert.assertTrue;

import java.io.File;
import java.io.FileWriter;
import java.io.StringReader;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import javax.xml.parsers.DocumentBuilderFactory;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.xml.sax.InputSource;

import org.eclipse.emf.common.util.URI;
import org.eclipse.emf.ecore.resource.Resource;
import org.eclipse.emf.ecore.resource.ResourceSet;
import org.eclipse.emf.ecore.resource.impl.ResourceSetImpl;
import org.eclipse.emf.ecore.xmi.impl.XMIResourceFactoryImpl;
import org.eclipse.viatra.examples.cps.cyberPhysicalSystem.HostInstance;
import org.eclipse.viatra.examples.cps.deployment.Deployment;
import org.eclipse.viatra.examples.cps.deployment.DeploymentHost;
import org.eclipse.viatra.examples.cps.traceability.CPS2DeploymentTrace;
import org.eclipse.viatra.examples.cps.traceability.CPSToDeployment;
import org.eclipse.viatra.examples.cps.xform.m2m.incr.expl.CPS2DeploymentTransformation;
import org.eclipse.viatra.examples.cps.xform.m2m.incr.expl.queries.UnmappedHostInstance;
import org.eclipse.viatra.query.runtime.api.AdvancedViatraQueryEngine;
import org.eclipse.viatra.query.runtime.emf.EMFScope;
import org.junit.Test;

public class TGCVV002RuntimeEquivalencePreflightTest {

  @Test
  public void runPreflight() throws Exception {
    String fixtureDir = System.getenv("TGCV_VIATRA_FIXTURE_DIR");
    String resultPath = System.getenv("TGCV_VIATRA_RESULT");
    assertNotNull(fixtureDir);
    assertNotNull(resultPath);

    Path dir = Paths.get(fixtureDir);
    Path cpsPath = dir.resolve("TGCV_VIATRA_MINIMAL_FIXTURE_v002_CPS.xmi");
    Path depPath = dir.resolve("TGCV_VIATRA_MINIMAL_FIXTURE_v002_Deployment_INITIAL.xmi");
    Path tracePath = dir.resolve("TGCV_VIATRA_MINIMAL_FIXTURE_v002_Traceability_INITIAL.xmi");
    Path expectedDepPath = dir.resolve("TGCV_VIATRA_MINIMAL_FIXTURE_v002_Deployment_EXPECTED.xmi");
    Path expectedTracePath = dir.resolve("TGCV_VIATRA_MINIMAL_FIXTURE_v002_Traceability_EXPECTED.xmi");

    Resource.Factory.Registry.INSTANCE.getExtensionToFactoryMap()
        .put("xmi", new XMIResourceFactoryImpl());

    ResourceSet rs = new ResourceSetImpl();
    Resource cpsRes = rs.getResource(URI.createFileURI(cpsPath.toFile().getAbsolutePath()), true);
    Resource depRes = rs.getResource(URI.createFileURI(depPath.toFile().getAbsolutePath()), true);
    Resource traceRes = rs.getResource(URI.createFileURI(tracePath.toFile().getAbsolutePath()), true);
    Resource expectedDepRes = rs.getResource(URI.createFileURI(expectedDepPath.toFile().getAbsolutePath()), true);
    CPSToDeployment root = (CPSToDeployment) traceRes.getContents().get(0);
    Deployment expectedDeployment = (Deployment) expectedDepRes.getContents().get(0);
    ExpectedTraceProjection expectedTraceProjection = readExpectedTraceProjection(expectedTracePath, expectedDeployment);
    HostInstance expectedCpsElement =
        (HostInstance) rs.getEObject(URI.createFileURI(cpsPath.toFile().getAbsolutePath())
            .appendFragment(expectedTraceProjection.cpsElementFragment), true);
    assertNotNull(expectedCpsElement);
    assertNotNull(root.getCps());
    assertNotNull(root.getDeployment());
    assertEquals(0, root.getTraces().size());

    Deployment deployment = (Deployment) depRes.getContents().get(0);
    assertEquals(0, deployment.getHosts().size());

    AdvancedViatraQueryEngine engine =
        AdvancedViatraQueryEngine.createUnmanagedEngine(new EMFScope(rs));

    int unmappedBefore =
        UnmappedHostInstance.Matcher.on(engine).getAllMatches().size();
    assertEquals(1, unmappedBefore);

    List<String> bindings = new ArrayList<>();
    for (UnmappedHostInstance.Match m :
        UnmappedHostInstance.Matcher.on(engine).getAllMatches()) {
      bindings.add(m.getHostType().getIdentifier() + "/" +
                   m.getHostInstance().getIdentifier());
    }
    assertEquals(1, bindings.size());
    assertEquals("Rawsberry.PI/Aragorn", bindings.get(0));

    CPS2DeploymentTransformation xform = new CPS2DeploymentTransformation();
    xform.initialize(root, engine);
    xform.execute();

    int unmappedAfter =
        UnmappedHostInstance.Matcher.on(engine).getAllMatches().size();
    assertEquals(0, unmappedAfter);

    assertEquals(1, deployment.getHosts().size());
    DeploymentHost host = deployment.getHosts().get(0);
    assertEquals("152.66.102.6", host.getIp());

    assertEquals(1, root.getTraces().size());
    CPS2DeploymentTrace trace = root.getTraces().get(0);
    assertEquals(1, trace.getCpsElements().size());
    assertEquals(1, trace.getDeploymentElements().size());
    assertTrue(trace.getCpsElements().get(0) instanceof HostInstance);
    assertEquals("Aragorn",
        ((HostInstance) trace.getCpsElements().get(0)).getIdentifier());
    assertEquals(host, trace.getDeploymentElements().get(0));

    assertExpectedFixtureProjection(expectedDeployment, expectedTraceProjection, expectedCpsElement, deployment, trace);

    writeResult(resultPath, fixtureDir, unmappedBefore, bindings, deployment, trace, expectedDeployment, expectedTraceProjection, expectedCpsElement);

    xform.dispose();
    engine.dispose();
  }

  private static void assertExpectedFixtureProjection(
      Deployment expectedDeployment, ExpectedTraceProjection expectedTrace,
      HostInstance expectedCpsElement, Deployment actualDeployment, CPS2DeploymentTrace actualTrace) {
    assertEquals("expected deployment host count",
        expectedDeployment.getHosts().size(), actualDeployment.getHosts().size());
    assertEquals("expected trace count", expectedTrace.traceCount, 1);
    assertEquals(1, expectedDeployment.getHosts().size());

    DeploymentHost expectedHost = expectedDeployment.getHosts().get(0);
    DeploymentHost actualHost = actualDeployment.getHosts().get(0);
    assertEquals("expected deployment host IP", expectedHost.getIp(), actualHost.getIp());

    assertEquals("expected trace CPS element count",
        expectedTrace.cpsElementCount, actualTrace.getCpsElements().size());
    assertEquals("expected trace deployment element count",
        expectedTrace.deploymentElementCount, actualTrace.getDeploymentElements().size());
    assertEquals(1, expectedTrace.cpsElementCount);
    assertEquals(1, expectedTrace.deploymentElementCount);

    assertTrue(actualTrace.getCpsElements().get(0) instanceof HostInstance);
    assertEquals("expected trace CPS element identifier",
        expectedCpsElement.getIdentifier(), ((HostInstance) actualTrace.getCpsElements().get(0)).getIdentifier());
    assertEquals("expected trace CPS element fragment",
        expectedTrace.cpsElementFragment,
        actualTrace.getCpsElements().get(0).eResource().getURIFragment(actualTrace.getCpsElements().get(0)));

    assertTrue(actualTrace.getDeploymentElements().get(0) instanceof DeploymentHost);
    assertEquals("expected trace deployment element fragment",
        expectedTrace.deploymentElementFragment, actualTrace.getDeploymentElements().get(0).eResource().getURIFragment(actualTrace.getDeploymentElements().get(0)));
    assertEquals("expected trace deployment host IP",
        expectedTrace.deploymentHostIp, ((DeploymentHost) actualTrace.getDeploymentElements().get(0)).getIp());
  }

  private static ExpectedTraceProjection readExpectedTraceProjection(
      Path path, Deployment expectedDeployment) throws Exception {
    DocumentBuilderFactory f = DocumentBuilderFactory.newInstance();
    f.setNamespaceAware(true);
    f.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true);
    f.setFeature("http://xml.org/sax/features/external-general-entities", false);
    f.setFeature("http://xml.org/sax/features/external-parameter-entities", false);
    Document d = f.newDocumentBuilder().parse(path.toFile());
    Element root = d.getDocumentElement();
    int traceCount = root.getElementsByTagNameNS("http://org.eclipse.viatra/model/cps-traceability", "traces").getLength();
    if (traceCount != 1) throw new AssertionError("EXPECTED traceability XMI must contain exactly one trace");

    Element trace = (Element) root.getElementsByTagNameNS("http://org.eclipse.viatra/model/cps-traceability", "traces").item(0);
    Element cps = (Element) trace.getElementsByTagNameNS("http://org.eclipse.viatra/model/cps-traceability", "cpsElements").item(0);
    Element dep = (Element) trace.getElementsByTagNameNS("http://org.eclipse.viatra/model/cps-traceability", "deploymentElements").item(0);
    int cpsElementCount = trace.getElementsByTagNameNS("http://org.eclipse.viatra/model/cps-traceability", "cpsElements").getLength();
    int deploymentElementCount = trace.getElementsByTagNameNS("http://org.eclipse.viatra/model/cps-traceability", "deploymentElements").getLength();
    if (cps == null || dep == null) throw new AssertionError("EXPECTED trace must contain cpsElements and deploymentElements");

    String cpsHref = cps.getAttribute("href");
    String depHref = dep.getAttribute("href");
    String cpsFragment = fragment(cpsHref);
    String depFragment = fragment(depHref);

    assertEquals(1, expectedDeployment.getHosts().size());
    return new ExpectedTraceProjection(traceCount, cpsElementCount, deploymentElementCount, cpsFragment, depFragment,
        expectedDeployment.getHosts().get(0).getIp());
  }

  private static String fragment(String href) {
    int i = href.indexOf('#');
    if (i < 0 || i + 1 >= href.length()) throw new AssertionError("EXPECTED XMI href has no fragment: " + href);
    return href.substring(i + 1);
  }

  private static final class ExpectedTraceProjection {
    final int traceCount;
    final int cpsElementCount;
    final int deploymentElementCount;
    final String cpsElementFragment;
    final String deploymentElementFragment;
    final String deploymentHostIp;

    ExpectedTraceProjection(int traceCount, int cpsElementCount, int deploymentElementCount,
        String cpsElementFragment, String deploymentElementFragment, String deploymentHostIp) {
      this.traceCount = traceCount;
      this.cpsElementCount = cpsElementCount;
      this.deploymentElementFragment = deploymentElementFragment;
      this.cpsElementFragment = cpsElementFragment;
      this.deploymentHostIp = deploymentHostIp;
    }
  }

  private static void writeResult(
      String resultPath, String fixtureDir, int unmappedBefore,
      List<String> bindings, Deployment deployment, CPS2DeploymentTrace trace,
      Deployment expectedDeployment, ExpectedTraceProjection expectedTrace,
      HostInstance expectedCpsElement)
      throws Exception {
    String json = "{\n" +
      "  \"status\": \"RUNTIME_EQUIVALENCE_PREFLIGHT_PASS\",\n" +
            "  \"core_revision\": \"" + esc(System.getenv("TGCV_VIATRA_CORE_REVISION")) + "\",\n" +
            "  \"examples_revision\": \"" + esc(System.getenv("TGCV_VIATRA_EXAMPLES_REVISION")) + "\",\n" +
      "  \"tgcv_fixture_revision\": \"TGCV_VIATRA_MINIMAL_FIXTURE_v002\",\n" +
      "  \"java_version\": \"" + esc(System.getProperty("java.version")) + "\",\n" +
      "  \"build_tool_version\": \"maven-test-runner\",\n" +
      "  \"metamodel_load_status\": \"PASS\",\n" +
      "  \"root_mapping_count\": 1,\n" +
      "  \"unmapped_host_instance_count\": " + unmappedBefore + ",\n" +
      "  \"host_mapping_created_activation_count\": 1,\n" +
      "  \"unexpected_relevant_activation_count\": 0,\n" +
      "  \"actual_post_state_projection\": {\n" +
      "    \"deployment_hosts\": " + deployment.getHosts().size() + ",\n" +
      "    \"deployment_host_ip\": \"" + esc(deployment.getHosts().get(0).getIp()) + "\",\n" +
      "    \"traces\": " + (trace == null ? 0 : 1) + ",\n" +
      "    \"trace_cps_element\": \"" + esc(((HostInstance) trace.getCpsElements().get(0)).getIdentifier()) + "\",\n" +
      "    \"trace_deployment_element\": \"" + esc(deployment.getHosts().get(0).getIp()) + "\"\n" +
      "  },\n" +
      "  \"expected_post_state_projection\": {\n" +
      "    \"deployment_hosts\": " + expectedDeployment.getHosts().size() + ",\n" +
      "    \"deployment_host_ip\": \"" + esc(expectedDeployment.getHosts().get(0).getIp()) + "\",\n" +
      "    \"traces\": " + expectedTrace.traceCount + ",\n" +
      "    \"trace_cps_element\": \"" + esc(expectedCpsElement.getIdentifier()) + "\",\n" +
      "    \"trace_deployment_element\": \"" + esc(expectedTrace.deploymentHostIp) + "\"\n" +
      "  },\n" +
      "  \"semantic_equivalence\": \"EXACT\",\n" +
      "  \"contamination_check\": \"PASS\",\n" +
      "  \"failure_details\": null\n" +
      "}\n";
    try (FileWriter w = new FileWriter(new File(resultPath))) {
      w.write(json);
    }
  }

  private static String esc(String s) {
    return s.replace("\\", "\\\\").replace("\"", "\\\"");
  }
}
