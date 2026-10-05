# veida-haystack

A [Haystack](https://haystack.deepset.ai) component that generates images with **no API key**.

```bash
pip install veida-haystack
```

```python
from haystack import Pipeline
from veida_haystack import VeidaImageGenerator

p = Pipeline()
p.add_component("image", VeidaImageGenerator(aspect_ratio="16:9"))
out = p.run({"image": {"prompt": "a paper boat on a calm lake at sunrise, soft light"}})
out["image"]["images"]  # ["https://cdn.veida.ai/uploads/....webp"]
```

Put it after a generator that writes the prompt (a blog post's summary, a product
description) and the pipeline returns an illustration URL along with the text.

It runs on the anonymous tier of [Veida](https://veida.ai/?utm_source=pypi-haystack&utm_medium=package):
nothing to configure, about seven images a day per machine, 1K output with a watermark, 40 to 120
seconds per image. When the allowance is spent or the content filter refuses a prompt, `run`
raises `veida.VeidaError` with a sentence saying which.

Signing in on veida.ai removes the watermark and opens larger models such as
[GPT Image 2](https://veida.ai/image/gpt-image-2?utm_source=pypi-haystack&utm_medium=package).
Prompt examples: [prompt library](https://veida.ai/image/prompts?utm_source=pypi-haystack&utm_medium=package).
Other clients: [veida.readthedocs.io](https://veida.readthedocs.io/). MIT.
