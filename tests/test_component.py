import sys

from haystack import Pipeline

from veida_haystack import VeidaImageGenerator

p = Pipeline()
p.add_component("image", VeidaImageGenerator(aspect_ratio="16:9"))
print("ok   pipeline builds")
if "live" in sys.argv:
    out = p.run({"image": {"prompt": "a paper boat on a calm lake at sunrise, soft light"}})
    url = out["image"]["images"][0]
    print("live:", url)
    assert url.startswith("https://")
