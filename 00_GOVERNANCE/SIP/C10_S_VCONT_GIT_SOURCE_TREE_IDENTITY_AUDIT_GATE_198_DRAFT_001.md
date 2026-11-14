# C10-S V_cont — Gate 198: canonical Git source-tree identity and edge-case vectors

**Status:** GIT TREE OBJECT RECONSTRUCTION PASS 362/362; SEMANTIC BOUNDARY DEFINED; MATERIALIZED SOURCE DIGEST OPEN  
**Branch:** research/c10-s-consolidation-draft  
**Parent:** Gate 197 — run-attempt and artifact association resolution  
**Scope:** Read-only audit of GitHub Git tree objects, independent reconstruction of Git tree object IDs for two existing tested commits, and deterministic synthetic edge-case vectors. No branch/ref was moved, no Git tree object was created, no workflow was launched, and no source code or scientific execution was performed.

## 1. Question and required distinction

Gate 195 proposes a source-tree observation with `commit_sha`, `tree_object_sha`, `tree_digest_algorithm`, `tree_digest` and `tree_digest_status`. The contract must distinguish:

1. the Git commit identity;
2. the root Git tree object identity;
3. the actual source materialization consumed by a runtime (including checkout filters, Git LFS payloads, submodules and generated/untracked inputs).

These are not interchangeable.

**Finding:** GitHub's Git Trees API returns the tree object SHA and its entries. The root tree object SHA is a canonical identity for the committed Git tree graph, but it is not a complete digest of the actual post-checkout runtime filesystem and is not a substitute for a materialized-source SHA-256 manifest.

## 2. Git tree object semantics

A Git tree object encodes the immediate entries of a directory. Each entry contributes:
- mode;
- filename bytes;
- NUL separator;
- referenced object ID bytes.

Tree entries recursively reference child tree objects. Git's object hash is calculated over the canonical object framing (`tree <byte-length>\0` followed by the raw tree payload). Directory entries use Git tree mode `40000` in the serialized object; GitHub's JSON API represents this as `040000`.

The GitHub API documents these relevant modes:
- `100644`: ordinary non-executable file/blob;
- `100755`: executable file/blob;
- `120000`: symlink, represented by a blob containing the link target;
- `040000`: directory/tree;
- `160000`: submodule/gitlink, represented by a commit object ID.

The GitHub API identifies these object IDs as SHA-1 IDs. The repository's observed tree and blob object IDs are 40 hexadecimal characters, consistent with SHA-1 object format.

**Normative proposal:** define the committed Git source-tree identity as:
- `tree_object_format = "sha1"`;
- `tree_digest_algorithm = "GIT_TREE_OBJECT_ID_SHA1"`;
- `tree_digest = <root tree object SHA returned by GitHub for the exact source commit>`.

This field is a Git object identity and reproducibility locator. It MUST NOT be described as a SHA-256 digest or as a cryptographic attestation of runtime materialization.

## 3. Independent reconstruction experiment

Two existing source commits used by Gate 196 were examined:

| Sample | Commit | GitHub commit root tree SHA |
|---|---|---|
| A | `244896092e6414ccd92bd31a19776dcf71266c15` | `9ccffa653009f93544eff7be21a1deb60dcc9475` |
| B | `dd886afd1bc68de231f5675e5364602914088453` | `4024968de415432cf857dfd014eb2688c729ee91` |

For each commit, the recursive Git Trees API response was used as the input inventory. A separate reconstruction routine:
1. grouped entries into their immediate parent trees;
2. applied Git tree ordering, treating directory names as if suffixed by `/` for ordering;
3. serialized each entry as mode, space, UTF-8 name, NUL, and raw 20-byte object ID;
4. serialized the Git object header and payload;
5. computed SHA-1 over those exact bytes;
6. compared the reconstructed ID with GitHub's SHA for every tree object.

| Sample | Recursive entries | Tree objects including root | Reconstructed matches | Mismatches |
|---|---:|---:|---:|---:|
| A | 3,451 | 181 | 181 | 0 |
| B | 3,451 | 181 | 181 | 0 |

**Result: 362/362 tree objects reconstructed exactly.** Both independently reconstructed root IDs match the GitHub commit's `tree.sha`.

This is a reproducibility test of the Git tree object serialization and recursive hierarchy, not a second independent cryptographic hash family. The exact source commits and API tree objects are retained as regression fixtures.

## 4. Deterministic edge-case vectors

The following synthetic vectors use Git object framing and SHA-1. They are intended as fixed regression vectors for a future implementation. They were computed without writing objects to GitHub or changing repository refs.

Common blob fixture:
- bytes: UTF-8 `hello\n`;
- blob OID: `ce013625030ba8dba906f756967f9e9ca394464a`.

