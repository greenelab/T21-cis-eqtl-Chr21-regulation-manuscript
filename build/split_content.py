"""Split the manuscript content into a main document and a supplement.

Writes two Manubot content directories under output/biorxiv/, so that each
document is built separately and gets its own reference list:

  main/content        every content file except the supplement
  supplement/content  front matter, the supplement, and the references

pandoc-fignos and pandoc-tablenos resolve cross-references only within one
document. References that cross between the two documents are therefore
replaced with literal labels before the build:

  - in the main text, supplementary items become their tags (e.g. S1);
  - in the supplement, main figures and tables become their numbers,
    counted in the order they are defined in the main text.

Usage: python build/split_content.py [content_dir] [output_dir]
"""

import re
import shutil
import sys
from pathlib import Path

SUPPLEMENT = "91.supplement.md"
SHARED = ["00.front-matter.md", "90.back-matter.md"]
DEFINITION = re.compile(r"\{#(fig|tbl):([A-Za-z0-9_-]+)([^}]*)\}")
TAG = re.compile(r'tag="([^"]+)"')


def labels(texts):
    """Map each defined figure/table id to its rendered label."""
    numbers = {"fig": 0, "tbl": 0}
    out = {}
    for text in texts:
        for kind, label_id, attrs in DEFINITION.findall(text):
            tag = TAG.search(attrs)
            if tag:
                out[f"{kind}:{label_id}"] = tag.group(1)
            else:
                numbers[kind] += 1
                out[f"{kind}:{label_id}"] = str(numbers[kind])
    return out


def resolve(text, external):
    """Replace {@kind:id} references to ids defined in the other document."""

    def swap(match):
        key = match.group(1)
        return external.get(key, match.group(0))

    return re.sub(r"\{@((?:fig|tbl):[A-Za-z0-9_-]+)\}", swap, text)


def link_images(content_dir, target):
    images = target / "images"
    if images.is_symlink() or images.exists():
        images.unlink() if images.is_symlink() else shutil.rmtree(images)
    images.symlink_to((content_dir / "images").resolve())


def main():
    content = Path(sys.argv[1] if len(sys.argv) > 1 else "content")
    out = Path(sys.argv[2] if len(sys.argv) > 2 else "output/biorxiv")
    md_files = sorted(content.glob("*.md"))
    main_files = [p for p in md_files if p.name != SUPPLEMENT]
    supp_text = (content / SUPPLEMENT).read_text()

    main_labels = labels(p.read_text() for p in main_files)
    supp_labels = labels([supp_text])

    for part in ("main", "supplement"):
        target = out / part / "content"
        if target.exists():
            shutil.rmtree(target)
        target.mkdir(parents=True)
        for extra in ("manual-references.json",):
            if (content / extra).exists():
                shutil.copy(content / extra, target / extra)
        link_images(content, target)

    # Main document: everything but the supplement.
    main_dir = out / "main" / "content"
    shutil.copy(content / "metadata.yaml", main_dir / "metadata.yaml")
    for path in main_files:
        (main_dir / path.name).write_text(resolve(path.read_text(), supp_labels))

    # Supplement: front matter, supplement, then references. The supplement is
    # renamed so that it sorts before the references section.
    supp_dir = out / "supplement" / "content"
    metadata = (content / "metadata.yaml").read_text()
    metadata = re.sub(
        r'^title: "(.*)"$',
        r'title: "Supplementary Information: \1"',
        metadata,
        count=1,
        flags=re.M,
    )
    (supp_dir / "metadata.yaml").write_text(metadata)
    for name in SHARED:
        shutil.copy(content / name, supp_dir / name)
    (supp_dir / "10.supplement.md").write_text(resolve(supp_text, main_labels))

    unresolved = []
    for part_dir in (main_dir, supp_dir):
        text = "\n".join(p.read_text() for p in sorted(part_dir.glob("*.md")))
        refs = set(re.findall(r"\{@((?:fig|tbl):[A-Za-z0-9_-]+)\}", text))
        unresolved += [f"{part_dir.parent.name}: {key}" for key in sorted(refs - set(labels([text])))]
    if unresolved:
        sys.exit("Unresolved cross-references:\n" + "\n".join(unresolved))
    print(f"main: {len(main_files)} files; supplement: {len(SHARED) + 1} files")
    print("main labels:", main_labels)
    print("supplement labels:", supp_labels)


if __name__ == "__main__":
    main()
