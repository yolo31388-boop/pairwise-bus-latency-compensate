import pytest
import av.bus_latency as mod

CASES = [
    ("latency_table_collect", (1,)),
    ("send_bus_compensate", (1,)),
    ("export_recompute", (1,)),
    ("rate_rebuild", (1,)),
    ("dry_wet_split", (1,)),
    ("master_align", (1,)),
    ("load_session", (1,)),
    ("build_graph", (1,)),
    ("render_mix", (1,)),
    ("present_mix", (1,)),
    ("validate_mix", (1,)),
    ("metrics_mix", (1,)),
    ("audit_mix", (1,)),
    ("fallback_mix", (1,)),
    ("determinism_mix", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
