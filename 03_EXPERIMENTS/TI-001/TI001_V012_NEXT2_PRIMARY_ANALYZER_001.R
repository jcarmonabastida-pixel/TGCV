#!/usr/bin/env Rscript

# TI001 V012 NEXT2 — primary pre-specified analysis
# Requires R >= 4.2 and packages: jsonlite, lme4
# This script does not modify the scientific result or fixture.

suppressPackageStartupMessages({
  library(jsonlite)
  library(lme4)
})

args <- commandArgs(trailingOnly = TRUE)
if (length(args) != 3) {
  stop("Usage: Rscript TI001_V012_NEXT2_PRIMARY_ANALYZER_001.R <result_json> <fixture_dir> <output_json>")
}

result_path <- args[[1]]
fixture_dir <- args[[2]]
output_path <- args[[3]]

EXPECTED_RESULT_SHA <- "4d63933cd508ce1749db2a1210caf6c49fe5233c18185fce87ed7d9fcdf1c103"
EXPECTED_COUNT <- 23040L
VALIDITY <- "VALID"
CONDITIONS <- c("INFORMATIVE", "SURFACE_PERMUTED", "UNINFORMATIVE_NULL", "CONTRADICTORY")
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

# Reconstruct presented future assignment from the immutable fixture.
fixture_files <- list.files(fixture_dir, pattern="^SHARD_[0-9]+\\.json$", full.names=TRUE)
if (length(fixture_files) != 24L) stop("Expected exactly 24 fixture shards")
fixture_units <- unlist(lapply(sort(fixture_files), function(p)
  fromJSON(paste(readLines(p, encoding="UTF-8", warn=FALSE), collapse="\\n"),
           simplifyDataFrame=FALSE)), recursive=FALSE)
if (length(fixture_units) != EXPECTED_COUNT) stop("Unexpected fixture unit count")
fixture_by_id <- setNames(fixture_units, vapply(fixture_units, function(x) x$id, character(1)))
if (length(fixture_by_id) != EXPECTED_COUNT) stop("Fixture IDs are not unique")

valid <- Filter(function(x) identical(x$validity, VALIDITY), decisions)
invalid_count <- length(decisions) - length(valid)

rows <- vector("list", length(valid) * 4L)
j <- 1L

for (d in valid) {
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
      unit_id = d$unit_id,
      selected = as.integer(selected == a),
      action_identity = factor(a, levels=ACTIONS),
      future_assignment = factor(slot, levels=SLOTS),
      presentation = factor(d$presentation),
      mapping_condition = factor(d$mapping_condition, levels=CONDITIONS),
      operationalisation = factor(paste0("O", d$o)),
      domain = factor(paste0("D", d$d)),
      stringsAsFactors=FALSE
    )
    j <- j + 1L
  }
}

dat <- do.call(rbind, rows)
dat$unit_id <- factor(dat$unit_id)

# Primary model: action identity × presented future assignment.
# One random intercept per decision unit is retained exactly as specified.
fit_full <- glmer(
  selected ~ action_identity * future_assignment +
    presentation + mapping_condition + operationalisation + domain +
    (1 | unit_id),
  data=dat, family=binomial(link="logit"),
  control=glmerControl(optimizer="bobyqa", optCtrl=list(maxfun=200000))
)

# Matched informative/null comparison:
# fit the same primary model separately within each condition, then
# compare the estimated action × future-assignment interaction vectors.
fit_condition <- function(cond) {
  dd <- droplevels(dat[dat$mapping_condition == cond, ])
  glmer(
    selected ~ action_identity * future_assignment +
      presentation + operationalisation + domain +
      (1 | unit_id),
    data=dd, family=binomial(link="logit"),
    control=glmerControl(optimizer="bobyqa", optCtrl=list(maxfun=200000))
  )
}

fit_inf <- fit_condition("INFORMATIVE")
fit_null <- fit_condition("UNINFORMATIVE_NULL")

interaction_terms <- grep("^action_identity.*:future_assignment",
                           names(fixef(fit_inf)), value=TRUE)

coef_table <- function(fit) {
  b <- fixef(fit)
  se <- sqrt(diag(vcov(fit)))
  z <- b / se
  p <- 2 * pnorm(abs(z), lower.tail=FALSE)
  out <- data.frame(term=names(b), estimate=b, std_error=se,
                    z=z, p_value=p, row.names=NULL)
  out[out$term %in% interaction_terms, , drop=FALSE]
}

inf_tab <- coef_table(fit_inf)
null_tab <- coef_table(fit_null)

# A direct omnibus interaction test within each condition.
reduced_condition <- function(cond) {
  dd <- droplevels(dat[dat$mapping_condition == cond, ])
  glmer(
    selected ~ action_identity + future_assignment +
      presentation + operationalisation + domain +
      (1 | unit_id),
    data=dd, family=binomial(link="logit"),
    control=glmerControl(optimizer="bobyqa", optCtrl=list(maxfun=200000))
  )
}

red_inf <- reduced_condition("INFORMATIVE")
red_null <- reduced_condition("UNINFORMATIVE_NULL")

lrt_inf <- anova(red_inf, fit_inf, test="Chisq")
lrt_null <- anova(red_null, fit_null, test="Chisq")

# No post-hoc threshold is introduced here. The numerical result is reported;
# mechanism classification remains subject to the pre-specified replication rule.

out <- list(
  artifact_id="TI001_V012_NEXT2_PRIMARY_ANALYSIS_RESULT_001",
  status="PRIMARY_ANALYSIS_COMPLETE",
  analysis_specification="TI001_V012_NEXT2_PRIMARY_ANALYSIS_SPECIFICATION_001",
  authorization_gate="TI001_V012_NEXT2_PRIMARY_ANALYSIS_AUTHORIZATION_GATE_001",
  result_sha256=EXPECTED_RESULT_SHA,
  fixture_dir_binding="TI001_V012_NEXT2_FIXTURE_REGENERATED_001",
  fixture_unit_traceability="VALIDATED_FOR_ALL_VALID_DECISIONS",
  total_decisions=length(decisions),
  valid_decisions=length(valid),
  invalid_decisions=invalid_count,
  primary_model="mixed-effects logistic regression",
  random_effects=list("decision_unit"),
  fixed_effects=c("action_identity","future_assignment","presentation",
                  "mapping_condition","operationalisation","domain",
                  "action_identity:future_assignment"),
  informative_interaction=inf_tab,
  uninformative_null_interaction=null_tab,
  informative_interaction_lrt=as.data.frame(lrt_inf),
  uninformative_null_interaction_lrt=as.data.frame(lrt_null),
  replication_status="NOT_ASSESSABLE_FROM_SINGLE_EXECUTION",
  interpretation_boundary="No TGCV-wide confirmation/falsification, no value/causal claim, no Transformational Intelligence claim.",
  secondary_mi_contrast_status="NOT_EXECUTED"
)

write(toJSON(out, auto_unbox=TRUE, pretty=TRUE, null="null"), output_path)
