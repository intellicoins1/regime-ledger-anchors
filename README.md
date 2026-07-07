# regime-ledger-anchors

**Public tamper-evidence anchors** for the (private) regime-engine ledger.

The regime engine records each regime transition as an append-only,
hash-chained `ledger_event` (canonical JSON → SHA-256, linked by `prev_hash`).
This repository publishes only the **anchors**: a per-day hash computed over
that day's event hashes. Anchors reveal no proprietary content — they let any
third party confirm the private ledger has not been rewritten after the fact.

## Anchor format (`anchors/YYYY-MM-DD.json`)

```json
{
  "ref_date": "2020-02-27",
  "event_count": 1,
  "anchor_hash": "<sha256 hex>",
  "canonical_body": "{\"event_hashes\":[\"<hex>\", ...],\"ref_date\":\"2020-02-27\"}"
}
```

`anchor_hash = sha256(canonical_body)`, where `canonical_body` is the
key-sorted, whitespace-free JSON of `{"event_hashes":[...], "ref_date": ...}`.

## Verify

```bash
python3 verify_anchor.py anchors/2020-02-27.json
```

Recomputes `anchor_hash` from `canonical_body` and checks it matches.

## Status

Baseline anchors are published from the verified private regime-engine ledger.
`anchors/EXAMPLE.json` remains a hypothetical sample; dated files under
`anchors/YYYY-MM-DD.json` are production anchors. Live heartbeat publication is
handled by the private regime-engine workflow when a same-day ledger event exists.
