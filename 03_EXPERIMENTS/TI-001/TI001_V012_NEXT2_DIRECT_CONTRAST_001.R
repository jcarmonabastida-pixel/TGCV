#!/usr/bin/env Rscript

# TI001 V012 NEXT2 — direct pre-specified informative-vs-null interaction contrast
# Reuses the already executed scientific result and immutable fixture.
# No scientific execution is performed by this script.
# Requires R >= 4.2 and packages: jsonlite, lme4

suppressPackageStartupMessages({
  library(jsonlite)
  library(lme4)
})

args <- commandArgs(trailingOnly=TRUE)
if (length(args) != 3) {
  stop("Usage: Rscript TI001_V012_NEXT2_DIRECT_CONTRAST_001.R <result_json> <fixture_dir> <output_json>")
}

result_path <- args[[1]]
fixture_dir <- args[[2]]
output_path <- args[[3]]

EXPECTED_RESULT_SHA <- "4d63933cd508ce1749db2a1210caf6c49fe5233c18185fce87ed7d9fcdf1c103"
EXPECTED_COUNT <- 23040L
VALIDITY <- "VALID"
CONDITIONS <- c("INFORMATIVE","UNINFORMATIVE_NULL")
ACTIONS <- c("A","B","C","D")
SLOTS <- c("slot_1","slot_2","slot_3","slot_4")

raw <- readLines(result_path, encoding="UTF-8", warn=FALSE)
result <- fromJSON(paste(raw, collapse="\n"), simplifyDataFrame=FALSE)

stopifnot(identical(result$decision_count, EXPECTED_COUNT))
stopifnot(isTRUE(result$scientific_execution))
stopifnot(identical(result$system_prompt_sha256,
  "660002f6506648fd0bfd703751f8996fae9fe0aaed3a48defbe78b2382c94122"))

decisions <- result$decisions
if (length(decisions) != EXPECTED_COUNT) stop("Unexpected decision count")

fixture_files <- list.files(fixture_dir, pattern="^SHARD_[0-9]+\\.json$", full.names=TRUE)
if (length(fixture_files) != 24L) stop("Expected exactly 24 fixture shards")

fixture_units <- unlist(lapply(sort(fixture_files), function(p)
  fromJSON(paste(readLines(p, encoding="UTF-8", warn=FALSE), collapse="\n"),
           simplifyDataFrame=FALSE)), recursive=FALSE)

if (length(fixture_units) != EXPECTED_COUNT) stop("Unexpected fixture unit count")
fixture_by_id <- setNames(fixture_units, vapply(fixture_units, function(x) x$id, character(1)))
if (length(fixture_by_id) != EXPECTED_COUNT) stop("Fixture IDs are not unique")

valid <- Filter(function(x) identical(x$validity, VALIDITY), decisions)

rows <- vector("list", length(valid) * 4L)
j <- 1L

for (d in valid) {
  if (!(d$mapping_condition %in% CONDITIONS)) next

  fu <- fixture_by_id[[d$unit_id]]
  if (is.null(fu)) stop(paste("Missing fixture unit:", d$unit_id))

  if (!identical(as.integer(fu$d), as.integer(d$d)) ||
      !identical(as.integer(fu$o), as.integer(d$o)) ||
      !identical(as.character(fu$m), as.character(d$mapping_condition)) ||
      !identical(as.integer(fu$p), as.integer(d$presentation)) ||
      !identical(as.integer(fu$k), as.integer(d$permutation_index)) ||
      !identical(as.integer(fu$r), as.integer(d$replicate))) {
    stop(paste("Result/fixture traceability mismatch:", d$unit_id))
  }

  f <- fu$f
  selected <- d$parsed_action
  if (!(selected %in% ACTIONS)) stop(paste("Invalid parsed action:", d$unit_id))

  for (a in ACTIONS) {
    slot <- unname(unlist(f[a]))
    if (length(slot) != 1L || !(slot %in% SLOTS)) {
      stop(paste("Invalid future assignment:", d$unit_id, a))
    }

    rows[[j]] <- data.frame(
      unit_id=d$unit_id,
      selected=as.integer(selected == a),
      action_identity=factor(a, levels=ACTIONS),
      future_assignment=factor(slot, levels=SLOTS),
      presentation=factor(d$presentation),
      mapping_condition=factor(d$mapping_condition, levels=CONDITIONS),
      operationalisation=factor(paste0("O", d$o)),
      domain=factor(paste0("D", d$d)),
      stringsAsFactors=FALSE
    )
    j <- j + 1L
  }
}

