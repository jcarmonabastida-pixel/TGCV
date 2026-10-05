package org.tgcv.viatra.v002.observer;

import org.eclipse.viatra.examples.cps.cyberPhysicalSystem.HostInstance;
import org.eclipse.viatra.examples.cps.deployment.DeploymentHost;
import org.eclipse.viatra.examples.cps.traceability.CPS2DeploymentTrace;
import org.eclipse.viatra.examples.cps.traceability.CPSToDeployment;
import org.eclipse.viatra.query.runtime.api.IPatternMatch;
import org.eclipse.viatra.transformation.evm.api.Activation;

final class V002FixtureStateCapture implements V002StateCapture {
    private final CPSToDeployment mapping;

    V002FixtureStateCapture(CPSToDeployment mapping) { this.mapping = mapping; }

    @Override
    public String capturePreState(Activation<?> activation) {
        HostInstance host = hostFrom(activation);
        return V002CanonicalStateSerializer.sha256(
            V002CanonicalStateSerializer.serialize(
                host.getIdentifier(), host.getNodeIp(), "", false));
    }

    @Override
    public String capturePostState(Activation<?> activation) {
        HostInstance host = hostFrom(activation);
        DeploymentHost deploymentHost = null;
        boolean tracePresent = false;
        for (DeploymentHost candidate : mapping.getDeployment().getHosts()) {
            if (host.getNodeIp().equals(candidate.getIp())) {
                deploymentHost = candidate;
                break;
            }
        }
        for (CPS2DeploymentTrace trace : mapping.getTraces()) {
            if (trace.getCpsElements().contains(host)) {
                tracePresent = true;
                break;
            }
        }
        if (deploymentHost == null || !tracePresent) {
            throw new IllegalStateException("V002 POST state missing HostMapping output");
        }
        return V002CanonicalStateSerializer.sha256(
            V002CanonicalStateSerializer.serialize(
                host.getIdentifier(), host.getNodeIp(), deploymentHost.getIp(), true));
    }

    private HostInstance hostFrom(Activation<?> activation) {
        if (!(activation.getAtom() instanceof IPatternMatch)) {
            throw new IllegalStateException("V002 activation atom is not an IPatternMatch");
        }
        Object host = ((IPatternMatch) activation.getAtom()).get("hostInstance");
        if (!(host instanceof HostInstance)) {
            throw new IllegalStateException(
                "V002 activation is not a HostRule HostInstance match");
        }
        return (HostInstance) host;
    }
}
