"""Validate the distributed instructions, manifests, licenses, and local links."""

import json
import re
import sys
from pathlib import Path

from skills_ref import validate


def main():
    root = Path(__file__).resolve().parents[1]
    errors = []
    skills = sorted((root / "skills").iterdir())
    if not skills:
        errors.append("No skills found")
    license_text = (root / "LICENSE").read_text()
    readme = (root / "README.md").read_text()
    for skill in skills:
        if not skill.is_dir():
            errors.append(f"Unexpected skills entry: {skill.name}")
            continue
        errors.extend(f"{skill.name}: {error}" for error in validate(skill))
        license_path = skill / "LICENSE"
        if not license_path.is_file() or license_path.read_text() != license_text:
            errors.append(f"{skill.name}: packaged MIT notice missing or changed")
        if f"(skills/{skill.name}/SKILL.md)" not in readme:
            errors.append(f"{skill.name}: missing catalogue entry")

    manifests = [
        json.loads((root / folder / "plugin.json").read_text())
        for folder in (".codex-plugin", ".claude-plugin")
    ]
    for manifest in manifests:
        if manifest["name"] != root.name or manifest["license"] != "MIT":
            errors.append("Manifest identity or license mismatch")
        if not re.fullmatch(r"\d+\.\d+\.\d+", manifest["version"]):
            errors.append("Manifest version must be a release semver")
        for forbidden in ("hooks", "mcpServers", "apps"):
            if forbidden in manifest:
                errors.append(f"Instructions-only pack declares {forbidden}")
    if manifests[0]["version"] != manifests[1]["version"]:
        errors.append("Native manifest versions differ")
    if manifests[0].get("skills") != "./skills/":
        errors.append("Codex skills path mismatch")

    markdown = [
        root / "README.md",
        root / "PRIVACY.md",
        *(root / "docs").rglob("*.md"),
        *(root / "skills").rglob("*.md"),
    ]
    for path in markdown:
        for target in re.findall(r"\]\(([^\s)]+)\)", path.read_text()):
            if "://" in target or target.startswith(("#", "mailto:")):
                continue
            target_path = (path.parent / target.split("#", 1)[0]).resolve()
            if not target_path.is_relative_to(root) or not target_path.exists():
                errors.append(f"{path.relative_to(root)}: invalid local link {target}")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Validated {len(skills)} skills, licenses, manifests, catalogue, and local links.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
