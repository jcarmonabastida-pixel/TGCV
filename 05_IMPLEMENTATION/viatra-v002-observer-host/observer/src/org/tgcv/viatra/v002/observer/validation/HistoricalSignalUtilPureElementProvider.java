package org.tgcv.viatra.v002.observer.validation;

import java.lang.reflect.Method;
import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

import org.eclipse.viatra.examples.cps.xform.m2m.util.SignalUtil;
import org.eclipse.viatra.query.patternlanguage.emf.validation.whitelist.IPureElementProvider;
import org.eclipse.viatra.query.patternlanguage.emf.validation.whitelist.PureWhitelist.PureElement;

public final class HistoricalSignalUtilPureElementProvider implements IPureElementProvider {

    @Override
    public Collection<PureElement> getPureElements() {
        List<PureElement> elements = new ArrayList<>();
        for (String methodName : new String[] { "isSend", "isWait", "getAppId", "getSignalId" }) {
            try {
                Method method = SignalUtil.class.getMethod(methodName, String.class);
                elements.add(pureMethod(method));
            } catch (NoSuchMethodException e) {
                throw new IllegalStateException(
                        "Historical SignalUtil method is missing: " + methodName, e);
            }
        }
        return elements;
    }
}
