package org.tgcv.viatra.v002.observer;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;

/**
 * Execution-plan boundary for the historical V002 batch transformation.
 *
 * This class deliberately contains no VIATRA engine access yet. It freezes the
 * historical rule order at the executor boundary so later engine wiring cannot
 * silently reorder the transformation.
 */
public final class V002SerialExecutor {

    public static final List<String> HISTORICAL_RULE_ORDER =
        Collections.unmodifiableList(Arrays.asList(
            "HostRule",
            "ApplicationRule",
            "StateMachineRule",
            "StateRule",
            "TransitionRule",
            "ActionRule"));

    public List<String> historicalRuleOrder() {
        return HISTORICAL_RULE_ORDER;
    }

    public void assertHistoricalRuleOrder() {
        if (!HISTORICAL_RULE_ORDER.equals(Arrays.asList(
                "HostRule",
                "ApplicationRule",
                "StateMachineRule",
                "StateRule",
                "TransitionRule",
                "ActionRule"))) {
            throw new IllegalStateException("V002 historical rule order has changed");
        }
    }
}
