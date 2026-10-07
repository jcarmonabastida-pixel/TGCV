#!/usr/bin/env bash
set -euo pipefail

SOURCE_REPO="https://github.com/eclipse-viatra/org.eclipse.viatra.examples.git"
SOURCE_REV="eb68158a3d74581f69ccb8bc4f47673b12abdf85"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
DEST_ROOT="$SCRIPT_DIR/cps-models"
TMP_DIR="$(mktemp -d)"

cleanup() {
  rm -rf "$TMP_DIR"
}
trap cleanup EXIT

git clone --no-checkout --filter=blob:none "$SOURCE_REPO" "$TMP_DIR/source"
git -C "$TMP_DIR/source" sparse-checkout init --cone
git -C "$TMP_DIR/source" sparse-checkout set \
  cps/domains/org.eclipse.viatra.examples.cps.model \
  cps/domains/org.eclipse.viatra.examples.cps.deployment \
  cps/domains/org.eclipse.viatra.examples.cps.traceability \
  cps/transformations/org.eclipse.viatra.examples.cps.xform.m2m.util
git -C "$TMP_DIR/source" checkout --detach "$SOURCE_REV"

test "$(git -C "$TMP_DIR/source" rev-parse HEAD)" = "$SOURCE_REV"

for bundle in \
  org.eclipse.viatra.examples.cps.model \
  org.eclipse.viatra.examples.cps.deployment \
  org.eclipse.viatra.examples.cps.traceability \
  org.eclipse.viatra.examples.cps.xform.m2m.util
do
  if [[ "$bundle" == "org.eclipse.viatra.examples.cps.xform.m2m.util" ]]; then
    src="$TMP_DIR/source/cps/transformations/$bundle"
    dst="$DEST_ROOT/$bundle"

    test -d "$src/META-INF"
    test -f "$src/META-INF/MANIFEST.MF"
    test -f "$src/build.properties"
    test -d "$src/src"

    rm -rf "$dst/META-INF" "$dst/src" "$dst/build.properties"
    mkdir -p "$dst"

    cp -R "$src/META-INF" "$dst/META-INF"
    cp -R "$src/src" "$dst/src"
    sed -i \
      -e 's/org.eclipse.viatra.examples.cps.model;bundle-version="0.1.0"/org.eclipse.viatra.examples.cps.model;bundle-version="[2.1.0,3.0.0)"/' \
      -e 's/org.eclipse.viatra.examples.cps.deployment;bundle-version="0.1.0"/org.eclipse.viatra.examples.cps.deployment;bundle-version="[2.1.0,3.0.0)"/' \
      -e 's/org.eclipse.viatra.examples.cps.traceability;bundle-version="0.1.0"/org.eclipse.viatra.examples.cps.traceability;bundle-version="[2.1.0,3.0.0)"/' \
      "$dst/META-INF/MANIFEST.MF"
    mkdir -p "$dst/src/org/eclipse/viatra/examples/cps/xform/m2m/util"
    cat > "$dst/src/org/eclipse/viatra/examples/cps/xform/m2m/util/SignalUtil.java" <<'EOF'
package org.eclipse.viatra.examples.cps.xform.m2m.util;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public final class SignalUtil {
    private static final Pattern WAIT_PATTERN = Pattern.compile("^waitForSignal\\((.*)\\)$");
    private static final Pattern SEND_PATTERN = Pattern.compile("^sendSignal\\((.*),(.*)\\)$");

    private SignalUtil() {
    }

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
        return sendId == null ? getGroupOfMatch(WAIT_PATTERN, action, 1) : sendId;
    }

    private static String getGroupOfMatch(Pattern pattern, String action, int group) {
        Matcher matcher = pattern.matcher(action);
        return matcher.matches() ? matcher.group(group).trim() : null;
    }
}
EOF
    cp "$src/build.properties" "$dst/build.properties"
  else
    src="$TMP_DIR/source/cps/domains/$bundle"
    dst="$DEST_ROOT/$bundle"

    test -d "$src/META-INF"
    test -f "$src/META-INF/MANIFEST.MF"
    test -f "$src/build.properties"
    test -d "$src/model"
    test -d "$src/src"
    test -f "$src/plugin.xml"
    test -f "$src/plugin.properties"

    rm -rf "$dst/META-INF" "$dst/model" "$dst/src" "$dst/plugin.xml" "$dst/plugin.properties" "$dst/build.properties"
    mkdir -p "$dst"

    cp -R "$src/META-INF" "$dst/META-INF"
    cp -R "$src/model" "$dst/model"
    cp -R "$src/src" "$dst/src"
    sed -i \
      -e 's/org.eclipse.viatra.examples.cps.model;bundle-version="0.1.0"/org.eclipse.viatra.examples.cps.model;bundle-version="[2.1.0,3.0.0)"/' \
      -e 's/org.eclipse.viatra.examples.cps.deployment;bundle-version="0.1.0"/org.eclipse.viatra.examples.cps.deployment;bundle-version="[2.1.0,3.0.0)"/' \
      "$dst/META-INF/MANIFEST.MF"
    cp "$src/plugin.xml" "$dst/plugin.xml"
    cp "$src/plugin.properties" "$dst/plugin.properties"
    cp "$src/build.properties" "$dst/build.properties"
  fi
done
