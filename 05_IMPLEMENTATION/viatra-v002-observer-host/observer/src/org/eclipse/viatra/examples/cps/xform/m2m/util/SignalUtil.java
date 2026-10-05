package org.eclipse.viatra.examples.cps.xform.m2m.util;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public final class SignalUtil {
    private static final Pattern WAIT_PATTERN =
        Pattern.compile("^waitForSignal\\((.*)\\)$");
    private static final Pattern SEND_PATTERN =
        Pattern.compile("^sendSignal\\((.*),(.*)\\)$");

    private SignalUtil() {}

    public static boolean isSend(String action) {
        return SEND_PATTERN.matcher(action).matches();
    }

    public static boolean isWait(String action) {
        return WAIT_PATTERN.matcher(action).matches();
    }

    public static String getAppId(String action) {
        return group(SEND_PATTERN, action, 1);
    }

    public static String getSignalId(String action) {
        String sendId = group(SEND_PATTERN, action, 2);
        return sendId == null ? group(WAIT_PATTERN, action, 1) : sendId;
    }

    private static String group(Pattern pattern, String action, int group) {
        Matcher matcher = pattern.matcher(action);
        return matcher.matches() ? matcher.group(group).trim() : null;
    }
}
