import pytest
from automoonbot.moonpy.data import HeteroGraphWrapper


def test_basics():
    wrapper = HeteroGraphWrapper()
    assert wrapper is not None

    wrapper.add_article("title", "summary", 1.0, "publisher", 1, {})
    assert wrapper.node_count() == 2
    assert wrapper.edge_count() == 1