rows <- rows[seq_len(j-1L)]
dat <- do.call(rbind, rows)
dat$unit_id <- factor(dat$unit_id)

# Direct primary contrast:
# Does the action-identity × future-assignment interaction differ between
# INFORMATIVE and matched UNINFORMATIVE_NULL conditions?
#
# Full model contains the three-way interaction.
# Reduced model removes only that three-way interaction.
# The likelihood-ratio test therefore tests the pre-specified difference
# between the two condition-specific interaction vectors.

fit_full <- glmer(
  selected ~ action_identity * future_assignment * mapping_condition +
    presentation + operationalisation + domain +
    (1 | unit_id),
  data=dat, family=binomial(link="logit"),
  control=glmerControl(optimizer="bobyqa", optCtrl=list(maxfun=200000))
)

fit_reduced <- glmer(
  selected ~ action_identity * future_assignment +
    action_identity:mapping_condition +
    future_assignment:mapping_condition +
    mapping_condition +
    presentation + operationalisation + domain +
    (1 | unit_id),
  data=dat, family=binomial(link="logit"),
  control=glmerControl(optimizer="bobyqa", optCtrl=list(maxfun=200000))
)

lrt <- anova(fit_reduced, fit_full, test="Chisq")

# Report the nine three-way interaction coefficients. These describe the
# direction of the condition difference for the action × assignment cells.
b <- fixef(fit_full)
three_way_terms <- grep(
  "^action_identity.*:future_assignment.*:mapping_condition",
  names(b), value=TRUE
)

se <- sqrt(diag(vcov(fit_full)))
z <- b / se
p <- 2 * pnorm(abs(z), lower.tail=FALSE)

three_way <- data.frame(
  term=three_way_terms,
  estimate=unname(b[three_way_terms]),
  std_error=unname(se[three_way_terms]),
  z=unname(z[three_way_terms]),
  p_value=unname(p[three_way_terms]),
  row.names=NULL
)

out <- list(
  artifact_id="TI001_V012_NEXT2_DIRECT_CONTRAST_RESULT_001",
  status="DIRECT_PRIMARY_CONTRAST_COMPLETE",
  analysis_specification="TI001_V012_NEXT2_PRIMARY_ANALYSIS_SPECIFICATION_001",
  authorization_gate="TI001_V012_NEXT2_PRIMARY_ANALYSIS_AUTHORIZATION_GATE_001",
  result_sha256=EXPECTED_RESULT_SHA,
  fixture_dir_binding="TI001_V012_NEXT2_FIXTURE_REGENERATED_001",
  fixture_unit_traceability="VALIDATED_FOR_ALL_VALID_DECISIONS_IN_TARGET_CONDITIONS",
  conditions_compared=CONDITIONS,
  valid_decisions_total=length(valid),
  valid_decisions_compared=sum(vapply(valid, function(x) x$mapping_condition %in% CONDITIONS, logical(1))),
  model="mixed-effects logistic regression",
  random_effects=list("decision_unit"),
  full_model="selected ~ action_identity * future_assignment * mapping_condition + presentation + operationalisation + domain + (1 | unit_id)",
  reduced_model="selected ~ action_identity * future_assignment + action_identity:mapping_condition + future_assignment:mapping_condition + mapping_condition + presentation + operationalisation + domain + (1 | unit_id)",
  primary_contrast="INFORMATIVE versus UNINFORMATIVE_NULL difference in action_identity × future_assignment interaction",
  three_way_interaction=three_way,
  direct_interaction_lrt=as.data.frame(lrt),
  replication_status="NOT_ASSESSABLE_FROM_SINGLE_EXECUTION",
  interpretation_boundary="No TGCV-wide confirmation/falsification, no value/causal claim, no Transformational Intelligence claim.",
  scientific_execution_performed=FALSE,
  secondary_mi_contrast_status="NOT_EXECUTED"
)

write(toJSON(out, auto_unbox=TRUE, pretty=TRUE, null="null"), output_path)
