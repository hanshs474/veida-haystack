"""Veida image generation as a Haystack component.

The component uses Veida's free anonymous tier, so a pipeline runs on a
machine with nothing configured: 1K output, watermarked, about seven images a
day per machine.
"""

from typing import Dict, List

import veida
from haystack import component


@component
class VeidaImageGenerator:
    """Generates an image from a prompt and returns its URL.

    Usage:
        ```python
        from veida_haystack import VeidaImageGenerator

        gen = VeidaImageGenerator(aspect_ratio="16:9")
        result = gen.run(prompt="a paper boat at sunrise, soft light")
        result["images"]  # ["https://cdn.veida.ai/..."]
        ```
    """

    def __init__(self, aspect_ratio: str = "1:1", timeout: float = 240.0):
        self.aspect_ratio = aspect_ratio
        self.timeout = timeout

    @component.output_types(images=List[str])
    def run(self, prompt: str) -> Dict[str, List[str]]:
        """Generate one image.

        Raises ``veida.VeidaError`` with a readable reason when the free
        allowance is spent or the prompt is refused.
        """
        url = veida.generate(prompt, aspect_ratio=self.aspect_ratio, timeout=self.timeout)
        return {"images": [url]}
