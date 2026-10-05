package org.tgcv.viatra.v002.observer;

import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import org.eclipse.viatra.query.patternlanguage.emf.util.PatternParserBuilder;
import org.eclipse.viatra.query.patternlanguage.emf.util.PatternParsingResults;
import org.eclipse.viatra.query.patternlanguage.emf.vql.Pattern;
import org.eclipse.viatra.query.runtime.api.IQuerySpecification;

public final class V002HistoricalVqlParserProbe {
    private V002HistoricalVqlParserProbe() {}

    public static void assertHistoricalVql(Path vqlFile) throws Exception {
        String text = new String(Files.readAllBytes(vqlFile), StandardCharsets.UTF_8);
        PatternParsingResults results = new PatternParserBuilder().parse(text);

        if (!results.validationOK()) {
            throw new IllegalStateException("Historical VQL validation failed: " + results);
        }

        List<String> names = new ArrayList<>();
        for (Pattern pattern : results.getPatterns()) {
            names.add(pattern.getName());
        }

        List<String> expected = Arrays.asList(
                "hostInstance", "cps2depTrace", "applicationInstance",
                "appInstanceWithStateMachine", "state", "transition",
                "action", "sendAction", "waitAction", "actionPair",
                "reachableHosts");

        if (!expected.equals(names)) {
            throw new IllegalStateException(
                    "Historical VQL pattern order/name surface changed: " + names);
        }

        List<String> specifications = new ArrayList<>();
        for (IQuerySpecification<?> specification : results.getQuerySpecifications()) {
            specifications.add(specification.getFullyQualifiedName());
        }

        if (specifications.size() != expected.size()) {
            throw new IllegalStateException(
                    "Expected " + expected.size()
                    + " public query specifications, got " + specifications.size());
        }
    }
}
