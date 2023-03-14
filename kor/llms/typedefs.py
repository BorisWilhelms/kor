"""Provide standard interface on tops of LLMs."""
import abc
import dataclasses
from typing import Dict, List


@dataclasses.dataclass(kw_only=True)
class CompletionModel(abc.ABC):
    """Abstract completion model interface."""

    def __call__(self, prompt: str) -> str:
        """Call the model."""
        raise NotImplementedError()


@dataclasses.dataclass(kw_only=True)
class ChatCompletionModel(abc.ABC):
    """Abstract chat completion model interface."""

    def __call__(self, messages: List[Dict[str, str]]) -> str:
        """Call the model."""
        raise NotImplementedError()
