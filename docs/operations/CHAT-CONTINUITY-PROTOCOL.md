# HIVE — Chat Continuity Protocol

Status: CANONICAL OPERATING STANDARD
Purpose: continue HIVE work across ChatGPT conversations without depending on conversational/model memory, screenshots, manually re-uploaded checkpoints, or the user re-explaining project state.

## 1. Core principle

GitHub is the continuity backbone. Conversation history and model memory are convenience signals only and are never canonical execution truth.

A fresh Sol session must be able to reconstruct the active HIVE state, operating style, review standard, prompt delivery standard, blockers and next necessary increment from repository-contained sources.

## 2. User continuation trigger

The following user intents are treated as equivalent continuity commands:

- `continue do chat anterior`
- `continue do chat anterior seguindo o mesmo padrão`
- `continue de onde paramos`
- `continue o HIVE de onde parou`
- materially equivalent wording that clearly asks to resume the same HIVE program.

The user SHOULD NOT need to upload a checkpoint, screenshot, ZIP, prompt PDF or repeat prior instructions merely to resume normal work when the GitHub connector is available.

## 3. Fresh-chat bootstrap sequence

On a continuity trigger, Sol MUST, before defining new implementation work:

1. resolve repository `KayzenRoot/hive-v2` and current default-branch HEAD;
2. read `docs/checkpoints/CURRENT.md` in full;
3. read `docs/source/AGENT-BOOTSTRAP.md`;
4. read `docs/source/HIVE-V2-CANONICAL-SOURCE-MAP.md`;
5. read `docs/operations/RESPONSE-AND-DELIVERY-STANDARD.md`;
6. read `docs/operations/REVIEW-STANDARD.md`;
7. read `docs/decisions/DECISIONS-LEDGER.md` when the requested action can affect an approved decision;
8. resolve the active Work Order / issue / PR / evidence relevant to the checkpoint;
9. retrieve only the additional scope, architecture, requirements, DoD and round material required for the current increment using progressive disclosure;
10. compare repository evidence with any remembered context and prefer repository evidence on conflict.

## 4. Continuity invariant

After bootstrap, Sol must be able to state from Git evidence:

- current project/version state;
- last approved increment;
- active issue / Work Order / PR if any;
- current verdict or gate;
- known blockers and risks;
- what is complete;
- what remains;
- next NECESSARY increment;
- whether implementation is authorized;
- response/review/prompt delivery format expected by the user.

If any of these cannot be resolved from Git, continuity is incomplete. Sol must repair the repository/checkpoint rather than silently relying on chat memory.

## 5. Checkpoint update rule

`docs/checkpoints/CURRENT.md` is the execution continuity pointer and MUST be updated whenever an approved increment materially changes:

- project phase;
- active Work Order;
- approved PR/merge state;
- gate/verdict;
- blockers;
- implementation authorization;
- canonical source status;
- next necessary increment;
- operating-protocol version when that protocol changes.

The checkpoint must remain concise. Detailed evidence belongs in issues, PRs, ADRs, evidence bundles and supporting documents, with the checkpoint linking or naming them.

## 6. Handoff state

A chat handoff does not create a parallel truth file per chat. The current checkpoint plus canonical operating documents form the handoff mechanism.

When useful for long or complex transitions, Sol MAY add a dated handoff snapshot under `docs/checkpoints/history/`, but `docs/checkpoints/CURRENT.md` remains the single active pointer.

## 7. No screenshot dependence

Screenshots may be used as supplementary evidence when they contain information unavailable through Git or connected tooling. They are not required merely to recover project state or response format.

## 8. Failure handling

If GitHub access is temporarily unavailable, Sol must not invent the missing state. It may use already-visible current-chat evidence for a limited response, while clearly marking repository reconciliation as required before a material implementation/governance decision.

## 9. Completion criterion

`CHAT_CONTINUITY_READY = true` when a clean new chat can receive only `continue do chat anterior` and reconstruct the active HIVE workflow through the repository with no user re-explanation.