| Case | Exact fixture | Expected object/tree OID | Required interpretation |
|---|---|---|---|
| Ordinary file | mode `100644`, path `hello`, blob above | `b4d01e9b0c4a9356736dfddf8830ba9a54f5271c` | Baseline |
| Executable bit | Same path/blob, mode `100755` | `9ef56a1d95f77052ab00ec42ca4a2f6b79c31cb1` | Mode changes tree OID |
| Symlink | mode `120000`, path `link`, blob bytes `target` | `f54827e757d92a4e529f1c73c65f2a9e9a1040b8` | Link target is blob content; mode distinguishes symlink |
| Nested tree | child tree contains baseline `hello`; root entry `dir` mode `40000` | child `b4d01e9b0c4a9356736dfddf8830ba9a54f5271c`; root `234ad52a178e424d52fb85e630648fc06505f29a` | Parent commits to child tree OID |
| Submodule/gitlink | mode `160000`, path `submodule`, commit `244896092e6414ccd92bd31a19776dcf71266c15` | `d8d15ee6b84c7ba27c081a4e232e4117f4b20972` | Parent tree records gitlink commit ID; does not recursively include submodule contents |
| LFS pointer blob | Canonical pointer text with version, `oid sha256:<64 hex>`, size 123; mode `100644`, path `large.bin` | blob `a0ca8cdb4b0f113f2b3367abaadd6e90652ec2f0`; tree `64070cbe02403ce5eccd68c9a63f9c17d176e00e` | Git tree commits to pointer blob, not the external LFS payload |
| Tracked attributes | `.gitattributes` bytes `*.txt text eol=lf\n` plus baseline file | `4bc462213018912a47e901790e7d491e36e4bab4` | Tracked attributes file is itself a tree entry; filter effects are not encoded as transformed runtime bytes |
| Empty tree | No entries | `4b825dc642cb6eb9a060e54bf8d69288fbee4904` | Empty directory has no tree entry in a parent; standalone empty tree object is known vector |

Required metamorphic checks:
- changing only `100644` to `100755` changes the tree OID;
- changing a symlink target blob changes its tree OID;
- changing a nested child tree changes all ancestor tree OIDs;
- changing a gitlink commit ID changes the parent tree OID;
- changing an LFS pointer's payload OID or size changes its blob/tree OID;
- adding/removing a tracked `.gitattributes` file changes the tree OID;
- adding an empty directory without any tracked entry does not change the parent tree;
- entry order in API JSON must not affect reconstructed OID; Git's canonical tree order must be applied.

## 5. Materialization boundary and special cases

### 5.1 Executable files

The executable bit is part of the tree entry mode and therefore affects the root tree OID. A checkout/runtime that loses or changes executable permissions can nevertheless differ from the committed tree; runtime materialization evidence must record effective file modes.

### 5.2 Symlinks

Git stores a symlink as a blob whose content is the target path and marks the tree entry with mode `120000`. The tree OID records the link target bytes and mode, but not whether a particular runtime safely resolves the link, nor the target file's final bytes after path resolution. A materialization verifier must preserve symlink identity and reject unsafe resolution according to the execution contract.

### 5.3 Submodules

A gitlink records a submodule commit ID, not the complete submodule object graph in the superproject tree. Therefore a root tree OID alone is insufficient to identify all code consumed when submodules are initialized. A source materialization manifest must enumerate each submodule path, repository identity, exact commit ID, and resolved nested tree identity; missing or floating submodule state is not verifiable.

### 5.4 Git LFS and .gitattributes

Git LFS stores pointer files in Git and stores the large payload outside the ordinary Git object database. Clean/smudge filters may replace the pointer with payload bytes in the working tree. The tracked `.gitattributes` file influences filter selection but does not place the transformed payload into the Git tree object.

Consequently, the Git tree OID commits to the pointer and attributes files, not necessarily to the bytes consumed by the program. A materialization manifest must record:
- path;
- Git blob OID and mode;
- whether the blob is an LFS pointer;
- pointer SHA-256 OID and declared size;
- resolved payload SHA-256 and actual byte length, or an explicit unavailable/mismatch state;
- the filter/materialization policy and tool version.

No claim is made that the two sampled C10-S commits are free of LFS pointers: the recursive tree inventories had no `.gitattributes` or `.gitmodules`, and no symlink/gitlink entries, but this pass did not inspect every small blob for pointer text or resolve external LFS payloads.

### 5.5 Empty directories

Git trees represent tracked entries, not empty filesystem directories. An empty directory has no parent-tree entry and cannot be represented by Git alone. If empty directories or generated directory structure matter to execution, they must be specified by the runtime/materialization contract, not inferred from the Git tree OID.

