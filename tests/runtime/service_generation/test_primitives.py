# Standard
from typing import Optional, Union

# Third Party
import pytest

# Local
from caikit.runtime.service_generation.primitives import (
    extract_data_model_type_from_union,
)
from sample_lib.data_model import SampleOutputType


def test_to_output_dm_type_with_dm():
    assert extract_data_model_type_from_union(SampleOutputType) == SampleOutputType


def test_to_output_dm_type_with_union_dm():
    assert (
        extract_data_model_type_from_union(Union[SampleOutputType, str])
        == SampleOutputType
    )


def test_to_output_dm_type_with_union_optional_dm():
    assert (
        extract_data_model_type_from_union(Union[Optional[SampleOutputType], str])
        == SampleOutputType
    )


def test_to_output_dm_type_raises_primitive():
    with pytest.raises(RuntimeError):
        extract_data_model_type_from_union(str)
