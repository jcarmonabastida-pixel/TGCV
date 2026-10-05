package org.tgcv.viatra.v002.observer.historical;

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
        return getGroupOfMatch(SEND_PATTERN, action, 1);
    }

    public static String getSignalId(String action) {
        String sendId = getGroupOfMatch(SEND_PATTERN, action, 2);
        if (sendId == null) {
            return getGroupOfMatch(WAIT_PATTERN, action, 1);
        }
        return sendId;
    }

    private static String getGroupOfMatch(Pattern pattern, String action, int group) {
        Matcher matcher = pattern.matcher(action);
        if (matcher.matches()) {
            return matcher.group(group).trim();
        }
        return null;
    }
}