### 5.6 Checkout filters, line endings and generated files

The root Git tree OID does not specify all checkout-time transformations, global/system Git configuration, clean/smudge filters, generated files, ignored files, environment-derived files, or runtime writes. A commit/tree identity alone cannot prove the bytes present at execution time.

## 6. Required Gate 195 schema refinement

The current proposed `source_tree` object conflates the Git object identity and actual materialized source. Split the concepts before freezing:

**Committed Git tree observation**
- `commit_sha`
- `tree_object_sha`
- `tree_object_format` (currently `sha1`)
- `tree_digest_algorithm` (currently `GIT_TREE_OBJECT_ID_SHA1`)
- `tree_digest` (same exact value as `tree_object_sha`)
- `tree_digest_status`

**Materialized source observation** — separate future contract, not closed by this gate:
- `materialization_manifest_schema`
- `materialization_manifest_sha256`
- `checkout_policy_id`
- `git_version`
- `filter_inventory`
- `lfs_payload_inventory`
- `submodule_inventory`
- `tracked_and_untracked_input_policy`
- `runtime_source_root` or equivalent exact execution input boundary
- `materialization_status`

Do not name the Git tree SHA-1 field simply `source_tree_sha256`. Do not substitute a GitHub ZIP digest (Gate 196) for either field.

**Security limitation:** Git's current repository object IDs are SHA-1. Preserve the exact Git tree OID for Git compatibility and lookup, but do not use it as the sole cryptographic integrity control. The materialized-source manifest must use SHA-256 over a separately specified canonical representation and must hash the actual bytes consumed by execution.

## 7. Sample repository observations

For both Gate 196 tested commits:
- root tree SHA matches the commit response;
- recursive tree response was not truncated;
- 3,451 entries and 181 tree objects including root;
- zero mode `120000` symlinks;
- zero mode `160000` gitlinks;
- no root `.gitattributes`;
- no root `.gitmodules`.

For the current Gate 197 research branch HEAD `700ccdee1ca609c06f3901aefbf51bc29b6e3315`:
- root tree SHA `94d6982b5e4f6babd4674ec40b3cf26ecd1832db`;
- recursive tree response not truncated;
- 3,517 entries;
- 180 descendant tree objects (181 including root);
- zero symlink and gitlink entries.

These are bounded observations of the named commits, not claims about all repository history.

## 8. Evidence disposition

| Question | Result |
|---|---|
| GitHub Git Trees API returns root tree object SHA and entries? | DOCUMENTED + OBSERVED |
| Independent serialization reconstructs every tree object in sample A? | PASS, 181/181 |
| Independent serialization reconstructs every tree object in sample B? | PASS, 181/181 |
| Executable mode changes tree identity? | SYNTHETIC VECTOR DEFINED |
| Symlink mode/target represented? | SYNTHETIC VECTOR DEFINED |
| Nested trees represented recursively? | SYNTHETIC VECTOR DEFINED |
| Submodule/gitlink scope represented? | SYNTHETIC VECTOR DEFINED |
| LFS pointer vs payload distinguished? | SEMANTIC BOUNDARY DEFINED; repository payload inventory OPEN |
| .gitattributes effect distinguished from stored tree bytes? | SEMANTIC BOUNDARY DEFINED |
| Empty directory representation? | CLOSED: not represented without tracked entries |
| Actual executed source materialization digest? | OPEN |
| Git tree SHA-1 sufficient as sole cryptographic integrity control? | NO |

## 9. Sources

- GitHub REST Git Trees API: https://docs.github.com/en/rest/git/trees
- Git LFS object/pointer and clean/smudge model: https://github.com/git-lfs/git-lfs/blob/main/docs/spec.md
- Git LFS filter behavior: https://github.com/git-lfs/git-lfs/blob/main/docs/man/git-lfs.adoc

## 10. Gate disposition and next step

**Gate 198: PARTIAL PASS.** The committed Git tree identity is now precisely defined and independently reconstructed for 362/362 tree objects across two existing tested commits. The synthetic edge-case vectors establish expected behavior for modes, symlinks, nested trees, submodules, LFS pointers, tracked attributes and empty trees.

The Git tree OID is not the actual runtime source-materialization digest. The materialized-source manifest and LFS/submodule resolution remain open; therefore Gate 195's complete SourceExecutionEvidence schema must not be frozen.

**Next operation:** define the materialization-manifest schema and canonical SHA-256 algorithm for the exact source inputs consumed by a C10-S execution, including checkout/filter policy, LFS payload resolution, submodule closure, generated/untracked inputs and path/mode semantics. First recover any existing package/source-freeze contract that already covers these fields; do not create a duplicate manifest if a compatible canonical artifact exists.
